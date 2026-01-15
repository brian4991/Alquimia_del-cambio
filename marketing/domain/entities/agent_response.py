"""
Agent Response Entity.

Structure for agent responses in debates and content generation.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    """
    Response structure for all marketing agents.
    
    Standardizes how agents communicate their proposals,
    critiques, and suggestions.
    """
    
    agent_role: str = Field(
        ...,
        description="Role of the responding agent"
    )
    
    content: str = Field(
        ...,
        description="Main content of the response"
    )
    
    response_type: str = Field(
        default="proposal",
        description="Type: proposal, critique, suggestion, synthesis"
    )
    
    confidence: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Confidence level (0-1)"
    )
    
    reasoning: Optional[str] = Field(
        default=None,
        description="Explanation of the reasoning"
    )
    
    suggestions: List[str] = Field(
        default_factory=list,
        description="Additional suggestions or alternatives"
    )
    
    agreement_level: Optional[int] = Field(
        default=None,
        ge=1,
        le=10,
        description="Agreement level with current proposal (1-10)"
    )
    
    concerns: List[str] = Field(
        default_factory=list,
        description="Concerns or potential issues"
    )
    
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )
    
    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "agent_role": "copywriter",
                "content": "Propongo el siguiente hook: '¿Sabías que el 80% de tus emociones...'",
                "response_type": "proposal",
                "confidence": 0.85,
                "reasoning": "Este hook usa una estadística para captar atención inmediata",
                "suggestions": ["Alternativa: '3 señales de que necesitas...'"],
                "agreement_level": 8,
                "concerns": ["Verificar la estadística antes de publicar"],
            }
        }
    
    def to_debate_entry(self) -> Dict[str, Any]:
        """
        Convert to debate log entry format.
        
        Returns:
            Dict suitable for storing in meeting debate_log.
        """
        return {
            "agent": self.agent_role,
            "type": self.response_type,
            "content": self.content,
            "confidence": self.confidence,
            "reasoning": self.reasoning,
            "suggestions": self.suggestions,
            "agreement_level": self.agreement_level,
            "concerns": self.concerns,
        }
