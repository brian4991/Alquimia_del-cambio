"""
Calendar API Endpoints.

Endpoints for managing the editorial calendar.
"""

from datetime import date, timedelta
from typing import Optional
from fastapi import APIRouter, HTTPException

from marketing.api.auth import require_admin
from marketing.api.schemas.responses import CalendarResponse, CalendarItemResponse
from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository

router = APIRouter()


@router.get("/", response_model=CalendarResponse)
async def get_calendar(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    platform: Optional[str] = None,
    current_admin = require_admin(),
):
    """
    Get calendar items for a date range.
    
    Defaults to current week if no dates provided.
    """
    repository = get_marketing_repository()
    
    # Default to current week
    if not start_date:
        start_date = date.today()
    if not end_date:
        end_date = start_date + timedelta(days=7)
    
    items = await repository.get_calendar_range(
        start_date=start_date,
        end_date=end_date,
        platform=platform,
    )
    
    # Get content for each item
    item_responses = []
    for item in items:
        content = await repository.get_content(item.content_id)
        item_responses.append(CalendarItemResponse(
            id=item.id,
            content_id=item.content_id,
            platform=item.platform,
            scheduled_date=item.scheduled_date,
            scheduled_time=item.scheduled_time,
            status=item.status,
            content=content.to_dict() if content else None,
        ))
    
    return CalendarResponse(
        items=item_responses,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/week", response_model=CalendarResponse)
async def get_week_calendar(
    week_offset: int = 0,
    platform: Optional[str] = None,
    current_admin = require_admin(),
):
    """
    Get calendar for a specific week.
    
    week_offset: 0 = current week, 1 = next week, -1 = last week, etc.
    """
    today = date.today()
    # Get Monday of current week
    monday = today - timedelta(days=today.weekday())
    # Apply offset
    start_date = monday + timedelta(weeks=week_offset)
    end_date = start_date + timedelta(days=6)
    
    return await get_calendar(
        start_date=start_date,
        end_date=end_date,
        platform=platform,
    )


@router.get("/month", response_model=CalendarResponse)
async def get_month_calendar(
    year: Optional[int] = None,
    month: Optional[int] = None,
    platform: Optional[str] = None,
    current_admin = require_admin(),
):
    """
    Get calendar for a specific month.
    
    Defaults to current month if not specified.
    """
    today = date.today()
    year = year or today.year
    month = month or today.month
    
    start_date = date(year, month, 1)
    
    # Get last day of month
    if month == 12:
        end_date = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = date(year, month + 1, 1) - timedelta(days=1)
    
    return await get_calendar(
        start_date=start_date,
        end_date=end_date,
        platform=platform,
    )


@router.post("/schedule/{content_id}")
async def schedule_content(
    content_id: int,
    scheduled_date: date,
    scheduled_time: Optional[str] = None,
    platform: Optional[str] = None,
    current_admin = require_admin(),
):
    """Schedule content for publication."""
    from marketing.domain.models import ContentCalendar
    
    repository = get_marketing_repository()
    
    # Get content
    content = await repository.get_content(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    # Create calendar entry
    calendar_item = ContentCalendar(
        content_id=content_id,
        platform=platform or content.platform,
        scheduled_date=scheduled_date,
        scheduled_time=scheduled_time,
        status="scheduled",
        manually_adjusted=True,
    )
    
    calendar_item = await repository.save_calendar_item(calendar_item)
    
    # Update content scheduled date
    content.scheduled_date = scheduled_date
    content.scheduled_time = scheduled_time
    await repository.save_content(content)
    
    return CalendarItemResponse(
        id=calendar_item.id,
        content_id=calendar_item.content_id,
        platform=calendar_item.platform,
        scheduled_date=calendar_item.scheduled_date,
        scheduled_time=calendar_item.scheduled_time,
        status=calendar_item.status,
    )


@router.patch("/item/{item_id}")
async def update_calendar_item(
    item_id: int,
    scheduled_date: Optional[date] = None,
    scheduled_time: Optional[str] = None,
    status: Optional[str] = None,
    current_admin = require_admin(),
):
    """Update a calendar item."""
    repository = get_marketing_repository()
    
    item = await repository.get_calendar_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Calendar item not found")
    
    if scheduled_date:
        item.scheduled_date = scheduled_date
        item.manually_adjusted = True
    if scheduled_time:
        item.scheduled_time = scheduled_time
    if status:
        item.status = status
    
    item = await repository.save_calendar_item(item)
    
    return CalendarItemResponse(
        id=item.id,
        content_id=item.content_id,
        platform=item.platform,
        scheduled_date=item.scheduled_date,
        scheduled_time=item.scheduled_time,
        status=item.status,
    )
