"""
Debate State Entity.

Tracks the state of ongoing debates in team meetings.
Used by LangGraph for state management.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

from marketing.domain.entities.agent_response import AgentResponse


class DebateRound(BaseModel):
    """
    Single round of debate.
    
    Contains all agent contributions for one iteration.
    """
    
    round_number: int = Field(
        ...,
        description="Round number (1-indexed)"
    )
    
    contributions: List[AgentResponse] = Field(
        default_factory=list,
        description="Agent contributions in this round"
    )
    
    consensus_reached: bool = Field(
        default=False,
        description="Whether consensus was reached"
    )
    
    consensus_level: Optional[float] = Field(
        default=None,
        description="Average agreement level if measured"
    )
    
    key_points: List[str] = Field(
        default_factory=list,
        description="Key points from this round"
    )
    
    divergences: List[str] = Field(
        default_factory=list,
        description="Points of disagreement"
    )


class DebateState(BaseModel):
    """
    Complete state of an ongoing debate.
    
    Used by LangGraph to track debate progress.
    """
    
    # Meeting context
    meeting_id: Optional[int] = Field(
        default=None,
        description="Associated meeting ID"
    )
    
    meeting_type: str = Field(
        ...,
        description="Type of meeting (brainstorm, review, planning)"
    )
    
    brief: str = Field(
        ...,
        description="Initial brief from Nicole"
    )
    
    # Debate progress
    current_round: int = Field(
        default=0,
        description="Current round number"
    )
    
    max_rounds: int = Field(
        default=3,
        description="Maximum rounds before forcing conclusion"
    )
    
    rounds: List[DebateRound] = Field(
        default_factory=list,
        description="All debate rounds"
    )
    
    # Current state
    current_proposal: Optional[str] = Field(
        default=None,
        description="Current proposal being discussed"
    )
    
    pending_agents: List[str] = Field(
        default_factory=list,
        description="Agents yet to contribute this round"
    )
    
    # Context
    voice_profile_summary: Optional[str] = Field(
        default=None,
        description="Voice profile for reference"
    )
    
    active_strategy_summary: Optional[str] = Field(
        default=None,
        description="Active strategy for reference"
    )
    
    additional_context: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional context data"
    )
    
    # Status
    status: str = Field(
        default="in_progress",
        description="Status: in_progress, consensus, needs_decision, completed"
    )
    
    # Timestamps
    started_at: datetime = Field(
        default_factory=datetime.now,
        description="When the debate started"
    )
    
    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "meeting_type": "brainstorm",
                "brief": "Necesitamos ideas para promocionar el próximo retiro",
                "current_round": 2,
                "max_rounds": 3,
                "status": "in_progress",
            }
        }
    
    def start_new_round(self) -> DebateRound:
        """
        Start a new debate round.
        
        Returns:
            New DebateRound instance.
        """
        self.current_round += 1
        new_round = DebateRound(round_number=self.current_round)
        self.rounds.append(new_round)
        
        # Reset pending agents to all team members
        self.pending_agents = [
            "strategist",
            "content_lead",
            "creative_director",
            "community_manager",
            "analyst",
            "copywriter",
            "brand_guardian",
        ]
        
        return new_round
    
    def add_contribution(self, response: AgentResponse) -> None:
        """
        Add an agent contribution to the current round.
        
        Args:
            response: Agent's response.
        """
        if not self.rounds:
            self.start_new_round()
        
        current_round = self.rounds[-1]
        current_round.contributions.append(response)
        
        # Remove from pending
        if response.agent_role in self.pending_agents:
            self.pending_agents.remove(response.agent_role)
    
    def check_consensus(self, threshold: float = 7.0) -> bool:
        """
        Check if consensus has been reached.
        
        Args:
            threshold: Minimum average agreement level for consensus.
            
        Returns:
            True if consensus reached.
        """
        if not self.rounds:
            return False
        
        current_round = self.rounds[-1]
        agreements = [
            c.agreement_level 
            for c in current_round.contributions 
            if c.agreement_level is not None
        ]
        
        if not agreements:
            return False
        
        avg_agreement = sum(agreements) / len(agreements)
        current_round.consensus_level = avg_agreement
        current_round.consensus_reached = avg_agreement >= threshold
        
        if current_round.consensus_reached:
            self.status = "consensus"
        
        return current_round.consensus_reached
    
    def should_conclude(self) -> bool:
        """
        Check if debate should conclude.
        
        Returns:
            True if max rounds reached or consensus achieved.
        """
        return (
            self.current_round >= self.max_rounds or
            self.status == "consensus"
        )
    
    def get_all_contributions(self) -> List[AgentResponse]:
        """
        Get all contributions across all rounds.
        
        Returns:
            Flat list of all agent responses.
        """
        contributions = []
        for round in self.rounds:
            contributions.extend(round.contributions)
        return contributions
