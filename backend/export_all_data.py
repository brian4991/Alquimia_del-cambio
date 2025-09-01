#!/usr/bin/env python3
"""
Script pour exporter toutes les données de la base locale SQLite
(utilisateurs, modules, thèmes, cartes, exercices, réponses, progrès)
"""
import sqlite3
import json
import os
from datetime import datetime

def export_all_data():
    """Exporter toutes les données de SQLite vers un fichier JSON"""
    
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    
    if not os.path.exists(db_path):
        print(f"❌ Base de données locale non trouvée à {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        export_data = {
            "export_date": str(datetime.now()),
            "export_type": "complete_database"
        }
        
        # === UTILISATEURS ===
        print("📥 Export des utilisateurs...")
        cursor.execute("""
            SELECT id, username, email, password_hash, role, provider, provider_id, 
                   is_active, is_validated, validated_modules, created_at
            FROM users
        """)
        users = cursor.fetchall()
        
        users_data = []
        for user in users:
            user_dict = {
                "id": user[0], "username": user[1], "email": user[2], "password_hash": user[3],
                "role": user[4], "provider": user[5], "provider_id": user[6],
                "is_active": bool(user[7]) if user[7] is not None else True,
                "is_validated": bool(user[8]) if user[8] is not None else False,
                "validated_modules": user[9] if user[9] else "[]",
                "created_at": user[10]
            }
            users_data.append(user_dict)
        
        export_data["users"] = users_data
        print(f"   ✅ {len(users_data)} utilisateurs exportés")
        
        # === MODULES ===
        print("📥 Export des modules...")
        cursor.execute("""
            SELECT id, title, description, objective, belief_to_transform, 
                   expected_results, recommended_book, audio_file, order_number, is_active
            FROM modules ORDER BY order_number
        """)
        modules = cursor.fetchall()
        
        modules_data = []
        for module in modules:
            module_dict = {
                "id": module[0], "title": module[1], "description": module[2],
                "objective": module[3], "belief_to_transform": module[4],
                "expected_results": module[5], "recommended_book": module[6],
                "audio_file": module[7], "order_number": module[8],
                "is_active": bool(module[9]) if module[9] is not None else True
            }
            modules_data.append(module_dict)
        
        export_data["modules"] = modules_data
        print(f"   ✅ {len(modules_data)} modules exportés")
        
        # === THEMES ===
        print("📥 Export des thèmes...")
        cursor.execute("""
            SELECT id, title, content, order_number, module_id
            FROM themes ORDER BY module_id, order_number
        """)
        themes = cursor.fetchall()
        
        themes_data = []
        for theme in themes:
            theme_dict = {
                "id": theme[0], "title": theme[1], "content": theme[2],
                "order_number": theme[3], "module_id": theme[4]
            }
            themes_data.append(theme_dict)
        
        export_data["themes"] = themes_data
        print(f"   ✅ {len(themes_data)} thèmes exportés")
        
        # === THEME CARDS ===
        print("📥 Export des cartes...")
        cursor.execute("""
            SELECT id, title, content, card_type, order_number, theme_id, 
                   is_editable, created_at, updated_at
            FROM theme_cards ORDER BY theme_id, order_number
        """)
        cards = cursor.fetchall()
        
        cards_data = []
        for card in cards:
            card_dict = {
                "id": card[0], "title": card[1], "content": card[2],
                "card_type": card[3], "order_number": card[4], "theme_id": card[5],
                "is_editable": bool(card[6]) if card[6] is not None else True,
                "created_at": card[7], "updated_at": card[8]
            }
            cards_data.append(card_dict)
        
        export_data["theme_cards"] = cards_data
        print(f"   ✅ {len(cards_data)} cartes exportées")
        
        # === EXERCISES ===
        print("📥 Export des exercices...")
        cursor.execute("""
            SELECT id, title, instructions, sub_questions, order_number, theme_id
            FROM exercises ORDER BY theme_id, order_number
        """)
        exercises = cursor.fetchall()
        
        exercises_data = []
        for exercise in exercises:
            exercise_dict = {
                "id": exercise[0], "title": exercise[1], "instructions": exercise[2],
                "sub_questions": exercise[3] if exercise[3] else "[]",
                "order_number": exercise[4], "theme_id": exercise[5]
            }
            exercises_data.append(exercise_dict)
        
        export_data["exercises"] = exercises_data
        print(f"   ✅ {len(exercises_data)} exercices exportés")
        
        # === RÉPONSES UTILISATEURS ===
        print("📥 Export des réponses...")
        cursor.execute("""
            SELECT user_id, exercise_id, response_text, submitted_at
            FROM user_responses
        """)
        responses = cursor.fetchall()
        
        responses_data = []
        for response in responses:
            resp_dict = {
                "user_id": response[0], "exercise_id": response[1],
                "response_text": response[2], "submitted_at": response[3]
            }
            responses_data.append(resp_dict)
        
        export_data["user_responses"] = responses_data
        print(f"   ✅ {len(responses_data)} réponses exportées")
        
        # === SOUS-RÉPONSES ===
        print("📥 Export des sous-réponses...")
        cursor.execute("""
            SELECT user_id, exercise_id, sub_question_index, response_text, submitted_at, updated_at
            FROM user_sub_question_responses
        """)
        sub_responses = cursor.fetchall()
        
        sub_responses_data = []
        for sub_resp in sub_responses:
            sub_resp_dict = {
                "user_id": sub_resp[0], "exercise_id": sub_resp[1],
                "sub_question_index": sub_resp[2], "response_text": sub_resp[3],
                "submitted_at": sub_resp[4], "updated_at": sub_resp[5]
            }
            sub_responses_data.append(sub_resp_dict)
        
        export_data["user_sub_question_responses"] = sub_responses_data
        print(f"   ✅ {len(sub_responses_data)} sous-réponses exportées")
        
        # === PROGRÈS ===
        print("📥 Export du progrès...")
        cursor.execute("""
            SELECT user_id, module_id, theme_id, exercise_id, completed, completed_at
            FROM user_progress
        """)
        progress = cursor.fetchall()
        
        progress_data = []
        for prog in progress:
            prog_dict = {
                "user_id": prog[0], "module_id": prog[1], "theme_id": prog[2],
                "exercise_id": prog[3], "completed": bool(prog[4]) if prog[4] is not None else False,
                "completed_at": prog[5]
            }
            progress_data.append(prog_dict)
        
        export_data["user_progress"] = progress_data
        print(f"   ✅ {len(progress_data)} entrées de progrès exportées")
        
        # === STATISTIQUES ===
        export_data["stats"] = {
            "total_users": len(users_data),
            "total_modules": len(modules_data),
            "total_themes": len(themes_data),
            "total_cards": len(cards_data),
            "total_exercises": len(exercises_data),
            "total_responses": len(responses_data),
            "total_sub_responses": len(sub_responses_data),
            "total_progress": len(progress_data)
        }
        
        # === SAUVEGARDER ===
        export_file = "complete_database_export.json"
        with open(export_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=True)
        
        print(f"\n🎉 Export complet réussi!")
        print(f"📁 Fichier: {export_file}")
        print(f"📊 Résumé:")
        print(f"   👥 {len(users_data)} utilisateurs")
        print(f"   📚 {len(modules_data)} modules")
        print(f"   🎯 {len(themes_data)} thèmes")
        print(f"   🃏 {len(cards_data)} cartes")
        print(f"   ✏️  {len(exercises_data)} exercices")
        print(f"   💬 {len(responses_data)} réponses")
        print(f"   🔢 {len(sub_responses_data)} sous-réponses")
        print(f"   📈 {len(progress_data)} entrées de progrès")
        
        # Afficher les modules trouvés
        print(f"\n📚 Modules trouvés:")
        for module in modules_data:
            print(f"   {module['order_number']}. {module['title']}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'export: {e}")
        return False

if __name__ == "__main__":
    export_all_data()
