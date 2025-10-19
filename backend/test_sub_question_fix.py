#!/usr/bin/env python3
"""
Quick test to verify sub_question_index string support
"""
from models import UserSubQuestionResponseDB
from database import SessionLocal

def test_sub_question_formats():
    """Test that database accepts both string formats"""
    
    db = SessionLocal()
    
    try:
        print("🧪 Testing sub_question_index string formats...\n")
        
        # Test 1: Create with legacy format (string representation of int)
        print("1️⃣ Testing legacy format (string '0')...")
        test1 = UserSubQuestionResponseDB(
            user_id=1,
            exercise_id=1,
            sub_question_index="0",  # Legacy format as string
            response_text="Test legacy format"
        )
        db.add(test1)
        db.flush()
        print("   ✅ Legacy format works!\n")
        
        # Test 2: Create with new format (section_X_question_Y)
        print("2️⃣ Testing new format (string 'section_0_question_0')...")
        test2 = UserSubQuestionResponseDB(
            user_id=1,
            exercise_id=1,
            sub_question_index="section_0_question_0",  # New format
            response_text="Test new format"
        )
        db.add(test2)
        db.flush()
        print("   ✅ New format works!\n")
        
        # Test 3: Query both
        print("3️⃣ Querying both formats...")
        results = db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.user_id == 1,
            UserSubQuestionResponseDB.exercise_id == 1
        ).all()
        print(f"   ✅ Found {len(results)} test records\n")
        
        # Cleanup test data
        print("4️⃣ Cleaning up test data...")
        db.query(UserSubQuestionResponseDB).filter(
            UserSubQuestionResponseDB.user_id == 1,
            UserSubQuestionResponseDB.exercise_id == 1,
            UserSubQuestionResponseDB.response_text.like("Test%")
        ).delete(synchronize_session=False)
        db.commit()
        print("   ✅ Test data cleaned up\n")
        
        print("✨ All tests passed! Database supports both formats.")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        db.rollback()
        return False
        
    finally:
        db.close()

if __name__ == "__main__":
    success = test_sub_question_formats()
    exit(0 if success else 1)

