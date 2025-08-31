#!/usr/bin/env python3
"""
Migration script to add sub-question responses table
"""
from database import engine, create_tables
from models import UserSubQuestionResponseDB
from sqlalchemy import text

def migrate_sub_questions():
    """Create the user_sub_question_responses table"""
    
    print("🔄 Starting sub-question responses migration...")
    
    try:
        # Create all tables (will only create missing ones)
        create_tables()
        
        # Verify the table was created
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name='user_sub_question_responses'
            """))
            
            if result.fetchone():
                print("✅ Table 'user_sub_question_responses' created successfully!")
                
                # Show table structure
                result = conn.execute(text("PRAGMA table_info(user_sub_question_responses)"))
                columns = result.fetchall()
                print("\n📋 Table structure:")
                for col in columns:
                    print(f"   - {col[1]} ({col[2]})")
                    
            else:
                print("❌ Failed to create table 'user_sub_question_responses'")
                return False
                
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    print("\n🎯 Sub-question responses system is ready!")
    print("   - New table: user_sub_question_responses")
    print("   - New endpoint: POST /submit-sub-question-response")
    print("   - Updated schema: SubQuestionResponseRequest")
    
    return True

if __name__ == "__main__":
    migrate_sub_questions()
