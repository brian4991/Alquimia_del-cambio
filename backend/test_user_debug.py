#!/usr/bin/env python3
"""
Test script to debug user theme access issues
"""

import requests
import json

def test_user_debug():
    print("🔍 Testing user debug endpoint...")
    
    # Try to login as admin first to get a token
    admin_login = {
        "username": "admin",
        "password": "admin123"
    }
    
    try:
        # Login as admin
        login_response = requests.post("http://localhost:8000/login", json=admin_login)
        
        if login_response.status_code == 200:
            admin_token = login_response.json()["access_token"]
            admin_headers = {"Authorization": f"Bearer {admin_token}"}
            
            # Get all users to find test user
            users_response = requests.get("http://localhost:8000/auth/admin/users/stats", headers=admin_headers)
            
            if users_response.status_code == 200:
                users_data = users_response.json()
                users = users_data.get("users", [])
                
                # Find validated test user
                test_user = None
                for user in users:
                    if user.get("is_validated") and user.get("role") != "admin":
                        test_user = user
                        break
                
                if test_user:
                    print(f"✅ Found validated test user: {test_user['username']} (ID: {test_user['id']})")
                    print(f"   is_validated: {test_user['is_validated']}")
                    print(f"   validated_modules: {test_user.get('validated_modules', [])}")
                    
                    # Now we need to get a token for this user - we can't do this easily
                    # So let's check the debug endpoint as admin but for this user
                    print(f"\n🔍 Checking theme completion status for user {test_user['id']}...")
                    
                    # Create a modified debug endpoint call
                    debug_url = f"http://localhost:8000/debug/theme/1/completion-status"
                    
                    # We need to modify the backend to accept user_id as a parameter for admin
                    print(f"❌ Can't test debug endpoint directly without user's token")
                    print(f"   Endpoint URL would be: {debug_url}")
                    
                    # Let's check modules access instead
                    print(f"\n🔍 Checking modules access...")
                    
                    # This won't work without the user's token, but let's see what we can check
                    print("Let's check the database directly...")
                    
                else:
                    print("❌ No validated non-admin users found")
                    print("Available users:")
                    for user in users:
                        print(f"   - {user['username']}: validated={user.get('is_validated')}, role={user.get('role')}")
            else:
                print(f"❌ Failed to get users: {users_response.text}")
        else:
            print(f"❌ Admin login failed: {login_response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def check_database_directly():
    print("\n🔍 Checking database directly...")
    
    import sqlite3
    import os
    
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get validated users
            cursor.execute("SELECT id, username, is_validated FROM users WHERE is_validated = 1 AND role != 'admin'")
            validated_users = cursor.fetchall()
            
            print("Validated non-admin users:")
            for user in validated_users:
                user_id, username, is_validated = user
                print(f"   - User {user_id} ({username}): is_validated={is_validated}")
                
                # Check their progress
                cursor.execute("SELECT theme_id, completed FROM user_progress WHERE user_id = ?", (user_id,))
                progress = cursor.fetchall()
                print(f"     Progress: {progress}")
                
                # Check their responses for theme 1
                cursor.execute("""
                    SELECT e.id, e.title, 
                           (SELECT COUNT(*) FROM user_responses ur WHERE ur.user_id = ? AND ur.exercise_id = e.id) as main_responses,
                           (SELECT COUNT(*) FROM user_sub_question_responses usr WHERE usr.user_id = ? AND usr.exercise_id = e.id) as sub_responses
                    FROM exercises e 
                    WHERE e.theme_id = 1 
                    ORDER BY e.order_number
                """, (user_id, user_id))
                
                responses = cursor.fetchall()
                print(f"     Theme 1 exercises responses:")
                for resp in responses:
                    print(f"       Exercise {resp[0]} ({resp[1]}): main={resp[2]}, sub={resp[3]}")
                
                # Check modules access
                cursor.execute("SELECT * FROM modules WHERE is_active = 1 ORDER BY order_number")
                modules = cursor.fetchall()
                print(f"     Available modules: {len(modules)}")
                
                # Check if user has access to module 1 themes
                print(f"\n     🔍 Checking theme access logic for user {user_id}:")
                cursor.execute("SELECT id, title, order_number FROM themes WHERE module_id = 1 ORDER BY order_number")
                themes = cursor.fetchall()
                
                for i, theme in enumerate(themes):
                    theme_id, title, order_num = theme
                    
                    # Check completion
                    cursor.execute("SELECT completed FROM user_progress WHERE user_id = ? AND theme_id = ?", (user_id, theme_id))
                    completion = cursor.fetchone()
                    is_completed = completion[0] if completion else False
                    
                    # Apply access logic (same as backend)
                    if i == 0:
                        is_unlocked = True  # First theme always unlocked for validated users
                    else:
                        # Check if previous theme is completed
                        prev_theme_id = themes[i-1][0]
                        cursor.execute("SELECT completed FROM user_progress WHERE user_id = ? AND theme_id = ? AND completed = 1", (user_id, prev_theme_id))
                        prev_completed = cursor.fetchone()
                        is_unlocked = prev_completed is not None
                    
                    print(f"       Theme {theme_id} ({title}): completed={is_completed}, unlocked={is_unlocked}")
                
                print("")
            
            conn.close()
        except Exception as e:
            print(f"❌ Database error: {e}")
    else:
        print(f"❌ Database not found at {db_path}")

if __name__ == "__main__":
    test_user_debug()
    check_database_directly()
