from database import SessionLocal
from models import Module, Theme, Exercise, ThemeCard
from init_module2 import init_module2

def recreate_module2():
    db = SessionLocal()
    try:
        # Find and delete existing Module 2
        existing_module2 = db.query(Module).filter(Module.order_number == 2).first()
        if existing_module2:
            print(f"Deleting existing Module 2: {existing_module2.title}")
            # Delete associated themes, cards, and exercises (cascade should handle this)
            db.delete(existing_module2)
            db.commit()
            print("Module 2 deleted successfully")
        
        # Create the new Module 2
        print("Creating new Module 2...")
        init_module2(db)
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    recreate_module2() 