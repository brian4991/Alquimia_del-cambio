#!/usr/bin/env python3
"""
Script pour vérifier et corriger le système de validation des modules
"""
import sqlite3
import json

def check_validation_system():
    """Vérifier l'état de la validation des modules"""
    
    print("🔍 Vérification du système de validation...")
    
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        
        # Vérifier la structure de la table users
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        
        print("\n📋 Structure de la table users:")
        for col in columns:
            print(f"   - {col[1]} ({col[2]})")
        
        # Vérifier les utilisateurs et leurs modules validés
        cursor.execute("SELECT id, username, validated_modules FROM users")
        users = cursor.fetchall()
        
        print(f"\n👥 Utilisateurs ({len(users)} trouvés):")
        for user in users:
            validated = user[2] if user[2] else "[]"
            print(f"   - ID: {user[0]}, Username: {user[1]}")
            print(f"     Modules validés: {validated}")
        
        # Vérifier les modules disponibles
        cursor.execute("SELECT id, title, order_number FROM modules WHERE is_active = 1 ORDER BY order_number")
        modules = cursor.fetchall()
        
        print(f"\n📚 Modules disponibles ({len(modules)} trouvés):")
        for module in modules:
            print(f"   - ID: {module[0]}, Ordre: {module[2]}, Titre: {module[1]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_validation(user_id=1, module_id=2):
    """Tester la validation d'un module pour un utilisateur"""
    
    print(f"\n🧪 Test de validation - User {user_id}, Module {module_id}")
    
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        
        # Récupérer l'utilisateur
        cursor.execute("SELECT id, username, validated_modules FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
        if not user:
            print(f"❌ Utilisateur {user_id} non trouvé")
            return False
        
        print(f"👤 Utilisateur: {user[1]}")
        
        # Parser les modules validés actuels
        current_validated = []
        if user[2]:
            try:
                if isinstance(user[2], str):
                    current_validated = json.loads(user[2])
                else:
                    current_validated = user[2]
            except:
                current_validated = []
        
        print(f"📋 Modules actuellement validés: {current_validated}")
        
        # Ajouter le module s'il n'est pas déjà validé
        if module_id not in current_validated:
            current_validated.append(module_id)
            
            # Sauvegarder en JSON string
            validated_json = json.dumps(current_validated)
            cursor.execute(
                "UPDATE users SET validated_modules = ? WHERE id = ?", 
                (validated_json, user_id)
            )
            conn.commit()
            
            print(f"✅ Module {module_id} ajouté aux validations")
            print(f"📋 Nouveaux modules validés: {current_validated}")
        else:
            print(f"ℹ️ Module {module_id} déjà validé")
        
        # Vérifier la sauvegarde
        cursor.execute("SELECT validated_modules FROM users WHERE id = ?", (user_id,))
        saved = cursor.fetchone()[0]
        print(f"💾 Sauvegardé en base: {saved}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Diagnostic du système de validation des modules\n")
    
    # Vérifier l'état actuel
    if check_validation_system():
        print("\n" + "="*50)
        
        # Tester la validation
        test_validation()
        
        print("\n" + "="*50)
        print("✅ Diagnostic terminé !")
        print("\n💡 Pour corriger les problèmes:")
        print("   1. Vérifiez que le serveur backend fonctionne")
        print("   2. Testez les endpoints de validation manuellement")
        print("   3. Vérifiez les logs du serveur pour les erreurs")
