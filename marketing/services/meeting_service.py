"""
Meeting Service.

High-level service for managing team meetings.
"""

from typing import Optional, Dict, Any, List
from datetime import datetime

from marketing.domain.models import TeamMeeting, GeneratedContent
from marketing.domain.models.meeting import MeetingType, MeetingStatus
from marketing.domain.entities.meeting_result import MeetingResult
from marketing.agents.orchestration.meeting_graph import MeetingGraph, get_meeting_graph
from marketing.agents.team import CopywriterAgent, CreativeDirectorAgent
from marketing.agents.base.agent_memory import AgentMemory, get_agent_memory
from marketing.services.persistence.sqlalchemy_repository import (
    SQLAlchemyMarketingRepository,
    get_marketing_repository,
)


class MeetingService:
    """
    High-level service for managing marketing team meetings.
    
    Provides:
    - Meeting creation and management
    - Debate orchestration
    - Decision handling
    - Output persistence
    """
    
    def __init__(
        self,
        repository: Optional[SQLAlchemyMarketingRepository] = None,
        meeting_graph: Optional[MeetingGraph] = None,
        memory: Optional[AgentMemory] = None,
    ) -> None:
        """
        Initialize meeting service.
        
        Args:
            repository: Data repository.
            meeting_graph: LangGraph meeting orchestrator.
            memory: Shared agent memory.
        """
        self._repository = repository or get_marketing_repository()
        self._memory = memory or get_agent_memory()
        self._meeting_graph = meeting_graph or get_meeting_graph(self._memory)
    
    async def create_meeting(
        self,
        meeting_type: str,
        brief: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> TeamMeeting:
        """
        Create a new team meeting.
        
        Args:
            meeting_type: Type of meeting (brainstorm, review, planning).
            brief: Initial brief from Nicole.
            context: Additional context.
            
        Returns:
            Created meeting.
        """
        meeting = TeamMeeting(
            meeting_type=meeting_type,
            status=MeetingStatus.IN_PROGRESS.value,
            brief_initial=brief,
            context=context or {},
        )
        
        return await self._repository.save_meeting(meeting)
    
    async def run_meeting(
        self,
        meeting_id: int,
    ) -> Dict[str, Any]:
        """
        Run a meeting through the full debate cycle.
        
        Args:
            meeting_id: ID of the meeting to run.
            
        Returns:
            Meeting state with results.
        """
        # Get the meeting
        meeting = await self._repository.get_meeting(meeting_id)
        if not meeting:
            raise ValueError(f"Meeting {meeting_id} not found")
        
        # Load context
        context = await self._build_meeting_context(meeting)
        
        # Run through LangGraph
        final_state = await self._meeting_graph.run_meeting(
            meeting_id=meeting_id,
            meeting_type=meeting.meeting_type,
            brief=meeting.brief_initial,
            context=context,
        )
        
        # Update meeting with results
        meeting.debate_log = final_state.get("debate_state", {}).get("rounds", [])
        meeting.debate_summary = self._extract_summary(final_state)
        meeting.options_proposed = final_state.get("meeting_result", {}).get("options", [])
        
        if final_state.get("meeting_result", {}).get("requires_decision"):
            meeting.status = MeetingStatus.AWAITING_DECISION.value
        else:
            meeting.status = MeetingStatus.COMPLETED.value
            meeting.completed_at = datetime.now()
        
        await self._repository.save_meeting(meeting)
        
        return final_state
    
    async def submit_decision(
        self,
        meeting_id: int,
        decision: str,
        feedback: Optional[str] = None,
    ) -> TeamMeeting:
        """
        Submit Nicole's decision for a meeting.
        
        Args:
            meeting_id: Meeting ID.
            decision: Nicole's decision (option ID or free text).
            feedback: Optional feedback for learning.
            
        Returns:
            Updated meeting.
        """
        meeting = await self._repository.get_meeting(meeting_id)
        if not meeting:
            raise ValueError(f"Meeting {meeting_id} not found")
        
        meeting.nicole_decision = decision
        meeting.nicole_feedback = feedback
        meeting.status = MeetingStatus.COMPLETED.value
        meeting.completed_at = datetime.now()
        
        # Generate outputs based on decision
        await self._generate_meeting_outputs(meeting, decision)
        
        return await self._repository.save_meeting(meeting)
    
    async def _build_meeting_context(self, meeting: TeamMeeting) -> Dict[str, Any]:
        """
        Build context for a meeting.
        
        Args:
            meeting: Meeting instance.
            
        Returns:
            Context dictionary.
        """
        context = dict(meeting.context or {})
        
        # Add voice profile
        voice_profile = await self._repository.get_active_voice_profile()
        if voice_profile:
            self._memory.set_voice_profile(voice_profile)
            context["voice_profile"] = voice_profile.get_voice_summary()
        
        # Add active strategies
        strategies = await self._repository.get_active_strategies()
        for strategy_type, strategy in strategies.items():
            self._memory.set_strategy(strategy_type, strategy)
        context["strategies"] = self._memory.get_strategies_summary()
        
        return context
    
    def _extract_summary(self, state: Dict[str, Any]) -> str:
        """
        Extract summary from meeting state.
        
        Args:
            state: Meeting state.
            
        Returns:
            Summary string.
        """
        result = state.get("meeting_result", {})
        return result.get("executive_summary", "Reunión completada.")
    
    async def _generate_meeting_outputs(
        self,
        meeting: TeamMeeting,
        decision: str,
    ) -> None:
        """
        Generate outputs based on meeting decision.
        
        Args:
            meeting: Meeting instance.
            decision: Nicole's decision.
        """
        if not meeting.outputs:
            meeting.outputs = []

        meeting.outputs.append({
            "type": "decision",
            "decision": decision,
            "timestamp": datetime.now().isoformat(),
        })

        # Try to generate content from the chosen option
        selected_option = self._select_option(meeting.options_proposed or [], decision)
        if not selected_option:
            return

        # Infer content type/platform from option text
        option_text = f"{selected_option.get('title', '')}\n{selected_option.get('description', '')}".lower()
        content_type = "reel" if any(k in option_text for k in ["reel", "tiktok", "short", "video"]) else "post"
        platform = "instagram"
        if "tiktok" in option_text:
            platform = "tiktok"
        elif "youtube" in option_text:
            platform = "youtube"
        elif "linkedin" in option_text:
            platform = "linkedin"
        elif "facebook" in option_text:
            platform = "facebook"

        copywriter = CopywriterAgent(memory=self._memory)
        creative_director = CreativeDirectorAgent(memory=self._memory)

        text_content = None
        visual_brief = None
        try:
            if content_type in ["reel", "video_script"]:
                text_response = await copywriter.write_reel_script(
                    topic=selected_option.get("title") or meeting.brief_initial,
                    duration_seconds=45,
                )
                text_content = text_response.content
            else:
                text_response = await copywriter.write_post_caption(
                    topic=selected_option.get("title") or meeting.brief_initial,
                    platform=platform,
                    objective="engagement",
                )
                text_content = text_response.content

            visual_response = await creative_director.create_visual_brief(
                content=text_content,
                platform=platform,
                content_type=content_type,
            )
            visual_brief = visual_response.content
        except Exception as e:
            # Fallback to option description if LLM fails
            text_content = selected_option.get("description") or meeting.brief_initial
            visual_brief = f"Brief visual basado en la opción seleccionada: {selected_option.get('title', '')}"
            meeting.outputs.append({
                "type": "generation_error",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            })

        content = GeneratedContent(
            content_type=content_type,
            platform=platform,
            title=selected_option.get("title"),
            text_content=text_content,
            visual_brief=visual_brief,
            status="draft",
            meeting_id=meeting.id,
        )
        content = await self._repository.save_content(content)

        meeting.outputs.append({
            "type": "generated_content",
            "content_id": content.id,
            "content_type": content_type,
            "platform": platform,
            "timestamp": datetime.now().isoformat(),
        })

    def _select_option(self, options: List[Dict[str, Any]], decision: str) -> Optional[Dict[str, Any]]:
        """Select the chosen option from a list based on the decision."""
        if not options:
            return None
        decision_norm = (decision or "").strip().lower()
        for opt in options:
            opt_id = str(opt.get("option_id", "")).strip().lower()
            if opt_id == decision_norm:
                return opt
        # If decision is numeric (1,2,3), try index
        if decision_norm.isdigit():
            idx = int(decision_norm) - 1
            if 0 <= idx < len(options):
                return options[idx]
        return options[0]
    
    async def get_meeting_history(
        self,
        limit: int = 10,
        meeting_type: Optional[str] = None,
    ) -> List[TeamMeeting]:
        """
        Get recent meeting history.
        
        Args:
            limit: Maximum meetings to return.
            meeting_type: Filter by type.
            
        Returns:
            List of meetings.
        """
        return await self._repository.list_meetings(
            meeting_type=meeting_type,
            limit=limit,
        )
    
    async def get_pending_decisions(self) -> List[TeamMeeting]:
        """
        Get meetings awaiting Nicole's decision.
        
        Returns:
            List of meetings pending decision.
        """
        return await self._repository.list_meetings(
            status=MeetingStatus.AWAITING_DECISION.value,
        )


# Factory function
def get_meeting_service() -> MeetingService:
    """Get meeting service instance."""
    return MeetingService()
