"""
Voice Profile API Endpoints.

Endpoints for managing the brand voice profile.
"""

from fastapi import APIRouter, HTTPException

from marketing.api.auth import require_admin
from marketing.api.schemas.responses import VoiceProfileResponse
from marketing.domain.models import BrandVoiceProfile
from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository
from marketing.services.memory.content_indexer import get_content_indexer

router = APIRouter()


@router.get("/profile", response_model=VoiceProfileResponse)
async def get_voice_profile(
    current_admin = require_admin(),
):
    """Get the active voice profile."""
    repository = get_marketing_repository()
    profile = await repository.get_active_voice_profile()
    
    if not profile:
        raise HTTPException(status_code=404, detail="No active voice profile found")
    
    return VoiceProfileResponse(
        id=profile.id,
        tone_descriptors=profile.tone_descriptors,
        vocabulary_frequent=profile.vocabulary_frequent,
        expressions_cles=profile.expressions_cles,
        topics_principaux=profile.topics_principaux,
        style_guidelines=profile.style_guidelines,
        analyzed_transcripts_count=profile.analyzed_transcripts_count,
        is_active=profile.is_active,
        updated_at=profile.updated_at,
    )


@router.post("/analyze")
async def analyze_voice(
    current_admin = require_admin(),
):
    """
    Analyze transcripts and content to generate/update voice profile.
    
    This indexes all content and creates a new voice profile.
    """
    repository = get_marketing_repository()
    indexer = get_content_indexer()
    
    # Index all content
    stats = await indexer.index_all()
    
    # Create new voice profile
    # In a full implementation, this would use the LLM to analyze
    # the indexed content and extract voice characteristics
    profile = BrandVoiceProfile(
        tone_descriptors=[
            "empoderador",
            "cálido",
            "profesional",
            "auténtico",
            "cercano",
        ],
        vocabulary_frequent=[
            "transformación",
            "emociones",
            "autoconocimiento",
            "bienestar",
            "crecimiento",
        ],
        expressions_cles=[
            "tu proceso",
            "conectar contigo",
            "gestión emocional",
            "alquimia del cambio",
        ],
        topics_principaux=[
            "gestión emocional",
            "autoestima",
            "relaciones",
            "transformación personal",
            "comunicación asertiva",
        ],
        style_guidelines="Tono cercano y empático. Usa preguntas reflexivas. "
                        "Evita jerga excesiva. Sé vulnerable y auténtica.",
        analyzed_transcripts_count=stats.get("transcripts", {}).get("indexed", 0),
        analyzed_content_count=stats.get("program", {}).get("indexed", 0),
        is_active=True,
    )
    
    # Deactivate previous profiles
    existing = await repository.get_active_voice_profile()
    if existing:
        existing.is_active = False
        await repository.save_voice_profile(existing)
    
    profile = await repository.save_voice_profile(profile)
    
    return {
        "message": "Voice profile created successfully",
        "profile_id": profile.id,
        "indexing_stats": stats,
    }


@router.post("/reindex")
async def reindex_content(
    current_admin = require_admin(),
):
    """
    Reindex all content for RAG.
    
    Clears existing index and reindexes all transcripts and program content.
    """
    indexer = get_content_indexer()
    stats = await indexer.reindex_all()
    
    return {
        "message": "Content reindexed successfully",
        "stats": stats,
    }


@router.patch("/profile")
async def update_voice_profile(
    tone_descriptors: list[str] = None,
    vocabulary_frequent: list[str] = None,
    expressions_cles: list[str] = None,
    topics_principaux: list[str] = None,
    style_guidelines: str = None,
    current_admin = require_admin(),
):
    """
    Manually update the voice profile.
    
    Allows Nicole to adjust the automatically generated profile.
    """
    repository = get_marketing_repository()
    profile = await repository.get_active_voice_profile()
    
    if not profile:
        raise HTTPException(status_code=404, detail="No active voice profile found")
    
    if tone_descriptors is not None:
        profile.tone_descriptors = tone_descriptors
    if vocabulary_frequent is not None:
        profile.vocabulary_frequent = vocabulary_frequent
    if expressions_cles is not None:
        profile.expressions_cles = expressions_cles
    if topics_principaux is not None:
        profile.topics_principaux = topics_principaux
    if style_guidelines is not None:
        profile.style_guidelines = style_guidelines
    
    profile = await repository.save_voice_profile(profile)
    
    return VoiceProfileResponse(
        id=profile.id,
        tone_descriptors=profile.tone_descriptors,
        vocabulary_frequent=profile.vocabulary_frequent,
        expressions_cles=profile.expressions_cles,
        topics_principaux=profile.topics_principaux,
        style_guidelines=profile.style_guidelines,
        analyzed_transcripts_count=profile.analyzed_transcripts_count,
        is_active=profile.is_active,
        updated_at=profile.updated_at,
    )
