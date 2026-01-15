"""
Request Schemas.

Pydantic models for API request validation.
"""

from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field


class CreateMeetingRequest(BaseModel):
    """Request to create a new meeting."""
    
    meeting_type: str = Field(
        ...,
        description="Type: brainstorm, review, or planning"
    )
    brief: str = Field(
        ...,
        min_length=10,
        description="Initial brief for the meeting"
    )
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional context"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "meeting_type": "brainstorm",
                "brief": "Necesitamos ideas para promocionar el próximo retiro de marzo",
                "context": {"event_date": "2026-03-15"},
            }
        }


class SubmitDecisionRequest(BaseModel):
    """Request to submit a decision for a meeting."""
    
    decision: str = Field(
        ...,
        description="Decision (option ID like 'A' or free text)"
    )
    feedback: Optional[str] = Field(
        default=None,
        description="Optional feedback for learning"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "decision": "A",
                "feedback": "Me gusta el enfoque emocional, pero ajustar el CTA",
            }
        }


class CreateContentRequest(BaseModel):
    """Request to create new content."""
    
    content_type: str = Field(
        ...,
        description="Type: post, reel, story, carousel, video_script"
    )
    platform: str = Field(
        ...,
        description="Platform: instagram, tiktok, youtube, linkedin, facebook"
    )
    topic: str = Field(
        ...,
        description="Topic or theme for the content"
    )
    objective: Optional[str] = Field(
        default=None,
        description="Objective of the content"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "content_type": "reel",
                "platform": "instagram",
                "topic": "3 señales de que necesitas trabajar tu autoestima",
                "objective": "engagement",
            }
        }


class UpdateContentRequest(BaseModel):
    """Request to update content."""
    
    status: Optional[str] = Field(
        default=None,
        description="New status"
    )
    text_content: Optional[str] = Field(
        default=None,
        description="Updated text content"
    )
    visual_brief: Optional[str] = Field(
        default=None,
        description="Updated visual brief"
    )
    hashtags: Optional[List[str]] = Field(
        default=None,
        description="Updated hashtags"
    )
    nicole_feedback: Optional[str] = Field(
        default=None,
        description="Feedback from Nicole"
    )
    scheduled_date: Optional[date] = Field(
        default=None,
        description="Scheduled publication date"
    )


class CreateStrategyRequest(BaseModel):
    """Request to create a new strategy."""
    
    strategy_type: str = Field(
        ...,
        description="Type: short, medium, or long"
    )
    objectives: str = Field(
        ...,
        description="Business objectives for the strategy"
    )
    period_start: date = Field(
        ...,
        description="Strategy start date"
    )
    period_end: date = Field(
        ...,
        description="Strategy end date"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "strategy_type": "medium",
                "objectives": "Aumentar ventas del programa en un 20%",
                "period_start": "2026-02-01",
                "period_end": "2026-04-30",
            }
        }


class CalendarRangeRequest(BaseModel):
    """Request for calendar range."""
    
    start_date: date = Field(
        ...,
        description="Range start date"
    )
    end_date: date = Field(
        ...,
        description="Range end date"
    )
    platform: Optional[str] = Field(
        default=None,
        description="Filter by platform"
    )


class ChatMessageRequest(BaseModel):
    """Request for a prioritized multi-agent chat message."""

    message: str = Field(
        ...,
        min_length=1,
        description="User message"
    )
    session_id: Optional[str] = Field(
        default=None,
        description="Existing chat session ID"
    )
    selected_agents: Optional[List[str]] = Field(
        default=None,
        description="List of selected agent roles"
    )
    max_agents: Optional[int] = Field(
        default=3,
        ge=1,
        le=5,
        description="Max agents to include in a round"
    )