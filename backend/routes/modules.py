from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import List
import json

from auth import get_current_user, get_current_admin_user
from database import get_db
from models import User, Module, Theme, Exercise, UserProgress, UserResponseDB, UserSubQuestionResponseDB, ThemeCard

from schemas import (
    ModuleResponse, ThemeResponse, ExerciseResponse, ExerciseResponseRequest, 
    SubQuestionResponseRequest,
    ThemeCardResponse, ThemeCardCreate, ThemeCardUpdate,
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
        
        # Count total cards for this theme
        total_cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme.id).count()
        
        result.append(ThemeResponse(
            id=theme.id,
            title=theme.title,
            content=theme.content,
            order_number=theme.order_number,
            module_id=theme.module_id,
            theme_type=theme.theme_type if hasattr(theme, 'theme_type') and theme.theme_type else "theme",
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
    
    # Count total cards for this theme
    total_cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme.id).count()
    
    return ThemeResponse(
        id=theme.id,
        title=theme.title,
        content=theme.content,
        order_number=theme.order_number,
        module_id=theme.module_id,
        theme_type=theme.theme_type if hasattr(theme, 'theme_type') and theme.theme_type else "theme",
        is_completed=theme_progress is not None,
        is_unlocked=True,  # We'll assume it's unlocked if they can access it
        total_cards=total_cards
    )

@router.get("/themes/{theme_id}/cards", response_model=List[ThemeCardResponse])
def get_theme_cards(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get all cards for a theme"""
    import json
    
    cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme_id).order_by(ThemeCard.order_number).all()
    
    result = []
    for card in cards:
        # Parse exercise data
        exercise_questions_parsed = []
        exercise_sections_parsed = []
        
        if card.card_type == "exercise":
            # Parse legacy exercise_questions
            if card.exercise_questions:
                try:
                    parsed_data = json.loads(card.exercise_questions)
                    if isinstance(parsed_data, list):
                        exercise_questions_parsed = []
                        for item in parsed_data:
                            if isinstance(item, str):
                                exercise_questions_parsed.append({
                                    "type": "text",
                                    "question": item
                                })
                            elif isinstance(item, dict):
                                exercise_questions_parsed.append(item)
                except Exception as e:
                    print(f"Error parsing exercise_questions for card {card.id}: {e}")
            
            # Parse new exercise_sections
            if hasattr(card, 'exercise_sections') and card.exercise_sections:
                try:
                    exercise_sections_parsed = json.loads(card.exercise_sections)
                except Exception as e:
                    print(f"Error parsing exercise_sections for card {card.id}: {e}")
                    exercise_sections_parsed = []
        
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
            exercise_instructions=card.exercise_instructions,
            exercise_questions=exercise_questions_parsed,
            exercise_sections=exercise_sections_parsed
        ))
    
    return result

@router.get("/cards/{card_id}", response_model=ThemeCardResponse)
def get_card(card_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get a specific card"""
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    return ThemeCardResponse(
        id=card.id,
        title=card.title,
        content=card.content,
        card_type=card.card_type,
        order_number=card.order_number,
        theme_id=card.theme_id,
        is_editable=card.is_editable,
        created_at=card.created_at,
        updated_at=card.updated_at
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
    
    # Set exercise-specific fields if this is an exercise card
    if card_data.card_type == "exercise":
        # Legacy fields (for backward compatibility)
        new_card.exercise_instructions = card_data.exercise_instructions
        
        if card_data.exercise_questions:
            questions_json = [q.dict() if hasattr(q, 'dict') else q for q in card_data.exercise_questions]
            new_card.exercise_questions = json.dumps(questions_json)
        else:
            new_card.exercise_questions = json.dumps([])
        
        # New sections system
        if card_data.exercise_sections:
            sections_json = [s.dict() if hasattr(s, 'dict') else s for s in card_data.exercise_sections]
            new_card.exercise_sections = json.dumps(sections_json)
        else:
            new_card.exercise_sections = json.dumps([])
    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    
    # Parse exercise data for response
    exercise_questions_parsed = []
    exercise_sections_parsed = []
    
    if new_card.card_type == "exercise":
        # Parse legacy questions
        if new_card.exercise_questions:
            try:
                exercise_questions_parsed = json.loads(new_card.exercise_questions)
            except Exception as e:
                exercise_questions_parsed = []
        
        # Parse new sections
        if hasattr(new_card, 'exercise_sections') and new_card.exercise_sections:
            try:
                exercise_sections_parsed = json.loads(new_card.exercise_sections)
            except Exception as e:
                exercise_sections_parsed = []
    
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
        exercise_sections=exercise_sections_parsed
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
    
    card.updated_at = func.now()
    
    db.commit()
    db.refresh(card)
    
    return ThemeCardResponse(
        id=card.id,
        title=card.title,
        content=card.content,
        card_type=card.card_type,
        order_number=card.order_number,
        theme_id=card.theme_id,
        is_editable=card.is_editable,
        created_at=card.created_at,
        updated_at=card.updated_at
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
        
        # Parse exercise_questions and exercise_sections from JSON
        exercise_questions = []
        if exercise.exercise_questions:
            try:
                import json
                exercise_questions = json.loads(exercise.exercise_questions) if isinstance(exercise.exercise_questions, str) else exercise.exercise_questions
            except:
                exercise_questions = []
        
        exercise_sections = []
        if exercise.exercise_sections:
            try:
                import json
                exercise_sections = json.loads(exercise.exercise_sections) if isinstance(exercise.exercise_sections, str) else exercise.exercise_sections
            except:
                exercise_sections = []
        
        result.append(ExerciseResponse(
            id=exercise.id,
            title=exercise.title,
            parent_title=exercise.parent_title,
            instructions=exercise.instructions,
            sub_questions=sub_questions,
            order_number=exercise.order_number,
            theme_id=exercise.theme_id,
            user_response=user_response.response_text if user_response else None,
            sub_question_responses=sub_responses_dict,
            exercise_instructions=exercise.exercise_instructions,
            exercise_questions=exercise_questions,
            exercise_sections=exercise_sections
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
    # Parse exercise data to handle both legacy and new formats
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
    
    # Validate based on the type of sub_question_index
    if isinstance(response.sub_question_index, int):
        # Legacy format: validate against sub_questions
        if not sub_questions or response.sub_question_index >= len(sub_questions):
            raise HTTPException(status_code=400, detail="Invalid sub-question index")
    elif isinstance(response.sub_question_index, str) and response.sub_question_index.startswith("section_"):
        # New format: validate against exercise_sections
        try:
            parts = response.sub_question_index.split("_")
            if len(parts) >= 4:  # section_X_question_Y
                section_index = int(parts[1])
                question_index = int(parts[3])
                
                if section_index >= len(exercise_sections):
                    raise HTTPException(status_code=400, detail="Invalid section index")
                
                section = exercise_sections[section_index]
                if not section.get('questions') or question_index >= len(section['questions']):
                    raise HTTPException(status_code=400, detail="Invalid question index in section")
            else:
                raise HTTPException(status_code=400, detail="Invalid sub-question index format")
        except (ValueError, IndexError):
            raise HTTPException(status_code=400, detail="Invalid sub-question index format")
    else:
        raise HTTPException(status_code=400, detail="Invalid sub-question index type")
    
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
    
    # Get theme_type from theme_data, default to "theme"
    theme_type_value = getattr(theme_data, 'theme_type', 'theme')
    print(f"[DEBUG] Creating theme with type: {theme_type_value}")
    
    new_theme = Theme(
        title=theme_data.title,
        content=theme_data.content,
        order_number=theme_data.order_number,
        module_id=module_id,
        theme_type=theme_type_value
    )
    
    db.add(new_theme)
    db.commit()
    db.refresh(new_theme)
    
    print(f"[DEBUG] Theme created with ID: {new_theme.id}, theme_type: {new_theme.theme_type}")
    
    return ThemeResponse(
        id=new_theme.id,
        title=new_theme.title,
        content=new_theme.content,
        order_number=new_theme.order_number,
        module_id=new_theme.module_id,
        theme_type=new_theme.theme_type or "theme",
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
    if theme_data.theme_type is not None:
        theme.theme_type = theme_data.theme_type
    
    db.commit()
    db.refresh(theme)
    
    # Count total cards for this theme
    total_cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme.id).count()
    
    return ThemeResponse(
        id=theme.id,
        title=theme.title,
        content=theme.content,
        order_number=theme.order_number,
        module_id=theme.module_id,
        theme_type=theme.theme_type if hasattr(theme, 'theme_type') else "theme",
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
    
    # Convert lists to JSON strings for storage
    import json
    sub_questions_json = json.dumps(exercise_data.sub_questions) if exercise_data.sub_questions else "[]"
    exercise_questions_json = json.dumps(exercise_data.exercise_questions) if exercise_data.exercise_questions else "[]"
    exercise_sections_json = json.dumps(exercise_data.exercise_sections) if exercise_data.exercise_sections else "[]"
    
    new_exercise = Exercise(
        title=exercise_data.title,
        parent_title=exercise_data.parent_title,
        instructions=exercise_data.instructions,
        sub_questions=sub_questions_json,
        order_number=exercise_data.order_number,
        theme_id=theme_id,
        exercise_instructions=exercise_data.exercise_instructions,
        exercise_questions=exercise_questions_json,
        exercise_sections=exercise_sections_json
    )
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    # Parse JSON fields back for response
    sub_questions = json.loads(new_exercise.sub_questions) if new_exercise.sub_questions else []
    exercise_questions = json.loads(new_exercise.exercise_questions) if new_exercise.exercise_questions else []
    exercise_sections = json.loads(new_exercise.exercise_sections) if new_exercise.exercise_sections else []
    
    return ExerciseResponse(
        id=new_exercise.id,
        title=new_exercise.title,
        parent_title=new_exercise.parent_title,
        instructions=new_exercise.instructions,
        sub_questions=sub_questions,
        order_number=new_exercise.order_number,
        theme_id=new_exercise.theme_id,
        user_response=None,
        sub_question_responses={},
        exercise_instructions=new_exercise.exercise_instructions,
        exercise_questions=exercise_questions,
        exercise_sections=exercise_sections
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
    if exercise_data.parent_title is not None:
        exercise.parent_title = exercise_data.parent_title
    if exercise_data.instructions is not None:
        exercise.instructions = exercise_data.instructions
    if exercise_data.sub_questions is not None:
        exercise.sub_questions = json.dumps(exercise_data.sub_questions) if exercise_data.sub_questions else "[]"
    if exercise_data.order_number is not None:
        exercise.order_number = exercise_data.order_number
    
    # Update new exercise fields
    if exercise_data.exercise_instructions is not None:
        exercise.exercise_instructions = exercise_data.exercise_instructions
    if exercise_data.exercise_questions is not None:
        exercise.exercise_questions = json.dumps(exercise_data.exercise_questions) if exercise_data.exercise_questions else "[]"
    if exercise_data.exercise_sections is not None:
        exercise.exercise_sections = json.dumps(exercise_data.exercise_sections) if exercise_data.exercise_sections else "[]"
    
    db.commit()
    db.refresh(exercise)
    
    # Parse JSON fields back for response
    sub_questions = json.loads(exercise.sub_questions) if exercise.sub_questions else []
    exercise_questions = json.loads(exercise.exercise_questions) if exercise.exercise_questions else []
    exercise_sections = json.loads(exercise.exercise_sections) if exercise.exercise_sections else []
    
    return ExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        parent_title=exercise.parent_title,
        instructions=exercise.instructions,
        sub_questions=sub_questions,
        order_number=exercise.order_number,
        theme_id=exercise.theme_id,
        user_response=None,
        sub_question_responses={},
        exercise_instructions=exercise.exercise_instructions,
        exercise_questions=exercise_questions,
        exercise_sections=exercise_sections
    )

@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Delete an exercise"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    try:
        # First, delete all related user responses
        db.query(UserResponseDB).filter(UserResponseDB.exercise_id == exercise_id).delete()
        
        # Delete all related sub-question responses
        db.query(UserSubQuestionResponseDB).filter(UserSubQuestionResponseDB.exercise_id == exercise_id).delete()
        
        # Now delete the exercise
        db.delete(exercise)
        db.commit()
        
        return {"message": "Exercise deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting exercise: {str(e)}")
