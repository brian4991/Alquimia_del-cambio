#!/usr/bin/env python3
"""
Debug script to test theme access logic
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Theme, UserProgress
import requests
import json

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_theme_access_logic():
    print("🔍 Testing theme access logic...")
    
    db = SessionLocal()
    
    try:
        # Get user 1
        user = db.query(User).filter(User.id == 1).first()
        if not user:
            print("❌ User 1 not found")
            return
            
        print(f"✅ User found: {user.username}")
        print(f"   is_validated: {user.is_validated}")
        print(f"   validated_modules: {user.validated_modules}")
        
        # Get themes for module 1
        themes = db.query(Theme).filter(Theme.module_id == 1).order_by(Theme.order_number).all()
        print(f"✅ Found {len(themes)} themes in module 1")
        
        # Check access logic for each theme
        user_is_validated = user.is_validated
        print(f"   user_is_validated = {user_is_validated}")
        
        for i, theme in enumerate(themes):
            print(f"\n--- Theme {i+1}: {theme.title} (ID: {theme.id}) ---")
            
            # Check if theme is completed
            theme_progress = db.query(UserProgress).filter(
                UserProgress.user_id == user.id,
                UserProgress.theme_id == theme.id,
                UserProgress.completed == True
            ).first()
            is_completed = theme_progress is not None
            print(f"   is_completed: {is_completed}")
            
            # Apply access logic
            if not user_is_validated:
                # Non-validated users: only first theme of module 1 is unlocked
                if i == 0:  # module_id == 1 is implicit since we're filtering by it
                    is_unlocked = True
                else:
                    is_unlocked = False
                print(f"   Logic: Non-validated user, theme {i+1} -> is_unlocked = {is_unlocked}")
            else:
                # Validated users: normal sequential progression
                if i == 0:
                    is_unlocked = True
                    print(f"   Logic: Validated user, first theme -> is_unlocked = {is_unlocked}")
                else:
                    # Check if previous theme is completed
                    prev_theme = themes[i-1]
                    prev_progress = db.query(UserProgress).filter(
                        UserProgress.user_id == user.id,
                        UserProgress.theme_id == prev_theme.id,
                        UserProgress.completed == True
                    ).first()
                    is_unlocked = prev_progress is not None
                    print(f"   Logic: Validated user, checking prev theme {prev_theme.id} -> is_unlocked = {is_unlocked}")
                    
            print(f"   FINAL: Theme {theme.id} is_unlocked = {is_unlocked}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

def test_api_endpoint():
    print("\n🔍 Testing API endpoint...")
    
    try:
        # Login as user 1
        login_response = requests.post("http://localhost:8000/login", json={
            "username": "brian.piorkowski1@gmail.com",
            "password": "password123"  # You'll need the actual password
        })
        
        if login_response.status_code != 200:
            print(f"❌ Login failed: {login_response.text}")
            return
            
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Test themes endpoint
        themes_response = requests.get("http://localhost:8000/modules/1/themes", headers=headers)
        
        if themes_response.status_code == 200:
            themes_data = themes_response.json()
            print(f"✅ API returned {len(themes_data)} themes")
            
            for theme in themes_data:
                print(f"   Theme {theme['id']}: {theme['title']}")
                print(f"     is_unlocked: {theme['is_unlocked']}")
                print(f"     is_completed: {theme['is_completed']}")
        else:
            print(f"❌ API call failed: {themes_response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - is the server running?")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_theme_access_logic()
    test_api_endpoint()
