from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import List

from auth import get_current_user
from database import get_db
from models import User, Module, Theme, Exercise, UserProgress, UserResponseDB, ThemeCard
from schemas import (
    ModuleResponse, ThemeResponse, ExerciseResponse, ExerciseResponseRequest, 
    ThemeCardResponse, ThemeCardCreate, ThemeCardUpdate,
    ModuleCreate, ModuleUpdate, ThemeCreate, ThemeUpdate, 
    ExerciseCreate, ExerciseUpdate
)

router = APIRouter(tags=["modules"])

@router.get("/modules", response_model=List[ModuleResponse])
def get_modules(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    result = []
    for module in modules:
        # Check if module is completed
        module_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.module_id == module.id,
            UserProgress.completed == True
        ).first()
        
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
            is_completed=module_progress is not None
        ))
    
    return result

@router.get("/modules/{module_id}/themes", response_model=List[ThemeResponse])
def get_module_themes(module_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    themes = db.query(Theme).filter(Theme.module_id == module_id).order_by(Theme.order_number).all()
    
    result = []
    for i, theme in enumerate(themes):
        # Check if theme is completed
        theme_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.theme_id == theme.id,
            UserProgress.completed == True
        ).first()
        
        # Theme is unlocked if it's the first one or if the previous theme is completed
        is_unlocked = i == 0  # First theme is always unlocked
        if i > 0:
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
            is_completed=theme_progress is not None,
            is_unlocked=is_unlocked,
            total_cards=total_cards
        ))
    
    return result

# ===============================
# THEME CARDS CRUD ROUTES
# ===============================

@router.get("/themes/{theme_id}/cards", response_model=List[ThemeCardResponse])
def get_theme_cards(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get all cards for a theme"""
    cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme_id).order_by(ThemeCard.order_number).all()
    return cards

@router.get("/cards/{card_id}", response_model=ThemeCardResponse)
def get_card(card_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get a specific card"""
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@router.post("/themes/{theme_id}/cards", response_model=ThemeCardResponse)
def create_card(theme_id: int, card_data: ThemeCardCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Create a new card"""
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
    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    
    return new_card

@router.put("/cards/{card_id}", response_model=ThemeCardResponse)
def update_card(card_id: int, card_data: ThemeCardUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Update a card"""
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
    
    return card

@router.delete("/cards/{card_id}")
def delete_card(card_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
        
        result.append(ExerciseResponse(
            id=exercise.id,
            title=exercise.title,
            question=exercise.question,
            instructions=exercise.instructions,
            order_number=exercise.order_number,
            theme_id=exercise.theme_id,
            user_response=user_response.response_text if user_response else None
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

@router.post("/complete-theme/{theme_id}")
def complete_theme(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Get the theme to access module_id
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Check if all exercises in the theme have responses
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).all()
    
    for exercise in exercises:
        response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        if not response:
            raise HTTPException(status_code=400, detail="All exercises must be completed before marking theme as complete")
    
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

# ===============================
# MODULES CRUD ROUTES
# ===============================

@router.post("/modules", response_model=ModuleResponse)
def create_module(module_data: ModuleCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
def update_module(module_id: int, module_data: ModuleUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
def delete_module(module_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
def create_theme(module_id: int, theme_data: ThemeCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
def update_theme(theme_id: int, theme_data: ThemeUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
    
    # Count total cards for this theme
    total_cards = db.query(ThemeCard).filter(ThemeCard.theme_id == theme.id).count()
    
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
def delete_theme(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
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
def create_exercise(theme_id: int, exercise_data: ExerciseCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Create a new exercise"""
    # Verify theme exists
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    new_exercise = Exercise(
        title=exercise_data.title,
        question=exercise_data.question,
        instructions=exercise_data.instructions,
        order_number=exercise_data.order_number,
        theme_id=theme_id
    )
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    return ExerciseResponse(
        id=new_exercise.id,
        title=new_exercise.title,
        question=new_exercise.question,
        instructions=new_exercise.instructions,
        order_number=new_exercise.order_number,
        theme_id=new_exercise.theme_id,
        user_response=None
    )

@router.put("/exercises/{exercise_id}", response_model=ExerciseResponse)
def update_exercise(exercise_id: int, exercise_data: ExerciseUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Update an exercise"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    # Update fields if provided
    if exercise_data.title is not None:
        exercise.title = exercise_data.title
    if exercise_data.question is not None:
        exercise.question = exercise_data.question
    if exercise_data.instructions is not None:
        exercise.instructions = exercise_data.instructions
    if exercise_data.order_number is not None:
        exercise.order_number = exercise_data.order_number
    
    db.commit()
    db.refresh(exercise)
    
    return ExerciseResponse(
        id=exercise.id,
        title=exercise.title,
        question=exercise.question,
        instructions=exercise.instructions,
        order_number=exercise.order_number,
        theme_id=exercise.theme_id,
        user_response=None
    )

@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Delete an exercise"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    db.delete(exercise)
    db.commit()
    
    return {"message": "Exercise deleted successfully"} 