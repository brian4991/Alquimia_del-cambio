"""
Chat API Endpoints.

Priority-based multi-agent chat round.
"""

from fastapi import APIRouter

from marketing.api.auth import require_admin
from marketing.api.schemas.requests import ChatMessageRequest
from marketing.api.schemas.responses import ChatResponse, ChatAgentMessage
from marketing.agents.orchestration.priority_chat import run_priority_round

router = APIRouter()


@router.post("/message", response_model=ChatResponse)
async def chat_message(
    request: ChatMessageRequest,
    current_admin=require_admin(),
):
    """Run a single prioritized agent round and return synthesis."""
    result = await run_priority_round(
        message=request.message,
        selected_agents=request.selected_agents,
        max_agents=request.max_agents or 3,
        session_id=request.session_id,
    )

    return ChatResponse(
        session_id=result.session_id,
        coordinator_message=result.coordinator_message,
        agent_messages=[
            ChatAgentMessage(role=m["role"], content=m["content"])
            for m in result.agent_messages
        ],
        used_agents=result.used_agents,
        skipped_agents=result.skipped_agents,
        intent=result.intent,
    )
