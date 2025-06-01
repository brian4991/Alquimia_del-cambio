from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from auth import get_current_user
from database import get_db
from models import User, Module, Theme, Exercise, UserProgress, UserResponseDB

router = APIRouter(tags=["legacy"])

@router.get("/steps", response_model=List[dict])
def get_steps_legacy(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint for compatibility with old frontend"""
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    result = []
    for module in modules:
        # Check if module is completed
        module_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.module_id == module.id,
            UserProgress.completed == True
        ).first()
        
        result.append({
            "id": module.id,
            "title": module.title,
            "description": module.description,
            "completed": module_progress is not None
        })
    
    return result

@router.get("/steps/{step_id}/exercises")
def get_step_exercises_legacy(step_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint - returns exercises from the first theme of the module"""
    # Get first theme of the module
    theme = db.query(Theme).filter(
        Theme.module_id == step_id,
        Theme.order_number == 1
    ).first()
    
    if not theme:
        return []
    
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme.id).order_by(Exercise.order_number).all()
    
    result = []
    for exercise in exercises:
        user_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        result.append({
            "id": exercise.id,
            "question": exercise.question,
            "user_response": user_response.response_text if user_response else None
        })
    
    return result

@router.post("/complete-step/{step_id}")
def complete_step_legacy(step_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint - completes the first theme of the module"""
    from .modules import complete_theme
    
    theme = db.query(Theme).filter(
        Theme.module_id == step_id,
        Theme.order_number == 1
    ).first()
    
    if theme:
        return complete_theme(theme.id, current_user, db)
    
    return {"message": "Step completed successfully"} 