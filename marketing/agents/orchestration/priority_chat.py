"""
Priority Chat Orchestrator.

Runs a single, bounded round with selected agents (prioritized) and returns
a coordinator synthesis to avoid infinite agent loops.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from uuid import uuid4

from marketing.agents.base.agent_memory import get_agent_memory
from marketing.agents.orchestration.coordinator import CoordinatorAgent
from marketing.agents.team import (
    StrategistAgent,
    ContentLeadAgent,
    CreativeDirectorAgent,
    CopywriterAgent,
    CommunityManagerAgent,
    BrandGuardianAgent,
    AnalystAgent,
)


AGENT_REGISTRY = {
    "strategist": StrategistAgent,
    "content_lead": ContentLeadAgent,
    "creative_director": CreativeDirectorAgent,
    "copywriter": CopywriterAgent,
    "community_manager": CommunityManagerAgent,
    "brand_guardian": BrandGuardianAgent,
    "analyst": AnalystAgent,
}

DEFAULT_PRIORITY = [
    "strategist",
    "content_lead",
    "creative_director",
    "copywriter",
    "community_manager",
    "brand_guardian",
    "analyst",
]


@dataclass
class ChatRoundResult:
    session_id: str
    coordinator_message: str
    agent_messages: List[Dict[str, str]]
    used_agents: List[str]
    skipped_agents: List[str]
    intent: str


class _SessionStore:
    """In-memory chat state (dev mode)."""

    def __init__(self) -> None:
        self._sessions: Dict[str, Dict[str, Any]] = {}

    def get_or_create(self, session_id: Optional[str]) -> Dict[str, Any]:
        if session_id and session_id in self._sessions:
            return self._sessions[session_id]
        new_id = session_id or str(uuid4())
        self._sessions[new_id] = {
            "id": new_id,
            "history": [],
            "last_summary": "",
            "round_count": 0,
        }
        return self._sessions[new_id]


_store = _SessionStore()


def _normalize_selected(selected_agents: Optional[List[str]]) -> List[str]:
    if not selected_agents:
        return DEFAULT_PRIORITY[:3]
    return [agent for agent in selected_agents if agent in AGENT_REGISTRY]


def _prioritize(selected_agents: List[str], max_agents: int) -> List[str]:
    ordered = [agent for agent in DEFAULT_PRIORITY if agent in selected_agents]
    return ordered[:max(1, max_agents)]


def _detect_intent(message: str) -> str:
    text = (message or "").lower()
    if any(token in text for token in ["guion", "script", "video", "reel", "tiktok"]):
        return "script"
    if any(token in text for token in ["calendario", "programar", "fecha", "schedule"]):
        return "schedule"
    return "brainstorm"


def _build_agent_prompt(role: str, message: str, last_summary: str, intent: str) -> str:
    base = [
        f"Usuario: {message}",
    ]
    if last_summary:
        base.append(f"Contexto previo: {last_summary}")
    base.append("Responde en 2-4 bullets claros.")

    if intent == "script":
        if role == "copywriter":
            base.append("Propón un guion breve (45s) con hook, desarrollo y CTA.")
        else:
            base.append("Aporta mejoras o ángulos creativos para el guion.")
    elif intent == "schedule":
        if role == "community_manager":
            base.append("Propón 2-3 fechas/horas óptimas y plataforma.")
        else:
            base.append("Sugiere timing y formato ideal.")
    else:
        base.append("Propón ideas concretas y accionables.")

    return "\n".join(base)


def _build_coordinator_prompt(message: str, agent_messages: List[Dict[str, str]]) -> str:
    contributions = "\n".join(
        [f"- {m['role']}: {m['content']}" for m in agent_messages]
    )
    return (
        "Sintetiza las contribuciones en un resumen claro y corto.\n"
        f"Usuario: {message}\n"
        "Contribuciones:\n"
        f"{contributions}\n\n"
        "Entrega:\n"
        "1) Resumen en 3-5 bullets\n"
        "2) 1-2 opciones concretas\n"
        "3) Pregunta de decisión al usuario"
    )


def _get_script_topic(message: str, last_summary: str) -> str:
    if last_summary:
        return f"{message}\n\nContexto previo:\n{last_summary}"
    return message


async def run_priority_round(
    message: str,
    selected_agents: Optional[List[str]] = None,
    max_agents: int = 3,
    session_id: Optional[str] = None,
) -> ChatRoundResult:
    session = _store.get_or_create(session_id)
    memory = get_agent_memory()

    normalized = _normalize_selected(selected_agents)
    used_agents = _prioritize(normalized, max_agents)
    skipped_agents = [a for a in normalized if a not in used_agents]

    intent = _detect_intent(message)
    agent_messages: List[Dict[str, str]] = []

    if intent == "script":
        role = "copywriter" if "copywriter" in used_agents else used_agents[0]
        agent_cls = AGENT_REGISTRY[role]
        agent = agent_cls(memory=memory)
        topic = _get_script_topic(message, session["last_summary"])
        text_response = await agent.write_reel_script(topic=topic, duration_seconds=45)
        agent_messages.append({"role": role, "content": text_response.content})
        coordinator_message = text_response.content
    else:
        for role in used_agents:
            agent_cls = AGENT_REGISTRY[role]
            agent = agent_cls(memory=memory)
            prompt = _build_agent_prompt(role, message, session["last_summary"], intent)
            agent_context = await agent._get_context(message)
            content = await agent._call_llm(
                prompt,
                context=agent_context,
                additional_system="Responde en máximo 90 palabras. No divagues.",
            )
            agent_messages.append({"role": role, "content": content})

        coordinator = CoordinatorAgent(memory=memory)
        coordinator_prompt = _build_coordinator_prompt(message, agent_messages)
        coordinator_context = await coordinator._get_context(message)
        coordinator_message = await coordinator._call_llm(
            coordinator_prompt,
            context=coordinator_context,
            additional_system="Sé conciso. Máximo 8 líneas.",
        )

    session["history"].append({"role": "user", "content": message})
    session["history"].append({"role": "coordinator", "content": coordinator_message})
    session["last_summary"] = coordinator_message
    session["round_count"] = session.get("round_count", 0) + 1

    if intent != "script" and session["round_count"] >= 2:
        coordinator_message = (
            f"{coordinator_message}\n\n"
            "¿Quieres que siga con preguntas o genero el guion ahora?"
        )
        session["history"][-1]["content"] = coordinator_message
        session["last_summary"] = coordinator_message

    return ChatRoundResult(
        session_id=session["id"],
        coordinator_message=coordinator_message,
        agent_messages=agent_messages,
        used_agents=used_agents,
        skipped_agents=skipped_agents,
        intent=intent,
    )
