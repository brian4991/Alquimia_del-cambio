"""
Meeting Result Entity.

Structure for the final output of a team meeting.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ProposedOption(BaseModel):
    """
    Option proposed to Nicole for decision.
    """
    
    option_id: str = Field(
        ...,
        description="Unique identifier (A, B, C, etc.)"
    )
    
    title: str = Field(
        ...,
        description="Short title for the option"
    )
    
    description: str = Field(
        ...,
        description="Detailed description"
    )
    
    pros: List[str] = Field(
        default_factory=list,
        description="Advantages of this option"
    )
    
    cons: List[str] = Field(
        default_factory=list,
        description="Disadvantages or risks"
    )
    
    supported_by: List[str] = Field(
        default_factory=list,
        description="Agents who support this option"
    )
    
    content_preview: Optional[str] = Field(
        default=None,
        description="Preview of content if applicable"
    )
    
    visual_brief: Optional[str] = Field(
        default=None,
        description="Visual brief if applicable"
    )


class MeetingResult(BaseModel):
    """
    Final result of a team meeting.
    
    Presented to Nicole for decision or information.
    """
    
    meeting_id: int = Field(
        ...,
        description="Associated meeting ID"
    )
    
    meeting_type: str = Field(
        ...,
        description="Type of meeting"
    )
    
    # Summary
    executive_summary: str = Field(
        ...,
        description="Brief summary of the meeting (3-4 lines)"
    )
    
    # Consensus points
    consensus_points: List[str] = Field(
        default_factory=list,
        description="Points where team agreed"
    )
    
    divergence_points: List[str] = Field(
        default_factory=list,
        description="Points where team disagreed"
    )
    
    # Options for decision
    options: List[ProposedOption] = Field(
        default_factory=list,
        description="Options for Nicole to choose from"
    )
    
    # Coordinator recommendation
    coordinator_recommendation: Optional[str] = Field(
        default=None,
        description="Coordinator's recommended option"
    )
    
    recommendation_reasoning: Optional[str] = Field(
        default=None,
        description="Why the coordinator recommends this option"
    )
    
    # Generated outputs (if any)
    generated_content: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Content generated during the meeting"
    )
    
    generated_strategies: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Strategies generated during the meeting"
    )
    
    calendar_suggestions: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Calendar entries suggested"
    )
    
    # Status
    requires_decision: bool = Field(
        default=True,
        description="Whether Nicole needs to make a decision"
    )
    
    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "meeting_id": 1,
                "meeting_type": "brainstorm",
                "executive_summary": "El equipo generó 3 conceptos para la campaña del retiro...",
                "consensus_points": ["Enfoque en testimonios", "Tono emocional"],
                "divergence_points": ["Timing de lanzamiento"],
                "options": [],
                "coordinator_recommendation": "A",
                "requires_decision": True,
            }
        }
    
    def format_for_display(self) -> str:
        """
        Format the result for display to Nicole.
        
        Returns:
            Formatted string for UI display.
        """
        parts = [
            f"## Resumen de la Reunión ({self.meeting_type.title()})",
            "",
            self.executive_summary,
            "",
        ]
        
        if self.consensus_points:
            parts.append("### Puntos de Consenso")
            for point in self.consensus_points:
                parts.append(f"- {point}")
            parts.append("")
        
        if self.divergence_points:
            parts.append("### Puntos de Divergencia")
            for point in self.divergence_points:
                parts.append(f"- {point}")
            parts.append("")
        
        if self.options:
            parts.append("### Opciones Propuestas")
            for opt in self.options:
                parts.append(f"\n**Opción {opt.option_id}: {opt.title}**")
                parts.append(opt.description)
                if opt.pros:
                    parts.append(f"✓ Pros: {', '.join(opt.pros)}")
                if opt.cons:
                    parts.append(f"✗ Contras: {', '.join(opt.cons)}")
            parts.append("")
        
        if self.coordinator_recommendation:
            parts.append(f"### Recomendación del Coordinador")
            parts.append(f"Opción recomendada: **{self.coordinator_recommendation}**")
            if self.recommendation_reasoning:
                parts.append(f"Razón: {self.recommendation_reasoning}")
        
        return "\n".join(parts)
