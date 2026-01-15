"""
Feedback Service.

Handles learning from Nicole's feedback to improve content generation.
"""

from typing import Optional, Dict, Any, List
from datetime import datetime

from marketing.services.memory.vector_store import VectorStoreService, get_vector_store
from marketing.services.persistence.sqlalchemy_repository import (
    SQLAlchemyMarketingRepository,
    get_marketing_repository,
)
from marketing.domain.models import GeneratedContent, BrandVoiceProfile


class FeedbackService:
    """
    Service for learning from Nicole's feedback.
    
    Provides:
    - Indexing approved content for future reference
    - Analyzing rejection patterns
    - Updating voice profile based on preferences
    """
    
    def __init__(
        self,
        repository: Optional[SQLAlchemyMarketingRepository] = None,
        vector_store: Optional[VectorStoreService] = None,
    ) -> None:
        """
        Initialize feedback service.
        
        Args:
            repository: Data repository.
            vector_store: Vector store for indexing.
        """
        self._repository = repository or get_marketing_repository()
        self._vector_store = vector_store or get_vector_store()
    
    async def process_approval(self, content: GeneratedContent) -> None:
        """
        Process approved content for learning.
        
        Indexes the approved content so future generations can learn from it.
        
        Args:
            content: Approved content.
        """
        # Index in vector store for RAG
        await self._vector_store.add_document(
            content=content.text_content,
            metadata={
                "type": "approved_content",
                "content_type": content.content_type,
                "platform": content.platform,
                "approved_at": datetime.now().isoformat(),
            }
        )
        
        # If there's a visual brief, index that too
        if content.visual_brief:
            await self._vector_store.add_document(
                content=content.visual_brief,
                metadata={
                    "type": "approved_visual_brief",
                    "content_type": content.content_type,
                    "platform": content.platform,
                    "approved_at": datetime.now().isoformat(),
                }
            )
    
    async def process_rejection(
        self,
        content: GeneratedContent,
        feedback: Optional[str] = None
    ) -> None:
        """
        Process rejected content for learning.
        
        Analyzes the rejection to improve future generations.
        
        Args:
            content: Rejected content.
            feedback: Nicole's feedback explaining the rejection.
        """
        if not feedback:
            return
        
        # Index the feedback for future reference
        await self._vector_store.add_document(
            content=f"RECHAZADO: {content.text_content[:200]}...\n\nFEEDBACK: {feedback}",
            metadata={
                "type": "rejection_feedback",
                "content_type": content.content_type,
                "platform": content.platform,
                "rejected_at": datetime.now().isoformat(),
            }
        )
    
    async def get_approval_stats(self) -> Dict[str, Any]:
        """
        Get statistics on content approvals/rejections.
        
        Returns:
            Stats dictionary.
        """
        # Get all content
        all_content = await self._repository.list_content(limit=1000)
        
        stats = {
            "total": len(all_content),
            "approved": 0,
            "rejected": 0,
            "draft": 0,
            "by_platform": {},
            "by_type": {},
        }
        
        for content in all_content:
            if content.status == "approved":
                stats["approved"] += 1
            elif content.status == "rejected":
                stats["rejected"] += 1
            else:
                stats["draft"] += 1
            
            # By platform
            platform = content.platform
            if platform not in stats["by_platform"]:
                stats["by_platform"][platform] = {"approved": 0, "rejected": 0, "total": 0}
            stats["by_platform"][platform]["total"] += 1
            if content.status == "approved":
                stats["by_platform"][platform]["approved"] += 1
            elif content.status == "rejected":
                stats["by_platform"][platform]["rejected"] += 1
            
            # By type
            ctype = content.content_type
            if ctype not in stats["by_type"]:
                stats["by_type"][ctype] = {"approved": 0, "rejected": 0, "total": 0}
            stats["by_type"][ctype]["total"] += 1
            if content.status == "approved":
                stats["by_type"][ctype]["approved"] += 1
            elif content.status == "rejected":
                stats["by_type"][ctype]["rejected"] += 1
        
        # Calculate approval rates
        if stats["total"] > 0:
            stats["approval_rate"] = stats["approved"] / stats["total"]
        else:
            stats["approval_rate"] = 0
        
        return stats
    
    async def get_common_feedback_themes(self) -> List[str]:
        """
        Analyze rejection feedback to find common themes.
        
        Returns:
            List of common feedback themes.
        """
        # Get rejected content with feedback
        rejected = await self._repository.list_content(status="rejected", limit=100)
        
        feedback_texts = [
            c.nicole_feedback 
            for c in rejected 
            if c.nicole_feedback
        ]
        
        if not feedback_texts:
            return []
        
        # Simple keyword extraction (in production, use NLP)
        common_words = {}
        for text in feedback_texts:
            words = text.lower().split()
            for word in words:
                if len(word) > 4:  # Skip short words
                    common_words[word] = common_words.get(word, 0) + 1
        
        # Sort by frequency
        sorted_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)
        
        return [word for word, count in sorted_words[:10] if count > 1]
    
    async def update_voice_profile_from_feedback(self) -> Optional[BrandVoiceProfile]:
        """
        Update the voice profile based on approved content patterns.
        
        Analyzes approved content to refine the voice profile.
        
        Returns:
            Updated voice profile or None.
        """
        # Get current profile
        profile = await self._repository.get_active_voice_profile()
        if not profile:
            return None
        
        # Get approved content
        approved = await self._repository.list_content(status="approved", limit=50)
        
        if len(approved) < 5:
            # Not enough data to update
            return profile
        
        # Extract patterns from approved content
        # (In production, use LLM to analyze patterns)
        
        # For now, just update the count
        profile.analyzed_content_count = len(approved)
        
        return await self._repository.save_voice_profile(profile)


# Factory function
def get_feedback_service() -> FeedbackService:
    """Get feedback service instance."""
    return FeedbackService()
