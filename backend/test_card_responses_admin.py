#!/usr/bin/env python3
"""
Test script to verify that card exercise responses are visible in admin panel
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_admin_can_see_card_responses():
    """Test that admin can see card exercise responses in user profiles"""
    print("🧪 Testing Admin Panel - Card Exercise Responses Visibility...")
    
    try:
        # Login as admin
        print("1. Logging in as admin...")
        login_data = {"username": "testadmin", "password": "testpass123"}
        response = requests.post(f"{BASE_URL}/login", data=login_data)
        if response.status_code != 200:
            print(f"❌ Admin login failed: {response.status_code}")
            return False
        
        admin_token = response.json()["access_token"]
        admin_headers = {"Authorization": f"Bearer {admin_token}"}
        print("✅ Admin login successful")
        
        # Create a test user
        print("2. Creating test user...")
        user_data = {"username": "testuser", "email": "test@test.com", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/register", json=user_data)
        if response.status_code not in [200, 201]:
            print(f"⚠️ User creation may have failed: {response.status_code} (might already exist)")
        
        # Login as test user
        print("3. Logging in as test user...")
        login_data = {"username": "testuser", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/login", data=login_data)
        if response.status_code != 200:
            print(f"❌ User login failed: {response.status_code}")
            return False
        
        user_token = response.json()["access_token"]
        user_headers = {"Authorization": f"Bearer {user_token}"}
        print("✅ User login successful")
        
        # Get user ID
        response = requests.get(f"{BASE_URL}/me", headers=user_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get user info: {response.status_code}")
            return False
        user_id = response.json()["id"]
        print(f"✅ Got user ID: {user_id}")
        
        # Get first theme
        print("4. Getting theme for exercise card...")
        response = requests.get(f"{BASE_URL}/modules/1/themes", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get themes: {response.status_code}")
            return False
        
        themes = response.json()
        if not themes:
            print("❌ No themes found")
            return False
        theme_id = themes[0]["id"]
        
        # Create exercise card as admin
        print("5. Creating exercise card as admin...")
        exercise_card_data = {
            "title": "Admin Test Exercise Card",
            "content": "<p>Test exercise for admin visibility</p>",
            "card_type": "exercise",
            "order_number": 998,
            "exercise_instructions": "Please answer the following questions for admin testing.",
            "exercise_questions": ["What is your favorite color?", "How do you feel today?"]
        }
        
        response = requests.post(
            f"{BASE_URL}/api/themes/{theme_id}/cards",
            headers=admin_headers,
            json=exercise_card_data
        )
        
        if response.status_code != 200:
            print(f"❌ Failed to create exercise card: {response.status_code}")
            print(f"Response: {response.text}")
            return False
        
        card = response.json()
        card_id = card["id"]
        print(f"✅ Exercise card created with ID: {card_id}")
        
        # Submit responses as user
        print("6. Submitting responses as user...")
        responses = [
            {"card_id": card_id, "question_index": 0, "response_text": "Blue is my favorite color"},
            {"card_id": card_id, "question_index": 1, "response_text": "I feel great today!"}
        ]
        
        for response_data in responses:
            response = requests.post(
                f"{BASE_URL}/cards/{card_id}/responses",
                headers=user_headers,
                json=response_data
            )
            if response.status_code != 200:
                print(f"❌ Failed to submit response: {response.status_code}")
                print(f"Response: {response.text}")
                return False
        
        print("✅ Responses submitted successfully")
        
        # Check admin can see responses
        print("7. Checking admin can see user responses...")
        response = requests.get(f"{BASE_URL}/auth/admin/users/{user_id}/responses", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get user responses as admin: {response.status_code}")
            return False
        
        responses = response.json()
        card_responses = [r for r in responses if r.get("response_type") == "card_exercise"]
        
        if len(card_responses) != 2:
            print(f"❌ Expected 2 card responses, got {len(card_responses)}")
            print(f"All responses: {responses}")
            return False
        
        print(f"✅ Admin can see {len(card_responses)} card exercise responses")
        
        # Verify response content
        for resp in card_responses:
            print(f"   - {resp['exercise_title']}: {resp['response_text'][:50]}...")
        
        # Check stats include card responses
        print("8. Checking stats include card responses...")
        response = requests.get(f"{BASE_URL}/auth/admin/users/stats", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get user stats: {response.status_code}")
            return False
        
        stats = response.json()
        print(f"✅ Total responses in stats: {stats['stats']['total_responses']}")
        
        # Find our test user in stats
        test_user_stats = next((u for u in stats['users'] if u['id'] == user_id), None)
        if test_user_stats:
            print(f"✅ Test user response count: {test_user_stats['response_count']}")
        
        # Clean up
        print("9. Cleaning up...")
        requests.delete(f"{BASE_URL}/api/cards/{card_id}", headers=admin_headers)
        print("✅ Test card deleted")
        
        print("\n🎉 All tests passed! Admin can see card exercise responses correctly.")
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Make sure it's running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == "__main__":
    success = test_admin_can_see_card_responses()
    sys.exit(0 if success else 1)
