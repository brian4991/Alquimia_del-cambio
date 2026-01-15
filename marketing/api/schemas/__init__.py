"""API schemas - Request and response models."""

from marketing.api.schemas.requests import (
    CreateMeetingRequest,
    SubmitDecisionRequest,
    CreateContentRequest,
    UpdateContentRequest,
    CreateStrategyRequest,
    CalendarRangeRequest,
)
from marketing.api.schemas.responses import (
    MeetingResponse,
    MeetingListResponse,
    ContentResponse,
    ContentListResponse,
    StrategyResponse,
    CalendarResponse,
    VoiceProfileResponse,
)

__all__ = [
    # Requests
    "CreateMeetingRequest",
    "SubmitDecisionRequest",
    "CreateContentRequest",
    "UpdateContentRequest",
    "CreateStrategyRequest",
    "CalendarRangeRequest",
    # Responses
    "MeetingResponse",
    "MeetingListResponse",
    "ContentResponse",
    "ContentListResponse",
    "StrategyResponse",
    "CalendarResponse",
    "VoiceProfileResponse",
]
