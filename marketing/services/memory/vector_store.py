"""
Vector Store Service.

Provides vector similarity search using pgvector.
Used for RAG (Retrieval Augmented Generation) to find relevant context.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from marketing.config import get_database_config, get_vector_store_config
from marketing.services.memory.embedding_service import (
    EmbeddingService,
    get_embedding_service,
)


class Document(BaseModel):
    """Document structure for vector store."""
    id: Optional[int] = None
    content: str
    metadata: Dict[str, Any] = {}
    embedding: Optional[List[float]] = None
    created_at: Optional[datetime] = None


class SearchResult(BaseModel):
    """Search result with similarity score."""
    document: Document
    score: float  # Cosine similarity (0-1, higher is better)


class VectorStoreService:
    """
    Vector store service using PostgreSQL with pgvector extension.
    
    Provides document indexing and similarity search for RAG.
    """
    
    def __init__(
        self,
        embedding_service: Optional[EmbeddingService] = None,
        collection_name: Optional[str] = None,
    ) -> None:
        """
        Initialize vector store service.
        
        Args:
            embedding_service: Service for creating embeddings.
            collection_name: Name of the collection/table.
        """
        self._embedding_service = embedding_service or get_embedding_service()
        self._config = get_vector_store_config()
        self._db_config = get_database_config()
        self._collection_name = collection_name or self._config.collection_name
        self._engine = None
        self._session_factory = None
    
    async def _get_engine(self):
        """Lazy initialization of async engine."""
        if self._engine is None:
            # Convert sync URL to async
            db_url = self._db_config.url
            if db_url.startswith("postgresql://"):
                db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
            elif not db_url.startswith("postgresql+asyncpg://"):
                db_url = f"postgresql+asyncpg://{db_url.split('://', 1)[1]}"
            
            self._engine = create_async_engine(db_url)
            self._session_factory = sessionmaker(
                self._engine, class_=AsyncSession, expire_on_commit=False
            )
        return self._engine
    
    async def _get_session(self) -> AsyncSession:
        """Get async database session."""
        await self._get_engine()
        return self._session_factory()
    
    async def initialize(self) -> None:
        """
        Initialize the vector store table.
        
        Creates the pgvector extension and documents table if they don't exist.
        """
        async with await self._get_session() as session:
            # Enable pgvector extension
            await session.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            
            # Create documents table
            await session.execute(text(f"""
                CREATE TABLE IF NOT EXISTS {self._collection_name} (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    metadata JSONB DEFAULT '{{}}',
                    embedding vector({self._config.embedding_dimension}),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            
            # Create index for similarity search
            await session.execute(text(f"""
                CREATE INDEX IF NOT EXISTS {self._collection_name}_embedding_idx
                ON {self._collection_name}
                USING ivfflat (embedding vector_cosine_ops)
                WITH (lists = 100)
            """))
            
            await session.commit()
    
    async def add_document(
        self,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Document:
        """
        Add a document to the vector store.
        
        Args:
            content: Document content.
            metadata: Optional metadata dict.
            
        Returns:
            Created document with ID and embedding.
        """
        # Create embedding
        embedding = await self._embedding_service.embed_text(content)
        
        async with await self._get_session() as session:
            result = await session.execute(
                text(f"""
                    INSERT INTO {self._collection_name} (content, metadata, embedding)
                    VALUES (:content, :metadata, :embedding)
                    RETURNING id, created_at
                """),
                {
                    "content": content,
                    "metadata": metadata or {},
                    "embedding": str(embedding),
                }
            )
            row = result.fetchone()
            await session.commit()
            
            return Document(
                id=row[0],
                content=content,
                metadata=metadata or {},
                embedding=embedding,
                created_at=row[1],
            )
    
    async def add_documents(
        self,
        documents: List[tuple[str, Dict[str, Any]]]
    ) -> List[Document]:
        """
        Add multiple documents to the vector store.
        
        Args:
            documents: List of (content, metadata) tuples.
            
        Returns:
            List of created documents.
        """
        # Create embeddings in batch
        contents = [doc[0] for doc in documents]
        embeddings = await self._embedding_service.embed_texts(contents)
        
        results = []
        async with await self._get_session() as session:
            for (content, metadata), embedding in zip(documents, embeddings):
                result = await session.execute(
                    text(f"""
                        INSERT INTO {self._collection_name} (content, metadata, embedding)
                        VALUES (:content, :metadata, :embedding)
                        RETURNING id, created_at
                    """),
                    {
                        "content": content,
                        "metadata": metadata,
                        "embedding": str(embedding),
                    }
                )
                row = result.fetchone()
                results.append(Document(
                    id=row[0],
                    content=content,
                    metadata=metadata,
                    embedding=embedding,
                    created_at=row[1],
                ))
            
            await session.commit()
        
        return results
    
    async def search(
        self,
        query: str,
        limit: int = 5,
        metadata_filter: Optional[Dict[str, Any]] = None
    ) -> List[SearchResult]:
        """
        Search for similar documents.
        
        Args:
            query: Search query text.
            limit: Maximum number of results.
            metadata_filter: Optional filter on metadata fields.
            
        Returns:
            List of search results with similarity scores.
        """
        # Create query embedding
        query_embedding = await self._embedding_service.embed_text(query)
        
        # Build query with optional metadata filter
        where_clause = ""
        params = {
            "embedding": str(query_embedding),
            "limit": limit,
        }
        
        if metadata_filter:
            conditions = []
            for i, (key, value) in enumerate(metadata_filter.items()):
                param_name = f"meta_{i}"
                conditions.append(f"metadata->>'{key}' = :{param_name}")
                params[param_name] = str(value)
            where_clause = "WHERE " + " AND ".join(conditions)
        
        async with await self._get_session() as session:
            result = await session.execute(
                text(f"""
                    SELECT 
                        id, content, metadata, created_at,
                        1 - (embedding <=> :embedding) as similarity
                    FROM {self._collection_name}
                    {where_clause}
                    ORDER BY embedding <=> :embedding
                    LIMIT :limit
                """),
                params
            )
            rows = result.fetchall()
            
            return [
                SearchResult(
                    document=Document(
                        id=row[0],
                        content=row[1],
                        metadata=row[2],
                        created_at=row[3],
                    ),
                    score=row[4],
                )
                for row in rows
            ]
    
    async def search_by_type(
        self,
        query: str,
        doc_type: str,
        limit: int = 5
    ) -> List[SearchResult]:
        """
        Search for similar documents of a specific type.
        
        Args:
            query: Search query text.
            doc_type: Document type (e.g., "transcript", "program", "approved_content").
            limit: Maximum number of results.
            
        Returns:
            List of search results.
        """
        return await self.search(query, limit, metadata_filter={"type": doc_type})
    
    async def delete_document(self, doc_id: int) -> bool:
        """
        Delete a document by ID.
        
        Args:
            doc_id: Document ID.
            
        Returns:
            True if deleted, False if not found.
        """
        async with await self._get_session() as session:
            result = await session.execute(
                text(f"DELETE FROM {self._collection_name} WHERE id = :id"),
                {"id": doc_id}
            )
            await session.commit()
            return result.rowcount > 0
    
    async def clear_collection(self) -> int:
        """
        Clear all documents from the collection.
        
        Returns:
            Number of deleted documents.
        """
        async with await self._get_session() as session:
            result = await session.execute(
                text(f"DELETE FROM {self._collection_name}")
            )
            await session.commit()
            return result.rowcount
    
    async def get_stats(self) -> Dict[str, Any]:
        """
        Get collection statistics.
        
        Returns:
            Dict with document count and type breakdown.
        """
        async with await self._get_session() as session:
            # Total count
            result = await session.execute(
                text(f"SELECT COUNT(*) FROM {self._collection_name}")
            )
            total = result.scalar()
            
            # Count by type
            result = await session.execute(
                text(f"""
                    SELECT metadata->>'type' as doc_type, COUNT(*) as count
                    FROM {self._collection_name}
                    GROUP BY metadata->>'type'
                """)
            )
            type_counts = {row[0] or "unknown": row[1] for row in result.fetchall()}
            
            return {
                "total_documents": total,
                "by_type": type_counts,
            }
    
    async def close(self) -> None:
        """Close database connections."""
        if self._engine:
            await self._engine.dispose()
            self._engine = None


# Singleton instance
_vector_store: Optional[VectorStoreService] = None


def get_vector_store():
    """
    Get vector store singleton.
    
    Returns either pgvector, Azure Search, or Mock based on config.
    """
    global _vector_store
    if _vector_store is None:
        from marketing.config import get_vector_store_config, get_azure_search_config
        
        config = get_vector_store_config()
        
        # Use mock if backend is "mock" or "none"
        if config.backend.lower() in ["mock", "none", "disabled"]:
            from marketing.services.memory.mock_vector_store import (
                MockVectorStoreService,
            )
            _vector_store = MockVectorStoreService()
            return _vector_store
        
        # Use Azure Search if configured
        if config.backend == "azure_search":
            from marketing.services.memory.azure_search_store import (
                AzureSearchStoreService,
            )
            azure_search_config = get_azure_search_config()
            
            if not azure_search_config.service_name or not azure_search_config.api_key:
                print("⚠️  Azure Search not configured, falling back to mock")
                from marketing.services.memory.mock_vector_store import (
                    MockVectorStoreService,
                )
                _vector_store = MockVectorStoreService()
                return _vector_store
            
            _vector_store = AzureSearchStoreService(
                search_service_name=azure_search_config.service_name,
                search_api_key=azure_search_config.api_key,
                index_name=azure_search_config.index_name,
            )
        else:
            # Default to pgvector, but fallback to mock if it fails
            try:
                _vector_store = VectorStoreService()
            except Exception as e:
                print(f"⚠️  pgvector initialization failed: {e}")
                print("⚠️  Falling back to mock vector store")
                from marketing.services.memory.mock_vector_store import (
                    MockVectorStoreService,
                )
                _vector_store = MockVectorStoreService()
    
    return _vector_store
