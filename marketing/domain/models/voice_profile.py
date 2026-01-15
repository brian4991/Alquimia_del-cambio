"""
Brand Voice Profile Model.

Stores the analyzed voice/style characteristics of Nicole.
Generated from transcript analysis and updated over time.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Boolean
from sqlalchemy.sql import func

from marketing.domain.models.base import MarketingBase


class BrandVoiceProfile(MarketingBase):
    """
    Brand voice profile for Nicole Ramirez.
    
    Contains analyzed characteristics from transcripts and content
    to ensure generated content matches her authentic voice.
    """
    
    __tablename__ = "marketing_voice_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Voice characteristics
    tone_descriptors = Column(JSON, nullable=False, default=list)
    """List of tone descriptors (e.g., ["empoderador", "calido", "profesional"])"""
    
    vocabulary_frequent = Column(JSON, nullable=False, default=list)
    """Frequently used words and phrases"""
    
    expressions_cles = Column(JSON, nullable=False, default=list)
    """Key expressions and catchphrases"""
    
    topics_principaux = Column(JSON, nullable=False, default=list)
    """Main topics she discusses"""
    
    style_guidelines = Column(Text, nullable=True)
    """Free-form style guidelines text"""
    
    # Analysis metadata
    analyzed_transcripts_count = Column(Integer, default=0)
    """Number of transcripts analyzed"""
    
    analyzed_content_count = Column(Integer, default=0)
    """Number of program content pieces analyzed"""
    
    # Status
    is_active = Column(Boolean, default=True)
    """Whether this is the active voice profile"""
    
    # Timestamps
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "tone_descriptors": self.tone_descriptors,
            "vocabulary_frequent": self.vocabulary_frequent,
            "expressions_cles": self.expressions_cles,
            "topics_principaux": self.topics_principaux,
            "style_guidelines": self.style_guidelines,
            "analyzed_transcripts_count": self.analyzed_transcripts_count,
            "analyzed_content_count": self.analyzed_content_count,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def get_voice_summary(self) -> str:
        """
        Get a summary of the voice profile for prompts.
        
        Returns:
            Formatted string describing the voice characteristics.
        """
        parts = []
        
        if self.tone_descriptors:
            parts.append(f"Tono: {', '.join(self.tone_descriptors)}")
        
        if self.vocabulary_frequent:
            vocab_sample = self.vocabulary_frequent[:10]
            parts.append(f"Vocabulario frecuente: {', '.join(vocab_sample)}")
        
        if self.expressions_cles:
            expr_sample = self.expressions_cles[:5]
            parts.append(f"Expresiones clave: {', '.join(expr_sample)}")
        
        if self.topics_principaux:
            parts.append(f"Temas principales: {', '.join(self.topics_principaux)}")
        
        if self.style_guidelines:
            parts.append(f"Guia de estilo: {self.style_guidelines}")
        
        return "\n".join(parts)
