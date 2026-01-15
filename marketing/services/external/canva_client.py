"""
Canva API Client.

Provides integration with Canva for visual content creation.
"""

from typing import Optional, Dict, Any, List
import httpx
from pydantic import BaseModel

from marketing.config import get_canva_config, CanvaConfig


class CanvaDesign(BaseModel):
    """Canva design structure."""
    id: str
    title: str
    url: str
    thumbnail_url: Optional[str] = None
    created_at: Optional[str] = None


class CanvaTemplate(BaseModel):
    """Canva template structure."""
    id: str
    name: str
    type: str
    thumbnail_url: Optional[str] = None


class CanvaClient:
    """
    Canva API client for visual content creation.
    
    Provides methods to:
    - Create designs from templates
    - Access Brand Kit elements
    - Generate designs from briefs
    """
    
    BASE_URL = "https://api.canva.com/rest/v1"
    
    def __init__(self, config: Optional[CanvaConfig] = None) -> None:
        """
        Initialize Canva client.
        
        Args:
            config: Canva configuration. If None, loads from environment.
        """
        self._config = config or get_canva_config()
        self._client: Optional[httpx.AsyncClient] = None
    
    @property
    def client(self) -> httpx.AsyncClient:
        """Lazy initialization of HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.BASE_URL,
                headers={
                    "Authorization": f"Bearer {self._config.api_key}",
                    "Content-Type": "application/json",
                },
                timeout=30.0,
            )
        return self._client
    
    async def get_brand_kit(self) -> Dict[str, Any]:
        """
        Get the brand kit for Nicole.
        
        Returns:
            Brand kit data including colors, fonts, logos.
        """
        if not self._config.brand_kit_id:
            return {"error": "No brand kit ID configured"}
        
        try:
            response = await self.client.get(f"/brand-kits/{self._config.brand_kit_id}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": str(e)}
    
    async def list_templates(
        self,
        design_type: Optional[str] = None,
        limit: int = 20
    ) -> List[CanvaTemplate]:
        """
        List available templates.
        
        Args:
            design_type: Filter by type (e.g., "instagram_post").
            limit: Maximum templates to return.
            
        Returns:
            List of available templates.
        """
        try:
            params = {"limit": limit}
            if design_type:
                params["type"] = design_type
            
            response = await self.client.get("/templates", params=params)
            response.raise_for_status()
            
            data = response.json()
            return [
                CanvaTemplate(
                    id=t["id"],
                    name=t.get("name", "Untitled"),
                    type=t.get("type", "unknown"),
                    thumbnail_url=t.get("thumbnail_url"),
                )
                for t in data.get("templates", [])
            ]
        except httpx.HTTPError as e:
            print(f"Error listing templates: {e}")
            return []
    
    async def create_design(
        self,
        title: str,
        design_type: str,
        template_id: Optional[str] = None,
    ) -> Optional[CanvaDesign]:
        """
        Create a new design.
        
        Args:
            title: Design title.
            design_type: Type of design.
            template_id: Optional template to start from.
            
        Returns:
            Created design or None on error.
        """
        try:
            payload = {
                "title": title,
                "design_type": design_type,
            }
            
            if template_id:
                payload["template_id"] = template_id
            
            if self._config.brand_kit_id:
                payload["brand_kit_id"] = self._config.brand_kit_id
            
            response = await self.client.post("/designs", json=payload)
            response.raise_for_status()
            
            data = response.json()
            return CanvaDesign(
                id=data["id"],
                title=data.get("title", title),
                url=data.get("url", ""),
                thumbnail_url=data.get("thumbnail_url"),
                created_at=data.get("created_at"),
            )
        except httpx.HTTPError as e:
            print(f"Error creating design: {e}")
            return None
    
    async def get_design(self, design_id: str) -> Optional[CanvaDesign]:
        """
        Get a design by ID.
        
        Args:
            design_id: Design ID.
            
        Returns:
            Design or None if not found.
        """
        try:
            response = await self.client.get(f"/designs/{design_id}")
            response.raise_for_status()
            
            data = response.json()
            return CanvaDesign(
                id=data["id"],
                title=data.get("title", ""),
                url=data.get("url", ""),
                thumbnail_url=data.get("thumbnail_url"),
                created_at=data.get("created_at"),
            )
        except httpx.HTTPError as e:
            print(f"Error getting design: {e}")
            return None
    
    async def export_design(
        self,
        design_id: str,
        format: str = "png",
    ) -> Optional[str]:
        """
        Export a design to a file.
        
        Args:
            design_id: Design ID to export.
            format: Export format (png, jpg, pdf).
            
        Returns:
            URL to exported file or None on error.
        """
        try:
            response = await self.client.post(
                f"/designs/{design_id}/export",
                json={"format": format}
            )
            response.raise_for_status()
            
            data = response.json()
            return data.get("url")
        except httpx.HTTPError as e:
            print(f"Error exporting design: {e}")
            return None
    
    def get_design_type_for_platform(
        self,
        platform: str,
        content_type: str
    ) -> str:
        """
        Get the Canva design type for a platform/content combination.
        
        Args:
            platform: Social media platform.
            content_type: Type of content.
            
        Returns:
            Canva design type string.
        """
        type_map = {
            ("instagram", "post"): "instagram_post",
            ("instagram", "story"): "instagram_story",
            ("instagram", "reel"): "instagram_story",
            ("tiktok", "reel"): "tiktok_video",
            ("tiktok", "video_script"): "tiktok_video",
            ("youtube", "video_script"): "youtube_thumbnail",
            ("linkedin", "post"): "linkedin_post",
            ("facebook", "post"): "facebook_post",
        }
        
        key = (platform.lower(), content_type.lower())
        return type_map.get(key, "presentation")
    
    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None


# Singleton instance
_canva_client: Optional[CanvaClient] = None


def get_canva_client() -> CanvaClient:
    """Get Canva client singleton."""
    global _canva_client
    if _canva_client is None:
        _canva_client = CanvaClient()
    return _canva_client
