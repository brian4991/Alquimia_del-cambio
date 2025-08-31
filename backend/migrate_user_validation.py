#!/usr/bin/env python3
"""
Migration script to add is_validated column to users table
"""

import sqlite3
import sys
import os

def migrate_database():
    """Add is_validated column to users table"""
    
    # Database path
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if column already exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'is_validated' in columns:
            print("Column 'is_validated' already exists in users table")
            return True
        
        # Add the new column
        print("Adding 'is_validated' column to users table...")
        cursor.execute("ALTER TABLE users ADD COLUMN is_validated BOOLEAN DEFAULT FALSE")
        
        # Commit changes
        conn.commit()
        print("Migration completed successfully!")
        
        # Verify the column was added
        cursor.execute("PRAGMA table_info(users)")
        columns_after = [column[1] for column in cursor.fetchall()]
        
        if 'is_validated' in columns_after:
            print("✅ Column 'is_validated' successfully added to users table")
            
            # Show current table structure
            print("\nCurrent users table structure:")
            cursor.execute("PRAGMA table_info(users)")
            for column in cursor.fetchall():
                print(f"  - {column[1]} ({column[2]}) {'NOT NULL' if column[3] else 'NULL'} DEFAULT {column[4] or 'None'}")
                
            return True
        else:
            print("❌ Failed to add column")
            return False
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("🔄 Starting user validation migration...")
    success = migrate_database()
    
    if success:
        print("🎉 Migration completed successfully!")
        sys.exit(0)
    else:
        print("💥 Migration failed!")
        sys.exit(1)
