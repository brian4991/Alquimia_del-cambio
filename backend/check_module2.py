from database import SessionLocal
from models import Module, Theme, Exercise, ThemeCard

def check_module2():
    db = SessionLocal()
    try:
        # Check all modules
        modules = db.query(Module).all()
        print("Modules in database:")
        for m in modules:
            print(f"  - {m.order_number}: {m.title}")
        
        # Check if Module 2 exists
        module2 = db.query(Module).filter(Module.order_number == 2).first()
        if module2:
            print(f"\nModule 2 found: {module2.title}")
            
            # Check themes
            themes = db.query(Theme).filter(Theme.module_id == module2.id).all()
            print(f"Themes: {len(themes)}")
            for t in themes:
                print(f"  - {t.order_number}: {t.title}")
            
            # Check cards
            cards_count = db.query(ThemeCard).join(Theme).filter(Theme.module_id == module2.id).count()
            print(f"Cards: {cards_count}")
            
            # Check exercises
            exercises_count = db.query(Exercise).join(Theme).filter(Theme.module_id == module2.id).count()
            print(f"Exercises: {exercises_count}")
            
            if cards_count == 0 and exercises_count == 0:
                print("Module 2 exists but has no content!")
                return False
            return True
        else:
            print("\nModule 2 NOT found")
            return False
    finally:
        db.close()

if __name__ == "__main__":
    check_module2() 