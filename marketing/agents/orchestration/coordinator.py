"""
Coordinator Agent.

Orchestrates team meetings and synthesizes debates.
"""

from typing import Optional, Dict, Any, List

from marketing.agents.base.base_agent import BaseAgent
from marketing.agents.base.agent_config import get_agent_config
from marketing.domain.entities.agent_response import AgentResponse
from marketing.domain.entities.debate_state import DebateState
from marketing.domain.entities.meeting_result import MeetingResult, ProposedOption
from marketing.services.llm.prompt_templates import PromptTemplates


class CoordinatorAgent(BaseAgent):
    """
    Coordinator Agent - Hub of the marketing team.
    
    Responsible for:
    - Orchestrating team meetings
    - Synthesizing debates
    - Presenting options to Nicole
    - Managing consensus building
    """
    
    @property
    def role(self) -> str:
        return "coordinator"
    
    async def process(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a coordination task.
        
        Args:
            task: Task description.
            context: Additional context.
            
        Returns:
            Coordination response.
        """
        agent_context = context or await self._get_context(task)
        
        prompt = f"""Como Coordinador del equipo, facilita la siguiente tarea:

**Tarea:**
{task}

Tu rol es:
1. Distribuir el trabajo entre los agentes apropiados
2. Facilitar la discusión
3. Sintetizar las contribuciones
4. Presentar opciones claras

¿Cómo organizarías esta tarea para el equipo?"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="coordination",
            confidence=0.9,
        )
    
    async def critique(
        self,
        proposal: str,
        proposer: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Coordinator doesn't critique, just synthesizes.
        
        Args:
            proposal: Proposal to review.
            proposer: Role of proposer.
            context: Additional context.
            
        Returns:
            Synthesis response.
        """
        # Coordinator synthesizes rather than critiques
        return await self.synthesize_single_contribution(proposal, proposer, context)
    
    async def synthesize_single_contribution(
        self,
        contribution: str,
        contributor: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Synthesize a single contribution.
        
        Args:
            contribution: Content to synthesize.
            contributor: Who contributed.
            context: Additional context.
            
        Returns:
            Synthesis response.
        """
        agent_context = context or await self._get_context(contribution)
        
        prompt = f"""Como Coordinador, resume la contribución de {contributor}:

**Contribución:**
{contribution}

Proporciona:
1. Puntos clave (bullet points)
2. Fortalezas de la propuesta
3. Áreas que necesitan más trabajo
4. Cómo integrar con el trabajo del equipo"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="synthesis",
            confidence=0.85,
        )
    
    async def synthesize_debate(
        self,
        debate_state: DebateState,
        context: Optional[Dict[str, Any]] = None
    ) -> MeetingResult:
        """
        Synthesize a complete debate into a meeting result.
        
        Args:
            debate_state: Current state of the debate.
            context: Additional context.
            
        Returns:
            MeetingResult with options for Nicole.
        """
        agent_context = context or await self._get_context(debate_state.brief)
        
        # Format all contributions
        contributions_text = self._format_contributions(debate_state)
        
        prompt = PromptTemplates.format_prompt(
            "SYNTHESIZE_DEBATE",
            debate_content=contributions_text
        )
        
        response_text = await self._call_llm(prompt, agent_context)
        
        # Parse the synthesis into structured result
        result = self._parse_synthesis_to_result(
            response_text,
            debate_state.meeting_id or 0,
            debate_state.meeting_type
        )
        
        return result
    
    def _format_contributions(self, debate_state: DebateState) -> str:
        """
        Format all contributions for synthesis.
        
        Args:
            debate_state: Debate state with contributions.
            
        Returns:
            Formatted string of contributions.
        """
        parts = []
        
        for round_data in debate_state.rounds:
            parts.append(f"\n### Ronda {round_data.round_number}")
            
            for contrib in round_data.contributions:
                parts.append(f"\n**{contrib.agent_role.title()}** ({contrib.response_type}):")
                parts.append(contrib.content)
                
                if contrib.agreement_level:
                    parts.append(f"Nivel de acuerdo: {contrib.agreement_level}/10")
                
                if contrib.concerns:
                    parts.append(f"Preocupaciones: {', '.join(contrib.concerns)}")
        
        return "\n".join(parts)
    
    def _parse_synthesis_to_result(
        self,
        synthesis_text: str,
        meeting_id: int,
        meeting_type: str
    ) -> MeetingResult:
        """
        Parse synthesis text into MeetingResult.
        
        Args:
            synthesis_text: Raw synthesis from LLM.
            meeting_id: Meeting ID.
            meeting_type: Type of meeting.
            
        Returns:
            Structured MeetingResult.
        """
        # Extract sections from synthesis
        lines = synthesis_text.split('\n')
        
        executive_summary = ""
        consensus_points = []
        divergence_points = []
        options = []
        recommendation = None
        recommendation_reasoning = None
        
        current_section = None
        current_option = None
        
        for line in lines:
            line = line.strip()
            
            # Detect sections
            if "resumen" in line.lower() or "summary" in line.lower():
                current_section = "summary"
                continue
            elif "consenso" in line.lower():
                current_section = "consensus"
                continue
            elif "divergencia" in line.lower() or "desacuerdo" in line.lower():
                current_section = "divergence"
                continue
            elif "opción" in line.lower() or "option" in line.lower():
                current_section = "options"
                # Check if this is a new option
                if any(c in line for c in ["A:", "B:", "C:", "1:", "2:", "3:"]):
                    if current_option:
                        options.append(current_option)
                    option_id = line[0] if line[0] in "ABC123" else str(len(options) + 1)
                    current_option = ProposedOption(
                        option_id=option_id,
                        title=line.split(":", 1)[-1].strip() if ":" in line else line,
                        description="",
                    )
                continue
            elif "recomendación" in line.lower() or "recommendation" in line.lower():
                current_section = "recommendation"
                continue
            
            # Process content based on current section
            if current_section == "summary" and line:
                executive_summary += line + " "
            elif current_section == "consensus" and line.startswith(("-", "*", "•")):
                consensus_points.append(line.lstrip("-*• "))
            elif current_section == "divergence" and line.startswith(("-", "*", "•")):
                divergence_points.append(line.lstrip("-*• "))
            elif current_section == "options" and current_option and line:
                current_option.description += line + " "
            elif current_section == "recommendation" and line:
                if not recommendation:
                    # First line is the recommendation
                    for opt_id in ["A", "B", "C", "1", "2", "3"]:
                        if opt_id in line:
                            recommendation = opt_id
                            break
                else:
                    recommendation_reasoning = (recommendation_reasoning or "") + line + " "
        
        # Add last option if exists
        if current_option:
            options.append(current_option)
        
        # If no structured options found, create a default one
        if not options:
            options.append(ProposedOption(
                option_id="A",
                title="Propuesta del equipo",
                description=synthesis_text[:500],
            ))
        
        return MeetingResult(
            meeting_id=meeting_id,
            meeting_type=meeting_type,
            executive_summary=executive_summary.strip() or "Reunión completada.",
            consensus_points=consensus_points,
            divergence_points=divergence_points,
            options=options,
            coordinator_recommendation=recommendation,
            recommendation_reasoning=recommendation_reasoning.strip() if recommendation_reasoning else None,
            requires_decision=len(options) > 1,
        )
    
    async def introduce_meeting(
        self,
        meeting_type: str,
        brief: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Introduce a new meeting to the team.
        
        Args:
            meeting_type: Type of meeting.
            brief: Initial brief.
            context: Additional context.
            
        Returns:
            Meeting introduction.
        """
        agent_context = context or await self._get_context(brief)
        
        template_map = {
            "brainstorm": "BRAINSTORM_INTRO",
            "review": "REVIEW_INTRO",
            "planning": "PLANNING_INTRO",
        }
        
        template_name = template_map.get(meeting_type, "BRAINSTORM_INTRO")
        
        # Build context for template
        template_context = {
            "objective": brief,
            "brief": brief,
            "context": agent_context.get("strategies", "No hay contexto adicional."),
            "content": brief,
            "content_type": "general",
            "platform": "múltiples",
            "period": "próximas semanas",
            "events": "Por definir",
        }
        
        intro_text = PromptTemplates.format_prompt(template_name, **template_context)
        
        prompt = f"""Como Coordinador, presenta esta reunión al equipo:

{intro_text}

Proporciona:
1. Introducción clara del objetivo
2. Qué se espera de cada agente
3. Cómo se tomará la decisión final
4. Tiempo estimado de la reunión"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="meeting_intro",
            confidence=0.95,
        )
    
    async def conclude_meeting(
        self,
        debate_state: DebateState,
        nicole_decision: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Conclude a meeting with final summary.
        
        Args:
            debate_state: Final debate state.
            nicole_decision: Nicole's decision if made.
            context: Additional context.
            
        Returns:
            Conclusion response.
        """
        agent_context = context or await self._get_context(debate_state.brief)
        
        decision_text = f"\n\n**Decisión de Nicole:** {nicole_decision}" if nicole_decision else ""
        
        prompt = f"""Como Coordinador, concluye la reunión:

**Tipo:** {debate_state.meeting_type}
**Brief original:** {debate_state.brief}
**Rondas completadas:** {debate_state.current_round}
**Estado final:** {debate_state.status}
{decision_text}

Proporciona:
1. Resumen de lo logrado
2. Próximos pasos concretos
3. Responsables de cada acción
4. Fecha límite sugerida"""

        response_text = await self._call_llm(prompt, agent_context)
        
        return AgentResponse(
            agent_role=self.role,
            content=response_text,
            response_type="meeting_conclusion",
            confidence=0.9,
        )
