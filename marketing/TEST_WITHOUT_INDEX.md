# Tester l'app en local sans index vectoriel

## 🎯 Mode Mock (Sans Index)

Tu peux tester l'app marketing **sans pgvector ni Azure Search** en utilisant le mode **mock**.

## 📋 Configuration

### Option 1 : Mode Mock explicite

Ajoute dans ton `.env` :

```bash
# Désactiver l'index vectoriel (mode mock)
VECTOR_STORE_BACKEND=mock
```

### Option 2 : Laisser vide (fallback automatique)

Si pgvector n'est pas configuré, le système basculera automatiquement en mode mock.

## ✅ Ce qui fonctionne sans index

- ✅ **Tous les agents marketing** (Strategist, Content Lead, etc.)
- ✅ **Réunions d'équipe** (débats, coordination)
- ✅ **Génération de contenu** (posts, scripts, calendrier)
- ✅ **Stratégies marketing** (court, moyen, long terme)
- ✅ **Interface admin** (tous les endpoints API)

## ⚠️ Ce qui ne fonctionne pas sans index

- ❌ **RAG (Recherche de contenu)** : Les agents ne pourront pas chercher dans :
  - Les transcripts Instagram
  - Le contenu du programme
  - Le contenu approuvé précédemment
  
- ⚠️ **Contenu moins personnalisé** : Les agents créeront du contenu générique, pas basé sur le style de Nicole

## 🚀 Comment tester

### 1. Configure le mode mock

```bash
# Dans ton .env
VECTOR_STORE_BACKEND=mock
```

### 2. Lance l'app

```bash
cd backend
python main.py
```

### 3. Teste les endpoints

```bash
# Health check
GET http://localhost:8000/api/marketing/health

# Créer une réunion
POST http://localhost:8000/api/marketing/meetings
{
  "topic": "Stratégie Instagram pour janvier",
  "goal": "Créer 5 posts sur la gestion émotionnelle"
}
```

### 4. Accède à l'admin panel

1. Va sur `http://localhost:5173/admin`
2. Clique sur le tab **Marketing**
3. Lance une réunion d'équipe

## 💡 Comportement en mode mock

- Les agents fonctionnent normalement
- Les recherches RAG retournent des listes vides (pas d'erreur)
- Le contenu généré sera générique (pas basé sur les transcripts)
- Tous les autres features fonctionnent

## 🔄 Activer l'index plus tard

Quand tu veux activer l'index :

1. **Option pgvector** :
   ```bash
   VECTOR_STORE_BACKEND=pgvector
   # Puis active pgvector dans PostgreSQL
   ```

2. **Option Azure Search** :
   ```bash
   VECTOR_STORE_BACKEND=azure_search
   AZURE_SEARCH_SERVICE_NAME=ton-service
   AZURE_SEARCH_API_KEY=ton-key
   ```

## ✅ Résumé

**Tu peux tester toute l'app marketing maintenant sans index !**

Le mode mock permet de :
- ✅ Tester l'interface
- ✅ Tester les agents
- ✅ Tester les réunions
- ✅ Générer du contenu (générique)

Tu pourras activer l'index plus tard pour avoir du contenu personnalisé basé sur les transcripts de Nicole.
