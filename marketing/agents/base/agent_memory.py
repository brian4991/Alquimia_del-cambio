"""
Agent Memory.

Provides memory access for agents including RAG and context.
"""

from typing import List, Optional, Dict, Any
from marketing.services.memory.vector_store import (
    VectorStoreService,
    get_vector_store,
    SearchResult,
)
from marketing.domain.models.voice_profile import BrandVoiceProfile
from marketing.domain.models.strategy import MarketingStrategy


class AgentMemory:
    """
    Memory interface for marketing agents.
    
    Provides access to:
    - Vector store for RAG
    - Voice profile
    - Active strategies
    - Conversation history
    """
    
    def __init__(
        self,
        vector_store: Optional[VectorStoreService] = None,
    ) -> None:
        """
        Initialize agent memory.
        
        Args:
            vector_store: Vector store service for RAG.
        """
        self._vector_store = vector_store or get_vector_store()
        self._voice_profile: Optional[BrandVoiceProfile] = None
        self._active_strategies: Dict[str, MarketingStrategy] = {}
        self._conversation_history: List[Dict[str, Any]] = []
    
    async def search_relevant_content(
        self,
        query: str,
        doc_types: Optional[List[str]] = None,
        limit: int = 5
    ) -> List[SearchResult]:
        """
        Search for relevant content using RAG.
        
        Returns empty list if vector store is not available (mock mode).
        
        Args:
            query: Search query.
            doc_types: Document types to search (e.g., ["transcript", "program_guide"]).
            limit: Maximum results.
            
        Returns:
            List of relevant search results.
        """
        if doc_types:
            # Search each type and combine results
            all_results = []
            per_type_limit = max(1, limit // len(doc_types))
            
            for doc_type in doc_types:
                results = await self._vector_store.search_by_type(
                    query=query,
                    doc_type=doc_type,
                    limit=per_type_limit
                )
                all_results.extend(results)
            
            # Sort by score and limit
            all_results.sort(key=lambda r: r.score, reverse=True)
            return all_results[:limit]
        else:
            return await self._vector_store.search(query=query, limit=limit)
    
    def set_voice_profile(self, profile: BrandVoiceProfile) -> None:
        """
        Set the active voice profile.
        
        Args:
            profile: Voice profile to use.
        """
        self._voice_profile = profile
    
    def get_voice_profile(self) -> Optional[BrandVoiceProfile]:
        """
        Get the active voice profile.
        
        Returns:
            Current voice profile or None.
        """
        return self._voice_profile
    
    def get_voice_summary(self) -> str:
        """
        Get voice profile summary for prompts.
        
        Returns:
            Formatted voice profile or default message.
        """
        if self._voice_profile:
            return self._voice_profile.get_voice_summary()
        return "No hay perfil de voz disponible."
    
    def set_strategy(self, strategy_type: str, strategy: MarketingStrategy) -> None:
        """
        Set an active strategy.
        
        Args:
            strategy_type: Type (short, medium, long).
            strategy: Strategy instance.
        """
        self._active_strategies[strategy_type] = strategy
    
    def get_strategy(self, strategy_type: str) -> Optional[MarketingStrategy]:
        """
        Get an active strategy by type.
        
        Args:
            strategy_type: Type to retrieve.
            
        Returns:
            Strategy or None.
        """
        return self._active_strategies.get(strategy_type)
    
    def get_strategies_summary(self) -> str:
        """
        Get summary of all active strategies.
        
        Returns:
            Formatted strategies summary.
        """
        if not self._active_strategies:
            return "No hay estrategias activas."
        
        parts = []
        for stype, strategy in self._active_strategies.items():
            parts.append(strategy.get_summary())
        
        return "\n\n".join(parts)
    
    def add_to_history(
        self,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Add entry to conversation history.
        
        Args:
            role: Role (user, assistant, agent).
            content: Content of the message.
            metadata: Additional metadata.
        """
        self._conversation_history.append({
            "role": role,
            "content": content,
            "metadata": metadata or {},
        })
    
    def get_recent_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent conversation history.
        
        Args:
            limit: Maximum entries to return.
            
        Returns:
            Recent history entries.
        """
        return self._conversation_history[-limit:]
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self._conversation_history = []
    
    async def get_context_for_agent(
        self,
        query: str,
        include_voice: bool = True,
        include_strategy: bool = True,
        rag_types: Optional[List[str]] = None,
        rag_limit: int = 3
    ) -> Dict[str, Any]:
        """
        Get full context for an agent.
        
        Args:
            query: Current query/topic for RAG.
            include_voice: Include voice profile.
            include_strategy: Include strategies.
            rag_types: Document types for RAG.
            rag_limit: RAG results limit.
            
        Returns:
            Context dictionary with all relevant information.
        """
        context = {}
        
        # Voice profile
        if include_voice:
            context["voice_profile"] = self.get_voice_summary()
        
        # Strategies
        if include_strategy:
            context["strategies"] = self.get_strategies_summary()
        
        # RAG results
        if rag_types:
            results = await self.search_relevant_content(
                query=query,
                doc_types=rag_types,
                limit=rag_limit
            )
            context["relevant_content"] = [
                {
                    "content": r.document.content[:500],  # Truncate for context
                    "type": r.document.metadata.get("type", "unknown"),
                    "score": r.score,
                }
                for r in results
            ]
        
        # Recent history
        context["recent_history"] = self.get_recent_history(5)
        
        return context


# Singleton instance
_agent_memory: Optional[AgentMemory] = None


def get_agent_memory() -> AgentMemory:
    """Get agent memory singleton."""
    global _agent_memory
    if _agent_memory is None:
        _agent_memory = AgentMemory()
    return _agent_memory
