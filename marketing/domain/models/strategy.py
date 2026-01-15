"""
Marketing Strategy Model.

Stores marketing strategies for short, medium, and long term.
"""

from datetime import datetime, date
from typing import List, Optional, Dict, Any
from enum import Enum
from sqlalchemy import Column, Integer, String, Text, DateTime, Date, JSON, ForeignKey
from sqlalchemy.sql import func

from marketing.domain.models.base import MarketingBase


class StrategyType(str, Enum):
    """Strategy time horizon."""
    SHORT = "short"      # 1-2 weeks
    MEDIUM = "medium"    # 1-3 months
    LONG = "long"        # 6-12 months


class MarketingStrategy(MarketingBase):
    """
    Marketing strategy for a specific time period.
    
    Defines objectives, content pillars, and target metrics.
    """
    
    __tablename__ = "marketing_strategies"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Strategy type and period
    strategy_type = Column(String(20), nullable=False)
    """Type: short, medium, or long term"""
    
    period_start = Column(Date, nullable=False)
    """Start date of the strategy period"""
    
    period_end = Column(Date, nullable=False)
    """End date of the strategy period"""
    
    # Strategy content
    title = Column(String(200), nullable=False)
    """Strategy title/name"""
    
    objectives = Column(JSON, nullable=False, default=list)
    """List of objectives for this period"""
    
    target_metrics = Column(JSON, nullable=True, default=dict)
    """Target KPIs (e.g., {"followers": 1000, "engagement_rate": 5})"""
    
    content_pillars = Column(JSON, nullable=False, default=list)
    """Content pillars/themes for this period"""
    
    key_messages = Column(JSON, nullable=True, default=list)
    """Key messages to communicate"""
    
    campaigns = Column(JSON, nullable=True, default=list)
    """Planned campaigns within this strategy"""
    
    # Status
    status = Column(String(20), default="draft")
    """Status: draft, active, completed, archived"""
    
    # Relationships
    created_by_meeting_id = Column(Integer, ForeignKey("marketing_meetings.id"), nullable=True)
    """Meeting that created this strategy"""
    
    # Timestamps
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "strategy_type": self.strategy_type,
            "period_start": self.period_start.isoformat() if self.period_start else None,
            "period_end": self.period_end.isoformat() if self.period_end else None,
            "title": self.title,
            "objectives": self.objectives,
            "target_metrics": self.target_metrics,
            "content_pillars": self.content_pillars,
            "key_messages": self.key_messages,
            "campaigns": self.campaigns,
            "status": self.status,
            "created_by_meeting_id": self.created_by_meeting_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_summary(self) -> str:
        """
        Get a summary of the strategy for prompts.
        
        Returns:
            Formatted string describing the strategy.
        """
        parts = [
            f"Estrategia {self.strategy_type}: {self.title}",
            f"Periodo: {self.period_start} - {self.period_end}",
        ]
        
        if self.objectives:
            parts.append(f"Objetivos: {', '.join(self.objectives)}")
        
        if self.content_pillars:
            parts.append(f"Pilares de contenido: {', '.join(self.content_pillars)}")
        
        if self.key_messages:
            parts.append(f"Mensajes clave: {', '.join(self.key_messages)}")
        
        return "\n".join(parts)
