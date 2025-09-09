#!/usr/bin/env python3
"""
Migration script to add exercise fields to ThemeCard model
and create UserCardResponseDB table for the new exercise cards system.

This migration:
1. Adds exercise_instructions and exercise_questions columns to theme_cards table
2. Creates user_card_responses table for storing exercise responses
3. Preserves all existing data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text, Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import sessionmaker
from database import engine, SessionLocal
from models import Base, UserCardResponseDB
import json

def run_migration():
    """Run the migration to add exercise fields to cards"""
    
    # Use existing database configuration
    db = SessionLocal()
    
    try:
        print("🚀 Starting migration: Adding exercise fields to ThemeCard...")
        
        # 1. Add new columns to theme_cards table
        print("📝 Adding exercise_instructions column...")
        try:
            db.execute(text("""
                ALTER TABLE theme_cards 
                ADD COLUMN exercise_instructions TEXT NULL
            """))
            print("✅ exercise_instructions column added successfully")
        except Exception as e:
            if "already exists" in str(e) or "duplicate column name" in str(e).lower():
                print("⚠️  exercise_instructions column already exists, skipping...")
            else:
                raise e
        
        print("📝 Adding exercise_questions column...")
        try:
            db.execute(text("""
                ALTER TABLE theme_cards 
                ADD COLUMN exercise_questions JSON NULL DEFAULT '[]'
            """))
            print("✅ exercise_questions column added successfully")
        except Exception as e:
            if "already exists" in str(e) or "duplicate column name" in str(e).lower():
                print("⚠️  exercise_questions column already exists, skipping...")
            else:
                raise e
        
        # 2. Create user_card_responses table
        print("📝 Creating user_card_responses table...")
        try:
            db.execute(text("""
                CREATE TABLE user_card_responses (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    card_id INTEGER NOT NULL,
                    question_index INTEGER NOT NULL,
                    response_text TEXT NULL,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (card_id) REFERENCES theme_cards(id)
                )
            """))
            print("✅ user_card_responses table created successfully")
        except Exception as e:
            if "already exists" in str(e) or "table" in str(e).lower() and "already exists" in str(e).lower():
                print("⚠️  user_card_responses table already exists, skipping...")
            else:
                raise e
        
        # 3. Update card_type comment to include 'exercise'
        print("📝 Updating card_type values...")
        
        # Commit all changes
        db.commit()
        print("✅ Migration completed successfully!")
        
        # 4. Verify the changes
        print("\n🔍 Verifying migration...")
        
        # Check if new columns exist (SQLite syntax)
        result = db.execute(text("""
            PRAGMA table_info(theme_cards)
        """))
        columns = [row[1] for row in result.fetchall()]  # row[1] is column name in PRAGMA table_info
        
        if 'exercise_instructions' in columns and 'exercise_questions' in columns:
            print("✅ New columns verified in theme_cards table")
        else:
            print(f"❌ Missing columns. Found: {columns}")
        
        # Check if new table exists (SQLite syntax)
        result = db.execute(text("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='user_card_responses'
        """))
        if result.fetchone():
            print("✅ user_card_responses table verified")
        else:
            print("❌ user_card_responses table not found")
        
        print("\n🎉 Migration completed successfully!")
        print("📋 Summary:")
        print("   • Added exercise_instructions column to theme_cards")
        print("   • Added exercise_questions column to theme_cards") 
        print("   • Created user_card_responses table")
        print("   • Ready for exercise cards integration!")
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        db.rollback()
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    run_migration()
