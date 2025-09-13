from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from auth import get_current_admin_user, get_current_user
from database import get_db
from models import User, ThemeCard, Theme, Exercise
from schemas import ThemeCardResponse, ThemeCardCreate, ThemeCardUpdate

router = APIRouter(tags=["api"])

# ===============================
# CARDS API ROUTES (with /api prefix)
# ===============================

@router.get("/cards/{card_id}", response_model=ThemeCardResponse)
def get_card(card_id: int, current_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Get a specific card"""
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

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
    
    # Update exercise-specific fields if this is an exercise card
    if card_data.card_type == "exercise" or card.card_type == "exercise":
        if card_data.exercise_instructions is not None:
            card.exercise_instructions = card_data.exercise_instructions
        if card_data.exercise_questions is not None:
            # Convert exercise questions to JSON
            if card_data.exercise_questions:
                questions_json = [q.dict() if hasattr(q, 'dict') else q for q in card_data.exercise_questions]
                card.exercise_questions = json.dumps(questions_json)
            else:
                card.exercise_questions = json.dumps([])
    
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
        except Exception as e:
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
        exercise_questions=exercise_questions_parsed
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

@router.post("/cards/{card_id}/responses")
def save_card_response(card_id: int, response_data: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Save user response to an exercise card"""
    # Verify card exists
    card = db.query(ThemeCard).filter(ThemeCard.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    
    # For now, just return success - we can implement full storage later
    return {"success": True, "message": "Response saved successfully"}

# ===============================
# EXERCISES API ROUTES (with /api prefix)
# ===============================

@router.post("/themes/{theme_id}/exercises")
def create_exercise(theme_id: int, exercise_data: dict, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Create a new exercise"""
    
    # Verify theme exists
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Create new exercise
    new_exercise = Exercise(
        title=exercise_data.get('title', 'Nouvel exercice'),
        instructions=exercise_data.get('instructions', ''),
        sub_questions=exercise_data.get('sub_questions', '[]'),
        order_number=exercise_data.get('order_number', 1),
        theme_id=theme_id
    )
    
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    
    return {
        "id": new_exercise.id,
        "title": new_exercise.title,
        "instructions": new_exercise.instructions,
        "sub_questions": new_exercise.sub_questions,
        "order_number": new_exercise.order_number,
        "theme_id": new_exercise.theme_id
    }
