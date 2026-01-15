"""
Team Meeting Model.

Stores information about marketing team meetings (brainstorm, review, planning).
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from marketing.domain.models.base import MarketingBase


class MeetingType(str, Enum):
    """Type of team meeting."""
    BRAINSTORM = "brainstorm"  # Idea generation
    REVIEW = "review"          # Content review
    PLANNING = "planning"      # Editorial planning


class MeetingStatus(str, Enum):
    """Meeting status."""
    IN_PROGRESS = "in_progress"
    AWAITING_DECISION = "awaiting_decision"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TeamMeeting(MarketingBase):
    """
    Team meeting record.
    
    Stores the meeting context, debate summary, and outcomes.
    """
    
    __tablename__ = "marketing_meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Meeting type and status
    meeting_type = Column(String(20), nullable=False)
    """Type: brainstorm, review, or planning"""
    
    status = Column(String(20), default="in_progress")
    """Status: in_progress, awaiting_decision, completed, cancelled"""
    
    # Input
    brief_initial = Column(Text, nullable=False)
    """Initial brief from Nicole"""
    
    context = Column(JSON, nullable=True, default=dict)
    """Additional context (strategy, voice profile, etc.)"""
    
    # Debate content
    debate_log = Column(JSON, nullable=True, default=list)
    """Full log of agent contributions"""
    
    debate_summary = Column(Text, nullable=True)
    """Summarized debate for Nicole"""
    
    # Options and decision
    options_proposed = Column(JSON, nullable=True, default=list)
    """Options presented to Nicole"""
    
    nicole_decision = Column(Text, nullable=True)
    """Nicole's final decision"""
    
    nicole_feedback = Column(Text, nullable=True)
    """Feedback from Nicole for learning"""
    
    # Outcomes
    outputs = Column(JSON, nullable=True, default=list)
    """Generated outputs (content, strategies, etc.)"""
    
    # Timestamps
    created_at = Column(DateTime, default=func.now())
    completed_at = Column(DateTime, nullable=True)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "meeting_type": self.meeting_type,
            "status": self.status,
            "brief_initial": self.brief_initial,
            "context": self.context,
            "debate_summary": self.debate_summary,
            "options_proposed": self.options_proposed,
            "nicole_decision": self.nicole_decision,
            "nicole_feedback": self.nicole_feedback,
            "outputs": self.outputs,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }
    
    def add_agent_contribution(
        self,
        agent_role: str,
        content: str,
        contribution_type: str = "proposal"
    ) -> None:
        """
        Add an agent's contribution to the debate log.
        
        Args:
            agent_role: Role of the contributing agent.
            content: Content of the contribution.
            contribution_type: Type (proposal, critique, suggestion).
        """
        if self.debate_log is None:
            self.debate_log = []
        
        self.debate_log.append({
            "agent": agent_role,
            "type": contribution_type,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        })
    
    def get_debate_for_synthesis(self) -> str:
        """
        Get debate content formatted for synthesis.
        
        Returns:
            Formatted string of all contributions.
        """
        if not self.debate_log:
            return "No hay contribuciones registradas."
        
        parts = []
        for entry in self.debate_log:
            parts.append(f"**{entry['agent']}** ({entry['type']}):\n{entry['content']}")
        
        return "\n\n---\n\n".join(parts)
