"""
Agent Configuration.

Configuration class for individual agents.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    """
    Configuration for a marketing agent.
    
    Defines the agent's behavior, capabilities, and constraints.
    """
    
    role: str = Field(
        ...,
        description="Agent's role identifier"
    )
    
    display_name: str = Field(
        ...,
        description="Human-readable name for display"
    )
    
    description: str = Field(
        ...,
        description="Description of the agent's responsibilities"
    )
    
    # LLM settings
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="LLM temperature for this agent"
    )
    
    max_tokens: int = Field(
        default=2000,
        description="Maximum tokens in response"
    )
    
    # Behavior settings
    can_propose: bool = Field(
        default=True,
        description="Whether agent can make proposals"
    )
    
    can_critique: bool = Field(
        default=True,
        description="Whether agent can critique others"
    )
    
    can_generate_content: bool = Field(
        default=False,
        description="Whether agent can generate final content"
    )
    
    # Memory settings
    use_voice_profile: bool = Field(
        default=True,
        description="Whether to include voice profile in context"
    )
    
    use_strategy_context: bool = Field(
        default=True,
        description="Whether to include active strategy in context"
    )
    
    rag_search_types: List[str] = Field(
        default_factory=lambda: ["transcript", "program_guide"],
        description="Document types to search in RAG"
    )
    
    rag_results_limit: int = Field(
        default=3,
        description="Maximum RAG results to include"
    )
    
    # Additional settings
    custom_settings: Dict[str, Any] = Field(
        default_factory=dict,
        description="Agent-specific custom settings"
    )
    
    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "role": "copywriter",
                "display_name": "Copywriter",
                "description": "Especialista en redacción de textos persuasivos",
                "temperature": 0.8,
                "can_generate_content": True,
            }
        }


# Pre-defined configurations for each agent
AGENT_CONFIGS = {
    "strategist": AgentConfig(
        role="strategist",
        display_name="Estratega",
        description="Define estrategias de marketing y objetivos",
        temperature=0.6,
        can_generate_content=False,
        rag_search_types=["program_guide"],
    ),
    "content_lead": AgentConfig(
        role="content_lead",
        display_name="Content Lead",
        description="Desarrolla estructura narrativa y storytelling",
        temperature=0.7,
        can_generate_content=True,
        rag_search_types=["transcript", "program_guide"],
    ),
    "creative_director": AgentConfig(
        role="creative_director",
        display_name="Director Creativo",
        description="Define dirección visual y briefs para Canva",
        temperature=0.8,
        can_generate_content=True,
        rag_search_types=["transcript"],
    ),
    "community_manager": AgentConfig(
        role="community_manager",
        display_name="Community Manager",
        description="Optimiza timing y engagement por plataforma",
        temperature=0.6,
        can_generate_content=False,
        rag_search_types=["transcript"],
    ),
    "analyst": AgentConfig(
        role="analyst",
        display_name="Analista",
        description="Evalúa propuestas con enfoque data-driven",
        temperature=0.5,
        can_generate_content=False,
        rag_search_types=[],
    ),
    "copywriter": AgentConfig(
        role="copywriter",
        display_name="Copywriter",
        description="Escribe captions, hooks y CTAs",
        temperature=0.8,
        can_generate_content=True,
        rag_search_types=["transcript"],
    ),
    "brand_guardian": AgentConfig(
        role="brand_guardian",
        display_name="Guardián de Marca",
        description="Valida coherencia con la voz de Nicole",
        temperature=0.5,
        can_critique=True,
        can_propose=False,
        can_generate_content=False,
        rag_search_types=["transcript"],
    ),
    "coordinator": AgentConfig(
        role="coordinator",
        display_name="Coordinador",
        description="Orquesta reuniones y sintetiza debates",
        temperature=0.6,
        can_propose=False,
        can_critique=False,
        can_generate_content=False,
        use_voice_profile=True,
        use_strategy_context=True,
    ),
}


def get_agent_config(role: str) -> AgentConfig:
    """
    Get configuration for an agent by role.
    
    Args:
        role: Agent role identifier.
        
    Returns:
        AgentConfig for the specified role.
        
    Raises:
        ValueError: If role is unknown.
    """
    config = AGENT_CONFIGS.get(role)
    if config is None:
        raise ValueError(f"Unknown agent role: {role}")
    return config
