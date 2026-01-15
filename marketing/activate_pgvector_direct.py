#!/usr/bin/env python3
"""
Script pour activer pgvector directement via SQLAlchemy.
Pas besoin de Railway CLI - utilise juste ta DATABASE_URL.

Usage:
    python marketing/activate_pgvector_direct.py
"""

import os
import sys
from pathlib import Path
from sqlalchemy import create_engine, text

# Charge le .env depuis la racine du projet
try:
    from dotenv import load_dotenv
    # Cherche .env à la racine du projet (2 niveaux au-dessus de marketing/)
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
        print(f"📄 Fichier .env chargé: {env_path}")
    else:
        # Essaie aussi à la racine actuelle
        load_dotenv()
except ImportError:
    print("⚠️  python-dotenv non installé, utilisation des variables d'environnement système")


def activate_pgvector():
    """Active pgvector directement via la connexion DB."""
    
    # Récupère DATABASE_URL depuis .env ou environnement
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print("❌ DATABASE_URL non trouvée dans l'environnement")
        print("💡 Assure-toi d'avoir DATABASE_URL dans ton .env")
        print()
        # Affiche où on cherche le .env
        env_path = Path(__file__).parent.parent / ".env"
        print(f"💡 Cherché dans: {env_path}")
        if not env_path.exists():
            print(f"   ❌ Fichier .env non trouvé à cet emplacement")
        return False
    
    print("=" * 60)
    print("🚀 Activation de pgvector")
    print("=" * 60)
    print()
    print(f"🔗 Connexion à: {database_url.split('@')[1] if '@' in database_url else 'database'}...")
    print()
    
    try:
        # Crée l'engine SQLAlchemy avec timeout
        print("⏳ Connexion à la base de données...")
        engine = create_engine(
            database_url,
            connect_args={
                "connect_timeout": 10,  # Timeout de 10 secondes
                "options": "-c statement_timeout=30000"  # 30 secondes pour les requêtes
            },
            pool_pre_ping=True,  # Vérifie la connexion avant utilisation
            echo=False
        )
        
        print("✅ Connexion établie!")
        print()
        
        with engine.connect() as conn:
            # Vérifie si pgvector est déjà activé
            print("📋 Vérification de l'état actuel...")
            result = conn.execute(text(
                "SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';"
            ))
            existing = result.fetchone()
            
            if existing:
                print(f"✅ pgvector est déjà activé (version {existing[1]})")
                return True
            
            # Active pgvector
            print("📦 Activation de l'extension pgvector...")
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            conn.commit()
            
            # Vérifie que c'est activé
            result = conn.execute(text(
                "SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';"
            ))
            row = result.fetchone()
            
            if row:
                print(f"✅ pgvector activé avec succès!")
                print(f"   Version: {row[1]}")
                print()
                
                # Affiche les infos de l'extension
                print("📊 Informations de l'extension:")
                result = conn.execute(text("""
                    SELECT 
                        extname,
                        extversion,
                        n.nspname as schema
                    FROM pg_extension e
                    JOIN pg_namespace n ON e.extnamespace = n.oid
                    WHERE extname = 'vector';
                """))
                info = result.fetchone()
                if info:
                    print(f"   Nom: {info[0]}")
                    print(f"   Version: {info[1]}")
                    print(f"   Schema: {info[2]}")
                
                return True
            else:
                print("❌ pgvector n'a pas pu être activé")
                return False
                
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Erreur: {error_msg}")
        print()
        
        if "timeout" in error_msg.lower() or "timed out" in error_msg.lower():
            print("⏱️  Timeout de connexion détecté")
            print("💡 Solutions:")
            print("   1. Vérifie ta connexion internet")
            print("   2. La DB Railway peut être lente, réessaye")
            print("   3. Utilise l'interface web Railway (plus fiable)")
        elif "connection" in error_msg.lower() or "refused" in error_msg.lower():
            print("🔌 Problème de connexion détecté")
            print("💡 Vérifie que:")
            print("   1. DATABASE_URL est correcte dans ton .env")
            print("   2. La DB Railway est accessible")
            print("   3. Pas de firewall qui bloque")
        else:
            print("💡 Vérifie que:")
            print("   1. DATABASE_URL est correcte dans ton .env")
            print("   2. Tu as les permissions sur la base de données")
            print("   3. La connexion réseau fonctionne")
        
        print()
        print("💡 Alternative rapide: Utilise Railway Dashboard → Database → Query")
        return False


def main():
    success = activate_pgvector()
    
    print()
    print("=" * 60)
    if success:
        print("✅ Terminé avec succès!")
        print()
        print("💡 Tu peux maintenant utiliser le module marketing!")
    else:
        print("❌ Échec de l'activation")
        print()
        print("💡 Alternative: Active pgvector via Railway Dashboard:")
        print("   1. Va sur https://railway.app")
        print("   2. Database → Query")
        print("   3. Exécute: CREATE EXTENSION IF NOT EXISTS vector;")
        sys.exit(1)
    print("=" * 60)


if __name__ == "__main__":
    main()
