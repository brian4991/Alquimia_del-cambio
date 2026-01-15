"""
Meeting Graph.

LangGraph-based state machine for team meetings.
"""

from typing import Optional, Dict, Any, TypedDict, Annotated, Sequence
from enum import Enum
import operator

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from marketing.domain.entities.debate_state import DebateState
from marketing.domain.entities.meeting_result import MeetingResult
from marketing.agents.orchestration.coordinator import CoordinatorAgent
from marketing.agents.orchestration.debate_manager import DebateManager
from marketing.agents.base.agent_memory import AgentMemory, get_agent_memory


class MeetingPhase(str, Enum):
    """Phases of a team meeting."""
    INTRODUCTION = "introduction"
    DEBATE = "debate"
    SYNTHESIS = "synthesis"
    DECISION = "decision"
    CONCLUSION = "conclusion"


class MeetingState(TypedDict):
    """State for the meeting graph."""
    meeting_id: int
    meeting_type: str
    brief: str
    phase: str
    debate_state: Optional[Dict[str, Any]]
    meeting_result: Optional[Dict[str, Any]]
    nicole_decision: Optional[str]
    context: Dict[str, Any]
    messages: Annotated[Sequence[str], operator.add]
    error: Optional[str]


class MeetingGraph:
    """
    LangGraph-based meeting orchestration.
    
    Manages the flow of team meetings through defined phases:
    1. Introduction - Coordinator introduces the meeting
    2. Debate - Agents discuss and debate
    3. Synthesis - Coordinator synthesizes the debate
    4. Decision - Wait for Nicole's decision (if needed)
    5. Conclusion - Wrap up and next steps
    """
    
    def __init__(self, memory: Optional[AgentMemory] = None) -> None:
        """
        Initialize meeting graph.
        
        Args:
            memory: Shared agent memory.
        """
        self._memory = memory or get_agent_memory()
        self._coordinator = CoordinatorAgent(memory=self._memory)
        self._debate_manager = DebateManager(memory=self._memory)
        self._checkpointer = MemorySaver()  # Must be created before _build_graph()
        self._graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """
        Build the LangGraph state machine.
        
        Returns:
            Configured StateGraph.
        """
        # Create the graph
        graph = StateGraph(MeetingState)
        
        # Add nodes
        graph.add_node("introduction", self._introduction_node)
        graph.add_node("debate", self._debate_node)
        graph.add_node("synthesis", self._synthesis_node)
        graph.add_node("await_decision", self._await_decision_node)
        graph.add_node("conclusion", self._conclusion_node)
        
        # Add edges
        graph.set_entry_point("introduction")
        
        graph.add_edge("introduction", "debate")
        graph.add_edge("debate", "synthesis")
        
        # Conditional edge after synthesis
        graph.add_conditional_edges(
            "synthesis",
            self._should_await_decision,
            {
                "await": "await_decision",
                "conclude": "conclusion",
            }
        )
        
        graph.add_edge("await_decision", "conclusion")
        graph.add_edge("conclusion", END)
        
        return graph.compile(checkpointer=self._checkpointer)
    
    async def _introduction_node(self, state: MeetingState) -> Dict[str, Any]:
        """
        Introduction phase node.
        
        Args:
            state: Current state.
            
        Returns:
            Updated state.
        """
        try:
            response = await self._coordinator.introduce_meeting(
                meeting_type=state["meeting_type"],
                brief=state["brief"],
                context=state.get("context"),
            )
            
            return {
                "phase": MeetingPhase.DEBATE.value,
                "messages": [f"[Coordinador] {response.content}"],
            }
        except Exception as e:
            return {
                "error": f"Error en introducción: {str(e)}",
                "messages": [f"[Error] {str(e)}"],
            }
    
    async def _debate_node(self, state: MeetingState) -> Dict[str, Any]:
        """
        Debate phase node.
        
        Args:
            state: Current state.
            
        Returns:
            Updated state with debate results.
        """
        try:
            debate_state = await self._debate_manager.run_full_debate(
                meeting_type=state["meeting_type"],
                brief=state["brief"],
                max_rounds=3,
                context=state.get("context"),
            )
            
            # Format messages from debate
            messages = []
            for round_data in debate_state.rounds:
                messages.append(f"\n--- Ronda {round_data.round_number} ---")
                for contrib in round_data.contributions:
                    messages.append(
                        f"[{contrib.agent_role.title()}] {contrib.content[:200]}..."
                    )
            
            return {
                "phase": MeetingPhase.SYNTHESIS.value,
                "debate_state": debate_state.model_dump(),
                "messages": messages,
            }
        except Exception as e:
            return {
                "error": f"Error en debate: {str(e)}",
                "messages": [f"[Error] {str(e)}"],
            }
    
    async def _synthesis_node(self, state: MeetingState) -> Dict[str, Any]:
        """
        Synthesis phase node.
        
        Args:
            state: Current state.
            
        Returns:
            Updated state with meeting result.
        """
        try:
            # Reconstruct debate state
            debate_state = DebateState(**state["debate_state"])
            debate_state.meeting_id = state["meeting_id"]
            
            # Synthesize
            result = await self._coordinator.synthesize_debate(
                debate_state=debate_state,
                context=state.get("context"),
            )
            
            return {
                "phase": MeetingPhase.DECISION.value if result.requires_decision else MeetingPhase.CONCLUSION.value,
                "meeting_result": result.model_dump(),
                "messages": [f"[Coordinador - Síntesis]\n{result.format_for_display()}"],
            }
        except Exception as e:
            return {
                "error": f"Error en síntesis: {str(e)}",
                "messages": [f"[Error] {str(e)}"],
            }
    
    def _should_await_decision(self, state: MeetingState) -> str:
        """
        Determine if we should wait for Nicole's decision.
        
        Args:
            state: Current state.
            
        Returns:
            "await" or "conclude".
        """
        if state.get("meeting_result"):
            result = state["meeting_result"]
            if result.get("requires_decision") and not state.get("nicole_decision"):
                return "await"
        return "conclude"
    
    async def _await_decision_node(self, state: MeetingState) -> Dict[str, Any]:
        """
        Await decision phase node.
        
        This is a placeholder - in real usage, the graph would pause here
        and resume when Nicole makes a decision.
        
        Args:
            state: Current state.
            
        Returns:
            Updated state.
        """
        # In a real implementation, this would pause and wait for input
        # For now, we just mark that we're awaiting decision
        return {
            "phase": MeetingPhase.DECISION.value,
            "messages": ["[Sistema] Esperando decisión de Nicole..."],
        }
    
    async def _conclusion_node(self, state: MeetingState) -> Dict[str, Any]:
        """
        Conclusion phase node.
        
        Args:
            state: Current state.
            
        Returns:
            Final state.
        """
        try:
            debate_state = DebateState(**state["debate_state"])
            
            response = await self._coordinator.conclude_meeting(
                debate_state=debate_state,
                nicole_decision=state.get("nicole_decision"),
                context=state.get("context"),
            )
            
            return {
                "phase": MeetingPhase.CONCLUSION.value,
                "messages": [f"[Coordinador - Conclusión]\n{response.content}"],
            }
        except Exception as e:
            return {
                "error": f"Error en conclusión: {str(e)}",
                "messages": [f"[Error] {str(e)}"],
            }
    
    async def run_meeting(
        self,
        meeting_id: int,
        meeting_type: str,
        brief: str,
        context: Optional[Dict[str, Any]] = None,
        thread_id: Optional[str] = None,
    ) -> MeetingState:
        """
        Run a complete meeting.
        
        Args:
            meeting_id: Meeting ID.
            meeting_type: Type of meeting.
            brief: Initial brief.
            context: Additional context.
            thread_id: Thread ID for checkpointing.
            
        Returns:
            Final meeting state.
        """
        initial_state: MeetingState = {
            "meeting_id": meeting_id,
            "meeting_type": meeting_type,
            "brief": brief,
            "phase": MeetingPhase.INTRODUCTION.value,
            "debate_state": None,
            "meeting_result": None,
            "nicole_decision": None,
            "context": context or {},
            "messages": [],
            "error": None,
        }
        
        config = {"configurable": {"thread_id": thread_id or f"meeting_{meeting_id}"}}
        
        # Run the graph
        final_state = await self._graph.ainvoke(initial_state, config)
        
        return final_state
    
    async def resume_with_decision(
        self,
        thread_id: str,
        decision: str,
    ) -> MeetingState:
        """
        Resume a paused meeting with Nicole's decision.
        
        Args:
            thread_id: Thread ID of the paused meeting.
            decision: Nicole's decision.
            
        Returns:
            Final meeting state.
        """
        config = {"configurable": {"thread_id": thread_id}}
        
        # Update state with decision
        update = {
            "nicole_decision": decision,
            "messages": [f"[Nicole] Decisión: {decision}"],
        }
        
        # Resume from checkpoint
        final_state = await self._graph.ainvoke(update, config)
        
        return final_state


# Factory function
def get_meeting_graph(memory: Optional[AgentMemory] = None) -> MeetingGraph:
    """Get meeting graph instance."""
    return MeetingGraph(memory=memory)
