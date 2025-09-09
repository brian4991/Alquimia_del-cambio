#!/usr/bin/env python3
"""
Migration script for Railway PostgreSQL to add exercise columns
This adds the missing columns to make Railway compatible with local development
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def migrate_railway_database():
    """Add exercise columns to Railway PostgreSQL database"""
    
    # Get Railway database URL
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        print("❌ DATABASE_URL not found. This script is for Railway deployment only.")
        print("💡 For local development, use: python migrate_cards_exercise_fields.py")
        return False
    
    print("🚀 Railway PostgreSQL Migration - Adding Exercise Columns")
    print("=" * 60)
    print(f"🔗 Database: {database_url[:50]}...")
    
    try:
        # Create engine and session
        engine = create_engine(database_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        print("✅ Connected to Railway PostgreSQL")
        
        # Check current table structure
        print("\n🔍 Checking current table structure...")
        result = db.execute(text("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'theme_cards' 
            ORDER BY ordinal_position
        """))
        
        existing_columns = {row[0]: row[1] for row in result.fetchall()}
        print(f"📋 Found {len(existing_columns)} existing columns")
        
        # Check if exercise columns already exist
        exercise_columns = ['exercise_instructions', 'exercise_questions']
        missing_columns = [col for col in exercise_columns if col not in existing_columns]
        
        if not missing_columns:
            print("✅ All exercise columns already exist! Migration not needed.")
            return True
        
        print(f"📝 Missing columns to add: {missing_columns}")
        
        # Add missing columns
        if 'exercise_instructions' in missing_columns:
            print("➕ Adding exercise_instructions column...")
            db.execute(text("""
                ALTER TABLE theme_cards 
                ADD COLUMN exercise_instructions TEXT NULL
            """))
            print("✅ exercise_instructions column added")
        
        if 'exercise_questions' in missing_columns:
            print("➕ Adding exercise_questions column...")
            db.execute(text("""
                ALTER TABLE theme_cards 
                ADD COLUMN exercise_questions JSON NULL DEFAULT '[]'
            """))
            print("✅ exercise_questions column added")
        
        # Create user_card_responses table if it doesn't exist
        print("📝 Creating user_card_responses table...")
        try:
            db.execute(text("""
                CREATE TABLE IF NOT EXISTS user_card_responses (
                    id SERIAL PRIMARY KEY,
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
            print("✅ user_card_responses table created/verified")
        except Exception as e:
            print(f"⚠️ user_card_responses table creation: {e}")
        
        # Commit all changes
        db.commit()
        print("✅ All changes committed successfully")
        
        # Verify the migration
        print("\n🔍 Verifying migration...")
        result = db.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'theme_cards' 
            AND column_name IN ('exercise_instructions', 'exercise_questions')
        """))
        
        new_columns = [row[0] for row in result.fetchall()]
        
        if len(new_columns) == 2:
            print("✅ Migration verification successful")
            print("🎉 Railway PostgreSQL now supports exercise cards!")
            print("\n📋 Summary:")
            print("   ✅ exercise_instructions column added")
            print("   ✅ exercise_questions column added") 
            print("   ✅ user_card_responses table created")
            print("   🚀 Railway is now compatible with local development")
            return True
        else:
            print(f"❌ Verification failed. Found columns: {new_columns}")
            return False
            
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        if 'db' in locals():
            db.rollback()
        return False
    finally:
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    success = migrate_railway_database()
    if success:
        print("\n🎯 Next steps:")
        print("   1. Redeploy your Railway app")
        print("   2. Exercise cards will work on production!")
        print("   3. Remove temporary compatibility code if desired")
    else:
        print("\n❌ Migration failed. Check logs above.")
    
    sys.exit(0 if success else 1)
