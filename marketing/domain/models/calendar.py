"""
Content Calendar Model.

Stores the editorial calendar for scheduled content.
"""

from datetime import datetime, date
from typing import Optional, Dict, Any
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.sql import func

from marketing.domain.models.base import MarketingBase


class CalendarStatus(str, Enum):
    """Calendar item status."""
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    SKIPPED = "skipped"
    RESCHEDULED = "rescheduled"


class ContentCalendar(MarketingBase):
    """
    Editorial calendar entry.
    
    Links content to specific publication dates/times.
    """
    
    __tablename__ = "marketing_calendar"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Linked content
    content_id = Column(Integer, ForeignKey("marketing_content.id"), nullable=False)
    """Reference to the content"""
    
    # Scheduling
    platform = Column(String(20), nullable=False)
    """Platform for this entry"""
    
    scheduled_date = Column(Date, nullable=False)
    """Scheduled publication date"""
    
    scheduled_time = Column(String(10), nullable=True)
    """Scheduled time (HH:MM)"""
    
    # Status
    status = Column(String(20), default="scheduled")
    """Status: scheduled, published, skipped, rescheduled"""
    
    # Metadata
    auto_suggested = Column(Boolean, default=False)
    """Whether this was auto-suggested by the AI"""
    
    manually_adjusted = Column(Boolean, default=False)
    """Whether Nicole manually adjusted this"""
    
    # Notes
    notes = Column(String(500), nullable=True)
    """Optional notes about this entry"""
    
    # Timestamps
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    published_at = Column(DateTime, nullable=True)
    """Actual publication timestamp"""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "content_id": self.content_id,
            "platform": self.platform,
            "scheduled_date": self.scheduled_date.isoformat() if self.scheduled_date else None,
            "scheduled_time": self.scheduled_time,
            "status": self.status,
            "auto_suggested": self.auto_suggested,
            "manually_adjusted": self.manually_adjusted,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "published_at": self.published_at.isoformat() if self.published_at else None,
        }
