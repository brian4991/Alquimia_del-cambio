from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.requests import Request
import os

from models import User
from database import get_db
from auth import create_access_token

# OAuth Configuration
config = Config(environ=os.environ)
oauth = OAuth(config)

# Google OAuth
oauth.register(
    name='google',
    client_id=config('GOOGLE_CLIENT_ID', default=''),
    client_secret=config('GOOGLE_CLIENT_SECRET', default=''),
    server_metadata_url='https://accounts.google.com/.well-known/openid_configuration',
    client_kwargs={
        'scope': 'openid email profile'
    },
)

# Facebook OAuth
oauth.register(
    name='facebook',
    client_id=config('FACEBOOK_CLIENT_ID', default=''),
    client_secret=config('FACEBOOK_CLIENT_SECRET', default=''),
    access_token_url='https://graph.facebook.com/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    api_base_url='https://graph.facebook.com/',
    client_kwargs={'scope': 'email'},
)

async def create_or_get_oauth_user(provider: str, user_info: dict, db: Session):
    """Create or get user from OAuth provider"""
    
    # Extract user info based on provider
    if provider == 'google':
        email = user_info.get('email')
        username = user_info.get('name', email.split('@')[0])
        provider_id = user_info.get('sub')
    elif provider == 'facebook':
        email = user_info.get('email')
        username = user_info.get('name', email.split('@')[0])
        provider_id = user_info.get('id')
    else:
        raise HTTPException(status_code=400, detail="Unsupported OAuth provider")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email not provided by OAuth provider")
    
    # Check if user already exists with this provider
    existing_user = db.query(User).filter(
        User.provider == provider,
        User.provider_id == str(provider_id)
    ).first()
    
    if existing_user:
        return existing_user
    
    # Check if user exists with same email but different provider
    email_user = db.query(User).filter(User.email == email).first()
    if email_user:
        # Link the OAuth account to existing user
        email_user.provider = provider
        email_user.provider_id = str(provider_id)
        db.commit()
        db.refresh(email_user)
        return email_user
    
    # Create new user
    new_user = User(
        username=username,
        email=email,
        password_hash='',  # OAuth users don't have passwords
        role='user',  # Default role for new users
        provider=provider,
        provider_id=str(provider_id),
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def generate_oauth_token(user: User):
    """Generate JWT token for OAuth user"""
    return create_access_token(data={
        "sub": user.username,
        "user_id": user.id,
        "role": user.role,
        "provider": user.provider
    })