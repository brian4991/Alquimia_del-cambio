"""
Meetings API Endpoints.

Endpoints for managing team meetings.
PROTECTED: Admin only access.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends

from marketing.api.auth import require_admin, get_admin_user
from marketing.api.schemas.requests import CreateMeetingRequest, SubmitDecisionRequest
from marketing.api.schemas.responses import MeetingResponse, MeetingListResponse
from marketing.services.meeting_service import get_meeting_service

router = APIRouter()


@router.post("/", response_model=MeetingResponse)
async def create_meeting(
    request: CreateMeetingRequest,
    background_tasks: BackgroundTasks,
    current_admin = require_admin(),
):
    """
    Create a new team meeting.
    
    This creates the meeting and starts the debate process in the background.
    """
    service = get_meeting_service()
    
    # Create meeting
    meeting = await service.create_meeting(
        meeting_type=request.meeting_type,
        brief=request.brief,
        context=request.context,
    )
    
    # Run meeting in background
    background_tasks.add_task(service.run_meeting, meeting.id)
    
    return MeetingResponse(
        id=meeting.id,
        meeting_type=meeting.meeting_type,
        status=meeting.status,
        brief_initial=meeting.brief_initial,
        debate_summary=meeting.debate_summary,
        options_proposed=meeting.options_proposed,
        nicole_decision=meeting.nicole_decision,
        nicole_feedback=meeting.nicole_feedback,
        created_at=meeting.created_at,
        completed_at=meeting.completed_at,
    )


@router.get("/pending", response_model=MeetingListResponse)
async def get_pending_decisions(
    current_admin = require_admin(),
    db = None,  # Not used but needed for compatibility
):
    """Get meetings awaiting Nicole's decision."""
    service = get_meeting_service()
    meetings = await service.get_pending_decisions()
    
    return MeetingListResponse(
        meetings=[
            MeetingResponse(
                id=m.id,
                meeting_type=m.meeting_type,
                status=m.status,
                brief_initial=m.brief_initial,
                debate_summary=m.debate_summary,
                options_proposed=m.options_proposed,
                nicole_decision=m.nicole_decision,
                nicole_feedback=m.nicole_feedback,
                created_at=m.created_at,
                completed_at=m.completed_at,
            )
            for m in meetings
        ],
        total=len(meetings),
    )


@router.get("/", response_model=MeetingListResponse)
async def list_meetings(
    meeting_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    current_admin = require_admin(),
):
    """List meetings with optional filters."""
    service = get_meeting_service()
    meetings = await service.get_meeting_history(
        limit=limit,
        meeting_type=meeting_type,
    )
    
    return MeetingListResponse(
        meetings=[
            MeetingResponse(
                id=m.id,
                meeting_type=m.meeting_type,
                status=m.status,
                brief_initial=m.brief_initial,
                debate_summary=m.debate_summary,
                options_proposed=m.options_proposed,
                nicole_decision=m.nicole_decision,
                nicole_feedback=m.nicole_feedback,
                created_at=m.created_at,
                completed_at=m.completed_at,
            )
            for m in meetings
        ],
        total=len(meetings),
    )


@router.get("/{meeting_id}", response_model=MeetingResponse)
async def get_meeting(
    meeting_id: int,
    current_admin = require_admin(),
):
    """Get a meeting by ID."""
    service = get_meeting_service()
    meeting = await service._repository.get_meeting(meeting_id)
    
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    return MeetingResponse(
        id=meeting.id,
        meeting_type=meeting.meeting_type,
        status=meeting.status,
        brief_initial=meeting.brief_initial,
        debate_summary=meeting.debate_summary,
        options_proposed=meeting.options_proposed,
        nicole_decision=meeting.nicole_decision,
        nicole_feedback=meeting.nicole_feedback,
        created_at=meeting.created_at,
        completed_at=meeting.completed_at,
    )


@router.post("/{meeting_id}/decision", response_model=MeetingResponse)
async def submit_decision(
    meeting_id: int,
    request: SubmitDecisionRequest,
    current_admin = require_admin(),
):
    """Submit Nicole's decision for a meeting."""
    service = get_meeting_service()
    
    try:
        meeting = await service.submit_decision(
            meeting_id=meeting_id,
            decision=request.decision,
            feedback=request.feedback,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    return MeetingResponse(
        id=meeting.id,
        meeting_type=meeting.meeting_type,
        status=meeting.status,
        brief_initial=meeting.brief_initial,
        debate_summary=meeting.debate_summary,
        options_proposed=meeting.options_proposed,
        nicole_decision=meeting.nicole_decision,
        nicole_feedback=meeting.nicole_feedback,
        created_at=meeting.created_at,
        completed_at=meeting.completed_at,
    )
