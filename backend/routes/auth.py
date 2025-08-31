from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from starlette.responses import JSONResponse

from auth import hash_password, verify_password, create_access_token, get_current_user, get_current_admin_user
from database import get_db
from models import User, UserResponseDB, Exercise, Theme, Module
from schemas import UserCreate, UserLogin, UserResponse, Token
from oauth import oauth, create_or_get_oauth_user, generate_oauth_token

router = APIRouter(tags=["authentication"])

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username, 
        email=user.email, 
        password_hash=hashed_password,
        role="user",  # Default role
        provider="local"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create access token
    access_token = create_access_token(data={
        "sub": db_user.username,
        "user_id": db_user.id,
        "role": db_user.role
    })
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not db_user.is_active:
        raise HTTPException(status_code=401, detail="Account is inactive")
    
    access_token = create_access_token(data={
        "sub": db_user.username,
        "user_id": db_user.id,
        "role": db_user.role
    })
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

# OAuth Routes

@router.get("/google")
async def google_login(request: Request):
    """Initiate Google OAuth login"""
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Google OAuth callback"""
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get('userinfo')
        
        if not user_info:
            # Fetch user info if not included in token
            resp = await oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo', token=token)
            user_info = resp.json()
        
        # Create or get user
        user = await create_or_get_oauth_user('google', user_info, db)
        
        # Generate token
        access_token = generate_oauth_token(user)
        
        # Redirect to frontend with token
        frontend_url = f"http://localhost:5174/auth/callback?token={access_token}"
        return RedirectResponse(url=frontend_url)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OAuth authentication failed: {str(e)}")

@router.get("/facebook")
async def facebook_login(request: Request):
    """Initiate Facebook OAuth login"""
    redirect_uri = request.url_for('facebook_callback')
    return await oauth.facebook.authorize_redirect(request, redirect_uri)

@router.get("/facebook/callback")
async def facebook_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Facebook OAuth callback"""
    try:
        token = await oauth.facebook.authorize_access_token(request)
        
        # Fetch user info from Facebook
        resp = await oauth.facebook.get('https://graph.facebook.com/me?fields=id,name,email', token=token)
        user_info = resp.json()
        
        # Create or get user
        user = await create_or_get_oauth_user('facebook', user_info, db)
        
        # Generate token
        access_token = generate_oauth_token(user)
        
        # Redirect to frontend with token
        frontend_url = f"http://localhost:5174/auth/callback?token={access_token}"
        return RedirectResponse(url=frontend_url)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OAuth authentication failed: {str(e)}")

# Admin Routes

@router.get("/auth/admin/users")
def get_all_users(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Get all users - Admin only"""
    users = db.query(User).all()
    return users

@router.patch("/auth/admin/users/{user_id}/role")
def update_user_role(
    user_id: int, 
    new_role: str,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Update user role - Admin only"""
    if new_role not in ["admin", "user"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.role = new_role
    db.commit()
    return {"message": f"User role updated to {new_role}"}

@router.get("/auth/admin/users/{user_id}/responses")
def get_user_responses(
    user_id: int,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Get all responses from a specific user - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get user responses with exercise and theme info
    responses = db.query(UserResponseDB, Exercise, Theme, Module).join(
        Exercise, UserResponseDB.exercise_id == Exercise.id
    ).join(
        Theme, Exercise.theme_id == Theme.id
    ).join(
        Module, Theme.module_id == Module.id
    ).filter(
        UserResponseDB.user_id == user_id
    ).order_by(UserResponseDB.submitted_at.desc()).all()
    
    result = []
    for response, exercise, theme, module in responses:
        result.append({
            "id": response.id,
            "exercise_id": exercise.id,
            "exercise_title": exercise.title,
            "theme_title": theme.title,
            "module_title": module.title,
            "response_text": response.response_text,
            "submitted_at": response.submitted_at,
        })
    
    return result

@router.get("/auth/admin/users/stats")
def get_users_stats(
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Get general statistics about users - Admin only"""
    
    total_users = db.query(func.count(User.id)).scalar()
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar()
    total_responses = db.query(func.count(UserResponseDB.id)).scalar()
    
    # Get users with their response counts and progress
    users_with_responses = db.query(
        User.id,
        User.username,
        User.email,
        User.role,
        User.provider,
        User.is_active,
        User.created_at,
        func.count(UserResponseDB.id).label('response_count')
    ).outerjoin(
        UserResponseDB, User.id == UserResponseDB.user_id
    ).group_by(User.id).all()
    
    users_data = []
    for user_data in users_with_responses:
        # Calculate user progress
        user_progress = get_user_progress(db, user_data.id)
        
        users_data.append({
            "id": user_data.id,
            "username": user_data.username,
            "email": user_data.email,
            "role": user_data.role,
            "provider": user_data.provider,
            "is_active": user_data.is_active,
            "created_at": user_data.created_at,
            "response_count": user_data.response_count,
            "progress": user_progress
        })
    
    return {
        "stats": {
            "total_users": total_users,
            "active_users": active_users,
            "total_responses": total_responses
        },
        "users": users_data
    }

def get_user_progress(db: Session, user_id: int):
    """Calculate user progress through modules, themes, and exercises"""
    # Get user's latest response to determine current position
    latest_response = db.query(UserResponseDB, Exercise, Theme, Module).join(
        Exercise, UserResponseDB.exercise_id == Exercise.id
    ).join(
        Theme, Exercise.theme_id == Theme.id
    ).join(
        Module, Theme.module_id == Module.id
    ).filter(
        UserResponseDB.user_id == user_id
    ).order_by(UserResponseDB.submitted_at.desc()).first()
    
    if not latest_response:
        return {
            "current_module": None,
            "current_theme": None,
            "current_exercise": None,
            "completed_modules": 0,
            "completed_themes": 0,
            "completed_exercises": 0,
            "total_modules": 0,
            "total_themes": 0,
            "total_exercises": 0,
            "progress_percentage": 0
        }
    
    response, exercise, theme, module = latest_response
    
    # Get total counts
    total_modules = db.query(func.count(Module.id)).scalar()
    total_themes = db.query(func.count(Theme.id)).scalar()
    total_exercises = db.query(func.count(Exercise.id)).scalar()
    
    # Get completed counts for this user
    completed_modules = db.query(func.count(func.distinct(Module.id))).join(
        Theme, Module.id == Theme.module_id
    ).join(
        Exercise, Theme.id == Exercise.theme_id
    ).join(
        UserResponseDB, Exercise.id == UserResponseDB.exercise_id
    ).filter(
        UserResponseDB.user_id == user_id
    ).scalar()
    
    completed_themes = db.query(func.count(func.distinct(Theme.id))).join(
        Exercise, Theme.id == Exercise.theme_id
    ).join(
        UserResponseDB, Exercise.id == UserResponseDB.exercise_id
    ).filter(
        UserResponseDB.user_id == user_id
    ).scalar()
    
    completed_exercises = db.query(func.count(UserResponseDB.id)).filter(
        UserResponseDB.user_id == user_id
    ).scalar()
    
    # Calculate progress percentage
    progress_percentage = 0
    if total_exercises > 0:
        progress_percentage = round((completed_exercises / total_exercises) * 100, 1)
    
    return {
        "current_module": {
            "id": module.id,
            "title": module.title,
            "order": module.order_number
        },
        "current_theme": {
            "id": theme.id,
            "title": theme.title,
            "order": theme.order_number
        },
        "current_exercise": {
            "id": exercise.id,
            "title": exercise.title,
            "order": exercise.order_number
        },
        "completed_modules": completed_modules,
        "completed_themes": completed_themes,
        "completed_exercises": completed_exercises,
        "total_modules": total_modules,
        "total_themes": total_themes,
        "total_exercises": total_exercises,
        "progress_percentage": progress_percentage
    } 