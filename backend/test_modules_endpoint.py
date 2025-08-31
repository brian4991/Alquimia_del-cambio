#!/usr/bin/env python3
"""
Test the modules endpoint directly
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi.testclient import TestClient
from main import app
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

def test_modules_endpoint():
    print("🔍 Testing modules endpoint...")
    
    db = SessionLocal()
    
    try:
        # Get user 1 (validated user)
        user = db.query(User).filter(User.id == 1).first()
        print(f"User: {user.username}, is_validated: {user.is_validated}")
        
        # Mock the current_user dependency
        def override_get_current_user():
            return user
            
        app.dependency_overrides[app.dependency_overrides] = override_get_current_user
        
        # Test the endpoint
        response = client.get("/modules")
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            modules = response.json()
            print(f"✅ Got {len(modules)} modules:")
            
            for module in modules:
                print(f"   Module {module['id']}: {module['title']}")
                print(f"     is_accessible: {module.get('is_accessible', 'Not specified')}")
        else:
            print(f"❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_modules_endpoint()
