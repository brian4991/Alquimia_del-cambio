#!/usr/bin/env python3
"""
Script pour importer toutes les donnees vers Railway (PostgreSQL) - Version sans emojis
"""
import json
import os
import sys
sys.path.insert(0, 'backend')

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Module, Theme, ThemeCard, Exercise, UserResponseDB, UserSubQuestionResponseDB, UserProgress

def import_complete_data_to_railway():
    """Importer toutes les donnees vers Railway PostgreSQL"""
    
    # Verifier si on a la DATABASE_URL (Railway)
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print("ERROR: DATABASE_URL not found")
        return False
    
    # Verifier si le fichier d'export existe
    export_file = "complete_database_export.json"
    if not os.path.exists(export_file):
        print(f"ERROR: Export file not found: {export_file}")
        return False
    
    try:
        # Lire le fichier d'export
        with open(export_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Loading export from {data.get('export_date', 'unknown date')}")
        stats = data.get('stats', {})
        for key, value in stats.items():
            print(f"  {key}: {value}")
        
        # Se connecter a Railway PostgreSQL
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        try:
            # === UTILISATEURS ===
            print("\nImporting users...")
            users_imported = 0
            users_skipped = 0
            user_id_mapping = {}
            
            for user_data in data.get('users', []):
                existing_user = db.query(User).filter(User.email == user_data['email']).first()
                
                if existing_user:
                    print(f"  User {user_data['email']} exists, mapping ID")
                    user_id_mapping[user_data['id']] = existing_user.id
                    users_skipped += 1
                    continue
                
                new_user = User(
                    username=user_data['username'], email=user_data['email'],
                    password_hash=user_data['password_hash'], role=user_data['role'],
                    provider=user_data.get('provider'), provider_id=user_data.get('provider_id'),
                    is_active=user_data.get('is_active', True),
                    is_validated=user_data.get('is_validated', False),
                    validated_modules=user_data.get('validated_modules', '[]')
                )
                
                db.add(new_user)
                db.flush()
                user_id_mapping[user_data['id']] = new_user.id
                users_imported += 1
            
            print(f"Users: {users_imported} imported, {users_skipped} skipped")
            
            # === MODULES ===
            print("\nImporting modules...")
            modules_imported = 0
            modules_skipped = 0
            module_id_mapping = {}
            
            for module_data in data.get('modules', []):
                existing_module = db.query(Module).filter(
                    Module.title == module_data['title'],
                    Module.order_number == module_data['order_number']
                ).first()
                
                if existing_module:
                    print(f"  Module '{module_data['title']}' exists, mapping ID")
                    module_id_mapping[module_data['id']] = existing_module.id
                    modules_skipped += 1
                    continue
                
                new_module = Module(
                    title=module_data['title'], description=module_data['description'],
                    objective=module_data['objective'], belief_to_transform=module_data['belief_to_transform'],
                    expected_results=module_data['expected_results'], recommended_book=module_data['recommended_book'],
                    audio_file=module_data['audio_file'], order_number=module_data['order_number'],
                    is_active=module_data.get('is_active', True)
                )
                
                db.add(new_module)
                db.flush()
                module_id_mapping[module_data['id']] = new_module.id
                modules_imported += 1
            
            print(f"Modules: {modules_imported} imported, {modules_skipped} skipped")
            
            # === THEMES ===
            print("\nImporting themes...")
            themes_imported = 0
            themes_skipped = 0
            theme_id_mapping = {}
            
            for theme_data in data.get('themes', []):
                old_module_id = theme_data['module_id']
                if old_module_id not in module_id_mapping:
                    print(f"  WARNING: Module not found for theme '{theme_data['title']}'")
                    continue
                
                new_module_id = module_id_mapping[old_module_id]
                
                existing_theme = db.query(Theme).filter(
                    Theme.title == theme_data['title'],
                    Theme.module_id == new_module_id,
                    Theme.order_number == theme_data['order_number']
                ).first()
                
                if existing_theme:
                    theme_id_mapping[theme_data['id']] = existing_theme.id
                    themes_skipped += 1
                    continue
                
                new_theme = Theme(
                    title=theme_data['title'], content=theme_data['content'],
                    order_number=theme_data['order_number'], module_id=new_module_id,
                    theme_type=theme_data.get('theme_type', 'theme')
                )
                
                db.add(new_theme)
                db.flush()
                theme_id_mapping[theme_data['id']] = new_theme.id
                themes_imported += 1
            
            print(f"Themes: {themes_imported} imported, {themes_skipped} skipped")
            
            # === CARTES ===
            print("\nImporting cards...")
            cards_imported = 0
            cards_skipped = 0
            
            for card_data in data.get('theme_cards', []):
                old_theme_id = card_data['theme_id']
                if old_theme_id not in theme_id_mapping:
                    continue
                
                new_theme_id = theme_id_mapping[old_theme_id]
                
                existing_card = db.query(ThemeCard).filter(
                    ThemeCard.title == card_data['title'],
                    ThemeCard.theme_id == new_theme_id,
                    ThemeCard.order_number == card_data['order_number']
                ).first()
                
                if existing_card:
                    cards_skipped += 1
                    continue
                
                new_card = ThemeCard(
                    title=card_data['title'], content=card_data['content'],
                    card_type=card_data['card_type'], order_number=card_data['order_number'],
                    theme_id=new_theme_id, is_editable=card_data.get('is_editable', True),
                    exercise_instructions=card_data.get('exercise_instructions'),
                    exercise_questions=card_data.get('exercise_questions'),
                    exercise_sections=card_data.get('exercise_sections')
                )
                
                db.add(new_card)
                cards_imported += 1
            
            print(f"Cards: {cards_imported} imported, {cards_skipped} skipped")
            
            # === EXERCICES ===
            print("\nImporting exercises...")
            exercises_imported = 0
            exercises_skipped = 0
            exercise_id_mapping = {}
            
            for exercise_data in data.get('exercises', []):
                old_theme_id = exercise_data['theme_id']
                if old_theme_id not in theme_id_mapping:
                    print(f"  WARNING: Theme not found for exercise '{exercise_data['title']}'")
                    continue
                
                new_theme_id = theme_id_mapping[old_theme_id]
                
                existing_exercise = db.query(Exercise).filter(
                    Exercise.title == exercise_data['title'],
                    Exercise.theme_id == new_theme_id,
                    Exercise.order_number == exercise_data['order_number']
                ).first()
                
                if existing_exercise:
                    exercise_id_mapping[exercise_data['id']] = existing_exercise.id
                    exercises_skipped += 1
                    continue
                
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
                db.flush()
                exercise_id_mapping[exercise_data['id']] = new_exercise.id
                exercises_imported += 1
                print(f"  Exercise '{exercise_data['title']}' imported")
            
            print(f"Exercises: {exercises_imported} imported, {exercises_skipped} skipped")
            
            # === COMMIT FINAL ===
            db.commit()
            
            print(f"\nImport completed successfully!")
            print(f"Summary:")
            print(f"  Users: {users_imported} imported")
            print(f"  Modules: {modules_imported} imported")
            print(f"  Themes: {themes_imported} imported")
            print(f"  Cards: {cards_imported} imported")
            print(f"  Exercises: {exercises_imported} imported")
            
            return True
            
        except Exception as e:
            db.rollback()
            print(f"ERROR during import: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            db.close()
            
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import_complete_data_to_railway()

