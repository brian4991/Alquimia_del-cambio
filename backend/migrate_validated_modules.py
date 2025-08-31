#!/usr/bin/env python3
"""
Migration script to add validated_modules column to users table
"""
from database import engine
from sqlalchemy import text

def migrate_validated_modules():
    """Add validated_modules column to users table"""
    
    print("🔄 Starting validated_modules migration...")
    
    try:
        with engine.connect() as conn:
            # Check if column already exists
            result = conn.execute(text("PRAGMA table_info(users)"))
            columns = [row[1] for row in result.fetchall()]
            
            if 'validated_modules' not in columns:
                # Add the column
                conn.execute(text("""
                    ALTER TABLE users 
                    ADD COLUMN validated_modules TEXT DEFAULT '[]'
                """))
                conn.commit()
                print("✅ Column 'validated_modules' added to users table!")
            else:
                print("✅ Column 'validated_modules' already exists!")
                
            # Show updated table structure
            result = conn.execute(text("PRAGMA table_info(users)"))
            columns = result.fetchall()
            print("\n📋 Updated users table structure:")
            for col in columns:
                print(f"   - {col[1]} ({col[2]})")
                    
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    print("\n🎯 User validation system is ready!")
    print("   - New column: validated_modules (JSON)")
    print("   - New endpoints: POST/DELETE /auth/admin/users/{user_id}/validate-module/{module_id}")
    print("   - Module access control implemented")
    
    return True

if __name__ == "__main__":
    migrate_validated_modules()
