"""
Mock Vector Store Service.

No-op implementation for testing without vector store.
Returns empty results but doesn't fail.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel

from marketing.services.memory.vector_store import Document, SearchResult


class MockVectorStoreService:
    """
    Mock vector store that does nothing.
    
    Useful for testing without pgvector or Azure Search configured.
    Returns empty results but allows the app to run.
    """
    
    def __init__(self, *args, **kwargs) -> None:
        """Initialize mock vector store (no-op)."""
        pass
    
    async def initialize(self) -> None:
        """Initialize (no-op)."""
        print("⚠️  Using Mock Vector Store - no indexing available")
        pass
    
    async def add_document(
        self,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Document:
        """
        Add document (no-op).
        
        Returns a mock document but doesn't actually store it.
        """
        return Document(
            id=0,
            content=content,
            metadata=metadata or {},
            created_at=datetime.now(),
        )
    
    async def search(
        self,
        query: str,
        limit: int = 5,
        doc_types: Optional[List[str]] = None,
        min_score: float = 0.0,
    ) -> List[SearchResult]:
        """
        Search (returns empty results).
        
        Returns empty list - agents will work without RAG context.
        """
        return []

    async def search_by_type(
        self,
        query: str,
        doc_type: str,
        limit: int = 5,
        min_score: float = 0.0,
    ) -> List[SearchResult]:
        """
        Search by type (returns empty results).
        
        Keeps compatibility with AgentMemory lookups.
        """
        return []
    
    async def clear_collection(self) -> int:
        """Clear collection (no-op)."""
        return 0
    
    async def get_stats(self) -> Dict[str, Any]:
        """Get stats (returns empty stats)."""
        return {
            "total_documents": 0,
            "backend": "mock",
            "note": "Mock vector store - no indexing available"
        }
    
    async def close(self) -> None:
        """Close (no-op)."""
        pass
