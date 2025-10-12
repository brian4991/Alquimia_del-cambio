"""
Migration script to add theme_type column to themes table
This will add a 'theme_type' column with default value 'theme' to all existing themes
"""
from sqlalchemy import create_engine, text
from database import SQLALCHEMY_DATABASE_URL
import os

def add_theme_type_column():
    """Add theme_type column to themes table"""
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    with engine.connect() as connection:
        try:
            # Check if column already exists
            check_query = text("""
                SELECT COUNT(*) 
                FROM pragma_table_info('themes') 
                WHERE name='theme_type'
            """)
            result = connection.execute(check_query)
            column_exists = result.scalar() > 0
            
            if column_exists:
                print("[OK] Column 'theme_type' already exists in themes table")
                return
            
            # Add the column with default value
            alter_query = text("""
                ALTER TABLE themes 
                ADD COLUMN theme_type VARCHAR(50) DEFAULT 'theme'
            """)
            connection.execute(alter_query)
            connection.commit()
            
            print("[OK] Successfully added 'theme_type' column to themes table")
            print("     All existing themes have been set to type 'theme'")
            
        except Exception as e:
            print(f"[ERROR] Error adding theme_type column: {e}")
            connection.rollback()
            raise

if __name__ == "__main__":
    print("[START] Starting migration: Adding theme_type column to themes table...")
    add_theme_type_column()
    print("[DONE] Migration completed!")

