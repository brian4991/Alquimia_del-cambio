#!/usr/bin/env python3
"""
Create a test admin user for testing exercise cards
"""

from database import SessionLocal
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_test_admin():
    """Create a test admin user"""
    db = SessionLocal()
    try:
        # Check if admin already exists
        existing_admin = db.query(User).filter(User.username == "testadmin").first()
        if existing_admin:
            print("✅ Test admin user already exists")
            return
        
        # Create admin user
        hashed_password = pwd_context.hash("testpass123")
        admin_user = User(
            username="testadmin",
            email="testadmin@test.com",
            password_hash=hashed_password,
            role="admin",
            is_active=True,
            is_validated=True
        )
        
        db.add(admin_user)
        db.commit()
        print("✅ Test admin user created:")
        print("   Username: testadmin")
        print("   Password: testpass123")
        print("   Role: admin")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_admin()
