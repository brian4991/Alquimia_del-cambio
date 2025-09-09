#!/usr/bin/env python3
"""
Test script to verify that table questions work correctly
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_table_question_creation():
    """Test creating an exercise card with table questions"""
    print("🧪 Testing Table Questions in Exercise Cards...")
    
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
        
        # Get first theme
        print("2. Getting theme...")
        response = requests.get(f"{BASE_URL}/modules/1/themes", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get themes: {response.status_code}")
            return False
        
        themes = response.json()
        if not themes:
            print("❌ No themes found")
            return False
        theme_id = themes[0]["id"]
        
        # Create exercise card with table question
        print("3. Creating exercise card with table question...")
        exercise_card_data = {
            "title": "Test Table Exercise Card",
            "content": "<p>Exercise with table questions</p>",
            "card_type": "exercise",
            "order_number": 997,
            "exercise_instructions": "Please fill in the table below.",
            "exercise_questions": [
                {
                    "type": "text",
                    "question": "What is your name?"
                },
                {
                    "type": "table",
                    "question": "Fill in your daily emotions:",
                    "table_config": {
                        "columns": [
                            {"title": "Day", "type": "text"},
                            {"title": "Emotion", "type": "text"},
                            {"title": "Intensity", "type": "number"}
                        ],
                        "rows": 7
                    }
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
        print(f"✅ Exercise card with table created with ID: {card_id}")
        
        # Verify the card structure
        print("4. Verifying card structure...")
        response = requests.get(f"{BASE_URL}/themes/{theme_id}/cards", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get cards: {response.status_code}")
            return False
        
        cards = response.json()
        exercise_card = next((c for c in cards if c["id"] == card_id), None)
        
        if not exercise_card:
            print("❌ Exercise card not found")
            return False
        
        questions = exercise_card.get("exercise_questions", [])
        if len(questions) != 2:
            print(f"❌ Expected 2 questions, got {len(questions)}")
            return False
        
        # Check text question
        text_question = questions[0]
        if text_question.get("type") != "text":
            print(f"❌ First question should be text type, got {text_question.get('type')}")
            return False
        
        # Check table question
        table_question = questions[1]
        if table_question.get("type") != "table":
            print(f"❌ Second question should be table type, got {table_question.get('type')}")
            return False
        
        table_config = table_question.get("table_config", {})
        columns = table_config.get("columns", [])
        
        if len(columns) != 3:
            print(f"❌ Expected 3 columns, got {len(columns)}")
            return False
        
        if table_config.get("rows") != 7:
            print(f"❌ Expected 7 rows, got {table_config.get('rows')}")
            return False
        
        print("✅ Card structure verified correctly")
        print(f"   - Text question: {text_question['question']}")
        print(f"   - Table question: {table_question['question']}")
        print(f"   - Table columns: {[col['title'] for col in columns]}")
        print(f"   - Table rows: {table_config['rows']}")
        
        # Clean up
        print("5. Cleaning up...")
        requests.delete(f"{BASE_URL}/api/cards/{card_id}", headers=admin_headers)
        print("✅ Test card deleted")
        
        print("\n🎉 All tests passed! Table questions work correctly.")
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
    success = test_table_question_creation()
    sys.exit(0 if success else 1)
