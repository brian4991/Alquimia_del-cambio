"""
Script d'initialisation du module Marketing.

À exécuter une fois après l'installation pour :
1. Créer les tables de la base de données
2. Activer l'extension pgvector
3. Indexer le contenu initial
4. Générer le profil de voix
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository
from marketing.services.memory.vector_store import get_vector_store
from marketing.services.memory.content_indexer import get_content_indexer
from marketing.config import get_database_config


async def init_marketing():
    """Initialize marketing module."""
    print("🚀 Initialisation du module Marketing...\n")
    
    # 1. Initialize database tables
    print("1️⃣  Création des tables de la base de données...")
    try:
        repository = get_marketing_repository()
        await repository.initialize_tables()
        print("   ✅ Tables créées avec succès\n")
    except Exception as e:
        print(f"   ❌ Erreur: {e}\n")
        return False
    
    # 2. Initialize vector store
    print("2️⃣  Initialisation du vector store (pgvector)...")
    try:
        vector_store = get_vector_store()
        await vector_store.initialize()
        print("   ✅ Vector store initialisé\n")
    except Exception as e:
        print(f"   ⚠️  Avertissement: {e}")
        print("   💡 Assurez-vous que l'extension pgvector est activée:\n")
        print("      CREATE EXTENSION IF NOT EXISTS vector;\n")
    
    # 3. Index content
    print("3️⃣  Indexation du contenu (transcripts + programme)...")
    try:
        indexer = get_content_indexer()
        stats = await indexer.index_all()
        print(f"   ✅ Contenu indexé:")
        print(f"      - Transcripts: {stats.get('transcripts', {}).get('indexed', 0)}")
        print(f"      - Programme: {stats.get('program', {}).get('indexed', 0)}")
        print(f"      - Total: {stats.get('total', {}).get('total_documents', 0)}\n")
    except Exception as e:
        print(f"   ⚠️  Avertissement: {e}")
        print("   💡 Vous pourrez indexer le contenu plus tard via l'API\n")
    
    # 4. Generate voice profile
    print("4️⃣  Génération du profil de voix...")
    print("   💡 Pour générer le profil de voix, utilisez l'API:")
    print("      POST /api/marketing/voice/analyze\n")
    
    print("✨ Initialisation terminée!")
    print("\n📝 Prochaines étapes:")
    print("   1. Vérifiez vos variables d'environnement (voir MARKETING_ENV_VARIABLES.md)")
    print("   2. Testez l'API: GET /api/marketing/health")
    print("   3. Lancez votre première réunion via l'interface admin")
    
    return True


if __name__ == "__main__":
    try:
        success = asyncio.run(init_marketing())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erreur fatale: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
