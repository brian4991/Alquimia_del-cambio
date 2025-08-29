#!/usr/bin/env python3
"""
Script pour migrer la base de données et ajouter les nouveaux champs pour les rôles utilisateur
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Add backend to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_db, engine
from models import Base, User
from auth import create_admin_user

def migrate_database():
    """Migrate the database to add new user fields"""
    print("🔄 Starting database migration...")
    
    try:
        # Create all tables (will add new columns if they don't exist)
        Base.metadata.create_all(bind=engine)
        print("✅ Database schema updated successfully")
        
        # Add default values for existing users
        with engine.begin() as conn:
            # Check if we need to update existing users
            result = conn.execute(text("SELECT COUNT(*) FROM users WHERE role IS NULL OR role = ''"))
            users_to_update = result.scalar()
            
            if users_to_update > 0:
                print(f"📝 Updating {users_to_update} existing users with default values...")
                
                # Set default values for existing users
                conn.execute(text("""
                    UPDATE users 
                    SET role = 'user', 
                        provider = 'local', 
                        is_active = 1
                    WHERE role IS NULL OR role = ''
                """))
                
                print("✅ Existing users updated with default values")
            else:
                print("✅ No existing users need updates")
                
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    return True

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
    print("🚀 Alquimia del Cambio - Database Migration")
    print("==========================================")
    
    # Step 1: Migrate database schema
    if not migrate_database():
        print("❌ Migration failed. Exiting.")
        sys.exit(1)
    
    # Step 2: Create default admin if needed
    create_default_admin()
    
    print("\n✨ Migration completed successfully!")
    print("\n📋 Next steps:")
    print("1. Update your .env file with OAuth credentials:")
    print("   - GOOGLE_CLIENT_ID=your_google_client_id")
    print("   - GOOGLE_CLIENT_SECRET=your_google_client_secret")
    print("   - FACEBOOK_CLIENT_ID=your_facebook_client_id")
    print("   - FACEBOOK_CLIENT_SECRET=your_facebook_client_secret")
    print("2. Change the default admin password")
    print("3. Test the authentication system")

if __name__ == "__main__":
    main()