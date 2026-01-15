# Configuration des Variables d'Environnement - Module Marketing

## Variables Requises

### 1. Azure OpenAI (OBLIGATOIRE)

Le module marketing nécessite Azure OpenAI pour fonctionner. Ajoutez ces variables à votre fichier `.env` :

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
```

**Optionnel** (valeurs par défaut fournies) :
```bash
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
```

### 2. Database PostgreSQL (OBLIGATOIRE)

Le module nécessite PostgreSQL avec l'extension `pgvector` :

```bash
DATABASE_URL=postgresql://user:password@host:port/database
```

**Important** : Assurez-vous que l'extension pgvector est activée :
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 3. Canva API (OPTIONNEL)

Pour la génération automatique de designs Canva :

```bash
CANVA_API_KEY=your-canva-api-key
CANVA_BRAND_KIT_ID=your-brand-kit-id
```

Sans ces variables, le module fonctionnera mais ne pourra pas créer de designs Canva automatiquement.

## Installation des Dépendances

Installez les dépendances du module marketing :

```bash
pip install -r marketing/requirements.txt
```

## Initialisation

### 1. Créer les tables de la base de données

Les tables seront créées automatiquement au démarrage, mais vous pouvez aussi les créer manuellement :

```python
from marketing.services.persistence.sqlalchemy_repository import get_marketing_repository

repository = get_marketing_repository()
await repository.initialize_tables()
```

### 2. Indexer le contenu (transcripts + programme)

Pour que les agents puissent utiliser RAG, indexez le contenu :

```python
from marketing.services.memory.content_indexer import get_content_indexer

indexer = get_content_indexer()
stats = await indexer.index_all()
print(f"Indexed: {stats}")
```

Ou via l'API :
```bash
POST /api/marketing/voice/reindex
```

### 3. Générer le profil de voix

Analysez les transcripts pour créer le profil de voix de Nicole :

```bash
POST /api/marketing/voice/analyze
```

## Vérification

Pour vérifier que tout fonctionne :

```bash
GET /api/marketing/health
```

Devrait retourner : `{"status": "healthy", "module": "marketing"}`

## Dépannage

### Erreur "Azure OpenAI endpoint not configured"
- Vérifiez que `AZURE_OPENAI_ENDPOINT` et `AZURE_OPENAI_API_KEY` sont définis

### Erreur "pgvector extension not found"
- Connectez-vous à PostgreSQL et exécutez : `CREATE EXTENSION vector;`

### Erreur "No active voice profile"
- Lancez l'analyse de voix : `POST /api/marketing/voice/analyze`

### Les agents ne trouvent pas de contenu pertinent
- Réindexez le contenu : `POST /api/marketing/voice/reindex`
