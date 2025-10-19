#!/usr/bin/env python3
"""
Script pour importer UNIQUEMENT les exercices vers Railway
"""
import json
import os
import sys
sys.path.insert(0, 'backend')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Module, Theme, Exercise

def import_exercises_to_railway():
    """Importer les exercices vers Railway PostgreSQL"""
    
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print("ERROR: DATABASE_URL not found")
        return False
    
    export_file = "complete_database_export.json"
    if not os.path.exists(export_file):
        print(f"ERROR: Export file not found: {export_file}")
        return False
    
    try:
        with open(export_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Loading exercises from export...")
        print(f"Total exercises in export: {len(data.get('exercises', []))}")
        
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        try:
            # Build theme mapping (old_id -> new_id) from Railway DB
            print("\nMapping themes from Railway DB...")
            themes = db.query(Theme).all()
            theme_mapping = {}
            for theme in themes:
                # Try to find matching theme in export by title
                for theme_export in data.get('themes', []):
                    if theme.title == theme_export['title'] and theme.order_number == theme_export['order_number']:
                        theme_mapping[theme_export['id']] = theme.id
                        break
            
            print(f"Themes mapped: {len(theme_mapping)}")
            
            # Import exercises
            print("\nImporting exercises...")
            exercises_imported = 0
            exercises_skipped = 0
            
            for exercise_data in data.get('exercises', []):
                old_theme_id = exercise_data['theme_id']
                
                if old_theme_id not in theme_mapping:
                    print(f"  SKIP: Theme not found for exercise '{exercise_data['title']}'")
                    exercises_skipped += 1
                    continue
                
                new_theme_id = theme_mapping[old_theme_id]
                
                # Check if exercise exists
                existing_exercise = db.query(Exercise).filter(
                    Exercise.title == exercise_data['title'],
                    Exercise.theme_id == new_theme_id
                ).first()
                
                if existing_exercise:
                    print(f"  EXISTS: '{exercise_data['title']}'")
                    exercises_skipped += 1
                    continue
                
                # Create new exercise
                new_exercise = Exercise(
                    title=exercise_data['title'],
                    parent_title=exercise_data.get('parent_title'),
                    instructions=exercise_data.get('instructions'),
                    sub_questions=exercise_data.get('sub_questions', '[]'),
                    order_number=exercise_data['order_number'],
                    theme_id=new_theme_id,
                    exercise_instructions=exercise_data.get('exercise_instructions'),
                    exercise_questions=exercise_data.get('exercise_questions'),
                    exercise_sections=exercise_data.get('exercise_sections')
                )
                
                db.add(new_exercise)
                exercises_imported += 1
                print(f"  IMPORT: '{exercise_data['title']}' (theme_id: {new_theme_id})")
            
            # Commit
            db.commit()
            
            print(f"\nImport completed!")
            print(f"Exercises imported: {exercises_imported}")
            print(f"Exercises skipped: {exercises_skipped}")
            
            # Verify
            total_exercises = db.query(Exercise).count()
            print(f"\nTotal exercises now in Railway DB: {total_exercises}")
            
            return True
            
        except Exception as e:
            db.rollback()
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            db.close()
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    import_exercises_to_railway()

