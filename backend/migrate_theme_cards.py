#!/usr/bin/env python3
"""
Migration endpoint for theme_cards table
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/admin/migrate-theme-cards")
def migrate_theme_cards_schema(db: Session = Depends(get_db)):
    """
    Add missing columns to theme_cards table
    """
    try:
        migrations = [
            # Add missing columns to theme_cards
            "ALTER TABLE theme_cards ADD COLUMN IF NOT EXISTS exercise_instructions text",
            "ALTER TABLE theme_cards ADD COLUMN IF NOT EXISTS exercise_questions text DEFAULT '[]'",
            "ALTER TABLE theme_cards ADD COLUMN IF NOT EXISTS exercise_sections text DEFAULT '[]'",
            "ALTER TABLE theme_cards ADD COLUMN IF NOT EXISTS created_at date",
            "ALTER TABLE theme_cards ADD COLUMN IF NOT EXISTS updated_at date"
        ]
        
        results = []
        for migration in migrations:
            try:
                db.execute(text(migration))
                results.append(f"✅ {migration}")
            except Exception as e:
                results.append(f"❌ {migration} - Error: {str(e)}")
        
        db.commit()
        
        return {
            "status": "completed",
            "results": results,
            "message": "Theme cards migration executed successfully!"
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Migration failed: {str(e)}")
