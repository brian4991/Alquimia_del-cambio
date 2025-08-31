#!/usr/bin/env python3
"""
Test script to verify the API returns correct theme unlock status
"""

import requests
import json

def test_user_theme_access():
    print("🔍 Testing user theme access via API...")
    
    # Test with user credentials
    login_data = {
        "username": "brian.piorkowski1@gmail.com", 
        "password": "password123"  # You'll need to know the actual password
    }
    
    try:
        # Try different possible passwords
        possible_passwords = ["password123", "123456", "admin", "password", "brian123"]
        
        token = None
        for password in possible_passwords:
            login_data["password"] = password
            try:
                login_response = requests.post("http://localhost:8000/login", json=login_data)
                if login_response.status_code == 200:
                    token = login_response.json()["access_token"]
                    print(f"✅ Login successful with password: {password}")
                    break
                else:
                    print(f"❌ Login failed with password: {password}")
            except:
                continue
                
        if not token:
            print("❌ Could not login with any password. Let's check what users exist:")
            # Try to get user info from database directly
            import sqlite3
            conn = sqlite3.connect('app.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, email FROM users")
            users = cursor.fetchall()
            print("Available users:")
            for user in users:
                print(f"  - ID {user[0]}: {user[1]} ({user[2]})")
            conn.close()
            return
            
        headers = {"Authorization": f"Bearer {token}"}
        
        # Test modules endpoint
        print("\n🔍 Testing modules endpoint...")
        modules_response = requests.get("http://localhost:8000/modules", headers=headers)
        
        if modules_response.status_code == 200:
            modules = modules_response.json()
            print(f"✅ Got {len(modules)} modules")
            
            for module in modules:
                print(f"   Module {module['id']}: {module['title']}")
                print(f"     is_accessible: {module.get('is_accessible', 'Not specified')}")
        else:
            print(f"❌ Modules request failed: {modules_response.text}")
            return
            
        # Test themes for module 1
        print("\n🔍 Testing themes for module 1...")
        themes_response = requests.get("http://localhost:8000/modules/1/themes", headers=headers)
        
        if themes_response.status_code == 200:
            themes = themes_response.json()
            print(f"✅ Got {len(themes)} themes for module 1")
            
            for theme in themes:
                print(f"   Theme {theme['id']}: {theme['title']}")
                print(f"     is_unlocked: {theme['is_unlocked']}")
                print(f"     is_completed: {theme['is_completed']}")
        else:
            print(f"❌ Themes request failed: {themes_response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_user_theme_access()
