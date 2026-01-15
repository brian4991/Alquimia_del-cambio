"""
Azure OpenAI Client Service.

Provides a unified interface to Azure OpenAI for all agents.
Supports multiple models (GPT-4o, embeddings) with async operations.
"""

from typing import Optional, List, Dict, Any, AsyncGenerator
from openai import AsyncAzureOpenAI
from pydantic import BaseModel

from marketing.config import get_azure_config, AzureOpenAIConfig


class ChatMessage(BaseModel):
    """Chat message structure."""
    role: str  # "system", "user", "assistant"
    content: str


class CompletionResponse(BaseModel):
    """Response from completion API."""
    content: str
    model: str
    usage: Dict[str, int]
    finish_reason: str


class EmbeddingResponse(BaseModel):
    """Response from embedding API."""
    embedding: List[float]
    model: str
    usage: Dict[str, int]


class AzureOpenAIClient:
    """
    Azure OpenAI client with support for chat completions and embeddings.
    
    Provides async methods for all operations to support concurrent agent calls.
    """
    
    def __init__(self, config: Optional[AzureOpenAIConfig] = None) -> None:
        """
        Initialize Azure OpenAI client.
        
        Args:
            config: Azure OpenAI configuration. If None, loads from environment.
        """
        self._config = config or get_azure_config()
        self._client: Optional[AsyncAzureOpenAI] = None
    
    @property
    def client(self) -> AsyncAzureOpenAI:
        """Lazy initialization of async client."""
        if self._client is None:
            self._client = AsyncAzureOpenAI(
                azure_endpoint=self._config.endpoint,
                api_key=self._config.api_key,
                api_version=self._config.api_version,
            )
        return self._client
    
    async def chat_completion(
        self,
        messages: List[ChatMessage],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs: Any
    ) -> CompletionResponse:
        """
        Generate chat completion.
        
        Args:
            messages: List of chat messages.
            model: Model deployment name. Defaults to GPT-4o.
            temperature: Sampling temperature (0-2).
            max_tokens: Maximum tokens in response.
            **kwargs: Additional parameters for the API.
            
        Returns:
            CompletionResponse with generated content.
        """
        deployment = model or self._config.deployment_gpt4o
        
        response = await self.client.chat.completions.create(
            model=deployment,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        
        return CompletionResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                "completion_tokens": response.usage.completion_tokens if response.usage else 0,
                "total_tokens": response.usage.total_tokens if response.usage else 0,
            },
            finish_reason=response.choices[0].finish_reason or "stop"
        )
    
    async def chat_completion_stream(
        self,
        messages: List[ChatMessage],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs: Any
    ) -> AsyncGenerator[str, None]:
        """
        Generate streaming chat completion.
        
        Args:
            messages: List of chat messages.
            model: Model deployment name. Defaults to GPT-4o.
            temperature: Sampling temperature (0-2).
            max_tokens: Maximum tokens in response.
            **kwargs: Additional parameters for the API.
            
        Yields:
            Content chunks as they are generated.
        """
        deployment = model or self._config.deployment_gpt4o
        
        stream = await self.client.chat.completions.create(
            model=deployment,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs
        )
        
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    async def create_embedding(
        self,
        text: str,
        model: Optional[str] = None
    ) -> EmbeddingResponse:
        """
        Create embedding for text.
        
        Args:
            text: Text to embed.
            model: Embedding model deployment name.
            
        Returns:
            EmbeddingResponse with embedding vector.
        """
        deployment = model or self._config.deployment_embedding
        
        response = await self.client.embeddings.create(
            model=deployment,
            input=text
        )
        
        return EmbeddingResponse(
            embedding=response.data[0].embedding,
            model=response.model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                "total_tokens": response.usage.total_tokens if response.usage else 0,
            }
        )
    
    async def create_embeddings_batch(
        self,
        texts: List[str],
        model: Optional[str] = None
    ) -> List[EmbeddingResponse]:
        """
        Create embeddings for multiple texts.
        
        Args:
            texts: List of texts to embed.
            model: Embedding model deployment name.
            
        Returns:
            List of EmbeddingResponse with embedding vectors.
        """
        deployment = model or self._config.deployment_embedding
        
        response = await self.client.embeddings.create(
            model=deployment,
            input=texts
        )
        
        return [
            EmbeddingResponse(
                embedding=data.embedding,
                model=response.model,
                usage={
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                    "total_tokens": response.usage.total_tokens if response.usage else 0,
                }
            )
            for data in response.data
        ]
    
    async def close(self) -> None:
        """Close the client connection."""
        if self._client is not None:
            await self._client.close()
            self._client = None


# Singleton instance
_client_instance: Optional[AzureOpenAIClient] = None


def get_azure_openai_client() -> AzureOpenAIClient:
    """Get Azure OpenAI client singleton."""
    global _client_instance
    if _client_instance is None:
        _client_instance = AzureOpenAIClient()
    return _client_instance
