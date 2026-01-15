"""
Content API Endpoints.

Endpoints for managing generated content.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException

from marketing.api.auth import require_admin
from marketing.api.schemas.requests import CreateContentRequest, UpdateContentRequest
from marketing.api.schemas.responses import ContentResponse, ContentListResponse
from marketing.domain.models import GeneratedContent
from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository
from marketing.services.feedback_service import get_feedback_service
from marketing.agents.team import CopywriterAgent, CreativeDirectorAgent
from marketing.agents.base.agent_memory import get_agent_memory

router = APIRouter()


@router.post("/generate", response_model=ContentResponse)
async def generate_content(
    request: CreateContentRequest,
    current_admin = require_admin(),
):
    """
    Generate new content using the marketing team.
    
    Uses the Copywriter and Creative Director agents.
    """
    memory = get_agent_memory()
    repository = get_marketing_repository()
    
    # Generate text content
    copywriter = CopywriterAgent(memory=memory)
    
    if request.content_type in ["reel", "video_script"]:
        text_response = await copywriter.write_reel_script(
            topic=request.topic,
            duration_seconds=30,
        )
    else:
        text_response = await copywriter.write_post_caption(
            topic=request.topic,
            platform=request.platform,
            objective=request.objective or "engagement",
        )
    
    # Generate visual brief
    creative_director = CreativeDirectorAgent(memory=memory)
    visual_response = await creative_director.create_visual_brief(
        content=text_response.content,
        platform=request.platform,
        content_type=request.content_type,
    )
    
    # Create content record
    content = GeneratedContent(
        content_type=request.content_type,
        platform=request.platform,
        text_content=text_response.content,
        visual_brief=visual_response.content,
        status="draft",
    )
    
    content = await repository.save_content(content)
    
    return ContentResponse(
        id=content.id,
        content_type=content.content_type,
        platform=content.platform,
        title=content.title,
        text_content=content.text_content,
        visual_brief=content.visual_brief,
        hashtags=content.hashtags,
        hook=content.hook,
        cta=content.cta,
        status=content.status,
        nicole_feedback=content.nicole_feedback,
        scheduled_date=content.scheduled_date,
        canva_design_url=content.canva_design_url,
        created_at=content.created_at,
    )


@router.get("/queue", response_model=ContentListResponse)
async def get_content_queue(
    current_admin = require_admin(),
):
    """Get content pending review."""
    repository = get_marketing_repository()
    contents = await repository.get_content_queue()
    
    return ContentListResponse(
        content=[
            ContentResponse(
                id=c.id,
                content_type=c.content_type,
                platform=c.platform,
                title=c.title,
                text_content=c.text_content,
                visual_brief=c.visual_brief,
                hashtags=c.hashtags,
                hook=c.hook,
                cta=c.cta,
                status=c.status,
                nicole_feedback=c.nicole_feedback,
                scheduled_date=c.scheduled_date,
                canva_design_url=c.canva_design_url,
                created_at=c.created_at,
            )
            for c in contents
        ],
        total=len(contents),
    )


@router.get("/{content_id}", response_model=ContentResponse)
async def get_content(
    content_id: int,
    current_admin = require_admin(),
):
    """Get content by ID."""
    repository = get_marketing_repository()
    content = await repository.get_content(content_id)
    
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    return ContentResponse(
        id=content.id,
        content_type=content.content_type,
        platform=content.platform,
        title=content.title,
        text_content=content.text_content,
        visual_brief=content.visual_brief,
        hashtags=content.hashtags,
        hook=content.hook,
        cta=content.cta,
        status=content.status,
        nicole_feedback=content.nicole_feedback,
        scheduled_date=content.scheduled_date,
        canva_design_url=content.canva_design_url,
        created_at=content.created_at,
    )


@router.patch("/{content_id}", response_model=ContentResponse)
async def update_content(
    content_id: int,
    request: UpdateContentRequest,
    current_admin = require_admin(),
):
    """Update content."""
    repository = get_marketing_repository()
    content = await repository.get_content(content_id)
    
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    # Update fields
    if request.status is not None:
        content.status = request.status
    if request.text_content is not None:
        content.text_content = request.text_content
    if request.visual_brief is not None:
        content.visual_brief = request.visual_brief
    if request.hashtags is not None:
        content.hashtags = request.hashtags
    if request.nicole_feedback is not None:
        content.nicole_feedback = request.nicole_feedback
    if request.scheduled_date is not None:
        content.scheduled_date = request.scheduled_date
    
    content = await repository.save_content(content)
    
    return ContentResponse(
        id=content.id,
        content_type=content.content_type,
        platform=content.platform,
        title=content.title,
        text_content=content.text_content,
        visual_brief=content.visual_brief,
        hashtags=content.hashtags,
        hook=content.hook,
        cta=content.cta,
        status=content.status,
        nicole_feedback=content.nicole_feedback,
        scheduled_date=content.scheduled_date,
        canva_design_url=content.canva_design_url,
        created_at=content.created_at,
    )


@router.post("/{content_id}/approve", response_model=ContentResponse)
async def approve_content(
    content_id: int,
    current_admin = require_admin(),
):
    """Approve content for publication."""
    repository = get_marketing_repository()
    content = await repository.get_content(content_id)
    
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    content.status = "approved"
    content = await repository.save_content(content)
    try:
        feedback_service = get_feedback_service()
        await feedback_service.process_approval(content)
    except Exception as error:
        print(f"⚠️  Feedback approval processing failed: {error}")
    
    return ContentResponse(
        id=content.id,
        content_type=content.content_type,
        platform=content.platform,
        title=content.title,
        text_content=content.text_content,
        visual_brief=content.visual_brief,
        hashtags=content.hashtags,
        hook=content.hook,
        cta=content.cta,
        status=content.status,
        nicole_feedback=content.nicole_feedback,
        scheduled_date=content.scheduled_date,
        canva_design_url=content.canva_design_url,
        created_at=content.created_at,
    )


@router.post("/{content_id}/reject", response_model=ContentResponse)
async def reject_content(
    content_id: int,
    feedback: Optional[str] = None,
    current_admin = require_admin(),
):
    """Reject content with optional feedback."""
    repository = get_marketing_repository()
    content = await repository.get_content(content_id)
    
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    content.status = "rejected"
    if feedback:
        content.nicole_feedback = feedback
    
    content = await repository.save_content(content)
    try:
        feedback_service = get_feedback_service()
        await feedback_service.process_rejection(content, feedback)
    except Exception as error:
        print(f"⚠️  Feedback rejection processing failed: {error}")
    
    return ContentResponse(
        id=content.id,
        content_type=content.content_type,
        platform=content.platform,
        title=content.title,
        text_content=content.text_content,
        visual_brief=content.visual_brief,
        hashtags=content.hashtags,
        hook=content.hook,
        cta=content.cta,
        status=content.status,
        nicole_feedback=content.nicole_feedback,
        scheduled_date=content.scheduled_date,
        canva_design_url=content.canva_design_url,
        created_at=content.created_at,
    )


@router.get("/", response_model=ContentListResponse)
async def list_content(
    status: Optional[str] = None,
    platform: Optional[str] = None,
    content_type: Optional[str] = None,
    limit: int = 20,
    current_admin = require_admin(),
):
    """List content with optional filters."""
    repository = get_marketing_repository()
    contents = await repository.list_content(
        status=status,
        platform=platform,
        content_type=content_type,
        limit=limit,
    )
    
    return ContentListResponse(
        content=[
            ContentResponse(
                id=c.id,
                content_type=c.content_type,
                platform=c.platform,
                title=c.title,
                text_content=c.text_content,
                visual_brief=c.visual_brief,
                hashtags=c.hashtags,
                hook=c.hook,
                cta=c.cta,
                status=c.status,
                nicole_feedback=c.nicole_feedback,
                scheduled_date=c.scheduled_date,
                canva_design_url=c.canva_design_url,
                created_at=c.created_at,
            )
            for c in contents
        ],
        total=len(contents),
    )


