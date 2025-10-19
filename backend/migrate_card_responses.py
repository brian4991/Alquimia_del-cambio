#!/usr/bin/env python3
"""
Migration script to create card_responses table
"""
from database import engine, create_tables
from models import CardResponse
from sqlalchemy import text

def migrate_card_responses():
    """Create the card_responses table"""
    
    print("🔄 Starting card_responses migration...")
    
    try:
        # Create all tables (will only create missing ones)
        create_tables()
        
        # Verify the table was created
        with engine.connect() as conn:
            # Check if this is PostgreSQL or SQLite
            db_dialect = engine.dialect.name
            
            if db_dialect == 'postgresql':
                result = conn.execute(text("""
                    SELECT table_name FROM information_schema.tables 
                    WHERE table_name='card_responses'
                """))
            else:  # SQLite
                result = conn.execute(text("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='card_responses'
                """))
            
            if result.fetchone():
                print("✅ Table 'card_responses' created successfully!")
                
                # Show table structure
                if db_dialect == 'postgresql':
                    result = conn.execute(text("""
                        SELECT column_name, data_type 
                        FROM information_schema.columns 
                        WHERE table_name = 'card_responses'
                        ORDER BY ordinal_position
                    """))
                    columns = result.fetchall()
                    print("\n📋 Table structure:")
                    for col in columns:
                        print(f"   - {col[0]} ({col[1]})")
                else:  # SQLite
                    result = conn.execute(text("PRAGMA table_info(card_responses)"))
                    columns = result.fetchall()
                    print("\n📋 Table structure:")
                    for col in columns:
                        print(f"   - {col[1]} ({col[2]})")
                    
            else:
                print("❌ Failed to create table 'card_responses'")
                return False
                
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    print("\n🎯 Card responses system is ready!")
    print("   - New table: card_responses")
    print("   - Stores user responses for card-based exercises")
    
    return True

if __name__ == "__main__":
    success = migrate_card_responses()
    exit(0 if success else 1)

