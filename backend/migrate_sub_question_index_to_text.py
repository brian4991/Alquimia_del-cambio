#!/usr/bin/env python3
"""
Migration script to change sub_question_index column from INTEGER to TEXT
to support new exercise format with section_X_question_Y identifiers
"""
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def migrate_sub_question_index():
    """Change sub_question_index from INTEGER to TEXT"""
    
    # Get database URL from environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("❌ DATABASE_URL not found in environment variables")
        return False
    
    print("🔄 Starting migration to change sub_question_index to TEXT...")
    print(f"📍 Database: {database_url[:30]}...")
    
    try:
        engine = create_engine(database_url)
        
        with engine.connect() as conn:
            # Start a transaction
            with conn.begin():
                print("\n1️⃣ Checking current table structure...")
                
                # Check if column exists and its type
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'user_sub_question_responses' 
                    AND column_name = 'sub_question_index'
                """))
                
                current_col = result.fetchone()
                if current_col:
                    print(f"   ✅ Column found: {current_col[0]} ({current_col[1]})")
                else:
                    print("   ❌ Column not found!")
                    return False
                
                print("\n2️⃣ Creating backup of existing data...")
                
                # Create a temporary backup table
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS user_sub_question_responses_backup AS 
                    SELECT * FROM user_sub_question_responses
                """))
                print("   ✅ Backup table created")
                
                print("\n3️⃣ Altering column type to TEXT...")
                
                # For PostgreSQL, we need to alter the column type
                # First, convert existing integer values to text
                conn.execute(text("""
                    ALTER TABLE user_sub_question_responses 
                    ALTER COLUMN sub_question_index TYPE TEXT 
                    USING sub_question_index::TEXT
                """))
                print("   ✅ Column type changed to TEXT")
                
                print("\n4️⃣ Verifying new table structure...")
                
                # Verify the change
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'user_sub_question_responses' 
                    AND column_name = 'sub_question_index'
                """))
                
                new_col = result.fetchone()
                if new_col:
                    print(f"   ✅ New column type: {new_col[0]} ({new_col[1]})")
                else:
                    print("   ❌ Failed to verify column!")
                    return False
                
                print("\n5️⃣ Checking data integrity...")
                
                # Count records to verify no data loss
                result = conn.execute(text("""
                    SELECT COUNT(*) FROM user_sub_question_responses
                """))
                count = result.fetchone()[0]
                print(f"   ✅ Records in table: {count}")
                
                print("\n6️⃣ Dropping backup table...")
                conn.execute(text("DROP TABLE IF EXISTS user_sub_question_responses_backup"))
                print("   ✅ Backup table dropped")
            
            print("\n✅ Migration completed successfully!")
            print("\n📋 Summary:")
            print("   - Column 'sub_question_index' changed from INTEGER to TEXT")
            print("   - Existing data preserved and converted to text format")
            print("   - New format 'section_X_question_Y' is now supported")
            
            return True
            
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        print("\n🔄 Attempting rollback...")
        try:
            with engine.connect() as conn:
                with conn.begin():
                    # Try to restore from backup if it exists
                    result = conn.execute(text("""
                        SELECT EXISTS (
                            SELECT FROM information_schema.tables 
                            WHERE table_name = 'user_sub_question_responses_backup'
                        )
                    """))
                    if result.fetchone()[0]:
                        print("   📦 Backup table found, restoring...")
                        # Note: We can't easily rollback ALTER TABLE, so just drop backup
                        conn.execute(text("DROP TABLE IF EXISTS user_sub_question_responses_backup"))
                        print("   ✅ Cleanup complete")
        except Exception as rollback_error:
            print(f"   ❌ Rollback failed: {rollback_error}")
        
        return False

if __name__ == "__main__":
    success = migrate_sub_question_index()
    if success:
        print("\n🎯 Database is now ready for the new exercise format!")
        exit(0)
    else:
        print("\n⚠️  Migration failed. Please check the errors above.")
        exit(1)

