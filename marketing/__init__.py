"""
Marketing Team Agentique - Module Principal

Equipe marketing virtuelle de 7 agents IA autonomes qui collaborent,
debattent et s'organisent via LangGraph.

Architecture hub-and-spoke avec un Coordinateur central,
memoire hybride (DB + vector store).
"""

__version__ = "1.0.0"
__author__ = "Alquimia del Cambio"

# Public API exports
from marketing.api.router import marketing_router

__all__ = ["marketing_router"]
