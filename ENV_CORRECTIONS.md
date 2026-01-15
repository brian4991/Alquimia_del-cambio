# Corrections pour ton .env

## ❌ Problèmes détectés

### 1. Nom de variable Azure OpenAI incorrect

Tu as mis :
```bash
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o
```

Mais le code attend :
```bash
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o
```

### 2. DATABASE_URL Railway

Tu as mis :
```bash
DATABASE_URL=postgresql://postgres:password@postgres.railway.internal:5432/railway
```

`postgres.railway.internal` est l'URL **interne** Railway qui ne fonctionne que depuis Railway.

Pour une connexion **locale**, tu dois utiliser l'URL **publique** Railway.

## ✅ Configuration corrigée

Remplace dans ton `.env` :

```bash
# Connexion à la DB Railway (production)
# IMPORTANT: Utilise l'URL PUBLIQUE Railway, pas .internal
# Trouve-la dans Railway Dashboard → Database → Connect → Public Network
DATABASE_URL=postgresql://postgres:auFAOILcQZPfnKycrzcJRgIsruWuJObt@containers-us-west-xxx.railway.app:5432/railway

# Variables Marketing
AZURE_OPENAI_API_KEY=YOUR_AZURE_OPENAI_API_KEY_HERE
AZURE_OPENAI_API_VERSION=2023-06-01-preview
AZURE_OPENAI_ENDPOINT=https://common-demo-openai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_GPT4O=gpt-4o  # ← CORRIGÉ (était CHAT_DEPLOYMENT_NAME)

# Autres variables existantes
SECRET_KEY=ton-secret-key-local
PORT=8000
```

## 🔍 Comment trouver l'URL publique Railway

1. Va sur Railway Dashboard
2. Sélectionne ton projet
3. Va dans l'onglet **Database**
4. Clique sur **Connect** ou **Public Network**
5. Copie l'URL qui ressemble à : `postgresql://postgres:password@containers-us-west-xxx.railway.app:5432/railway`

## ⚠️ Alternative : Utiliser l'URL interne Railway

Si tu veux vraiment utiliser `.internal`, tu dois :
1. Soit être connecté au VPN Railway (si disponible)
2. Soit utiliser Railway CLI : `railway connect`

Mais pour le développement local, l'URL publique est plus simple.
