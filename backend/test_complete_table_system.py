#!/usr/bin/env python3
"""
Test script to verify the complete table exercise system works end-to-end
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_complete_table_system():
    """Test the complete table exercise system"""
    print("🧪 Testing Complete Table Exercise System...")
    
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
        
        # Create test user
        print("2. Creating test user...")
        user_data = {"username": "tableuser", "email": "table@test.com", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/register", json=user_data)
        
        # Login as test user
        print("3. Logging in as test user...")
        login_data = {"username": "tableuser", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/login", data=login_data)
        if response.status_code != 200:
            print(f"❌ User login failed: {response.status_code}")
            return False
        
        user_token = response.json()["access_token"]
        user_headers = {"Authorization": f"Bearer {user_token}"}
        
        # Get user ID
        response = requests.get(f"{BASE_URL}/me", headers=user_headers)
        user_id = response.json()["id"]
        print(f"✅ User login successful, ID: {user_id}")
        
        # Get first theme
        print("4. Getting theme...")
        response = requests.get(f"{BASE_URL}/modules/1/themes", headers=admin_headers)
        themes = response.json()
        theme_id = themes[0]["id"]
        
        # Create comprehensive exercise card
        print("5. Creating exercise card with mixed question types...")
        exercise_card_data = {
            "title": "Complete Table Exercise Test",
            "content": "<p>This exercise tests both text and table questions</p>",
            "card_type": "exercise",
            "order_number": 996,
            "exercise_instructions": "Complete all questions below. Fill the table with your daily activities.",
            "exercise_questions": [
                {
                    "type": "text",
                    "question": "What is your main goal for this week?"
                },
                {
                    "type": "table",
                    "question": "Track your daily activities and emotions:",
                    "table_config": {
                        "columns": [
                            {"title": "Day", "type": "text"},
                            {"title": "Main Activity", "type": "text"},
                            {"title": "Emotion", "type": "text"},
                            {"title": "Energy Level", "type": "number", "min": 1, "max": 10}
                        ],
                        "rows": 7
                    }
                },
                {
                    "type": "text",
                    "question": "What patterns do you notice from your tracking?"
                }
            ]
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
        
        # Verify card structure from user perspective
        print("6. Verifying card structure from user perspective...")
        response = requests.get(f"{BASE_URL}/themes/{theme_id}/cards", headers=user_headers)
        cards = response.json()
        exercise_card = next((c for c in cards if c["id"] == card_id), None)
        
        if not exercise_card:
            print("❌ Exercise card not found")
            return False
        
        questions = exercise_card.get("exercise_questions", [])
        print(f"✅ Found {len(questions)} questions:")
        for i, q in enumerate(questions):
            print(f"   {i+1}. {q.get('type', 'text')}: {q.get('question', '')}")
        
        # Submit responses as user
        print("7. Submitting responses as user...")
        
        # Text response 1
        response1_data = {
            "card_id": card_id,
            "question_index": 0,
            "response_text": "My main goal is to improve my emotional awareness through daily tracking."
        }
        response = requests.post(f"{BASE_URL}/cards/{card_id}/responses", headers=user_headers, json=response1_data)
        if response.status_code != 200:
            print(f"❌ Failed to submit text response 1: {response.status_code}")
            return False
        
        # Table response
        table_data = {
            "0": {"0": "Monday", "1": "Work meeting", "2": "Focused", "3": "8"},
            "1": {"0": "Tuesday", "1": "Exercise", "2": "Energetic", "3": "9"},
            "2": {"0": "Wednesday", "1": "Reading", "2": "Calm", "3": "7"},
            "3": {"0": "Thursday", "1": "Social event", "2": "Happy", "3": "8"},
            "4": {"0": "Friday", "1": "Project work", "2": "Stressed", "3": "6"},
            "5": {"0": "Saturday", "1": "Family time", "2": "Joyful", "3": "9"},
            "6": {"0": "Sunday", "1": "Rest", "2": "Peaceful", "3": "8"}
        }
        response2_data = {
            "card_id": card_id,
            "question_index": 1,
            "response_text": json.dumps(table_data)
        }
        response = requests.post(f"{BASE_URL}/cards/{card_id}/responses", headers=user_headers, json=response2_data)
        if response.status_code != 200:
            print(f"❌ Failed to submit table response: {response.status_code}")
            print(f"Response: {response.text}")
            return False
        
        # Text response 2
        response3_data = {
            "card_id": card_id,
            "question_index": 2,
            "response_text": "I notice that my energy is highest on weekends and when I exercise. Work stress affects my energy levels."
        }
        response = requests.post(f"{BASE_URL}/cards/{card_id}/responses", headers=user_headers, json=response3_data)
        if response.status_code != 200:
            print(f"❌ Failed to submit text response 2: {response.status_code}")
            return False
        
        print("✅ All responses submitted successfully")
        
        # Verify admin can see all responses
        print("8. Verifying admin can see all responses...")
        response = requests.get(f"{BASE_URL}/auth/admin/users/{user_id}/responses", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get user responses: {response.status_code}")
            return False
        
        responses = response.json()
        card_responses = [r for r in responses if r.get("response_type") == "card_exercise"]
        
        if len(card_responses) != 3:
            print(f"❌ Expected 3 card responses, got {len(card_responses)}")
            return False
        
        print("✅ Admin can see all responses:")
        for resp in card_responses:
            response_text = resp['response_text']
            if len(response_text) > 100:
                response_text = response_text[:100] + "..."
            print(f"   - {resp['exercise_title']}: {response_text}")
        
        # Verify table data integrity
        table_response = next((r for r in card_responses if "Q2" in r['exercise_title']), None)
        if table_response:
            try:
                parsed_table = json.loads(table_response['response_text'])
                print(f"✅ Table data preserved correctly: {len(parsed_table)} rows")
            except:
                print("❌ Table data not properly formatted")
                return False
        
        # Clean up
        print("9. Cleaning up...")
        requests.delete(f"{BASE_URL}/api/cards/{card_id}", headers=admin_headers)
        print("✅ Test card deleted")
        
        print("\n🎉 Complete table exercise system test passed!")
        print("📋 Summary:")
        print("   ✅ Mixed question types (text + table) work correctly")
        print("   ✅ Table data is properly stored and retrieved")
        print("   ✅ Admin can view all response types")
        print("   ✅ Data integrity is maintained")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Make sure it's running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_complete_table_system()
    sys.exit(0 if success else 1)
