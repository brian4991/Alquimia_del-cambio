"""
SQLAlchemy Repository Implementation.

Concrete implementation of MarketingRepository using SQLAlchemy.
"""

from typing import List, Optional, Dict, Any
from datetime import date
from sqlalchemy import select, and_, or_, create_engine
from sqlalchemy.orm import Session, sessionmaker
from contextlib import asynccontextmanager
from sqlalchemy.util import greenlet_spawn
import sys
from pathlib import Path

from marketing.config import get_database_config
from marketing.services.persistence.repository import MarketingRepository
from marketing.domain.models import (
    BrandVoiceProfile,
    MarketingStrategy,
    TeamMeeting,
    GeneratedContent,
    ContentCalendar,
)
from marketing.domain.models.base import MarketingBase

# Try to use the same DB connection as the backend
try:
    backend_path = str(Path(__file__).parent.parent.parent.parent / "backend")
    if backend_path not in sys.path:
        sys.path.insert(0, backend_path)
    from database import engine as backend_engine, SessionLocal as BackendSessionLocal
    USE_BACKEND_DB = True
    print("✅ Marketing DB: Using backend database connection (sync)")
except ImportError:
    USE_BACKEND_DB = False
    backend_engine = None
    BackendSessionLocal = None
    print("⚠️  Marketing DB: Using separate database connection")


class SQLAlchemyMarketingRepository(MarketingRepository):
    """
    SQLAlchemy implementation of MarketingRepository.
    
    Provides async database operations for all marketing models.
    """
    
    def __init__(self, database_url: Optional[str] = None) -> None:
        """
        Initialize repository.
        
        Uses the same DB connection as the backend if available (sync),
        otherwise falls back to async connection.
        
        Args:
            database_url: Database connection URL.
        """
        self._db_config = get_database_config()
        self._database_url = database_url or self._db_config.url
        
        # Use backend DB connection if available (sync, works with Railway)
        if USE_BACKEND_DB and backend_engine:
            self._engine = backend_engine
            self._session_factory = BackendSessionLocal
            self._use_sync = True
        else:
            # Fallback to async connection
            self._engine = None
            self._session_factory = None
            self._use_sync = False
    
    def _get_sync_session(self) -> Session:
        """Get sync database session (uses backend connection)."""
        return self._session_factory()
    
    async def _get_async_engine(self):
        """Lazy initialization of async engine (fallback only)."""
        if self._engine is None:
            db_url = self._database_url
            if db_url.startswith("postgresql://"):
                db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
            
            from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
            from sqlalchemy.orm import sessionmaker
            
            self._engine = create_async_engine(
                db_url,
                pool_pre_ping=True,
                pool_size=1,
                max_overflow=1,
                pool_timeout=5,
                connect_args={
                    "command_timeout": 15,
                    "server_settings": {
                        "application_name": "marketing_module",
                    }
                },
                echo=False,
            )
            self._session_factory = sessionmaker(
                self._engine, class_=AsyncSession, expire_on_commit=False
            )
        return self._engine
    
    class _AsyncSessionShim:
        """Async-compatible wrapper around a sync SQLAlchemy Session."""
        def __init__(self, session: Session) -> None:
            self._session = session

        async def execute(self, *args, **kwargs):
            return self._session.execute(*args, **kwargs)

        async def commit(self) -> None:
            self._session.commit()

        async def refresh(self, *args, **kwargs) -> None:
            self._session.refresh(*args, **kwargs)

        async def merge(self, *args, **kwargs):
            return self._session.merge(*args, **kwargs)

        async def delete(self, *args, **kwargs) -> None:
            self._session.delete(*args, **kwargs)

        def add(self, *args, **kwargs) -> None:
            self._session.add(*args, **kwargs)

        def close(self) -> None:
            self._session.close()

    @asynccontextmanager
    async def _get_session(self):
        """Get database session (sync or async) as an async context manager."""
        if self._use_sync:
            session = self._get_sync_session()
            shim = self._AsyncSessionShim(session)
            try:
                yield shim
            finally:
                session.close()
        else:
            async with self._session_factory() as session:
                yield session
    
    async def initialize_tables(self) -> None:
        """Create all marketing tables."""
        if self._use_sync:
            # Use sync engine
            MarketingBase.metadata.create_all(bind=self._engine)
        else:
            # Use async engine
            engine = await self._get_async_engine()
            async with engine.begin() as conn:
                await conn.run_sync(MarketingBase.metadata.create_all)
    
    # ==================== Voice Profile ====================
    
    async def get_active_voice_profile(self) -> Optional[BrandVoiceProfile]:
        """Get the active voice profile."""
        async with self._get_session() as session:
            result = await session.execute(
                select(BrandVoiceProfile).where(BrandVoiceProfile.is_active == True)
            )
            return result.scalar_one_or_none()
    
    async def save_voice_profile(self, profile: BrandVoiceProfile) -> BrandVoiceProfile:
        """Save or update a voice profile."""
        async with self._get_session() as session:
            if profile.id:
                await session.merge(profile)
            else:
                session.add(profile)
            await session.commit()
            await session.refresh(profile)
            return profile
    
    # ==================== Strategies ====================
    
    async def get_strategy(self, strategy_id: int) -> Optional[MarketingStrategy]:
        """Get a strategy by ID."""
        async with self._get_session() as session:
            result = await session.execute(
                select(MarketingStrategy).where(MarketingStrategy.id == strategy_id)
            )
            return result.scalar_one_or_none()
    
    async def get_active_strategies(self) -> Dict[str, MarketingStrategy]:
        """Get all active strategies by type."""
        async with self._get_session() as session:
            result = await session.execute(
                select(MarketingStrategy).where(MarketingStrategy.status == "active")
            )
            strategies = result.scalars().all()
            return {s.strategy_type: s for s in strategies}
    
    async def save_strategy(self, strategy: MarketingStrategy) -> MarketingStrategy:
        """Save or update a strategy."""
        async with self._get_session() as session:
            if strategy.id:
                await session.merge(strategy)
            else:
                session.add(strategy)
            await session.commit()
            await session.refresh(strategy)
            return strategy
    
    async def list_strategies(
        self,
        strategy_type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 10
    ) -> List[MarketingStrategy]:
        """List strategies with optional filters."""
        async with self._get_session() as session:
            query = select(MarketingStrategy)
            
            conditions = []
            if strategy_type:
                conditions.append(MarketingStrategy.strategy_type == strategy_type)
            if status:
                conditions.append(MarketingStrategy.status == status)
            
            if conditions:
                query = query.where(and_(*conditions))
            
            query = query.order_by(MarketingStrategy.created_at.desc()).limit(limit)
            
            result = await session.execute(query)
            return list(result.scalars().all())
    
    # ==================== Meetings ====================
    
    async def get_meeting(self, meeting_id: int) -> Optional[TeamMeeting]:
        """Get a meeting by ID."""
        async with self._get_session() as session:
            result = await session.execute(
                select(TeamMeeting).where(TeamMeeting.id == meeting_id)
            )
            return result.scalar_one_or_none()
    
    async def save_meeting(self, meeting: TeamMeeting) -> TeamMeeting:
        """Save or update a meeting."""
        try:
            async with self._get_session() as session:
                if meeting.id:
                    meeting = await session.merge(meeting)
                else:
                    session.add(meeting)
                await session.commit()
                await session.refresh(meeting)
                return meeting
        except Exception as e:
            # Log error but don't fail silently
            import traceback
            print(f"❌ Error saving meeting: {e}")
            traceback.print_exc()
            raise
    
    async def list_meetings(
        self,
        meeting_type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 10
    ) -> List[TeamMeeting]:
        """List meetings with optional filters."""
        async with self._get_session() as session:
            query = select(TeamMeeting)
            
            conditions = []
            if meeting_type:
                conditions.append(TeamMeeting.meeting_type == meeting_type)
            if status:
                conditions.append(TeamMeeting.status == status)
            
            if conditions:
                query = query.where(and_(*conditions))
            
            query = query.order_by(TeamMeeting.created_at.desc()).limit(limit)
            
            result = await session.execute(query)
            return list(result.scalars().all())
    
    # ==================== Content ====================
    
    async def get_content(self, content_id: int) -> Optional[GeneratedContent]:
        """Get content by ID."""
        async with self._get_session() as session:
            result = await session.execute(
                select(GeneratedContent).where(GeneratedContent.id == content_id)
            )
            return result.scalar_one_or_none()
    
    async def save_content(self, content: GeneratedContent) -> GeneratedContent:
        """Save or update content."""
        async with self._get_session() as session:
            if content.id:
                content = await session.merge(content)
            else:
                session.add(content)
            await session.commit()
            await session.refresh(content)
            return content
    
    async def list_content(
        self,
        status: Optional[str] = None,
        platform: Optional[str] = None,
        content_type: Optional[str] = None,
        limit: int = 20
    ) -> List[GeneratedContent]:
        """List content with optional filters."""
        async with self._get_session() as session:
            query = select(GeneratedContent)
            
            conditions = []
            if status:
                conditions.append(GeneratedContent.status == status)
            if platform:
                conditions.append(GeneratedContent.platform == platform)
            if content_type:
                conditions.append(GeneratedContent.content_type == content_type)
            
            if conditions:
                query = query.where(and_(*conditions))
            
            query = query.order_by(GeneratedContent.created_at.desc()).limit(limit)
            
            result = await session.execute(query)
            return list(result.scalars().all())
    
    async def get_content_queue(self, limit: int = 20) -> List[GeneratedContent]:
        """Get content pending review."""
        async with self._get_session() as session:
            result = await session.execute(
                select(GeneratedContent)
                .where(GeneratedContent.status.in_(["draft", "review"]))
                .order_by(GeneratedContent.created_at.desc())
                .limit(limit)
            )
            return list(result.scalars().all())
    
    # ==================== Calendar ====================
    
    async def get_calendar_item(self, item_id: int) -> Optional[ContentCalendar]:
        """Get a calendar item by ID."""
        async with self._get_session() as session:
            result = await session.execute(
                select(ContentCalendar).where(ContentCalendar.id == item_id)
            )
            return result.scalar_one_or_none()
    
    async def save_calendar_item(self, item: ContentCalendar) -> ContentCalendar:
        """Save or update a calendar item."""
        async with self._get_session() as session:
            if item.id:
                await session.merge(item)
            else:
                session.add(item)
            await session.commit()
            await session.refresh(item)
            return item
    
    async def get_calendar_range(
        self,
        start_date: date,
        end_date: date,
        platform: Optional[str] = None
    ) -> List[ContentCalendar]:
        """Get calendar items in a date range."""
        async with self._get_session() as session:
            query = select(ContentCalendar).where(
                and_(
                    ContentCalendar.scheduled_date >= start_date,
                    ContentCalendar.scheduled_date <= end_date,
                )
            )
            
            if platform:
                query = query.where(ContentCalendar.platform == platform)
            
            query = query.order_by(ContentCalendar.scheduled_date)
            
            result = await session.execute(query)
            return list(result.scalars().all())
    
    async def close(self) -> None:
        """Close database connections."""
        if self._engine:
            await self._engine.dispose()
            self._engine = None


# Singleton instance
_repository: Optional[SQLAlchemyMarketingRepository] = None


def get_marketing_repository() -> SQLAlchemyMarketingRepository:
    """Get marketing repository singleton."""
    global _repository
    if _repository is None:
        _repository = SQLAlchemyMarketingRepository()
    return _repository
