"""
Response Schemas.

Pydantic models for API responses.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime, date
from pydantic import BaseModel, Field


class MeetingResponse(BaseModel):
    """Response for a single meeting."""
    
    id: int
    meeting_type: str
    status: str
    brief_initial: str
    debate_summary: Optional[str] = None
    options_proposed: Optional[List[Dict[str, Any]]] = None
    nicole_decision: Optional[str] = None
    nicole_feedback: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class MeetingListResponse(BaseModel):
    """Response for meeting list."""
    
    meetings: List[MeetingResponse]
    total: int


class ContentResponse(BaseModel):
    """Response for a single content piece."""
    
    id: int
    content_type: str
    platform: str
    title: Optional[str] = None
    text_content: str
    visual_brief: Optional[str] = None
    hashtags: Optional[List[str]] = None
    hook: Optional[str] = None
    cta: Optional[str] = None
    status: str
    nicole_feedback: Optional[str] = None
    scheduled_date: Optional[date] = None
    canva_design_url: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class ContentListResponse(BaseModel):
    """Response for content list."""
    
    content: List[ContentResponse]
    total: int


class StrategyResponse(BaseModel):
    """Response for a strategy."""
    
    id: int
    strategy_type: str
    title: str
    period_start: date
    period_end: date
    objectives: List[str]
    content_pillars: List[str]
    key_messages: Optional[List[str]] = None
    target_metrics: Optional[Dict[str, Any]] = None
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class CalendarItemResponse(BaseModel):
    """Response for a calendar item."""
    
    id: int
    content_id: int
    platform: str
    scheduled_date: date
    scheduled_time: Optional[str] = None
    status: str
    content: Optional[ContentResponse] = None
    
    class Config:
        from_attributes = True


class CalendarResponse(BaseModel):
    """Response for calendar range."""
    
    items: List[CalendarItemResponse]
    start_date: date
    end_date: date


class VoiceProfileResponse(BaseModel):
    """Response for voice profile."""
    
    id: int
    tone_descriptors: List[str]
    vocabulary_frequent: List[str]
    expressions_cles: List[str]
    topics_principaux: List[str]
    style_guidelines: Optional[str] = None
    analyzed_transcripts_count: int
    is_active: bool
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    """Error response."""
    
    error: str
    detail: Optional[str] = None


class ChatAgentMessage(BaseModel):
    """Agent message in chat response."""

    role: str
    content: str


class ChatResponse(BaseModel):
    """Response for a chat round."""

    session_id: str
    coordinator_message: str
    agent_messages: List[ChatAgentMessage]
    used_agents: List[str]
    skipped_agents: List[str]
    intent: str