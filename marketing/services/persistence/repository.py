"""
Repository Interface.

Abstract interface for marketing data persistence.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import date

from marketing.domain.models import (
    BrandVoiceProfile,
    MarketingStrategy,
    TeamMeeting,
    GeneratedContent,
    ContentCalendar,
)


class MarketingRepository(ABC):
    """
    Abstract repository interface for marketing data.
    
    Provides CRUD operations for all marketing models.
    """
    
    # ==================== Voice Profile ====================
    
    @abstractmethod
    async def get_active_voice_profile(self) -> Optional[BrandVoiceProfile]:
        """Get the active voice profile."""
        pass
    
    @abstractmethod
    async def save_voice_profile(self, profile: BrandVoiceProfile) -> BrandVoiceProfile:
        """Save or update a voice profile."""
        pass
    
    # ==================== Strategies ====================
    
    @abstractmethod
    async def get_strategy(self, strategy_id: int) -> Optional[MarketingStrategy]:
        """Get a strategy by ID."""
        pass
    
    @abstractmethod
    async def get_active_strategies(self) -> Dict[str, MarketingStrategy]:
        """Get all active strategies by type."""
        pass
    
    @abstractmethod
    async def save_strategy(self, strategy: MarketingStrategy) -> MarketingStrategy:
        """Save or update a strategy."""
        pass
    
    @abstractmethod
    async def list_strategies(
        self,
        strategy_type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 10
    ) -> List[MarketingStrategy]:
        """List strategies with optional filters."""
        pass
    
    # ==================== Meetings ====================
    
    @abstractmethod
    async def get_meeting(self, meeting_id: int) -> Optional[TeamMeeting]:
        """Get a meeting by ID."""
        pass
    
    @abstractmethod
    async def save_meeting(self, meeting: TeamMeeting) -> TeamMeeting:
        """Save or update a meeting."""
        pass
    
    @abstractmethod
    async def list_meetings(
        self,
        meeting_type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 10
    ) -> List[TeamMeeting]:
        """List meetings with optional filters."""
        pass
    
    # ==================== Content ====================
    
    @abstractmethod
    async def get_content(self, content_id: int) -> Optional[GeneratedContent]:
        """Get content by ID."""
        pass
    
    @abstractmethod
    async def save_content(self, content: GeneratedContent) -> GeneratedContent:
        """Save or update content."""
        pass
    
    @abstractmethod
    async def list_content(
        self,
        status: Optional[str] = None,
        platform: Optional[str] = None,
        content_type: Optional[str] = None,
        limit: int = 20
    ) -> List[GeneratedContent]:
        """List content with optional filters."""
        pass
    
    @abstractmethod
    async def get_content_queue(self, limit: int = 20) -> List[GeneratedContent]:
        """Get content pending review."""
        pass
    
    # ==================== Calendar ====================
    
    @abstractmethod
    async def get_calendar_item(self, item_id: int) -> Optional[ContentCalendar]:
        """Get a calendar item by ID."""
        pass
    
    @abstractmethod
    async def save_calendar_item(self, item: ContentCalendar) -> ContentCalendar:
        """Save or update a calendar item."""
        pass
    
    @abstractmethod
    async def get_calendar_range(
        self,
        start_date: date,
        end_date: date,
        platform: Optional[str] = None
    ) -> List[ContentCalendar]:
        """Get calendar items in a date range."""
        pass
