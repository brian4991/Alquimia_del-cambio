from database import SessionLocal
from models import Module, Theme, Exercise, ThemeCard

def check_module3():
    db = SessionLocal()
    try:
        # Check Module 3
        module3 = db.query(Module).filter(Module.order_number == 3).first()
        if module3:
            print(f"✅ Module 3: {module3.title}")
            print(f"   Description: {module3.description[:100]}...")
            print(f"   Objective: {module3.objective[:100]}...")
            
            # Check themes
            themes = db.query(Theme).filter(Theme.module_id == module3.id).all()
            print(f"\n📚 Themes ({len(themes)}):")
            for t in themes:
                print(f"   {t.order_number}. {t.title}")
                
                # Count cards per theme
                cards_count = db.query(ThemeCard).filter(ThemeCard.theme_id == t.id).count()
                exercises_count = db.query(Exercise).filter(Exercise.theme_id == t.id).count()
                print(f"      └─ Cards: {cards_count}, Exercises: {exercises_count}")
            
            # Total counts
            total_cards = db.query(ThemeCard).join(Theme).filter(Theme.module_id == module3.id).count()
            total_exercises = db.query(Exercise).join(Theme).filter(Theme.module_id == module3.id).count()
            
            print(f"\n📊 Totals:")
            print(f"   Total Cards: {total_cards}")
            print(f"   Total Exercises: {total_exercises}")
            
        else:
            print("❌ Module 3 not found")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_module3() 