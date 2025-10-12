"""
Script pour synchroniser la base de données locale vers Railway
- Exporte toutes les données de SQLite local
- Supprime toutes les données de Railway PostgreSQL
- Importe les nouvelles données
"""
import json
import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from models import Base, Module, Theme, ThemeCard, User

def export_local_data():
    """Exporter toutes les données de la base SQLite locale"""
    print("📦 Exportation des données locales...")
    
    # Connect to local SQLite
    engine = create_engine("sqlite:///./backend/app.db", connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        data = {
            "users": [],
            "modules": [],
            "themes": [],
            "cards": []
        }
        
        # Export users
        users = db.query(User).all()
        for user in users:
            data["users"].append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password_hash": user.password_hash,
                "role": user.role,
                "provider": user.provider,
                "provider_id": user.provider_id,
                "is_active": user.is_active
            })
        print(f"   ✓ {len(data['users'])} utilisateurs")
        
        # Export modules
        modules = db.query(Module).order_by(Module.order_number).all()
        for module in modules:
            data["modules"].append({
                "id": module.id,
                "title": module.title,
                "description": module.description,
                "objective": module.objective,
                "belief_to_transform": module.belief_to_transform,
                "expected_results": module.expected_results,
                "recommended_book": module.recommended_book,
                "audio_file": module.audio_file,
                "order_number": module.order_number,
                "is_active": module.is_active
            })
        print(f"   ✓ {len(data['modules'])} modules")
        
        # Export themes
        themes = db.query(Theme).order_by(Theme.module_id, Theme.order_number).all()
        for theme in themes:
            data["themes"].append({
                "id": theme.id,
                "title": theme.title,
                "content": theme.content,
                "module_id": theme.module_id,
                "order_number": theme.order_number,
                "theme_type": theme.theme_type
            })
        print(f"   ✓ {len(data['themes'])} thèmes")
        
        # Export cards
        cards = db.query(ThemeCard).order_by(ThemeCard.theme_id, ThemeCard.order_number).all()
        for card in cards:
            data["cards"].append({
                "id": card.id,
                "theme_id": card.theme_id,
                "title": card.title,
                "content": card.content,
                "card_type": card.card_type,
                "order_number": card.order_number,
                "exercise_instructions": card.exercise_instructions,
                "exercise_questions": card.exercise_questions
            })
        print(f"   ✓ {len(data['cards'])} cartes")
        
        return data
    finally:
        db.close()

def clear_railway_database(db):
    """Supprimer toutes les données de Railway"""
    print("\n🗑️  Suppression des données Railway...")
    
    try:
        # Delete in order to respect foreign keys
        # First, delete all data from tables that might have foreign keys
        from sqlalchemy import text
        
        # Disable foreign key checks temporarily for easier deletion
        db.execute(text("SET session_replication_role = 'replica';"))
        
        # Delete from all tables
        deleted_cards = db.query(ThemeCard).delete()
        print(f"   ✓ {deleted_cards} cartes supprimées")
        
        # Try to delete from exercises table if it exists
        try:
            db.execute(text("DELETE FROM exercises"))
            print(f"   ✓ Exercices supprimés")
        except:
            pass
        
        # Try to delete from user_responses if it exists
        try:
            db.execute(text("DELETE FROM user_responses"))
            print(f"   ✓ Réponses utilisateurs supprimées")
        except:
            pass
        
        deleted_themes = db.query(Theme).delete()
        print(f"   ✓ {deleted_themes} thèmes supprimés")
        
        deleted_modules = db.query(Module).delete()
        print(f"   ✓ {deleted_modules} modules supprimés")
        
        # Keep admin user but delete others
        deleted_users = db.query(User).filter(User.role != 'admin').delete()
        print(f"   ✓ {deleted_users} utilisateurs non-admin supprimés")
        
        # Re-enable foreign key checks
        db.execute(text("SET session_replication_role = 'origin';"))
        
        db.commit()
        print("   ✓ Toutes les données supprimées")
        return True
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        db.rollback()
        return False

def import_to_railway(data):
    """Importer les données vers Railway PostgreSQL"""
    
    # Get Railway database URL
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print("❌ DATABASE_URL non trouvée.")
        print("💡 Exécutez: railway login && railway link")
        print("💡 Puis: railway run python sync_db_to_railway.py")
        return False
    
    # Convert postgres:// to postgresql:// if needed
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    print(f"\n🔗 Connexion à Railway PostgreSQL...")
    print(f"   URL: {DATABASE_URL[:50]}...")
    
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        print("   ✓ Tables créées/vérifiées")
        
        # Add theme_type column if it doesn't exist
        try:
            from sqlalchemy import text
            db.execute(text("ALTER TABLE themes ADD COLUMN IF NOT EXISTS theme_type VARCHAR(50) DEFAULT 'theme'"))
            db.commit()
            print("   ✓ Colonne theme_type ajoutée/vérifiée")
        except Exception as e:
            print(f"   Note: {e}")
        
        # Clear existing data
        if not clear_railway_database(db):
            return False
        
        # Import users
        print("\n📥 Import des données vers Railway...")
        for user_data in data["users"]:
            user = User(**user_data)
            db.merge(user)
        db.commit()
        print(f"   ✓ {len(data['users'])} utilisateurs importés")
        
        # Import modules
        for module_data in data["modules"]:
            module = Module(**module_data)
            db.merge(module)
        db.commit()
        print(f"   ✓ {len(data['modules'])} modules importés")
        
        # Import themes
        for theme_data in data["themes"]:
            theme = Theme(**theme_data)
            db.merge(theme)
        db.commit()
        print(f"   ✓ {len(data['themes'])} thèmes importés")
        
        # Import cards
        for card_data in data["cards"]:
            card = ThemeCard(**card_data)
            db.merge(card)
        db.commit()
        print(f"   ✓ {len(data['cards'])} cartes importées")
        
        # Verify import
        print("\n✅ Vérification de l'import...")
        modules = db.query(Module).order_by(Module.order_number).all()
        for module in modules:
            theme_count = db.query(Theme).filter(Theme.module_id == module.id).count()
            card_count = db.query(ThemeCard).join(Theme).filter(Theme.module_id == module.id).count()
            print(f"   {module.order_number}. {module.title}")
            print(f"      → {theme_count} thèmes, {card_count} cartes")
        
        db.close()
        print("\n🎉 Synchronisation réussie!")
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'import: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("🚂 Synchronisation Base de Données Locale → Railway")
    print("=" * 60)
    
    # Export local data
    data = export_local_data()
    
    # Import to Railway
    success = import_to_railway(data)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ La base de données Railway est maintenant synchronisée!")
        print("=" * 60)
    else:
        print("\n❌ La synchronisation a échoué")
        sys.exit(1)

if __name__ == "__main__":
    main()

