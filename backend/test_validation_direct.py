#!/usr/bin/env python3
"""
Test direct de la validation des modules
"""
import sqlite3
import json
from database import get_db
from models import User, Module
from sqlalchemy.orm import Session

def test_direct_validation():
    """Test direct de validation en base"""
    
    print("🧪 Test direct de validation des modules")
    print("="*50)
    
    # Test avec SQLAlchemy (comme dans l'API)
    db = next(get_db())
    
    try:
        # Récupérer l'utilisateur 1
        user = db.query(User).filter(User.id == 1).first()
        if not user:
            print("❌ Utilisateur 1 non trouvé")
            return
        
        print(f"👤 Utilisateur: {user.username}")
        print(f"📋 Modules validés actuels: {user.validated_modules}")
        
        # Parser les modules validés actuels
        validated_modules = []
        if user.validated_modules:
            try:
                if isinstance(user.validated_modules, str):
                    validated_modules = json.loads(user.validated_modules) if user.validated_modules.strip() else []
                elif isinstance(user.validated_modules, list):
                    validated_modules = user.validated_modules
            except (json.JSONDecodeError, AttributeError):
                validated_modules = []
        
        print(f"📋 Modules parsés: {validated_modules}")
        
        # Ajouter le module 3 s'il n'est pas déjà validé
        module_id = 3
        if module_id not in validated_modules:
            validated_modules.append(module_id)
            
            # Sauvegarder comme string JSON
            user.validated_modules = json.dumps(validated_modules)
            db.commit()
            
            print(f"✅ Module {module_id} ajouté")
            print(f"📋 Nouveaux modules validés: {validated_modules}")
            print(f"💾 Sauvegardé en base: {user.validated_modules}")
        else:
            print(f"ℹ️ Module {module_id} déjà validé")
        
        # Vérifier la sauvegarde
        db.refresh(user)
        print(f"🔍 Vérification après refresh: {user.validated_modules}")
        
        # Test avec SQLite direct
        print("\n" + "="*30)
        print("🔍 Vérification SQLite directe:")
        
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT validated_modules FROM users WHERE id = 1")
        result = cursor.fetchone()
        print(f"💾 En base SQLite: {result[0] if result else 'None'}")
        conn.close()
        
    finally:
        db.close()

if __name__ == "__main__":
    test_direct_validation()
    print("\n✅ Test terminé !")
