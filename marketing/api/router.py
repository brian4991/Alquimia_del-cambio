"""
Main Marketing API Router.

Aggregates all marketing endpoints.
"""

from fastapi import APIRouter

from marketing.api.endpoints import meetings, content, calendar, strategy, voice, chat

# Create main router
marketing_router = APIRouter(tags=["marketing"])

# Include sub-routers
marketing_router.include_router(
    meetings.router,
    prefix="/meetings",
    tags=["meetings"],
)

marketing_router.include_router(
    content.router,
    prefix="/content",
    tags=["content"],
)

marketing_router.include_router(
    calendar.router,
    prefix="/calendar",
    tags=["calendar"],
)

marketing_router.include_router(
    strategy.router,
    prefix="/strategy",
    tags=["strategy"],
)

marketing_router.include_router(
    voice.router,
    prefix="/voice",
    tags=["voice"],
)

marketing_router.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"],
)


@marketing_router.get("/health")
async def health_check():
    """
    Health check endpoint.
    
    Public endpoint - no auth required for monitoring.
    """
    return {"status": "healthy", "module": "marketing"}
