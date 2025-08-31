#!/usr/bin/env python3
"""
Test script to diagnose user validation API issues
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_user_validation():
    print("🔍 Testing User Validation API...")
    
    # First, let's check if we can get users stats (admin endpoint)
    print("\n1. Testing admin authentication...")
    
    # You'll need to replace these with actual admin credentials
    login_data = {
        "username": "admin",  # Replace with actual admin username
        "password": "admin123"  # Replace with actual admin password
    }
    
    try:
        # Login as admin
        login_response = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"Login response status: {login_response.status_code}")
        
        if login_response.status_code == 200:
            login_result = login_response.json()
            token = login_result.get("access_token")
            print(f"✅ Admin login successful")
            
            headers = {"Authorization": f"Bearer {token}"}
            
            # Get users stats to find a user ID
            print("\n2. Getting users list...")
            users_response = requests.get(f"{BASE_URL}/auth/admin/users/stats", headers=headers)
            print(f"Users stats response status: {users_response.status_code}")
            
            if users_response.status_code == 200:
                users_data = users_response.json()
                users = users_data.get("users", [])
                
                if users:
                    # Find a non-admin user to test validation
                    test_user = None
                    for user in users:
                        if user.get("role") != "admin":
                            test_user = user
                            break
                    
                    if test_user:
                        user_id = test_user["id"]
                        print(f"✅ Found test user: {test_user['username']} (ID: {user_id})")
                        print(f"   Current validation status: {test_user.get('is_validated', 'Unknown')}")
                        
                        # Test validation endpoint
                        print(f"\n3. Testing validation endpoint for user {user_id}...")
                        validate_response = requests.post(f"{BASE_URL}/auth/admin/users/{user_id}/validate", headers=headers)
                        print(f"Validation response status: {validate_response.status_code}")
                        print(f"Validation response: {validate_response.text}")
                        
                        if validate_response.status_code == 200:
                            print("✅ Validation successful!")
                        else:
                            print("❌ Validation failed!")
                            print(f"Error details: {validate_response.text}")
                    else:
                        print("❌ No non-admin users found to test")
                else:
                    print("❌ No users found")
            else:
                print(f"❌ Failed to get users: {users_response.text}")
        else:
            print(f"❌ Admin login failed: {login_response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - is the backend server running on localhost:8000?")
    except Exception as e:
        print(f"❌ Error: {e}")

def check_database_schema():
    print("\n🔍 Checking database schema...")
    
    import sqlite3
    import os
    
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check users table structure
            cursor.execute("PRAGMA table_info(users)")
            columns = cursor.fetchall()
            
            print("Users table columns:")
            has_is_validated = False
            for column in columns:
                print(f"  - {column[1]} ({column[2]}) DEFAULT {column[4] or 'None'}")
                if column[1] == 'is_validated':
                    has_is_validated = True
            
            if has_is_validated:
                print("✅ is_validated column exists")
                
                # Check current validation status of users
                cursor.execute("SELECT id, username, is_validated FROM users")
                users = cursor.fetchall()
                
                print("\nCurrent users validation status:")
                for user in users:
                    print(f"  - User {user[0]} ({user[1]}): is_validated = {user[2]}")
            else:
                print("❌ is_validated column missing!")
                
            conn.close()
        except Exception as e:
            print(f"❌ Database error: {e}")
    else:
        print(f"❌ Database not found at {db_path}")

if __name__ == "__main__":
    check_database_schema()
    test_user_validation()
