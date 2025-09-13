from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from auth import get_current_admin_user
from models import User

router = APIRouter()

@router.post("/admin/migrate-exercise-fields")
def migrate_exercise_fields(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Temporary endpoint to migrate exercise fields"""
    results = []
    
    # Add exercise_instructions column
    try:
        db.execute(text("ALTER TABLE theme_cards ADD COLUMN exercise_instructions TEXT NULL"))
        results.append("✅ exercise_instructions column added")
    except Exception as e:
        if "already exists" in str(e) or "duplicate column" in str(e).lower():
            results.append("⚠️ exercise_instructions column already exists")
        else:
            results.append(f"❌ Error adding exercise_instructions: {e}")
    
    # Add exercise_questions column
    try:
        db.execute(text("ALTER TABLE theme_cards ADD COLUMN exercise_questions JSON NULL DEFAULT '[]'"))
        results.append("✅ exercise_questions column added")
    except Exception as e:
        if "already exists" in str(e) or "duplicate column" in str(e).lower():
            results.append("⚠️ exercise_questions column already exists")
        else:
            results.append(f"❌ Error adding exercise_questions: {e}")
    
    # Create user_card_responses table
    try:
        db.execute(text("""
            CREATE TABLE user_card_responses (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                card_id INTEGER NOT NULL,
                question_index INTEGER NOT NULL,
                response_text TEXT NULL,
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (card_id) REFERENCES theme_cards(id) ON DELETE CASCADE
            )
        """))
        results.append("✅ user_card_responses table created")
    except Exception as e:
        if "already exists" in str(e).lower():
            results.append("⚠️ user_card_responses table already exists")
        else:
            results.append(f"❌ Error creating user_card_responses: {e}")
    
    try:
        db.commit()
        return {"success": True, "message": "Migration completed", "details": results}
    except Exception as e:
        db.rollback()
        return {"success": False, "error": str(e), "details": results}
