#!/usr/bin/env python3
"""
Temporary migration endpoint to fix database schema
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/admin/migrate-database")
def migrate_database_schema(db: Session = Depends(get_db)):
    """
    Temporary endpoint to migrate database schema
    REMOVE THIS AFTER MIGRATION IS COMPLETE
    """
    try:
        migrations = [
            # Fix exercises table - only updated_at column
            "ALTER TABLE exercises DROP COLUMN IF EXISTS updated_at",
            "ALTER TABLE exercises ADD COLUMN updated_at date"
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
            "message": "Migration executed successfully!"
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Migration failed: {str(e)}")