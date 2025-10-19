"""
Script to set user as admin in local database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

# Local SQLite database
DATABASE_URL = "sqlite:///./app.db"

# Create engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def set_user_admin(email: str):
    db = SessionLocal()
    try:
        # Find user by email
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            print(f"✗ User not found with email: {email}")
            return
        
        print(f"✓ User found:")
        print(f"  Username: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Current Role: {user.role}")
        
        if user.role == "admin":
            print(f"  → User is already admin!")
        else:
            user.role = "admin"
            user.is_validated = True
            user.is_active = True
            db.commit()
            print(f"  → Role updated to admin! ✓")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    email = "brian.piorkowski@inetum.com"
    print(f"Setting user {email} as admin...")
    print("-" * 50)
    set_user_admin(email)
    print("-" * 50)
    print("Done!")

