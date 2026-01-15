# Configuration Azure Search (Alternative à pgvector)

## 🎯 Pourquoi utiliser Azure Search ?

Si tu as déjà Azure Search configuré, c'est **beaucoup mieux** que pgvector :

✅ **Avantages Azure Search** :
- Pas besoin d'activer pgvector sur PostgreSQL
- Recherche hybride (vectorielle + texte)
- Plus scalable et performant
- Intégration native avec Azure
- Gestion automatique des index

❌ **pgvector** :
- Nécessite l'extension PostgreSQL
- Recherche vectorielle basique uniquement
- Gestion manuelle des index

## 📋 Configuration

### 1. Variables d'environnement

Ajoute dans ton `.env` :

```bash
# Choisir le backend (pgvector ou azure_search)
VECTOR_STORE_BACKEND=azure_search

# Azure Search Configuration
AZURE_SEARCH_SERVICE_NAME=ton-service-name
AZURE_SEARCH_API_KEY=ton-api-key
AZURE_SEARCH_INDEX_NAME=marketing-content  # Optionnel, défaut: marketing-content
```

### 2. Où trouver tes credentials Azure Search

1. Va sur **Azure Portal** → **Azure AI Search**
2. Sélectionne ton service
3. **Settings** → **Keys**
4. Copie :
   - **Service name** : `ton-service-name.search.windows.net` → `ton-service-name`
   - **Admin key** : Utilise celui-ci comme `AZURE_SEARCH_API_KEY`

### 3. Exemple complet `.env`

```bash
# Backend vector store
VECTOR_STORE_BACKEND=azure_search

# Azure Search
AZURE_SEARCH_SERVICE_NAME=my-marketing-search
AZURE_SEARCH_API_KEY=ABC123XYZ...
AZURE_SEARCH_INDEX_NAME=marketing-content

# Azure OpenAI (toujours nécessaire pour les embeddings)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-openai-key
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
```

## 🚀 Utilisation

Une fois configuré, le module marketing utilisera automatiquement Azure Search au lieu de pgvector.

L'index sera créé automatiquement au premier lancement.

## 🔄 Migration depuis pgvector

Si tu veux migrer depuis pgvector vers Azure Search :

1. Configure Azure Search dans `.env`
2. Lance l'indexation :
   ```bash
   POST /api/marketing/voice/reindex
   ```
3. Les données seront indexées dans Azure Search

## ✅ Vérification

Teste que ça fonctionne :

```bash
GET /api/marketing/health
```

Tu devrais voir que le backend est `azure_search`.

## 💰 Coût Azure Search

Azure Search a un coût mensuel selon le tier :
- **Free** : Gratuit (limité)
- **Basic** : ~$75/mois
- **Standard** : À partir de ~$250/mois

Vérifie ton tier actuel sur Azure Portal.
