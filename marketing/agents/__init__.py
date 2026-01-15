"""Agents layer - Marketing team agents."""

from marketing.agents.base.base_agent import BaseAgent
from marketing.agents.base.agent_config import AgentConfig
from marketing.agents.base.agent_memory import AgentMemory

from marketing.agents.team.strategist import StrategistAgent
from marketing.agents.team.content_lead import ContentLeadAgent
from marketing.agents.team.creative_director import CreativeDirectorAgent
from marketing.agents.team.community_manager import CommunityManagerAgent
from marketing.agents.team.analyst import AnalystAgent
from marketing.agents.team.copywriter import CopywriterAgent
from marketing.agents.team.brand_guardian import BrandGuardianAgent

from marketing.agents.orchestration.coordinator import CoordinatorAgent

__all__ = [
    # Base
    "BaseAgent",
    "AgentConfig",
    "AgentMemory",
    # Team
    "StrategistAgent",
    "ContentLeadAgent",
    "CreativeDirectorAgent",
    "CommunityManagerAgent",
    "AnalystAgent",
    "CopywriterAgent",
    "BrandGuardianAgent",
    # Orchestration
    "CoordinatorAgent",
]
