#!/usr/bin/env python3
"""
Migration script to update exercises table:
- Remove 'question' column
- Add 'sub_questions' JSON column
"""

import sqlite3
import json
from pathlib import Path

def migrate_exercises():
    """Update exercises table structure"""
    db_path = Path(__file__).parent / "app.db"
    
    if not db_path.exists():
        print("Database not found. Creating new structure...")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if old structure exists
        cursor.execute("PRAGMA table_info(exercises)")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        
        if 'question' not in column_names:
            print("Migration already applied or 'question' column doesn't exist")
            return
        
        print("Starting migration...")
        
        # Step 1: Create temporary table with new structure
        cursor.execute("""
            CREATE TABLE exercises_new (
                id INTEGER PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                instructions TEXT,
                sub_questions TEXT DEFAULT '[]',
                order_number INTEGER NOT NULL,
                theme_id INTEGER NOT NULL,
                FOREIGN KEY (theme_id) REFERENCES themes (id)
            )
        """)
        
        # Step 2: Migrate data - convert 'question' to first sub_question
        cursor.execute("SELECT id, title, question, instructions, order_number, theme_id FROM exercises")
        exercises = cursor.fetchall()
        
        for exercise in exercises:
            id_, title, question, instructions, order_number, theme_id = exercise
            
            # Convert old question to first sub-question
            sub_questions = [question] if question else []
            sub_questions_json = json.dumps(sub_questions)
            
            cursor.execute("""
                INSERT INTO exercises_new (id, title, instructions, sub_questions, order_number, theme_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id_, title, instructions, sub_questions_json, order_number, theme_id))
        
        # Step 3: Drop old table and rename new one
        cursor.execute("DROP TABLE exercises")
        cursor.execute("ALTER TABLE exercises_new RENAME TO exercises")
        
        # Step 4: Recreate indexes if any existed
        cursor.execute("CREATE INDEX IF NOT EXISTS ix_exercises_id ON exercises (id)")
        
        conn.commit()
        print(f"✅ Migration completed successfully! Migrated {len(exercises)} exercises.")
        
        # Verify migration
        cursor.execute("SELECT id, title, sub_questions FROM exercises LIMIT 3")
        sample = cursor.fetchall()
        print("\n📋 Sample data after migration:")
        for row in sample:
            print(f"  ID {row[0]}: {row[1]} -> {row[2]}")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Migration failed: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_exercises()