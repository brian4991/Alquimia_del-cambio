# 🚀 Guide de Déploiement - Alquimia del Cambio

## Option 1: Vercel Fullstack (Recommandée)

### Étapes :

1. **Connecter à GitHub/GitLab :**
   ```bash
   # Si pas déjà fait, push ton code
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Déployer sur Vercel :**
   - Va sur [vercel.com](https://vercel.com)
   - Connecte ton repo GitHub
   - Sélectionne ce projet
   - ✅ Déployé automatiquement !

3. **Variables d'environnement (si nécessaire) :**
   - Dans Vercel Dashboard → Settings → Environment Variables
   - Ajoute les clés secrètes si tu en as

## Option 2: Frontend + Backend séparés

### Frontend (Vercel) :
```bash
cd frontend
npm install
vercel --prod
```

### Backend (Railway) :
1. [railway.app](https://railway.app) → New Project
2. Connect GitHub → Sélectionne `/backend`
3. ✅ Auto-déployé !

## Option 3: Netlify + Backend sur Render

### Frontend (Netlify) :
```bash
cd frontend
npm run build
# Drag & drop du dossier `dist` sur netlify.com
```

### Backend (Render) :
1. [render.com](https://render.com) → New Web Service
2. Connect repo → Root = `/backend`
3. Build: `pip install -r requirements.txt`
4. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 🔧 Configuration Frontend

### Variables d'environnement :
Crée un fichier `.env` dans `/frontend` :
```
VITE_API_URL=https://ton-backend.vercel.app
```

### Mettre à jour les appels API :
```javascript
// Remplace localhost par ton URL de production
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

## ✅ Checklist avant déploiement :

- [ ] Backend démarre localement
- [ ] Frontend build sans erreurs (`npm run build`)
- [ ] Images dans `/public` (pas de paths absolus)
- [ ] Variables d'environnement configurées
- [ ] CORS autorise les domaines de production

## 🎯 URLs finales typiques :
- **Frontend :** `https://alquimia-del-cambio.vercel.app`
- **Backend :** `https://alquimia-backend.vercel.app`
- **Docs API :** `https://alquimia-backend.vercel.app/docs` 