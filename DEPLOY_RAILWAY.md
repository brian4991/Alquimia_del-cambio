# 🚂 Déploiement Backend sur Railway

## ✅ Fichiers de Configuration Créés

- **`backend/railway.toml`** - Configuration Railway
- **`backend/Procfile`** - Commande de démarrage 
- **`backend/runtime.txt`** - Version Python
- **`backend/config.example`** - Variables d'environnement

## 🚀 Étapes de Déploiement

### 1. Compte Railway
1. Allez sur [railway.app](https://railway.app)
2. Connectez-vous avec GitHub
3. Cliquez "Start a New Project"

### 2. Déploiement GitHub
1. Sélectionnez **"Deploy from GitHub repo"**
2. Choisissez votre repo `brian4991/Alquimia_del-cambio`
3. Railway détecte automatiquement Python
4. **IMPORTANT**: Changez le **Root Directory** vers `backend/`

### 3. Configuration Variables
Dans Railway Dashboard > Variables :
```
PORT=8000
PYTHONPATH=/app
SECRET_KEY=votre-clé-secrète-forte
```

### 4. Première Build
- Railway va automatiquement installer les dépendances
- Démarrer uvicorn avec votre FastAPI
- Vous obtiendrez une URL comme : `https://votre-app.railway.app`

## 🔗 Après le Déploiement

### Tester l'API
```bash
curl https://votre-app.railway.app/
curl https://votre-app.railway.app/docs
```

### Mettre à jour le Frontend
Modifiez `frontend/src/config.js` ligne 3 :
```javascript
apiUrl: import.meta.env.PROD 
  ? 'https://votre-app.railway.app'  // 👈 Votre URL Railway
  : 'http://localhost:8000',
```

## 💰 Coûts Railway

- **5$ gratuits par mois** 
- Puis environ **5-10$/mois** selon l'usage
- Base de données incluse

## 🔄 Auto-Deploy

Une fois configuré, chaque `git push` sur `main` redéploie automatiquement !

## 🆘 Support

Si problème, vérifiez :
1. Logs dans Railway Dashboard
2. Variables d'environnement
3. Root Directory = `backend/` 