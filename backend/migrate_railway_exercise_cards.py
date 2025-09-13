#!/usr/bin/env python3
"""
Migration script for Railway deployment - Add exercise fields to ThemeCard model
This migration adds exercise_instructions and exercise_questions columns to theme_cards table
and creates user_card_responses table for Railway production database.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import json

def get_railway_connection():
    """Get Railway database connection"""
    # Railway provides DATABASE_URL environment variable
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not found")
        print("This script should be run on Railway deployment")
        return None
    
    # Convert postgres:// to postgresql:// if needed (Railway compatibility)
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal, engine

def run_migration():
    """Run the migration to add exercise fields to cards"""
    
    connection_info = get_railway_connection()
    if not connection_info:
        return False
    
    SessionLocal, engine = connection_info
    db = SessionLocal()
    
    try:
        print("🚀 Starting Railway migration: Adding exercise fields to ThemeCard...")
        
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
                print(f"❌ Error adding exercise_instructions: {e}")
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
                print(f"❌ Error adding exercise_questions: {e}")
                raise e
        
        # 2. Create user_card_responses table
        print("📝 Creating user_card_responses table...")
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
            print("✅ user_card_responses table created successfully")
        except Exception as e:
            if "already exists" in str(e).lower():
                print("⚠️  user_card_responses table already exists, skipping...")
            else:
                print(f"❌ Error creating user_card_responses table: {e}")
                raise e
        
        # 3. Commit all changes
        db.commit()
        print("✅ Migration completed successfully!")
        
        # 4. Verify the changes
        print("\n🔍 Verifying migration...")
        
        # Check if new columns exist
        result = db.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'theme_cards' 
            AND column_name IN ('exercise_instructions', 'exercise_questions')
        """))
        columns = [row[0] for row in result.fetchall()]
        
        if 'exercise_instructions' in columns and 'exercise_questions' in columns:
            print("✅ New columns verified in theme_cards table")
        else:
            print(f"⚠️ Missing columns. Found: {columns}")
        
        # Check if user_card_responses table exists
        result = db.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_name = 'user_card_responses'
        """))
        tables = [row[0] for row in result.fetchall()]
        
        if 'user_card_responses' in tables:
            print("✅ user_card_responses table verified")
        else:
            print("⚠️ user_card_responses table not found")
        
        print("\n🎉 Railway migration completed successfully!")
        print("📋 Summary:")
        print("   • Added exercise_instructions column to theme_cards")
        print("   • Added exercise_questions column to theme_cards")
        print("   • Created user_card_responses table")
        print("   • Ready for exercise cards integration!")
        
        return True
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        db.rollback()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    print("🚂 Railway Exercise Cards Migration")
    print("=" * 50)
    
    success = run_migration()
    
    if success:
        print("\n✅ Migration completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Migration failed!")
        sys.exit(1)
