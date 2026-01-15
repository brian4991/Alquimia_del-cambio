"""
Embedding Service.

Provides text embedding functionality using Azure OpenAI.
Used for indexing documents and similarity search.
"""

from typing import List, Optional
from marketing.services.llm.azure_openai_client import (
    AzureOpenAIClient,
    get_azure_openai_client,
)


class EmbeddingService:
    """
    Service for creating text embeddings.
    
    Uses Azure OpenAI's text-embedding-ada-002 model.
    """
    
    def __init__(self, client: Optional[AzureOpenAIClient] = None) -> None:
        """
        Initialize embedding service.
        
        Args:
            client: Azure OpenAI client. If None, uses singleton.
        """
        self._client = client or get_azure_openai_client()
    
    async def embed_text(self, text: str) -> List[float]:
        """
        Create embedding for a single text.
        
        Args:
            text: Text to embed.
            
        Returns:
            Embedding vector (1536 dimensions for ada-002).
        """
        response = await self._client.create_embedding(text)
        return response.embedding
    
    async def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for multiple texts.
        
        Args:
            texts: List of texts to embed.
            
        Returns:
            List of embedding vectors.
        """
        responses = await self._client.create_embeddings_batch(texts)
        return [r.embedding for r in responses]
    
    async def embed_document(
        self,
        content: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ) -> List[tuple[str, List[float]]]:
        """
        Embed a document by splitting into chunks.
        
        Args:
            content: Document content.
            chunk_size: Maximum characters per chunk.
            chunk_overlap: Overlap between chunks.
            
        Returns:
            List of (chunk_text, embedding) tuples.
        """
        chunks = self._split_text(content, chunk_size, chunk_overlap)
        embeddings = await self.embed_texts(chunks)
        return list(zip(chunks, embeddings))
    
    def _split_text(
        self,
        text: str,
        chunk_size: int,
        chunk_overlap: int
    ) -> List[str]:
        """
        Split text into overlapping chunks.
        
        Args:
            text: Text to split.
            chunk_size: Maximum characters per chunk.
            chunk_overlap: Overlap between chunks.
            
        Returns:
            List of text chunks.
        """
        if len(text) <= chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            
            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence endings
                for sep in ['. ', '.\n', '! ', '!\n', '? ', '?\n']:
                    last_sep = text[start:end].rfind(sep)
                    if last_sep != -1:
                        end = start + last_sep + len(sep)
                        break
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            start = end - chunk_overlap
        
        return chunks


# Singleton instance
_embedding_service: Optional[EmbeddingService] = None


def get_embedding_service() -> EmbeddingService:
    """Get embedding service singleton."""
    global _embedding_service
    if _embedding_service is None:
        _embedding_service = EmbeddingService()
    return _embedding_service
