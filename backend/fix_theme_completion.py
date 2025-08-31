#!/usr/bin/env python3
"""
Script to fix theme completion for users with sub-question responses
"""

import requests
import json

def fix_user_theme_completion():
    print("🔧 Fixing theme completion for user test...")
    
    # Login as admin
    admin_login = {
        "username": "admin",
        "password": "admin123"
    }
    
    try:
        login_response = requests.post("http://localhost:8000/login", json=admin_login)
        
        if login_response.status_code == 200:
            admin_token = login_response.json()["access_token"]
            admin_headers = {"Authorization": f"Bearer {admin_token}"}
            
            print("✅ Admin login successful")
            
            # Try to force complete theme 1 for user 3 (test)
            user_id = 3
            theme_id = 1
            
            force_complete_url = f"http://localhost:8000/admin/force-complete-theme/{theme_id}/{user_id}"
            
            print(f"🔧 Attempting to force complete theme {theme_id} for user {user_id}...")
            
            force_response = requests.post(force_complete_url, headers=admin_headers)
            
            if force_response.status_code == 200:
                result = force_response.json()
                print(f"✅ Success: {result['message']}")
            else:
                print(f"❌ Failed: {force_response.status_code} - {force_response.text}")
                
        else:
            print(f"❌ Admin login failed: {login_response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def test_theme_completion_endpoint():
    print("\n🧪 Testing theme completion with new logic...")
    
    # We can't easily test this without user credentials
    # But let's check if the server is running and responds
    
    try:
        health_response = requests.get("http://localhost:8000/docs")
        if health_response.status_code == 200:
            print("✅ Server is running")
        else:
            print("❌ Server might not be running")
    except:
        print("❌ Server is not accessible")

if __name__ == "__main__":
    fix_user_theme_completion()
    test_theme_completion_endpoint()
