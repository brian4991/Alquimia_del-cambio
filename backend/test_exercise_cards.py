#!/usr/bin/env python3
"""
Test script to create and test exercise cards functionality
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_exercise_card_creation():
    """Test creating an exercise card"""
    print("🧪 Testing Exercise Cards System...")
    
    # First, we need to login as admin to get a token
    login_data = {
        "username": "testadmin",
        "password": "testpass123"
    }
    
    try:
        # Login
        print("1. Logging in as admin...")
        response = requests.post(f"{BASE_URL}/login", data=login_data)
        if response.status_code != 200:
            print(f"❌ Login failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
        
        token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        print("✅ Login successful")
        
        # Get first theme to test with
        print("2. Getting themes...")
        themes_response = requests.get(f"{BASE_URL}/modules/1/themes", headers=headers)
        if themes_response.status_code != 200:
            print(f"❌ Failed to get themes: {themes_response.status_code}")
            return False
        
        themes = themes_response.json()
        if not themes:
            print("❌ No themes found")
            return False
        
        theme_id = themes[0]["id"]
        print(f"✅ Using theme ID: {theme_id}")
        
        # Create exercise card
        print("3. Creating exercise card...")
        exercise_card_data = {
            "title": "Test Exercise Card",
            "content": "<p>This is a test exercise card created by the automated test.</p>",
            "card_type": "exercise",
            "order_number": 999,  # High number to avoid conflicts
            "exercise_instructions": "Complete the following questions to reflect on your experience.",
            "exercise_questions": [
                "What did you learn from this experience?",
                "How will you apply this knowledge in the future?",
                "What challenges did you face?"
            ]
        }
        
        create_response = requests.post(
            f"{BASE_URL}/api/themes/{theme_id}/cards",
            headers=headers,
            json=exercise_card_data
        )
        
        if create_response.status_code != 200:
            print(f"❌ Failed to create exercise card: {create_response.status_code}")
            print(f"Response: {create_response.text}")
            return False
        
        card = create_response.json()
        card_id = card["id"]
        print(f"✅ Exercise card created with ID: {card_id}")
        
        # Verify the card was created with exercise fields
        print("4. Verifying card creation...")
        get_response = requests.get(f"{BASE_URL}/themes/{theme_id}/cards", headers=headers)
        if get_response.status_code != 200:
            print(f"❌ Failed to get cards: {get_response.status_code}")
            return False
        
        cards = get_response.json()
        exercise_card = next((c for c in cards if c["id"] == card_id), None)
        
        if not exercise_card:
            print("❌ Exercise card not found in cards list")
            return False
        
        if exercise_card["card_type"] != "exercise":
            print(f"❌ Card type is {exercise_card['card_type']}, expected 'exercise'")
            return False
        
        if not exercise_card.get("exercise_questions"):
            print("❌ Exercise questions not found")
            return False
        
        print(f"✅ Exercise card verified: {len(exercise_card['exercise_questions'])} questions")
        
        # Test response submission
        print("5. Testing response submission...")
        response_data = {
            "card_id": card_id,
            "question_index": 0,
            "response_text": "This is a test response to the first question."
        }
        
        response_response = requests.post(
            f"{BASE_URL}/cards/{card_id}/responses",
            headers=headers,
            json=response_data
        )
        
        if response_response.status_code != 200:
            print(f"❌ Failed to submit response: {response_response.status_code}")
            print(f"Response: {response_response.text}")
            return False
        
        print("✅ Response submitted successfully")
        
        # Verify response was saved
        print("6. Verifying response was saved...")
        get_responses = requests.get(f"{BASE_URL}/cards/{card_id}/responses", headers=headers)
        if get_responses.status_code != 200:
            print(f"❌ Failed to get responses: {get_responses.status_code}")
            return False
        
        responses = get_responses.json()
        if not responses.get("responses") or 0 not in responses["responses"]:
            print("❌ Response not found")
            return False
        
        print("✅ Response verified")
        
        # Clean up - delete the test card
        print("7. Cleaning up test card...")
        delete_response = requests.delete(f"{BASE_URL}/api/cards/{card_id}", headers=headers)
        if delete_response.status_code == 200:
            print("✅ Test card deleted")
        else:
            print(f"⚠️ Failed to delete test card: {delete_response.status_code}")
        
        print("\n🎉 All tests passed! Exercise cards system is working correctly.")
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Make sure it's running on http://localhost:8000")
        return False
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == "__main__":
    success = test_exercise_card_creation()
    sys.exit(0 if success else 1)
