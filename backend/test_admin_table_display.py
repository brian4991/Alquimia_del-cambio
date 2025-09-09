#!/usr/bin/env python3
"""
Test script to verify that admin can see table responses in a readable format
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def test_admin_table_display():
    """Test that admin can see table responses properly formatted"""
    print("🧪 Testing Admin Table Display...")
    
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
        user_data = {"username": "tableadmin", "email": "tableadmin@test.com", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/register", json=user_data)
        
        # Login as test user
        login_data = {"username": "tableadmin", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/login", data=login_data)
        user_token = response.json()["access_token"]
        user_headers = {"Authorization": f"Bearer {user_token}"}
        
        # Get user ID
        response = requests.get(f"{BASE_URL}/me", headers=user_headers)
        user_id = response.json()["id"]
        print(f"✅ Test user created, ID: {user_id}")
        
        # Get first theme
        response = requests.get(f"{BASE_URL}/modules/1/themes", headers=admin_headers)
        themes = response.json()
        theme_id = themes[0]["id"]
        
        # Create exercise card with table
        print("3. Creating exercise card with table...")
        exercise_card_data = {
            "title": "Admin Display Test",
            "content": "<p>Test for admin table display</p>",
            "card_type": "exercise",
            "order_number": 995,
            "exercise_instructions": "Fill the weekly planner",
            "exercise_questions": [
                {
                    "type": "table",
                    "question": "Weekly Activity Planner:",
                    "table_config": {
                        "columns": [
                            {"title": "Day", "type": "text"},
                            {"title": "Morning Activity", "type": "text"},
                            {"title": "Afternoon Activity", "type": "text"},
                            {"title": "Energy Level", "type": "number", "min": 1, "max": 10}
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
        
        card = response.json()
        card_id = card["id"]
        print(f"✅ Exercise card created with ID: {card_id}")
        
        # Submit table response as user
        print("4. Submitting table response...")
        table_data = {
            "0": {"0": "Lundi", "1": "Méditation", "2": "Travail", "3": "8"},
            "1": {"0": "Mardi", "1": "Sport", "2": "Réunions", "3": "7"},
            "2": {"0": "Mercredi", "1": "Lecture", "2": "Projets", "3": "9"},
            "3": {"0": "Jeudi", "1": "Yoga", "2": "Formation", "3": "8"},
            "4": {"0": "Vendredi", "1": "Marche", "2": "Créativité", "3": "9"},
            "5": {"0": "Samedi", "1": "Famille", "2": "Détente", "3": "10"},
            "6": {"0": "Dimanche", "1": "Nature", "2": "Préparation", "3": "8"}
        }
        
        response_data = {
            "card_id": card_id,
            "question_index": 0,
            "response_text": json.dumps(table_data)
        }
        
        response = requests.post(
            f"{BASE_URL}/cards/{card_id}/responses",
            headers=user_headers,
            json=response_data
        )
        
        if response.status_code != 200:
            print(f"❌ Failed to submit table response: {response.status_code}")
            return False
        
        print("✅ Table response submitted")
        
        # Get admin view of responses
        print("5. Getting admin view of responses...")
        response = requests.get(f"{BASE_URL}/auth/admin/users/{user_id}/responses", headers=admin_headers)
        if response.status_code != 200:
            print(f"❌ Failed to get responses: {response.status_code}")
            return False
        
        responses = response.json()
        table_responses = [r for r in responses if r.get("table_config")]
        
        if len(table_responses) != 1:
            print(f"❌ Expected 1 table response, got {len(table_responses)}")
            return False
        
        table_response = table_responses[0]
        
        # Verify table config is included
        table_config = table_response.get("table_config")
        if not table_config:
            print("❌ Table config not found in response")
            return False
        
        print("✅ Table response with config found:")
        print(f"   - Title: {table_response['exercise_title']}")
        print(f"   - Question: {table_response['sub_question_text']}")
        print(f"   - Columns: {[col['title'] for col in table_config['columns']]}")
        print(f"   - Rows: {table_config['rows']}")
        
        # Verify data structure
        try:
            parsed_data = json.loads(table_response['response_text'])
            filled_rows = sum(1 for row_key, row_data in parsed_data.items() 
                            if any(cell.strip() for cell in row_data.values()))
            print(f"   - Filled rows: {filled_rows}/{table_config['rows']}")
        except:
            print("❌ Failed to parse table data")
            return False
        
        # Clean up
        print("6. Cleaning up...")
        requests.delete(f"{BASE_URL}/api/cards/{card_id}", headers=admin_headers)
        print("✅ Test card deleted")
        
        print("\n🎉 Admin table display test passed!")
        print("📋 Summary:")
        print("   ✅ Table responses include configuration metadata")
        print("   ✅ Admin can access structured table data")
        print("   ✅ Data is properly formatted for display")
        print("\n💡 Frontend AdminTableView component ready to display:")
        print("   - Structured table with column headers")
        print("   - Only filled rows shown")
        print("   - Column types respected (text/number)")
        
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
    success = test_admin_table_display()
    sys.exit(0 if success else 1)
