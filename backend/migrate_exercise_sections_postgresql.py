#!/usr/bin/env python3
"""
Migration script to add exercise sections and questions fields to exercises table (PostgreSQL)
"""

import os
import sys
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_database_url():
    """Get database URL from environment variables"""
    # Try to get from Railway environment variables
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        # Fallback to local PostgreSQL if available
        database_url = os.getenv('POSTGRES_URL', 'postgresql://localhost:5432/alquimia')
    return database_url

def migrate_database():
    """Add new fields to exercises table"""
    
    database_url = get_database_url()
    if not database_url:
        print("❌ No database URL found. Please set DATABASE_URL environment variable.")
        return False
    
    print(f"Connecting to database: {database_url[:50]}...")
    
    try:
        # Create engine and session
        engine = create_engine(database_url)
        inspector = inspect(engine)
        
        # Check if exercises table exists
        if 'exercises' not in inspector.get_table_names():
            print("❌ Exercises table not found!")
            return False
        
        # Get existing columns
        columns = [col['name'] for col in inspector.get_columns('exercises')]
        print(f"Current columns: {', '.join(columns)}")
        
        with engine.connect() as conn:
            print("Starting migration: Adding exercise sections and questions fields...")
            
            # Add exercise_instructions if it doesn't exist
            if 'exercise_instructions' not in columns:
                print("Adding exercise_instructions column...")
                conn.execute(text('ALTER TABLE exercises ADD COLUMN exercise_instructions TEXT'))
                conn.commit()
            else:
                print("exercise_instructions column already exists")
                
            # Add exercise_questions if it doesn't exist
            if 'exercise_questions' not in columns:
                print("Adding exercise_questions column...")
                conn.execute(text('ALTER TABLE exercises ADD COLUMN exercise_questions TEXT DEFAULT \'[]\''))
                conn.commit()
            else:
                print("exercise_questions column already exists")
                
            # Add exercise_sections if it doesn't exist
            if 'exercise_sections' not in columns:
                print("Adding exercise_sections column...")
                conn.execute(text('ALTER TABLE exercises ADD COLUMN exercise_sections TEXT DEFAULT \'[]\''))
                conn.commit()
            else:
                print("exercise_sections column already exists")
                
            # Add created_at if it doesn't exist
            if 'created_at' not in columns:
                print("Adding created_at column...")
                conn.execute(text('ALTER TABLE exercises ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'))
                conn.commit()
            else:
                print("created_at column already exists")
                
            # Add updated_at if it doesn't exist
            if 'updated_at' not in columns:
                print("Adding updated_at column...")
                conn.execute(text('ALTER TABLE exercises ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'))
                conn.commit()
            else:
                print("updated_at column already exists")
            
            print("Migration completed successfully!")
            
            # Verify the changes
            print("\nVerifying table structure:")
            inspector = inspect(engine)
            columns_info = inspector.get_columns('exercises')
            for col in columns_info:
                print(f"  {col['name']} ({col['type']})")
                
    except Exception as e:
        print(f"Error during migration: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Exercise Sections Migration Script (PostgreSQL)")
    print("===============================================")
    
    if migrate_database():
        print("\n✅ Migration completed successfully!")
    else:
        print("\n❌ Migration failed!")
        sys.exit(1)
