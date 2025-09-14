#!/usr/bin/env python3
"""
Migration script to add exercise sections and questions fields to exercises table
"""

import sqlite3
import sys
import os

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def migrate_database():
    """Add new fields to exercises table"""
    
    # Connect to the database
    db_path = 'app.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        print("Starting migration: Adding exercise sections and questions fields...")
        
        # Check if columns already exist
        cursor.execute("PRAGMA table_info(exercises)")
        columns = [column[1] for column in cursor.fetchall()]
        
        # Add exercise_instructions if it doesn't exist
        if 'exercise_instructions' not in columns:
            print("Adding exercise_instructions column...")
            cursor.execute('ALTER TABLE exercises ADD COLUMN exercise_instructions TEXT')
        else:
            print("exercise_instructions column already exists")
            
        # Add exercise_questions if it doesn't exist
        if 'exercise_questions' not in columns:
            print("Adding exercise_questions column...")
            cursor.execute('ALTER TABLE exercises ADD COLUMN exercise_questions TEXT')
            cursor.execute('UPDATE exercises SET exercise_questions = "[]" WHERE exercise_questions IS NULL')
        else:
            print("exercise_questions column already exists")
            
        # Add exercise_sections if it doesn't exist
        if 'exercise_sections' not in columns:
            print("Adding exercise_sections column...")
            cursor.execute('ALTER TABLE exercises ADD COLUMN exercise_sections TEXT')
            cursor.execute('UPDATE exercises SET exercise_sections = "[]" WHERE exercise_sections IS NULL')
        else:
            print("exercise_sections column already exists")
            
        # Add created_at if it doesn't exist
        if 'created_at' not in columns:
            print("Adding created_at column...")
            cursor.execute('ALTER TABLE exercises ADD COLUMN created_at DATETIME')
            cursor.execute('UPDATE exercises SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL')
        else:
            print("created_at column already exists")
            
        # Add updated_at if it doesn't exist
        if 'updated_at' not in columns:
            print("Adding updated_at column...")
            cursor.execute('ALTER TABLE exercises ADD COLUMN updated_at DATETIME')
            cursor.execute('UPDATE exercises SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL')
        else:
            print("updated_at column already exists")
        
        # Commit the changes
        conn.commit()
        print("Migration completed successfully!")
        
        # Verify the changes
        print("\nVerifying table structure:")
        cursor.execute("PRAGMA table_info(exercises)")
        columns_info = cursor.fetchall()
        for col in columns_info:
            print(f"  {col[1]} ({col[2]})")
            
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
    
    return True

if __name__ == "__main__":
    print("Exercise Sections Migration Script")
    print("==================================")
    
    if migrate_database():
        print("\n✅ Migration completed successfully!")
    else:
        print("\n❌ Migration failed!")
        sys.exit(1)
