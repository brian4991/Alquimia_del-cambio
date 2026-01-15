"""
Configuration centralisee pour le module Marketing.

Toutes les configurations (Azure, Canva, DB, etc.) sont gerees ici.
Utilise des variables d'environnement pour les secrets.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class AzureOpenAIConfig(BaseSettings):
    """Configuration Azure OpenAI."""
    
    endpoint: str = Field(
        default="",
        alias="AZURE_OPENAI_ENDPOINT",
        description="Azure OpenAI endpoint URL"
    )
    api_key: str = Field(
        default="",
        alias="AZURE_OPENAI_API_KEY",
        description="Azure OpenAI API key"
    )
    api_version: str = Field(
        default="2024-02-15-preview",
        alias="AZURE_OPENAI_API_VERSION",
        description="Azure OpenAI API version"
    )
    deployment_gpt4o: str = Field(
        default="gpt-4o",
        alias="AZURE_OPENAI_DEPLOYMENT_GPT4O",
        description="GPT-4o deployment name"
    )
    deployment_embedding: str = Field(
        default="text-embedding-ada-002",
        alias="AZURE_OPENAI_DEPLOYMENT_EMBEDDING",
        description="Embedding model deployment name"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


class CanvaConfig(BaseSettings):
    """Configuration Canva API."""
    
    api_key: str = Field(
        default="",
        alias="CANVA_API_KEY",
        description="Canva API key"
    )
    brand_kit_id: Optional[str] = Field(
        default=None,
        alias="CANVA_BRAND_KIT_ID",
        description="Canva Brand Kit ID"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


class DatabaseConfig(BaseSettings):
    """Configuration Database."""
    
    url: str = Field(
        default="postgresql://localhost/alquimia",
        alias="DATABASE_URL",
        description="Database connection URL"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


class AzureSearchConfig(BaseSettings):
    """Configuration Azure AI Search."""
    
    service_name: str = Field(
        default="",
        alias="AZURE_SEARCH_SERVICE_NAME",
        description="Azure Search service name"
    )
    api_key: str = Field(
        default="",
        alias="AZURE_SEARCH_API_KEY",
        description="Azure Search API key"
    )
    index_name: str = Field(
        default="marketing-content",
        alias="AZURE_SEARCH_INDEX_NAME",
        description="Azure Search index name"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


class VectorStoreConfig(BaseSettings):
    """Configuration Vector Store (pgvector or Azure Search)."""
    
    # Backend choice: "pgvector" or "azure_search"
    backend: str = Field(
        default="pgvector",
        alias="VECTOR_STORE_BACKEND",
        description="Vector store backend: 'pgvector' or 'azure_search'"
    )
    
    # pgvector settings
    collection_name: str = Field(
        default="marketing_embeddings",
        description="Collection name for embeddings (pgvector)"
    )
    embedding_dimension: int = Field(
        default=1536,
        description="Dimension of embeddings (ada-002 = 1536)"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


class MarketingConfig(BaseSettings):
    """Configuration principale du module Marketing."""
    
    # Target audience
    target_language: str = Field(
        default="es",
        description="Target language for content (es = Spanish)"
    )
    target_audience: str = Field(
        default="Femmes 25-50 ans",
        description="Target audience description"
    )
    
    # Content settings
    posts_per_week: int = Field(
        default=5,
        description="Target posts per week (4-5)"
    )
    max_hashtags: int = Field(
        default=5,
        description="Maximum hashtags per post (3-5)"
    )
    
    # Platforms
    platforms: list[str] = Field(
        default=["instagram", "tiktok", "youtube", "linkedin", "facebook"],
        description="Target social media platforms"
    )
    
    # Agent settings
    max_debate_cycles: int = Field(
        default=3,
        description="Maximum debate cycles before forcing consensus"
    )
    
    class Config:
        env_file = ".env"
        extra = "ignore"


# Singleton instances
_azure_config: Optional[AzureOpenAIConfig] = None
_azure_search_config: Optional[AzureSearchConfig] = None
_canva_config: Optional[CanvaConfig] = None
_database_config: Optional[DatabaseConfig] = None
_vector_store_config: Optional[VectorStoreConfig] = None
_marketing_config: Optional[MarketingConfig] = None


def get_azure_config() -> AzureOpenAIConfig:
    """Get Azure OpenAI configuration singleton."""
    global _azure_config
    if _azure_config is None:
        _azure_config = AzureOpenAIConfig()
    return _azure_config


def get_canva_config() -> CanvaConfig:
    """Get Canva configuration singleton."""
    global _canva_config
    if _canva_config is None:
        _canva_config = CanvaConfig()
    return _canva_config


def get_database_config() -> DatabaseConfig:
    """Get Database configuration singleton."""
    global _database_config
    if _database_config is None:
        _database_config = DatabaseConfig()
    return _database_config


def get_azure_search_config() -> AzureSearchConfig:
    """Get Azure Search configuration singleton."""
    global _azure_search_config
    if _azure_search_config is None:
        _azure_search_config = AzureSearchConfig()
    return _azure_search_config


def get_vector_store_config() -> VectorStoreConfig:
    """Get Vector Store configuration singleton."""
    global _vector_store_config
    if _vector_store_config is None:
        _vector_store_config = VectorStoreConfig()
    return _vector_store_config


def get_marketing_config() -> MarketingConfig:
    """Get Marketing configuration singleton."""
    global _marketing_config
    if _marketing_config is None:
        _marketing_config = MarketingConfig()
    return _marketing_config
