"""
Compatibility models for Railway deployment
These models work with databases that don't have exercise columns yet
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class ThemeCardCompat(Base):
    """Compatible ThemeCard model without exercise fields"""
    __tablename__ = "theme_cards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    card_type = Column(String(50), default="content")
    order_number = Column(Integer, nullable=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    is_editable = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

def use_compatible_model():
    """Check if we should use the compatible model"""
    import os
    # Use compatible model if on Railway (DATABASE_URL exists)
    return os.environ.get("DATABASE_URL") is not None
