from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from starlette.responses import JSONResponse
import json

from auth import hash_password, verify_password, create_access_token, get_current_user, get_current_admin_user
from database import get_db
from models import User, UserResponseDB, UserSubQuestionResponseDB, Exercise, Theme, Module
from schemas import UserCreate, UserLogin, UserResponse, Token
from oauth import oauth, create_or_get_oauth_user, generate_oauth_token

router = APIRouter(tags=["authentication"])

# Local authentication (for development only)
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
    # Use explicit redirect URI to match Google Console configuration
    import os
    import logging
    logger = logging.getLogger(__name__)
    
    # Determine the correct backend URL
    # Priority: 1. BACKEND_URL env var, 2. Custom domain from Host header, 3. request.base_url
    backend_url = os.environ.get("BACKEND_URL")
    
    if not backend_url:
        # Check if we're using a custom domain (api.nicoleramirezpsicoach.com)
        host = request.headers.get("host", "").lower()
        if "api.nicoleramirezpsicoach.com" in host:
            # Use HTTPS with custom domain
            backend_url = "https://api.nicoleramirezpsicoach.com"
        else:
            # Fallback to request base URL (Railway URL)
            backend_url = str(request.base_url).rstrip('/')
    
    redirect_uri = f"{backend_url}/auth/google/callback"
    
    # Log for debugging
    logger.info(f"OAuth login initiated - redirect_uri: {redirect_uri}, backend_url: {backend_url}, host: {request.headers.get('host')}")
    
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Google OAuth callback"""
    try:
        # Log the request URL for debugging
        import os
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"OAuth callback received: {request.url}")
        
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get('userinfo')
        
        if not user_info:
            # Fetch user info if not included in token
            resp = await oauth.google.get('https://www.googleapis.com/oauth2/v3/userinfo', token=token)
            user_info = resp.json()
        
        # Create or get user
        user = await create_or_get_oauth_user('google', user_info, db)
        
        # Generate token
        access_token = generate_oauth_token(user)
        
        # Redirect to frontend with token
        # Determine the correct frontend URL
        frontend_url_env = os.environ.get("FRONTEND_URL")
        
        if not frontend_url_env or "vercel.app" in frontend_url_env.lower() or "alquimia-del-cambio" in frontend_url_env.lower():
            # Use the new domain if FRONTEND_URL is not set or points to old domain
            frontend_url_env = "https://www.nicoleramirezpsicoach.com"
        
        frontend_url = f"{frontend_url_env}/auth/callback?token={access_token}"
        
        # Log for debugging
        logger.info(f"OAuth callback redirecting to: {frontend_url}")
        
        return RedirectResponse(url=frontend_url)
        
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"OAuth callback error: {str(e)}", exc_info=True)
        # Return more detailed error message
        error_msg = str(e)
        if "mismatching_state" in error_msg or "state" in error_msg.lower():
            error_msg += " - Vérifiez que le redirect URI dans Google OAuth Console correspond exactement à l'URL du callback."
        raise HTTPException(status_code=400, detail=f"OAuth authentication failed: {error_msg}")

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

@router.get("/admin/users")
def get_all_users(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Get all users - Admin only"""
    users = db.query(User).all()
    return users

@router.get("/admin/modules")
def get_all_modules_admin(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Get all modules for admin - no access control"""
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    result = []
    for module in modules:
        result.append({
            "id": module.id,
            "title": module.title,
            "description": module.description,
            "objective": module.objective,
            "belief_to_transform": module.belief_to_transform,
            "expected_results": module.expected_results,
            "recommended_book": module.recommended_book,
            "audio_file": module.audio_file,
            "order_number": module.order_number
        })
    
    return result

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

@router.post("/admin/users/{user_id}/validate-module/{module_id}")
def validate_user_module(
    user_id: int,
    module_id: int,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Validate user progression for a specific module - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if module exists
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    # Get current validated modules
    validated_modules = []
    if user.validated_modules:
        try:
            if isinstance(user.validated_modules, str):
                validated_modules = json.loads(user.validated_modules) if user.validated_modules.strip() else []
            elif isinstance(user.validated_modules, list):
                validated_modules = user.validated_modules
        except (json.JSONDecodeError, AttributeError):
            validated_modules = []
    
    # Add module to validated list if not already there
    if module_id not in validated_modules:
        validated_modules.append(module_id)
        # Save as JSON string
        user.validated_modules = json.dumps(validated_modules)
        db.commit()
        
        return {
            "message": f"Module {module.title} validated for user {user.username}",
            "validated_modules": validated_modules
        }
    else:
        return {
            "message": f"Module {module.title} already validated for user {user.username}",
            "validated_modules": validated_modules
        }

@router.delete("/admin/users/{user_id}/validate-module/{module_id}")
def revoke_user_module_validation(
    user_id: int,
    module_id: int,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Revoke user validation for a specific module - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if module exists
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    # Get current validated modules
    validated_modules = []
    if user.validated_modules:
        try:
            if isinstance(user.validated_modules, str):
                validated_modules = json.loads(user.validated_modules) if user.validated_modules.strip() else []
            elif isinstance(user.validated_modules, list):
                validated_modules = user.validated_modules
        except (json.JSONDecodeError, AttributeError):
            validated_modules = []
    
    # Remove module from validated list
    if module_id in validated_modules:
        validated_modules.remove(module_id)
        # Save as JSON string
        user.validated_modules = json.dumps(validated_modules)
        db.commit()
        
        return {
            "message": f"Module {module.title} validation revoked for user {user.username}",
            "validated_modules": validated_modules
        }
    else:
        return {
            "message": f"Module {module.title} was not validated for user {user.username}",
            "validated_modules": validated_modules
        }

@router.post("/admin/users/{user_id}/validate")
def validate_user(
    user_id: int,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Validate a user to enable normal progression - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_validated = True
    db.commit()
    
    return {"message": f"User {user.username} has been validated and can now progress normally"}

@router.delete("/admin/users/{user_id}/validate")
def revoke_user_validation(
    user_id: int,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Revoke user validation - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_validated = False
    db.commit()
    
    return {"message": f"User {user.username} validation has been revoked"}

@router.get("/admin/users/{user_id}/responses")
def get_user_responses(
    user_id: int,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Get all responses from a specific user - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    result = []
    
    # Get old-style user responses (user_responses table)
    old_responses = db.query(UserResponseDB, Exercise, Theme, Module).join(
        Exercise, UserResponseDB.exercise_id == Exercise.id
    ).join(
        Theme, Exercise.theme_id == Theme.id
    ).join(
        Module, Theme.module_id == Module.id
    ).filter(
        UserResponseDB.user_id == user_id
    ).order_by(UserResponseDB.submitted_at.desc()).all()
    
    for response, exercise, theme, module in old_responses:
        result.append({
            "id": f"old_{response.id}",
            "exercise_id": exercise.id,
            "exercise_title": exercise.title,
            "theme_title": theme.title,
            "module_title": module.title,
            "response_text": response.response_text,
            "response_type": "main",
            "sub_question_index": None,
            "submitted_at": response.submitted_at,
        })
    
    # Get new-style sub-question responses (user_sub_question_responses table)
    sub_responses = db.query(UserSubQuestionResponseDB, Exercise, Theme, Module).join(
        Exercise, UserSubQuestionResponseDB.exercise_id == Exercise.id
    ).join(
        Theme, Exercise.theme_id == Theme.id
    ).join(
        Module, Theme.module_id == Module.id
    ).filter(
        UserSubQuestionResponseDB.user_id == user_id
    ).order_by(UserSubQuestionResponseDB.submitted_at.desc()).all()
    
    for response, exercise, theme, module in sub_responses:
        # Parse sub_questions and exercise_sections from JSON if they exist
        import json
        sub_questions = []
        if exercise.sub_questions:
            try:
                sub_questions = json.loads(exercise.sub_questions) if isinstance(exercise.sub_questions, str) else exercise.sub_questions
            except:
                sub_questions = []
        
        exercise_sections = []
        if exercise.exercise_sections:
            try:
                exercise_sections = json.loads(exercise.exercise_sections) if isinstance(exercise.exercise_sections, str) else exercise.exercise_sections
            except:
                exercise_sections = []
        
        # Get the question text based on the index type
        sub_question_text = "Question"
        exercise_title_suffix = ""
        response_type = "sub_question"
        
        # Handle both int and string representations
        if isinstance(response.sub_question_index, int):
            # Legacy format: integer index
            if sub_questions and response.sub_question_index < len(sub_questions):
                sub_question_text = sub_questions[response.sub_question_index]
                exercise_title_suffix = f" - Q{response.sub_question_index + 1}"
        elif isinstance(response.sub_question_index, str):
            # Check if it's a string representation of an integer (legacy format stored as string)
            try:
                index_int = int(response.sub_question_index)
                if sub_questions and index_int < len(sub_questions):
                    sub_question_text = sub_questions[index_int]
                    exercise_title_suffix = f" - Q{index_int + 1}"
            except ValueError:
                # Not a plain integer, check if it's the new "section_X_question_Y" format
                if response.sub_question_index.startswith("section_"):
                    response_type = "exercise_section"
                    try:
                        parts = response.sub_question_index.split("_")
                        if len(parts) >= 4:  # section_X_question_Y
                            section_index = int(parts[1])
                            question_index = int(parts[3])
                            
                            if section_index < len(exercise_sections):
                                section = exercise_sections[section_index]
                                section_title = section.get('title', f'Section {section_index + 1}')
                                
                                if section.get('questions') and question_index < len(section['questions']):
                                    question = section['questions'][question_index]
                                    sub_question_text = question.get('question', 'Question')
                                    exercise_title_suffix = f" - {section_title} - Q{question_index + 1}"
                                else:
                                    exercise_title_suffix = f" - {section_title}"
                            else:
                                exercise_title_suffix = f" - {response.sub_question_index}"
                    except (ValueError, IndexError):
                        exercise_title_suffix = f" - {response.sub_question_index}"
        
        result.append({
            "id": f"sub_{response.id}",
            "exercise_id": exercise.id,
            "exercise_title": f"{exercise.title}{exercise_title_suffix}",
            "theme_title": theme.title,
            "module_title": module.title,
            "response_text": response.response_text,
            "response_type": response_type,
            "sub_question_index": response.sub_question_index,
            "sub_question_text": sub_question_text,
            "submitted_at": response.submitted_at,
        })
    
    # Card exercise responses removed for Railway compatibility
    
    # Sort all responses by date (most recent first)
    result.sort(key=lambda x: x['submitted_at'], reverse=True)
    
    return result

@router.get("/admin/users/{user_id}/current-responses")
def get_user_current_responses(
    user_id: int,
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Get current responses from a user (only for existing exercises) - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    result = []
    
    # Get all modules, themes, and exercises with their current responses
    modules = db.query(Module).all()
    
    for module in modules:
        module_data = {
            "module_id": module.id,
            "module_title": module.title,
            "themes": []
        }
        
        for theme in module.themes:
            theme_data = {
                "theme_id": theme.id,
                "theme_title": theme.title,
                "exercises": []
            }
            
            for exercise in theme.exercises:
                # Parse exercise data
                import json
                sub_questions = []
                if exercise.sub_questions:
                    try:
                        sub_questions = json.loads(exercise.sub_questions) if isinstance(exercise.sub_questions, str) else exercise.sub_questions
                    except:
                        sub_questions = []
                
                exercise_sections = []
                if exercise.exercise_sections:
                    try:
                        exercise_sections = json.loads(exercise.exercise_sections) if isinstance(exercise.exercise_sections, str) else exercise.exercise_sections
                    except:
                        exercise_sections = []
                
                exercise_data = {
                    "exercise_id": exercise.id,
                    "exercise_title": exercise.title,
                    "exercise_instructions": exercise.exercise_instructions,
                    "sub_questions": sub_questions,
                    "exercise_sections": exercise_sections,
                    "responses": []
                }
                
                # Get main exercise response
                main_response = db.query(UserResponseDB).filter(
                    UserResponseDB.user_id == user_id,
                    UserResponseDB.exercise_id == exercise.id
                ).first()
                
                if main_response:
                    exercise_data["responses"].append({
                        "id": f"old_{main_response.id}",
                        "type": "main",
                        "question_text": "Respuesta principal",
                        "response_text": main_response.response_text,
                        "submitted_at": main_response.submitted_at
                    })
                
                # Get sub-question responses (both legacy and new format)
                sub_responses = db.query(UserSubQuestionResponseDB).filter(
                    UserSubQuestionResponseDB.user_id == user_id,
                    UserSubQuestionResponseDB.exercise_id == exercise.id
                ).all()
                
                for sub_response in sub_responses:
                    question_text = "Question"
                    response_type = "sub_question"
                    
                    if isinstance(sub_response.sub_question_index, int):
                        # Legacy format: integer
                        if sub_questions and sub_response.sub_question_index < len(sub_questions):
                            question_text = sub_questions[sub_response.sub_question_index]
                    elif isinstance(sub_response.sub_question_index, str):
                        # Check if it's a string representation of an integer (legacy format stored as string)
                        try:
                            index_int = int(sub_response.sub_question_index)
                            if sub_questions and index_int < len(sub_questions):
                                question_text = sub_questions[index_int]
                        except ValueError:
                            # Not a plain integer, check if it's the new "section_X_question_Y" format
                            if sub_response.sub_question_index.startswith("section_"):
                                response_type = "exercise_section"
                                try:
                                    parts = sub_response.sub_question_index.split("_")
                                    if len(parts) >= 4:
                                        section_index = int(parts[1])
                                        question_index = int(parts[3])
                                        
                                        if section_index < len(exercise_sections):
                                            section = exercise_sections[section_index]
                                            section_title = section.get('title', f'Section {section_index + 1}')
                                            
                                            if section.get('questions') and question_index < len(section['questions']):
                                                question = section['questions'][question_index]
                                                question_text = f"{section_title} - {question.get('question', 'Question')}"
                                except (ValueError, IndexError):
                                    question_text = sub_response.sub_question_index
                    
                    exercise_data["responses"].append({
                        "id": f"sub_{sub_response.id}",
                        "type": response_type,
                        "question_text": question_text,
                        "response_text": sub_response.response_text,
                        "submitted_at": sub_response.updated_at or sub_response.created_at,
                        "sub_question_index": sub_response.sub_question_index
                    })
                
                # Only include exercises that have responses
                if exercise_data["responses"]:
                    theme_data["exercises"].append(exercise_data)
            
            # Only include themes that have exercises with responses
            if theme_data["exercises"]:
                module_data["themes"].append(theme_data)
        
        # Only include modules that have themes with exercises with responses
        if module_data["themes"]:
            result.append(module_data)
    
    return result

@router.put("/admin/users/{user_id}/responses/{response_id}")
def update_user_response(
    user_id: int,
    response_id: str,  # Format: "old_123" or "sub_456"
    response_data: dict,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Update a user response - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Parse response_id to determine type and actual ID
    if response_id.startswith("old_"):
        # Old-style response
        actual_id = int(response_id.replace("old_", ""))
        response = db.query(UserResponseDB).filter(
            UserResponseDB.id == actual_id,
            UserResponseDB.user_id == user_id
        ).first()
        if not response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        response.response_text = response_data.get("response_text", response.response_text)
        response.submitted_at = func.now()
        
    elif response_id.startswith("sub_"):
        # Sub-question response
        actual_id = int(response_id.replace("sub_", ""))
        response = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.id == actual_id,
            UserSubQuestionResponseDB.user_id == user_id
        ).first()
        if not response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        response.response_text = response_data.get("response_text", response.response_text)
        response.updated_at = func.now()
    else:
        raise HTTPException(status_code=400, detail="Invalid response ID format")
    
    db.commit()
    return {"message": "Response updated successfully"}

@router.delete("/admin/users/{user_id}/responses/{response_id}")
def delete_user_response(
    user_id: int,
    response_id: str,  # Format: "old_123" or "sub_456"
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Delete a user response - Admin only"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Parse response_id to determine type and actual ID
    if response_id.startswith("old_"):
        # Old-style response
        actual_id = int(response_id.replace("old_", ""))
        response = db.query(UserResponseDB).filter(
            UserResponseDB.id == actual_id,
            UserResponseDB.user_id == user_id
        ).first()
        if not response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        db.delete(response)
        
    elif response_id.startswith("sub_"):
        # Sub-question response
        actual_id = int(response_id.replace("sub_", ""))
        response = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.id == actual_id,
            UserSubQuestionResponseDB.user_id == user_id
        ).first()
        if not response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        db.delete(response)
    else:
        raise HTTPException(status_code=400, detail="Invalid response ID format")
    
    db.commit()
    return {"message": "Response deleted successfully"}

@router.get("/admin/users/stats")
def get_users_stats(
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Get general statistics about users - Admin only"""
    
    total_users = db.query(func.count(User.id)).scalar()
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar()
    
    # Count all types of responses
    old_responses = db.query(func.count(UserResponseDB.id)).scalar()
    sub_responses = db.query(func.count(UserSubQuestionResponseDB.id)).scalar()
    
    # Card exercise responses removed for Railway compatibility
    total_responses = old_responses + sub_responses
    
    # Get users with their response counts and progress
    # We'll calculate response counts separately since we have multiple tables
    users_base = db.query(
        User.id,
        User.username,
        User.email,
        User.role,
        User.provider,
        User.is_active,
        User.created_at
    ).all()
    
    users_data = []
    for user_data in users_base:
        # Get the full user object for validated_modules
        full_user = db.query(User).filter(User.id == user_data.id).first()
        
        # Calculate total response count for this user from all tables
        old_count = db.query(func.count(UserResponseDB.id)).filter(UserResponseDB.user_id == user_data.id).scalar() or 0
        sub_count = db.query(func.count(UserSubQuestionResponseDB.id)).filter(UserSubQuestionResponseDB.user_id == user_data.id).scalar() or 0
        # Card exercise responses removed for Railway compatibility
        total_response_count = old_count + sub_count
        
        # Calculate user progress
        user_progress = get_user_progress(db, user_data.id)
        
        # Parse validated_modules
        validated_modules = []
        if full_user.validated_modules:
            try:
                if isinstance(full_user.validated_modules, str):
                    validated_modules = json.loads(full_user.validated_modules)
                else:
                    validated_modules = full_user.validated_modules
            except:
                validated_modules = []
        
        users_data.append({
            "id": user_data.id,
            "username": user_data.username,
            "email": user_data.email,
            "role": user_data.role,
            "provider": user_data.provider,
            "is_active": user_data.is_active,
            "is_validated": full_user.is_validated,
            "created_at": user_data.created_at,
            "response_count": total_response_count,
            "validated_modules": validated_modules,
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