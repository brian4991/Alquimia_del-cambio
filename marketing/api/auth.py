"""
Authentication helper for marketing routes.

Provides admin-only access protection.
"""

from typing import Optional
from fastapi import Depends, HTTPException
import sys
from pathlib import Path

# Try to import auth from main app
try:
    backend_path = str(Path(__file__).parent.parent.parent.parent / "backend")
    if backend_path not in sys.path:
        sys.path.insert(0, backend_path)
    from auth import get_current_admin_user as _get_current_admin_user
    from models import User
    from database import get_db as _get_db
    AUTH_AVAILABLE = True
    print("✅ Marketing auth: Using backend authentication")
except ImportError as e:
    AUTH_AVAILABLE = False
    User = None
    _get_db = None
    print(f"⚠️  Marketing auth: Backend auth not available, using dummy auth: {e}")
    
    def _get_current_admin_user():
        """Fallback if auth not available."""
        return None
    
    def _get_db():
        """Fallback if db not available."""
        return None


def require_admin():
    """
    Dependency to require admin authentication.
    
    Returns:
        Dependency function for FastAPI routes.
    """
    if not AUTH_AVAILABLE:
        # In development/testing, create a dummy dependency that accepts any args
        def _dummy_admin(*args, **kwargs):
            # Return a mock admin user object
            class MockAdmin:
                id = 1
                username = "admin"
                role = "admin"
                is_active = True
                is_validated = True
            return MockAdmin()
        return Depends(_dummy_admin)
    
    # Use the imported function directly, same as other routes
    return Depends(_get_current_admin_user)


def get_admin_user(current_admin: Optional[User] = None) -> User:
    """
    Get admin user or raise exception.
    
    Args:
        current_admin: Admin user from dependency.
        
    Returns:
        Admin user.
        
    Raises:
        HTTPException: If not authenticated or not admin.
    """
    if not AUTH_AVAILABLE:
        # Development mode - allow
        return None
    
    if current_admin is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    if getattr(current_admin, "role", None) != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    return current_admin
