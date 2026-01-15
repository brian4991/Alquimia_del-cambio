"""
Azure AI Search Vector Store Service.

Alternative to pgvector using Azure AI Search for vector similarity search.
Better integration with Azure ecosystem and more features.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel
import httpx
import json

from marketing.config import get_azure_config
from marketing.services.memory.embedding_service import (
    EmbeddingService,
    get_embedding_service,
)


class Document(BaseModel):
    """Document structure for vector store."""
    id: Optional[str] = None
    content: str
    metadata: Dict[str, Any] = {}
    embedding: Optional[List[float]] = None
    created_at: Optional[datetime] = None


class SearchResult(BaseModel):
    """Search result with similarity score."""
    document: Document
    score: float  # Relevance score (0-1, higher is better)


class AzureSearchStoreService:
    """
    Vector store service using Azure AI Search.
    
    Provides document indexing and similarity search for RAG.
    """
    
    def __init__(
        self,
        embedding_service: Optional[EmbeddingService] = None,
        search_service_name: Optional[str] = None,
        search_api_key: Optional[str] = None,
        index_name: Optional[str] = None,
    ) -> None:
        """
        Initialize Azure Search store service.
        
        Args:
            embedding_service: Service for creating embeddings.
            search_service_name: Azure Search service name.
            search_api_key: Azure Search API key.
            index_name: Name of the search index.
        """
        self._embedding_service = embedding_service or get_embedding_service()
        self._azure_config = get_azure_config()
        
        # Azure Search config from env or parameters
        self._search_service_name = search_service_name or self._get_env("AZURE_SEARCH_SERVICE_NAME", "your-search-service")
        self._search_api_key = search_api_key or self._get_env("AZURE_SEARCH_API_KEY", "")
        self._index_name = index_name or self._get_env("AZURE_SEARCH_INDEX_NAME", "marketing-content")
        
        self._search_endpoint = f"https://{self._search_service_name}.search.windows.net"
        self._api_version = "2023-11-01"
    
    def _get_env(self, key: str, default: str) -> str:
        """Get environment variable."""
        import os
        return os.getenv(key, default)
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get HTTP client for Azure Search API."""
        return httpx.AsyncClient(
            base_url=self._search_endpoint,
            headers={
                "api-key": self._search_api_key,
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )
    
    async def initialize(self) -> None:
        """
        Initialize the Azure Search index.
        
        Creates the index if it doesn't exist.
        """
        async with await self._get_client() as client:
            # Check if index exists
            try:
                response = await client.get(
                    f"/indexes/{self._index_name}",
                    params={"api-version": self._api_version}
                )
                if response.status_code == 200:
                    return  # Index already exists
            except:
                pass
            
            # Create index schema
            index_schema = {
                "name": self._index_name,
                "fields": [
                    {
                        "name": "id",
                        "type": "Edm.String",
                        "key": True,
                    },
                    {
                        "name": "content",
                        "type": "Edm.String",
                        "searchable": True,
                        "analyzer": "standard.lucene",
                    },
                    {
                        "name": "contentVector",
                        "type": "Collection(Edm.Single)",
                        "dimensions": 1536,  # text-embedding-ada-002 dimension
                        "vectorSearchProfile": "default-vector-profile",
                    },
                    {
                        "name": "metadata",
                        "type": "Edm.String",
                        "searchable": False,
                    },
                    {
                        "name": "type",
                        "type": "Edm.String",
                        "filterable": True,
                        "facetable": True,
                    },
                    {
                        "name": "source",
                        "type": "Edm.String",
                        "filterable": True,
                    },
                    {
                        "name": "created_at",
                        "type": "Edm.DateTimeOffset",
                        "filterable": True,
                    },
                ],
                "vectorSearch": {
                    "profiles": [
                        {
                            "name": "default-vector-profile",
                            "algorithm": "default-algorithm",
                        }
                    ],
                    "algorithms": [
                        {
                            "name": "default-algorithm",
                            "kind": "hnsw",
                            "parameters": {
                                "m": 4,
                                "efConstruction": 400,
                                "efSearch": 500,
                            }
                        }
                    ],
                },
            }
            
            # Create index
            response = await client.put(
                f"/indexes/{self._index_name}",
                params={"api-version": self._api_version},
                json=index_schema
            )
            
            if response.status_code not in [200, 201]:
                raise Exception(f"Failed to create index: {response.text}")
    
    async def add_document(
        self,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Document:
        """
        Add a document to the index.
        
        Args:
            content: Document content.
            metadata: Optional metadata.
            
        Returns:
            Created document.
        """
        # Generate embedding
        embedding = await self._embedding_service.create_embedding(content)
        
        # Create document
        doc_id = metadata.get("id") if metadata else None
        if not doc_id:
            import uuid
            doc_id = str(uuid.uuid4())
        
        document = {
            "id": doc_id,
            "content": content,
            "contentVector": embedding,
            "metadata": json.dumps(metadata or {}),
            "type": metadata.get("type", "unknown") if metadata else "unknown",
            "source": metadata.get("source", "unknown") if metadata else "unknown",
            "created_at": datetime.now().isoformat(),
        }
        
        # Upload to Azure Search
        async with await self._get_client() as client:
            response = await client.post(
                f"/indexes/{self._index_name}/docs/index",
                params={"api-version": self._api_version},
                json={"value": [document]}
            )
            
            if response.status_code not in [200, 201]:
                raise Exception(f"Failed to add document: {response.text}")
        
        return Document(
            id=doc_id,
            content=content,
            metadata=metadata or {},
            embedding=embedding,
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
        Search for similar documents.
        
        Args:
            query: Search query.
            limit: Maximum results.
            doc_types: Filter by document types.
            min_score: Minimum relevance score.
            
        Returns:
            List of search results.
        """
        # Generate query embedding
        query_embedding = await self._embedding_service.embed_text(query)
        
        # Build filter
        filters = []
        if doc_types:
            type_filter = " or ".join([f"type eq '{t}'" for t in doc_types])
            filters.append(f"({type_filter})")
        
        filter_str = " and ".join(filters) if filters else None
        
        # Build search request
        search_request = {
            "vector": {
                "value": query_embedding,
                "kNearestNeighborsCount": limit,
                "fields": "contentVector",
            },
            "select": "id,content,metadata,type,source,created_at",
            "top": limit,
        }
        
        if filter_str:
            search_request["filter"] = filter_str
        
        # Execute search
        async with await self._get_client() as client:
            response = await client.post(
                f"/indexes/{self._index_name}/docs/search",
                params={"api-version": self._api_version},
                json=search_request
            )
            
            if response.status_code != 200:
                raise Exception(f"Search failed: {response.text}")
            
            results_data = response.json()
        
        # Convert to SearchResult objects
        results = []
        for hit in results_data.get("value", []):
            score = hit.get("@search.score", 0.0) / 100.0  # Normalize score
            
            if score < min_score:
                continue
            
            try:
                metadata = json.loads(hit.get("metadata", "{}"))
            except:
                metadata = {}
            
            document = Document(
                id=hit.get("id"),
                content=hit.get("content", ""),
                metadata=metadata,
                created_at=datetime.fromisoformat(hit.get("created_at", datetime.now().isoformat())),
            )
            
            results.append(SearchResult(document=document, score=score))
        
        return results
    
    async def clear_collection(self) -> int:
        """Clear all documents from the index."""
        # Delete all documents by querying and deleting
        async with await self._get_client() as client:
            # Search for all documents
            response = await client.get(
                f"/indexes/{self._index_name}/docs",
                params={
                    "api-version": self._api_version,
                    "$select": "id",
                    "$top": 10000,
                }
            )
            
            if response.status_code != 200:
                return 0
            
            docs = response.json().get("value", [])
            
            if not docs:
                return 0
            
            # Delete all documents
            delete_actions = [{"@search.action": "delete", "id": doc["id"]} for doc in docs]
            
            response = await client.post(
                f"/indexes/{self._index_name}/docs/index",
                params={"api-version": self._api_version},
                json={"value": delete_actions}
            )
            
            return len(delete_actions) if response.status_code in [200, 201] else 0
    
    async def get_stats(self) -> Dict[str, Any]:
        """Get index statistics."""
        async with await self._get_client() as client:
            response = await client.get(
                f"/indexes/{self._index_name}/stats",
                params={"api-version": self._api_version}
            )
            
            if response.status_code != 200:
                return {"error": "Failed to get stats"}
            
            return response.json()


# Factory function
def get_azure_search_store(
    search_service_name: Optional[str] = None,
    search_api_key: Optional[str] = None,
    index_name: Optional[str] = None,
) -> AzureSearchStoreService:
    """Create Azure Search store instance."""
    return AzureSearchStoreService(
        search_service_name=search_service_name,
        search_api_key=search_api_key,
        index_name=index_name,
    )
