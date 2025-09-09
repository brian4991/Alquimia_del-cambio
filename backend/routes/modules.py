from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import List

from auth import get_current_user, get_current_admin_user
from database import get_db
from models import User, Module, Theme, Exercise, UserProgress, UserResponseDB, UserSubQuestionResponseDB, ThemeCard

# Railway compatibility helper
def get_theme_card_count_safe(db, theme_id):
    """Safe way to count theme cards that works on both local and Railway"""
    import os
    if os.environ.get("DATABASE_URL"):
        # Railway: use raw SQL
        from sqlalchemy import text
        result = db.execute(text("SELECT COUNT(*) FROM theme_cards WHERE theme_id = :theme_id"), {"theme_id": theme_id})
        return result.scalar()
    else:
        # Local: normal SQLAlchemy
        return db.query(ThemeCard).filter(ThemeCard.theme_id == theme_id).count()

def get_theme_card_safe(db, card_id):
    """Safe way to get a theme card that works on both local and Railway"""
    import os
    if os.environ.get("DATABASE_URL"):
        # Railway: use raw SQL
        from sqlalchemy import text
        result = db.execute(text("""
            SELECT id, title, content, card_type, order_number, theme_id, is_editable, created_at, updated_at
            FROM theme_cards WHERE id = :card_id
        """), {"card_id": card_id})
        row = result.fetchone()
        if not row:
            return None
        # Create a simple object with the data
        class SimpleCard:
            def __init__(self, data):
                self.id, self.title, self.content, self.card_type, self.order_number, self.theme_id, self.is_editable, self.created_at, self.updated_at = data
        return SimpleCard(row)
    else:
        # Local: normal SQLAlchemy
        return db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
from schemas import (
    ModuleResponse, ThemeResponse, ExerciseResponse, ExerciseResponseRequest, 
    SubQuestionResponseRequest,
    ThemeCardResponse, ThemeCardCreate, ThemeCardUpdate,
    CardExerciseResponseRequest, CardExerciseResponseUpdate, CardExerciseResponse,
    ModuleCreate, ModuleUpdate, ThemeCreate, ThemeUpdate, 
    ExerciseCreate, ExerciseUpdate
)

router = APIRouter(tags=["modules"])

@router.get("/modules", response_model=List[ModuleResponse])
def get_modules(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    # Get user's validated modules
    validated_modules = current_user.validated_modules or []
    if isinstance(validated_modules, str):
        import json
        validated_modules = json.loads(validated_modules)
    
    result = []
    for module in modules:
        # Check if user has access to this module
        # Module 1 is always accessible, others need validation
        has_access = module.order_number == 1 or module.id in validated_modules
        
        # Check if module is completed
        module_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.module_id == module.id,
            UserProgress.completed == True
        ).first()
        
        # Calculate progress based on completed themes
        themes = db.query(Theme).filter(Theme.module_id == module.id).all()
        themes_count = len(themes)
        
        if themes_count > 0:
            completed_themes = db.query(UserProgress).filter(
                UserProgress.user_id == current_user.id,
                UserProgress.module_id == module.id,
                UserProgress.theme_id.isnot(None),
                UserProgress.completed == True
            ).count()
            
            progress_percentage = int((completed_themes / themes_count) * 100)
        else:
            progress_percentage = 0
        
        result.append(ModuleResponse(
            id=module.id,
            title=module.title,
            description=module.description,
            objective=module.objective,
            belief_to_transform=module.belief_to_transform,
            expected_results=module.expected_results,
            recommended_book=module.recommended_book,
            audio_file=module.audio_file,
            order_number=module.order_number,
            is_completed=module_progress is not None,
            is_accessible=has_access,
            progress=progress_percentage,
            themes_count=themes_count
        ))
    
    return result

@router.get("/modules/{module_id}/themes", response_model=List[ThemeResponse])
def get_module_themes(module_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    themes = db.query(Theme).filter(Theme.module_id == module_id).order_by(Theme.order_number).all()
    
    # Check if user is validated
    user_is_validated = current_user.is_validated
    
    result = []
    for i, theme in enumerate(themes):
        # Check if theme is completed
        theme_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.theme_id == theme.id,
            UserProgress.completed == True
        ).first()
        
        # Check if theme is unlocked
        if not user_is_validated:
            # Non-validated users: only first theme of module 1 is unlocked
            if module_id == 1 and i == 0:
                is_unlocked = True
            else:
                is_unlocked = False
        else:
            # Validated users: normal sequential progression
            if i == 0:
                is_unlocked = True
            else:
                # Check if previous theme is completed
                prev_theme = themes[i-1]
                prev_progress = db.query(UserProgress).filter(
                    UserProgress.user_id == current_user.id,
                    UserProgress.theme_id == prev_theme.id,
                    UserProgress.completed == True
                ).first()
                is_unlocked = prev_progress is not None
        
        # Count total cards for this theme (Railway compatible)
        total_cards = get_theme_card_count_safe(db, theme.id)
        
        result.append(ThemeResponse(
            id=theme.id,
            title=theme.title,
            content=theme.content,
            order_number=theme.order_number,
            module_id=theme.module_id,
            is_completed=theme_progress is not None,
            is_unlocked=is_unlocked,
            total_cards=total_cards
        ))
    
    return result

# ===============================
# THEME CARDS CRUD ROUTES
# ===============================

@router.get("/themes/{theme_id}", response_model=ThemeResponse)
def get_theme(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get a specific theme"""
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Check if theme is completed
    theme_progress = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.theme_id == theme.id,
        UserProgress.completed == True
    ).first()
    
    # Count total cards for this theme (Railway compatible)
    total_cards = get_theme_card_count_safe(db, theme.id)
    
    return ThemeResponse(
        id=theme.id,
        title=theme.title,
        content=theme.content,
        order_number=theme.order_number,
        module_id=theme.module_id,
        is_completed=theme_progress is not None,
        is_unlocked=True,  # We'll assume it's unlocked if they can access it
        total_cards=total_cards
    )

@router.get("/themes/{theme_id}/cards", response_model=List[ThemeCardResponse])
def get_theme_cards(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get all cards for a theme"""
    import os
    
    # Simple approach: disable exercise features on Railway for now
    is_railway = os.environ.get("DATABASE_URL") is not None
    
    if is_railway:
        # Railway: simple query without exercise columns
        from sqlalchemy import text
        sql_query = text("""
            SELECT id, title, content, card_type, order_number, theme_id, is_editable, 
                   created_at, updated_at
            FROM theme_cards 
            WHERE theme_id = :theme_id 
            ORDER BY order_number
        """)
        
        result_proxy = db.execute(sql_query, {"theme_id": theme_id})
        cards_data = result_proxy.fetchall()
        
        result = []
        for card_row in cards_data:
            card_id, title, content, card_type, order_number, theme_id_val, is_editable, created_at, updated_at = card_row
            
            result.append(ThemeCardResponse(
                id=card_id,
                title=title,
                content=content,
                card_type=card_type,
                order_number=order_number,
                theme_id=theme_id_val,
                is_editable=is_editable,
                created_at=created_at,
                updated_at=updated_at,
                exercise_instructions=None,
                exercise_questions=[],
                user_responses=None
            ))
        
        return result
    
    else:
        # Local: full functionality with exercise columns
        cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme_id).order_by(ThemeCard.order_number).all()
        
        result = []
        for card in cards:
            # Basic card data
            exercise_instructions = getattr(card, 'exercise_instructions', None)
            exercise_questions = []
            user_responses = None
            
            # Process exercise data if available
            if card.card_type == "exercise":
                try:
                    from models import UserCardResponseDB
                    
                    # Get user responses
                    responses = db.query(UserCardResponseDB).filter(
                        UserCardResponseDB.user_id == current_user.id,
                        UserCardResponseDB.card_id == card.id
                    ).all()
                    
                    user_responses = {resp.question_index: resp.response_text for resp in responses}
                    
                    # Parse exercise questions (simplified to strings for now)
                    if hasattr(card, 'exercise_questions') and card.exercise_questions:
                        import json
                        try:
                            parsed = json.loads(card.exercise_questions) if isinstance(card.exercise_questions, str) else card.exercise_questions
                            exercise_questions = [str(q) if isinstance(q, dict) else str(q) for q in parsed]
                        except:
                            exercise_questions = []
                            
                except Exception:
                    pass
            
            result.append(ThemeCardResponse(
                id=card.id,
                title=card.title,
                content=card.content,
                card_type=card.card_type,
                order_number=card.order_number,
                theme_id=card.theme_id,
                is_editable=card.is_editable,
                created_at=card.created_at,
                updated_at=card.updated_at,
                exercise_instructions=exercise_instructions,
                exercise_questions=exercise_questions,
                user_responses=user_responses
            ))
        
        return result

@router.get("/cards/{card_id}", response_model=ThemeCardResponse)
def get_card(card_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get a specific card"""
    card = get_theme_card_safe(db, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    # Return compatible response
    return ThemeCardResponse(
        id=card.id,
        title=card.title,
        content=card.content,
        card_type=card.card_type,
        order_number=card.order_number,
        theme_id=card.theme_id,
        is_editable=card.is_editable,
        created_at=card.created_at,
        updated_at=card.updated_at,
        exercise_instructions=getattr(card, 'exercise_instructions', None),
        exercise_questions=getattr(card, 'exercise_questions', []),
        user_responses=None
    )

@router.post("/themes/{theme_id}/cards", response_model=ThemeCardResponse)
def create_card(theme_id: int, card_data: ThemeCardCreate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Create a new card"""
    import json
    
    # Verify theme exists
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Create new card
    new_card = ThemeCard(
        title=card_data.title,
        content=card_data.content,
        card_type=card_data.card_type,
        order_number=card_data.order_number,
        theme_id=theme_id
    )
    
    # Set exercise-specific fields if this is an exercise card (only if columns exist)
    if card_data.card_type == "exercise":
        if hasattr(new_card, 'exercise_instructions'):
            new_card.exercise_instructions = card_data.exercise_instructions
        if hasattr(new_card, 'exercise_questions'):
            # Convert ExerciseQuestion objects to JSON
            if card_data.exercise_questions:
                questions_json = [q.dict() if hasattr(q, 'dict') else q for q in card_data.exercise_questions]
                new_card.exercise_questions = json.dumps(questions_json)
            else:
                new_card.exercise_questions = json.dumps([])
    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    
    # Parse exercise_questions for response
    exercise_questions_parsed = []
    if new_card.card_type == "exercise" and new_card.exercise_questions:
        try:
            exercise_questions_parsed = json.loads(new_card.exercise_questions)
        except:
            exercise_questions_parsed = []
    
    return ThemeCardResponse(
        id=new_card.id,
        title=new_card.title,
        content=new_card.content,
        card_type=new_card.card_type,
        order_number=new_card.order_number,
        theme_id=new_card.theme_id,
        is_editable=new_card.is_editable,
        created_at=new_card.created_at,
        updated_at=new_card.updated_at,
        exercise_instructions=new_card.exercise_instructions,
        exercise_questions=exercise_questions_parsed,
        user_responses=None
    )

@router.put("/cards/{card_id}", response_model=ThemeCardResponse)
def update_card(card_id: int, card_data: ThemeCardUpdate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Update a card"""
    import json
    
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    # Update fields if provided
    if card_data.title is not None:
        card.title = card_data.title
    if card_data.content is not None:
        card.content = card_data.content
    if card_data.card_type is not None:
        card.card_type = card_data.card_type
    if card_data.order_number is not None:
        card.order_number = card_data.order_number
    
    # Update exercise-specific fields (only if columns exist)
    if card_data.exercise_instructions is not None and hasattr(card, 'exercise_instructions'):
        card.exercise_instructions = card_data.exercise_instructions
    if card_data.exercise_questions is not None and hasattr(card, 'exercise_questions'):
        # Convert ExerciseQuestion objects to JSON
        questions_json = [q.dict() if hasattr(q, 'dict') else q for q in card_data.exercise_questions]
        card.exercise_questions = json.dumps(questions_json)
    
    # Clear exercise fields if card type is changed from exercise to something else (only if columns exist)
    if card_data.card_type is not None and card_data.card_type != "exercise":
        if hasattr(card, 'exercise_instructions'):
            card.exercise_instructions = None
        if hasattr(card, 'exercise_questions'):
            card.exercise_questions = None
    
    card.updated_at = func.now()
    
    db.commit()
    db.refresh(card)
    
    # Parse exercise_questions for response
    exercise_questions_parsed = []
    if card.card_type == "exercise" and card.exercise_questions:
        try:
            exercise_questions_parsed = json.loads(card.exercise_questions)
        except:
            exercise_questions_parsed = []
    
    return ThemeCardResponse(
        id=card.id,
        title=card.title,
        content=card.content,
        card_type=card.card_type,
        order_number=card.order_number,
        theme_id=card.theme_id,
        is_editable=card.is_editable,
        created_at=card.created_at,
        updated_at=card.updated_at,
        exercise_instructions=card.exercise_instructions,
        exercise_questions=exercise_questions_parsed,
        user_responses=None
    )

@router.delete("/cards/{card_id}")
def delete_card(card_id: int, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Delete a card"""
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    db.delete(card)
    db.commit()
    
    return {"message": "Card deleted successfully"}

# ===============================
# EXISTING ROUTES (Updated)
# ===============================

@router.get("/themes/{theme_id}/exercises", response_model=List[ExerciseResponse])
def get_theme_exercises(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).order_by(Exercise.order_number).all()
    
    result = []
    for exercise in exercises:
        # Get user's response if it exists
        user_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        # Get user's sub-question responses
        sub_question_responses = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.user_id == current_user.id,
            UserSubQuestionResponseDB.exercise_id == exercise.id
        ).order_by(UserSubQuestionResponseDB.sub_question_index).all()
        
        # Create a dict for quick lookup of responses by index
        sub_responses_dict = {
            resp.sub_question_index: resp.response_text 
            for resp in sub_question_responses
        }
        
        # Parse sub_questions from JSON string to list
        sub_questions = []
        if exercise.sub_questions:
            try:
                import json
                sub_questions = json.loads(exercise.sub_questions) if isinstance(exercise.sub_questions, str) else exercise.sub_questions
            except:
                sub_questions = []
        
        result.append(ExerciseResponse(
            id=exercise.id,
            title=exercise.title,
            instructions=exercise.instructions,
            sub_questions=sub_questions,
            order_number=exercise.order_number,
            theme_id=exercise.theme_id,
            user_response=user_response.response_text if user_response else None,
            sub_question_responses=sub_responses_dict
        ))
    
    return result

@router.post("/submit-response")
def submit_response(response: ExerciseResponseRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Check if response already exists
    existing_response = db.query(UserResponseDB).filter(
        UserResponseDB.user_id == current_user.id,
        UserResponseDB.exercise_id == response.exercise_id
    ).first()
    
    if existing_response:
        # Update existing response
        existing_response.response_text = response.response_text
        existing_response.submitted_at = func.now()
    else:
        # Create new response
        db_response = UserResponseDB(
            user_id=current_user.id,
            exercise_id=response.exercise_id,
            response_text=response.response_text
        )
        db.add(db_response)
    
    db.commit()
    return {"message": "Response submitted successfully"}

@router.post("/submit-sub-question-response")
def submit_sub_question_response(
    response: SubQuestionResponseRequest, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """Submit or update response to a specific sub-question"""
    
    # Validate exercise exists
    exercise = db.query(Exercise).filter(Exercise.id == response.exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    # Validate sub_question_index is valid
    if not exercise.sub_questions or response.sub_question_index >= len(exercise.sub_questions):
        raise HTTPException(status_code=400, detail="Invalid sub-question index")
    
    # Check if response already exists
    existing_response = db.query(UserSubQuestionResponseDB).filter(
        UserSubQuestionResponseDB.user_id == current_user.id,
        UserSubQuestionResponseDB.exercise_id == response.exercise_id,
        UserSubQuestionResponseDB.sub_question_index == response.sub_question_index
    ).first()
    
    if existing_response:
        # Update existing response
        existing_response.response_text = response.response_text
        existing_response.updated_at = func.now()
    else:
        # Create new response
        db_response = UserSubQuestionResponseDB(
            user_id=current_user.id,
            exercise_id=response.exercise_id,
            sub_question_index=response.sub_question_index,
            response_text=response.response_text
        )
        db.add(db_response)
    
    db.commit()
    return {
        "message": "Sub-question response submitted successfully",
        "exercise_id": response.exercise_id,
        "sub_question_index": response.sub_question_index
    }

@router.post("/complete-theme/{theme_id}")
def complete_theme(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Get the theme to access module_id
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Check if all exercises in the theme have responses
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).all()
    
    for exercise in exercises:
        # Check for main response
        main_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        # Check for sub-question responses
        sub_responses = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.user_id == current_user.id,
            UserSubQuestionResponseDB.exercise_id == exercise.id
        ).all()
        
        # Exercise is complete if it has either main response OR sub-question responses
        if not main_response and not sub_responses:
            raise HTTPException(status_code=400, detail=f"Exercise '{exercise.title}' must be completed before marking theme as complete")
    
    # Mark theme as completed
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.theme_id == theme_id
    ).first()
    
    if progress:
        progress.completed = True
        progress.completed_at = func.now()
    else:
        progress = UserProgress(
            user_id=current_user.id,
            module_id=theme.module_id,
            theme_id=theme_id,
            completed=True,
            completed_at=func.now()
        )
        db.add(progress)
    
    db.commit()
    return {"message": "Theme completed successfully"}

@router.get("/debug/theme/{theme_id}/completion-status")
def debug_theme_completion_status(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Debug endpoint to check theme completion status"""
    # Get all exercises for this theme
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).all()
    
    result = {
        "theme_id": theme_id,
        "user_id": current_user.id,
        "exercises": [],
        "can_complete": True,
        "missing_responses": []
    }
    
    for exercise in exercises:
        # Check main response
        main_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        # Check sub-question responses
        sub_responses = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.user_id == current_user.id,
            UserSubQuestionResponseDB.exercise_id == exercise.id
        ).all()
        
        exercise_info = {
            "exercise_id": exercise.id,
            "title": exercise.title,
            "has_main_response": main_response is not None,
            "sub_responses_count": len(sub_responses),
            "sub_questions_count": len(exercise.sub_questions) if exercise.sub_questions else 0
        }
        
        if not main_response:
            result["can_complete"] = False
            result["missing_responses"].append(f"Exercise {exercise.id}: No main response")
            
        result["exercises"].append(exercise_info)
    
    return result

@router.post("/admin/force-complete-theme/{theme_id}/{user_id}")
def admin_force_complete_theme(
    theme_id: int, 
    user_id: int, 
    current_admin: User = Depends(get_current_admin_user), 
    db: Session = Depends(get_db)
):
    """Admin endpoint to force complete a theme for a user"""
    # Get the theme
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Get the user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Mark theme as completed
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.theme_id == theme_id
    ).first()
    
    if progress:
        progress.completed = True
        progress.completed_at = func.now()
    else:
        progress = UserProgress(
            user_id=user_id,
            module_id=theme.module_id,
            theme_id=theme_id,
            completed=True,
            completed_at=func.now()
        )
        db.add(progress)
    
    db.commit()
    return {"message": f"Theme {theme.title} force completed for user {user.username}"}

# ===============================
# MODULES CRUD ROUTES
# ===============================

@router.post("/modules", response_model=ModuleResponse)
def create_module(module_data: ModuleCreate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Create a new module"""
    new_module = Module(
        title=module_data.title,
        description=module_data.description,
        objective=module_data.objective,
        belief_to_transform=module_data.belief_to_transform,
        expected_results=module_data.expected_results,
        recommended_book=module_data.recommended_book,
        audio_file=module_data.audio_file,
        order_number=module_data.order_number,
        is_active=True
    )
    
    db.add(new_module)
    db.commit()
    db.refresh(new_module)
    
    return ModuleResponse(
        id=new_module.id,
        title=new_module.title,
        description=new_module.description,
        objective=new_module.objective,
        belief_to_transform=new_module.belief_to_transform,
        expected_results=new_module.expected_results,
        recommended_book=new_module.recommended_book,
        audio_file=new_module.audio_file,
        order_number=new_module.order_number,
        is_completed=False
    )

@router.put("/modules/{module_id}", response_model=ModuleResponse)
def update_module(module_id: int, module_data: ModuleUpdate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Update a module"""
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    # Update fields if provided
    if module_data.title is not None:
        module.title = module_data.title
    if module_data.description is not None:
        module.description = module_data.description
    if module_data.objective is not None:
        module.objective = module_data.objective
    if module_data.belief_to_transform is not None:
        module.belief_to_transform = module_data.belief_to_transform
    if module_data.expected_results is not None:
        module.expected_results = module_data.expected_results
    if module_data.recommended_book is not None:
        module.recommended_book = module_data.recommended_book
    if module_data.audio_file is not None:
        module.audio_file = module_data.audio_file
    if module_data.order_number is not None:
        module.order_number = module_data.order_number
    if module_data.is_active is not None:
        module.is_active = module_data.is_active
    
    db.commit()
    db.refresh(module)
    
    return ModuleResponse(
        id=module.id,
        title=module.title,
        description=module.description,
        objective=module.objective,
        belief_to_transform=module.belief_to_transform,
        expected_results=module.expected_results,
        recommended_book=module.recommended_book,
        audio_file=module.audio_file,
        order_number=module.order_number,
        is_completed=False
    )

@router.delete("/modules/{module_id}")
def delete_module(module_id: int, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Delete a module"""
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    db.delete(module)
    db.commit()
    
    return {"message": "Module deleted successfully"}

# ===============================
# THEMES CRUD ROUTES
# ===============================

@router.post("/modules/{module_id}/themes", response_model=ThemeResponse)
def create_theme(module_id: int, theme_data: ThemeCreate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Create a new theme"""
    # Verify module exists
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    new_theme = Theme(
        title=theme_data.title,
        content=theme_data.content,
        order_number=theme_data.order_number,
        module_id=module_id
    )
    
    db.add(new_theme)
    db.commit()
    db.refresh(new_theme)
    
    return ThemeResponse(
        id=new_theme.id,
        title=new_theme.title,
        content=new_theme.content,
        order_number=new_theme.order_number,
        module_id=new_theme.module_id,
        is_completed=False,
        is_unlocked=True,
        total_cards=0
    )

@router.put("/themes/{theme_id}", response_model=ThemeResponse)
def update_theme(theme_id: int, theme_data: ThemeUpdate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Update a theme"""
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Update fields if provided
    if theme_data.title is not None:
        theme.title = theme_data.title
    if theme_data.content is not None:
        theme.content = theme_data.content
    if theme_data.order_number is not None:
        theme.order_number = theme_data.order_number
    
    db.commit()
    db.refresh(theme)
    
    # Count total cards for this theme (Railway compatible)
    total_cards = get_theme_card_count_safe(db, theme.id)
    
    return ThemeResponse(
        id=theme.id,
        title=theme.title,
        content=theme.content,
        order_number=theme.order_number,
        module_id=theme.module_id,
        is_completed=False,
        is_unlocked=True,
        total_cards=total_cards
    )

@router.delete("/themes/{theme_id}")
def delete_theme(theme_id: int, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Delete a theme"""
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    db.delete(theme)
    db.commit()
    
    return {"message": "Theme deleted successfully"}

# ===============================
# EXERCISES CRUD ROUTES
# ===============================

@router.post("/themes/{theme_id}/exercises", response_model=ExerciseResponse)
def create_exercise(theme_id: int, exercise_data: ExerciseCreate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Create a new exercise"""
    # Verify theme exists
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    new_exercise = Exercise(
        title=exercise_data.title,
        instructions=exercise_data.instructions,
        sub_questions=exercise_data.sub_questions,
        order_number=exercise_data.order_number,
        theme_id=theme_id
    )
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    return ExerciseResponse(
        id=new_exercise.id,
        title=new_exercise.title,
        instructions=new_exercise.instructions,
        sub_questions=new_exercise.sub_questions or [],
        order_number=new_exercise.order_number,
        theme_id=new_exercise.theme_id,
        user_response=None
    )

@router.put("/exercises/{exercise_id}", response_model=ExerciseResponse)
def update_exercise(exercise_id: int, exercise_data: ExerciseUpdate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Update an exercise"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    # Update fields if provided
    if exercise_data.title is not None:
        exercise.title = exercise_data.title
    if exercise_data.instructions is not None:
        exercise.instructions = exercise_data.instructions
    if exercise_data.sub_questions is not None:
        exercise.sub_questions = exercise_data.sub_questions
    if exercise_data.order_number is not None:
        exercise.order_number = exercise_data.order_number
    
    db.commit()
    db.refresh(exercise)
    
    return ExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        instructions=exercise.instructions,
        sub_questions=exercise.sub_questions or [],
        order_number=exercise.order_number,
        theme_id=exercise.theme_id,
        user_response=None
    )

@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Delete an exercise"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    db.delete(exercise)
    db.commit()
    
    return {"message": "Exercise deleted successfully"}

# ===============================
# CARD EXERCISE RESPONSE ROUTES
# ===============================

@router.post("/cards/{card_id}/responses")
def submit_card_exercise_response(
    card_id: int, 
    response_data: CardExerciseResponseRequest, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """Submit or update a response to an exercise card question"""
    from models import UserCardResponseDB
    
    # Verify card exists and is an exercise card
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    if card.card_type != "exercise":
        raise HTTPException(status_code=400, detail="Card is not an exercise card")
    
    # Check if response already exists
    existing_response = db.query(UserCardResponseDB).filter(
        UserCardResponseDB.user_id == current_user.id,
        UserCardResponseDB.card_id == card_id,
        UserCardResponseDB.question_index == response_data.question_index
    ).first()
    
    if existing_response:
        # Update existing response
        existing_response.response_text = response_data.response_text
        existing_response.updated_at = func.now()
        db.commit()
        db.refresh(existing_response)
        return {
            "message": "Response updated successfully",
            "response_id": existing_response.id
        }
    else:
        # Create new response
        new_response = UserCardResponseDB(
            user_id=current_user.id,
            card_id=card_id,
            question_index=response_data.question_index,
            response_text=response_data.response_text
        )
        db.add(new_response)
        db.commit()
        db.refresh(new_response)
        return {
            "message": "Response submitted successfully",
            "response_id": new_response.id
        }

@router.get("/cards/{card_id}/responses")
def get_card_exercise_responses(
    card_id: int, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """Get all responses for an exercise card (current user only)"""
    from models import UserCardResponseDB
    
    # Verify card exists and is an exercise card
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    if card.card_type != "exercise":
        raise HTTPException(status_code=400, detail="Card is not an exercise card")
    
    # Get user's responses for this card
    responses = db.query(UserCardResponseDB).filter(
        UserCardResponseDB.user_id == current_user.id,
        UserCardResponseDB.card_id == card_id
    ).order_by(UserCardResponseDB.question_index).all()
    
    return {
        "card_id": card_id,
        "responses": {resp.question_index: resp.response_text for resp in responses}
    }

@router.delete("/cards/{card_id}/responses/{question_index}")
def delete_card_exercise_response(
    card_id: int,
    question_index: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a specific response to an exercise card question"""
    from models import UserCardResponseDB
    
    # Find and delete the response
    response = db.query(UserCardResponseDB).filter(
        UserCardResponseDB.user_id == current_user.id,
        UserCardResponseDB.card_id == card_id,
        UserCardResponseDB.question_index == question_index
    ).first()
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    db.delete(response)
    db.commit()
    
    return {"message": "Response deleted successfully"} 