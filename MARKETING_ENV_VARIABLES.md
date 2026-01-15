# Variables d'Environnement - Module Marketing

## Variables OBLIGATOIRES

Ajoutez ces variables à votre fichier `.env` à la racine du projet :

### Azure OpenAI (REQUIS)
```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
```

### Database PostgreSQL (REQUIS)
```bash
DATABASE_URL=postgresql://user:password@host:port/database
```

**Important** : La base de données doit avoir l'extension `pgvector` activée :
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

## Variables OPTIONNELLES

### Azure OpenAI (valeurs par défaut)
```bash
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
```

### Canva API (optionnel)
```bash
CANVA_API_KEY=your-canva-api-key
CANVA_BRAND_KIT_ID=your-brand-kit-id
```

Sans Canva, le module fonctionnera mais ne pourra pas créer de designs automatiquement.

## Exemple de fichier .env complet

```bash
# Variables existantes de l'app Alquimia
DATABASE_URL=postgresql://user:password@localhost:5432/alquimia
SECRET_KEY=your-secret-key

# Variables Marketing (à ajouter)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=text-embedding-ada-002

# Canva (optionnel)
CANVA_API_KEY=your-canva-api-key
CANVA_BRAND_KIT_ID=your-brand-kit-id
```

## Installation

1. **Installer les dépendances** :
```bash
pip install -r marketing/requirements.txt
```

2. **Activer pgvector dans PostgreSQL** :
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

3. **Indexer le contenu** (via API après démarrage) :
```bash
POST /api/marketing/voice/reindex
```

4. **Générer le profil de voix** :
```bash
POST /api/marketing/voice/analyze
```

## Vérification

Testez que tout fonctionne :
```bash
GET /api/marketing/health
```
