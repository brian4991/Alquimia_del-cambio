"""
Strategy API Endpoints.

Endpoints for managing marketing strategies.
"""

from typing import Optional
from datetime import date, timedelta
import json
from fastapi import APIRouter, HTTPException

from marketing.api.auth import require_admin
from marketing.api.schemas.requests import CreateStrategyRequest
from marketing.api.schemas.responses import StrategyResponse
from marketing.domain.models import MarketingStrategy, GeneratedContent, ContentCalendar
from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository
from marketing.agents.team import StrategistAgent
from marketing.agents.base.agent_memory import get_agent_memory

router = APIRouter()


@router.post("/generate", response_model=StrategyResponse)
async def generate_strategy(
    request: CreateStrategyRequest,
    current_admin = require_admin(),
):
    """
    Generate a new marketing strategy using the Strategist agent.
    """
    memory = get_agent_memory()
    repository = get_marketing_repository()
    
    # Generate strategy using agent
    strategist = StrategistAgent(memory=memory)
    response = await strategist.generate_strategy(
        strategy_type=request.strategy_type,
        objectives=request.objectives,
    )
    
    # Create strategy record
    strategy = MarketingStrategy(
        strategy_type=request.strategy_type,
        period_start=request.period_start,
        period_end=request.period_end,
        title=f"Estrategia {request.strategy_type} - {request.period_start}",
        objectives=[request.objectives],
        content_pillars=[],  # Will be extracted from response
        status="draft",
    )
    
    # Parse response to extract structured data
    # (In a full implementation, use structured output from LLM)
    strategy = await repository.save_strategy(strategy)
    
    return StrategyResponse(
        id=strategy.id,
        strategy_type=strategy.strategy_type,
        title=strategy.title,
        period_start=strategy.period_start,
        period_end=strategy.period_end,
        objectives=strategy.objectives,
        content_pillars=strategy.content_pillars,
        key_messages=strategy.key_messages,
        target_metrics=strategy.target_metrics,
        status=strategy.status,
        created_at=strategy.created_at,
    )


def _parse_recommendations(raw_text: str) -> list[dict]:
    try:
        parsed = json.loads(raw_text)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    return []


@router.post("/{strategy_id}/recommendations")
async def generate_calendar_recommendations(
    strategy_id: int,
    current_admin=require_admin(),
):
    """Generate calendar recommendations based on a strategy."""
    repository = get_marketing_repository()
    strategy = await repository.get_strategy(strategy_id)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")

    memory = get_agent_memory()
    strategist = StrategistAgent(memory=memory)
    prompt = f"""
Genera 6 recomendaciones de contenidos para calendario en formato JSON.
Cada item debe tener: title, platform, content_type, days_from_now (int 1-30).
Plataformas posibles: instagram, tiktok, youtube, linkedin, facebook.
Tipos: post, reel, story, carousel, video_script.
Objetivos: {', '.join(strategy.objectives or [])}
Pilares: {', '.join(strategy.content_pillars or [])}
"""
    raw = await strategist._call_llm(prompt)
    recommendations = _parse_recommendations(raw)
    if not recommendations:
        recommendations = [
            {
                "title": f"Confianza en uno mismo - Tip práctico #{i + 1}",
                "platform": platform,
                "content_type": "reel",
                "days_from_now": i * 3 + 1,
            }
            for i, platform in enumerate(["instagram", "tiktok", "youtube", "linkedin", "facebook", "instagram"])
        ]

    created_items = []
    today = date.today()
    for rec in recommendations[:10]:
        title = rec.get("title") or "Contenido recomendado"
        platform = rec.get("platform") or "instagram"
        content_type = rec.get("content_type") or "post"
        days_from_now = max(1, int(rec.get("days_from_now") or 1))

        content = GeneratedContent(
            content_type=content_type,
            platform=platform,
            title=title,
            text_content=title,
            status="draft",
            strategy_id=strategy.id,
        )
        content = await repository.save_content(content)

        calendar_item = ContentCalendar(
            content_id=content.id,
            platform=platform,
            scheduled_date=today + timedelta(days=days_from_now),
            scheduled_time=None,
            status="scheduled",
            auto_suggested=True,
        )
        calendar_item = await repository.save_calendar_item(calendar_item)
        created_items.append(calendar_item.id)

    return {
        "strategy_id": strategy.id,
        "created_items": created_items,
        "count": len(created_items),
    }


@router.get("/active")
async def get_active_strategies(
    current_admin = require_admin(),
):
    """Get all active strategies by type."""
    repository = get_marketing_repository()
    strategies = await repository.get_active_strategies()
    
    return {
        strategy_type: StrategyResponse(
            id=strategy.id,
            strategy_type=strategy.strategy_type,
            title=strategy.title,
            period_start=strategy.period_start,
            period_end=strategy.period_end,
            objectives=strategy.objectives,
            content_pillars=strategy.content_pillars,
            key_messages=strategy.key_messages,
            target_metrics=strategy.target_metrics,
            status=strategy.status,
            created_at=strategy.created_at,
        )
        for strategy_type, strategy in strategies.items()
    }


@router.get("/{strategy_id}", response_model=StrategyResponse)
async def get_strategy(
    strategy_id: int,
    current_admin = require_admin(),
):
    """Get a strategy by ID."""
    repository = get_marketing_repository()
    strategy = await repository.get_strategy(strategy_id)
    
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    return StrategyResponse(
        id=strategy.id,
        strategy_type=strategy.strategy_type,
        title=strategy.title,
        period_start=strategy.period_start,
        period_end=strategy.period_end,
        objectives=strategy.objectives,
        content_pillars=strategy.content_pillars,
        key_messages=strategy.key_messages,
        target_metrics=strategy.target_metrics,
        status=strategy.status,
        created_at=strategy.created_at,
    )


@router.post("/{strategy_id}/activate", response_model=StrategyResponse)
async def activate_strategy(
    strategy_id: int,
    current_admin = require_admin(),
):
    """Activate a strategy."""
    repository = get_marketing_repository()
    strategy = await repository.get_strategy(strategy_id)
    
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    
    # Deactivate other strategies of same type
    existing = await repository.list_strategies(
        strategy_type=strategy.strategy_type,
        status="active",
    )
    for s in existing:
        s.status = "archived"
        await repository.save_strategy(s)
    
    # Activate this one
    strategy.status = "active"
    strategy = await repository.save_strategy(strategy)
    
    return StrategyResponse(
        id=strategy.id,
        strategy_type=strategy.strategy_type,
        title=strategy.title,
        period_start=strategy.period_start,
        period_end=strategy.period_end,
        objectives=strategy.objectives,
        content_pillars=strategy.content_pillars,
        key_messages=strategy.key_messages,
        target_metrics=strategy.target_metrics,
        status=strategy.status,
        created_at=strategy.created_at,
    )


@router.get("/", response_model=list[StrategyResponse])
async def list_strategies(
    strategy_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    current_admin = require_admin(),
):
    """List strategies with optional filters."""
    repository = get_marketing_repository()
    strategies = await repository.list_strategies(
        strategy_type=strategy_type,
        status=status,
        limit=limit,
    )
    
    return [
        StrategyResponse(
            id=s.id,
            strategy_type=s.strategy_type,
            title=s.title,
            period_start=s.period_start,
            period_end=s.period_end,
            objectives=s.objectives,
            content_pillars=s.content_pillars,
            key_messages=s.key_messages,
            target_metrics=s.target_metrics,
            status=s.status,
            created_at=s.created_at,
        )
        for s in strategies
    ]
