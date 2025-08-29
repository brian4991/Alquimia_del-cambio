#!/usr/bin/env python3
"""
Script de migration SQL explicite pour ajouter les nouveaux champs utilisateur
"""

import sqlite3
import os
import sys
from sqlalchemy.orm import sessionmaker

# Add backend to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import engine
from models import User
from auth import create_admin_user

def migrate_user_table():
    """Migrate user table by adding new columns"""
    db_path = './app.db'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    print("🔄 Starting SQL migration...")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get current table structure
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        print(f"📋 Current columns: {columns}")
        
        # Add new columns if they don't exist
        if 'role' not in columns:
            print("➕ Adding 'role' column...")
            cursor.execute("ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'user'")
            
        if 'provider' not in columns:
            print("➕ Adding 'provider' column...")
            cursor.execute("ALTER TABLE users ADD COLUMN provider VARCHAR(50)")
            
        if 'provider_id' not in columns:
            print("➕ Adding 'provider_id' column...")
            cursor.execute("ALTER TABLE users ADD COLUMN provider_id VARCHAR(100)")
            
        if 'is_active' not in columns:
            print("➕ Adding 'is_active' column...")
            cursor.execute("ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT 1")
        
        # Update existing users with default values
        print("📝 Updating existing users...")
        cursor.execute("""
            UPDATE users 
            SET role = 'user', 
                provider = 'local', 
                is_active = 1
            WHERE role IS NULL OR role = ''
        """)
        
        conn.commit()
        conn.close()
        
        print("✅ SQL migration completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ SQL migration failed: {e}")
        if conn:
            conn.close()
        return False

def create_default_admin():
    """Create default admin user if none exists"""
    print("👤 Checking for admin users...")
    
    # Get database session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Check if any admin exists
        admin_count = db.query(User).filter(User.role == "admin").count()
        
        if admin_count == 0:
            print("🔧 No admin user found. Creating default admin...")
            
            # Create default admin
            admin_user = create_admin_user(
                username="admin",
                email="admin@alquimiadelcambio.com",
                password="admin123",  # Change this in production!
                db=db
            )
            
            print(f"✅ Admin user created successfully!")
            print(f"   Username: {admin_user.username}")
            print(f"   Email: {admin_user.email}")
            print(f"   ⚠️  Default password: admin123 (CHANGE THIS IN PRODUCTION!)")
            
        else:
            print(f"✅ Found {admin_count} admin user(s) - no action needed")
            
    except Exception as e:
        print(f"❌ Failed to create admin user: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Main migration function"""
    print("🚀 Alquimia del Cambio - SQL Migration")
    print("=====================================")
    
    # Step 1: Migrate database schema
    if not migrate_user_table():
        print("❌ Migration failed. Exiting.")
        sys.exit(1)
    
    # Step 2: Create default admin if needed
    create_default_admin()
    
    print("\n✨ Migration completed successfully!")
    print("\n📋 Next steps:")
    print("1. Create a .env file with OAuth credentials:")
    print("   - GOOGLE_CLIENT_ID=your_google_client_id")
    print("   - GOOGLE_CLIENT_SECRET=your_google_client_secret")
    print("   - FACEBOOK_CLIENT_ID=your_facebook_client_id")
    print("   - FACEBOOK_CLIENT_SECRET=your_facebook_client_secret")
    print("   - SECRET_KEY=your-secret-jwt-key")
    print("2. Change the default admin password")
    print("3. Install new dependencies: pip install authlib httpx")
    print("4. Test the authentication system")

if __name__ == "__main__":
    main()