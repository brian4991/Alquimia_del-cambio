#!/usr/bin/env python3
"""
Script pour importer toutes les données exportées vers Railway (PostgreSQL)
"""
import json
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Module, Theme, ThemeCard, Exercise, UserResponseDB, UserSubQuestionResponseDB, UserProgress

def import_complete_data_to_railway():
    """Importer toutes les données vers Railway PostgreSQL"""
    
    # Vérifier si on a la DATABASE_URL (Railway)
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print("❌ DATABASE_URL non trouvée. Assurez-vous d'être connecté à Railway.")
        print("💡 Utilisez: railway login && railway link")
        return False
    
    # Vérifier si le fichier d'export existe
    export_file = "complete_database_export.json"
    if not os.path.exists(export_file):
        print(f"❌ Fichier d'export non trouvé: {export_file}")
        print("💡 Exécutez d'abord: python export_all_data.py")
        return False
    
    try:
        # Lire le fichier d'export
        with open(export_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"📁 Chargement de l'export du {data.get('export_date', 'date inconnue')}")
        print(f"📊 Données à importer:")
        stats = data.get('stats', {})
        for key, value in stats.items():
            print(f"   {key.replace('total_', '').replace('_', ' ').title()}: {value}")
        
        # Se connecter à Railway PostgreSQL
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        try:
            # === UTILISATEURS ===
            print("\n🔄 Import des utilisateurs...")
            users_imported = 0
            users_skipped = 0
            user_id_mapping = {}  # ancien_id -> nouveau_id
            
            for user_data in data.get('users', []):
                existing_user = db.query(User).filter(User.email == user_data['email']).first()
                
                if existing_user:
                    print(f"⚠️  Utilisateur {user_data['email']} existe déjà, mapping ID")
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
                db.flush()  # Pour obtenir l'ID
                user_id_mapping[user_data['id']] = new_user.id
                users_imported += 1
                print(f"✅ Utilisateur {user_data['email']} ajouté (ID: {user_data['id']} -> {new_user.id})")
            
            print(f"💾 {users_imported} utilisateurs importés, {users_skipped} ignorés")
            
            # === MODULES ===
            print("\n🔄 Import des modules...")
            modules_imported = 0
            modules_skipped = 0
            module_id_mapping = {}
            
            for module_data in data.get('modules', []):
                # Vérifier si le module existe déjà (par titre et ordre)
                existing_module = db.query(Module).filter(
                    Module.title == module_data['title'],
                    Module.order_number == module_data['order_number']
                ).first()
                
                if existing_module:
                    print(f"⚠️  Module '{module_data['title']}' existe déjà, mapping ID")
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
                print(f"✅ Module '{module_data['title']}' ajouté (ID: {module_data['id']} -> {new_module.id})")
            
            print(f"💾 {modules_imported} modules importés, {modules_skipped} ignorés")
            
            # === THEMES ===
            print("\n🔄 Import des thèmes...")
            themes_imported = 0
            themes_skipped = 0
            theme_id_mapping = {}
            
            for theme_data in data.get('themes', []):
                old_module_id = theme_data['module_id']
                if old_module_id not in module_id_mapping:
                    print(f"⚠️  Module parent non trouvé pour thème '{theme_data['title']}'")
                    continue
                
                new_module_id = module_id_mapping[old_module_id]
                
                existing_theme = db.query(Theme).filter(
                    Theme.title == theme_data['title'],
                    Theme.module_id == new_module_id,
                    Theme.order_number == theme_data['order_number']
                ).first()
                
                if existing_theme:
                    print(f"⚠️  Thème '{theme_data['title']}' existe déjà, mapping ID")
                    theme_id_mapping[theme_data['id']] = existing_theme.id
                    themes_skipped += 1
                    continue
                
                new_theme = Theme(
                    title=theme_data['title'], content=theme_data['content'],
                    order_number=theme_data['order_number'], module_id=new_module_id
                )
                
                db.add(new_theme)
                db.flush()
                theme_id_mapping[theme_data['id']] = new_theme.id
                themes_imported += 1
                print(f"✅ Thème '{theme_data['title']}' ajouté (ID: {theme_data['id']} -> {new_theme.id})")
            
            print(f"💾 {themes_imported} thèmes importés, {themes_skipped} ignorés")
            
            # === CARTES ===
            print("\n🔄 Import des cartes...")
            cards_imported = 0
            cards_skipped = 0
            
            for card_data in data.get('theme_cards', []):
                old_theme_id = card_data['theme_id']
                if old_theme_id not in theme_id_mapping:
                    print(f"⚠️  Thème parent non trouvé pour carte '{card_data['title']}'")
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
                    theme_id=new_theme_id, is_editable=card_data.get('is_editable', True)
                )
                
                db.add(new_card)
                cards_imported += 1
            
            print(f"💾 {cards_imported} cartes importées, {cards_skipped} ignorées")
            
            # === EXERCICES ===
            print("\n🔄 Import des exercices...")
            exercises_imported = 0
            exercises_skipped = 0
            exercise_id_mapping = {}
            
            for exercise_data in data.get('exercises', []):
                old_theme_id = exercise_data['theme_id']
                if old_theme_id not in theme_id_mapping:
                    print(f"⚠️  Thème parent non trouvé pour exercice '{exercise_data['title']}'")
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
                    title=exercise_data['title'], instructions=exercise_data['instructions'],
                    sub_questions=exercise_data.get('sub_questions', '[]'),
                    order_number=exercise_data['order_number'], theme_id=new_theme_id
                )
                
                db.add(new_exercise)
                db.flush()
                exercise_id_mapping[exercise_data['id']] = new_exercise.id
                exercises_imported += 1
            
            print(f"💾 {exercises_imported} exercices importés, {exercises_skipped} ignorés")
            
            # === RÉPONSES ET PROGRÈS ===
            print("\n🔄 Import des réponses et du progrès...")
            
            # Réponses principales
            responses_imported = 0
            for resp_data in data.get('user_responses', []):
                if (resp_data['user_id'] in user_id_mapping and 
                    resp_data['exercise_id'] in exercise_id_mapping):
                    
                    new_response = UserResponseDB(
                        user_id=user_id_mapping[resp_data['user_id']],
                        exercise_id=exercise_id_mapping[resp_data['exercise_id']],
                        response_text=resp_data['response_text']
                    )
                    db.add(new_response)
                    responses_imported += 1
            
            # Sous-réponses
            sub_responses_imported = 0
            for sub_resp_data in data.get('user_sub_question_responses', []):
                if (sub_resp_data['user_id'] in user_id_mapping and 
                    sub_resp_data['exercise_id'] in exercise_id_mapping):
                    
                    new_sub_response = UserSubQuestionResponseDB(
                        user_id=user_id_mapping[sub_resp_data['user_id']],
                        exercise_id=exercise_id_mapping[sub_resp_data['exercise_id']],
                        sub_question_index=sub_resp_data['sub_question_index'],
                        response_text=sub_resp_data['response_text']
                    )
                    db.add(new_sub_response)
                    sub_responses_imported += 1
            
            # Progrès
            progress_imported = 0
            for prog_data in data.get('user_progress', []):
                if (prog_data['user_id'] in user_id_mapping and 
                    prog_data['module_id'] in module_id_mapping and
                    prog_data['theme_id'] in theme_id_mapping and
                    prog_data['exercise_id'] in exercise_id_mapping):
                    
                    new_progress = UserProgress(
                        user_id=user_id_mapping[prog_data['user_id']],
                        module_id=module_id_mapping[prog_data['module_id']],
                        theme_id=theme_id_mapping[prog_data['theme_id']],
                        exercise_id=exercise_id_mapping[prog_data['exercise_id']],
                        completed=prog_data['completed']
                    )
                    db.add(new_progress)
                    progress_imported += 1
            
            print(f"💾 {responses_imported} réponses, {sub_responses_imported} sous-réponses, {progress_imported} progrès importés")
            
            # === COMMIT FINAL ===
            db.commit()
            
            print(f"\n🎉 Import complet terminé avec succès!")
            print(f"📊 Résumé final:")
            print(f"   👥 Utilisateurs: {users_imported} importés, {users_skipped} ignorés")
            print(f"   📚 Modules: {modules_imported} importés, {modules_skipped} ignorés")
            print(f"   🎯 Thèmes: {themes_imported} importés, {themes_skipped} ignorés")
            print(f"   🃏 Cartes: {cards_imported} importées, {cards_skipped} ignorées")
            print(f"   ✏️  Exercices: {exercises_imported} importés, {exercises_skipped} ignorés")
            print(f"   💬 Réponses: {responses_imported} importées")
            print(f"   📈 Progrès: {progress_imported} importés")
            
            # Vérifier les modules dans Railway
            print(f"\n📚 Modules maintenant dans Railway:")
            railway_modules = db.query(Module).order_by(Module.order_number).all()
            for module in railway_modules:
                theme_count = db.query(Theme).filter(Theme.module_id == module.id).count()
                print(f"   {module.order_number}. {module.title} ({theme_count} thèmes)")
            
            return True
            
        except Exception as e:
            db.rollback()
            print(f"❌ Erreur lors de l'import: {e}")
            return False
        finally:
            db.close()
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    import_complete_data_to_railway()
