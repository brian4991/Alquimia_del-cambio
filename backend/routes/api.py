from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from auth import get_current_admin_user
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

@router.post("/themes/{theme_id}/cards", response_model=ThemeCardResponse)
def create_card(theme_id: int, card_data: ThemeCardCreate, current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
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
