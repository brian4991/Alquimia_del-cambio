"""
Script to create admin user in local database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auth import hash_password
from models import User, Base

# Local SQLite database
DATABASE_URL = "sqlite:///./app.db"

# Create engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_admin_user():
    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == "brian.piorkowski@inetum.com").first()
        
        if existing_user:
            print(f"✓ User already exists: {existing_user.username}")
            print(f"  Email: {existing_user.email}")
            print(f"  Role: {existing_user.role}")
            
            # Update to admin if not already
            if existing_user.role != "admin":
                existing_user.role = "admin"
                db.commit()
                print(f"  → Updated role to admin!")
            return existing_user
        
        # Create new admin user
        admin_password = "admin123"  # Default password
        hashed_password = hash_password(admin_password)
        
        admin_user = User(
            username="brian",
            email="brian.piorkowski@inetum.com",
            password_hash=hashed_password,
            role="admin",
            provider="local",
            is_active=True,
            is_validated=True
        )
        
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        
        print(f"✓ Admin user created successfully!")
        print(f"  Username: {admin_user.username}")
        print(f"  Email: {admin_user.email}")
        print(f"  Password: {admin_password}")
        print(f"  Role: {admin_user.role}")
        
        return admin_user
        
    except Exception as e:
        print(f"✗ Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating admin user in local database...")
    print("-" * 50)
    create_admin_user()
    print("-" * 50)
    print("Done!")

