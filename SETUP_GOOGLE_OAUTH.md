# 🔐 Configuration Google OAuth - Guide Complet

## 📋 Vue d'ensemble

Ce guide explique comment configurer l'authentification Google OAuth pour l'application Alquimia del Cambio.

**Code déjà en place:**
- ✅ Routes backend OAuth (`/auth/google`, `/auth/google/callback`)
- ✅ Composant frontend `OAuthCallback.jsx`
- ✅ Bouton "Continuer avec Google" dans `Login.jsx`

**Il manque seulement:** Les credentials Google (Client ID & Client Secret)

---

## 🚀 Étape 1: Créer un Projet Google Cloud

### 1.1 Accéder à Google Cloud Console
1. Va sur [Google Cloud Console](https://console.cloud.google.com/)
2. Connecte-toi avec ton compte Google
3. Clique sur **"Select a project"** en haut → **"NEW PROJECT"**

### 1.2 Créer le projet
- **Project name:** `Alquimia del Cambio`
- **Organization:** (laisser par défaut)
- Clique sur **"CREATE"**

---

## 🔑 Étape 2: Configurer OAuth Consent Screen

### 2.1 Activer Google+ API
1. Dans le menu ☰ → **"APIs & Services"** → **"Library"**
2. Recherche **"Google+ API"**
3. Clique dessus et **"ENABLE"**

### 2.2 Configurer OAuth consent screen
1. Menu ☰ → **"APIs & Services"** → **"OAuth consent screen"**
2. Choisis **"External"** (pour permettre à tous les utilisateurs de se connecter)
3. Clique **"CREATE"**

### 2.3 Remplir les informations
**App information:**
- **App name:** `Alquimia del Cambio`
- **User support email:** ton email
- **App logo:** (optionnel - tu peux upload le logo plus tard)

**App domain:**
- Pour l'instant, laisse vide ou mets ton domaine Railway si tu veux
- **Note:** Pour Railway, tu devras aussi ajouter le domaine dans "Authorized domains" (voir section suivante)

**Developer contact information:**
- **Email addresses:** ton email

Clique **"SAVE AND CONTINUE"**

### 2.4 Authorized domains (IMPORTANT!)
Avant de continuer, retourne à l'onglet **"OAuth consent screen"**:

1. Scroll jusqu'à **"Authorized domains"**
2. Clique **"ADD DOMAIN"**
3. Ajoute:
   ```
   railway.app
   ```
   
   ⚠️ **NOTES IMPORTANTES:**
   - Pour Railway, ajoute seulement `railway.app` (pas le sous-domaine complet)
   - N'ajoute PAS `localhost` ici (pas accepté par Google)
   - `localhost` sera configuré plus tard dans les Credentials
   
4. Clique **"SAVE"**

### 2.5 Scopes
1. Retourne à l'assistant de configuration
2. Clique **"ADD OR REMOVE SCOPES"**
3. Sélectionne:
   - ✅ `.../auth/userinfo.email`
   - ✅ `.../auth/userinfo.profile`
   - ✅ `openid`
4. Clique **"UPDATE"** puis **"SAVE AND CONTINUE"**

### 2.6 Test users (mode développement)
Si tu es en mode "Testing", ajoute tes emails de test:
1. Clique **"ADD USERS"**
2. Ajoute ton email et ceux des testeurs
3. **"SAVE AND CONTINUE"**

---

## 🎫 Étape 3: Créer les Credentials OAuth

### 3.1 Créer OAuth Client ID
1. Menu ☰ → **"APIs & Services"** → **"Credentials"**
2. Clique **"+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. **Application type:** `Web application`

### 3.2 Configurer les URIs

**Name:** `Alquimia del Cambio Web Client`

**Authorized JavaScript origins:**
```
http://localhost:5173
http://localhost:8000
https://alquimiadel-cambio-production.up.railway.app
```

**Authorized redirect URIs:**
```
http://localhost:8000/auth/google/callback
https://alquimiadel-cambio-production.up.railway.app/auth/google/callback
```

⚠️ **IMPORTANT:** 
- Les URLs `localhost` sont pour le développement local
- Remplace `alquimiadel-cambio-production.up.railway.app` par ton URL Railway backend réelle
- Les redirect URIs doivent se terminer par `/auth/google/callback`

### 3.3 Récupérer les credentials
Après création, tu verras une popup avec:
- **Client ID:** `123456789-abcdef.apps.googleusercontent.com`
- **Client Secret:** `GOCSPX-xxxxxxxxxxxxx`

**📋 Copie ces valeurs, tu en auras besoin!**

---

## 💻 Étape 4: Configuration Locale (Développement)

### 4.1 Créer fichier .env backend
Crée `backend/.env`:

```env
# Google OAuth
GOOGLE_CLIENT_ID=ton-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=ton-client-secret

# JWT Secret (génère une clé aléatoire forte)
SECRET_KEY=une-cle-secrete-tres-longue-et-complexe-123456789

# Base de données locale
DATABASE_URL=sqlite:///./app.db
```

### 4.2 Générer une SECRET_KEY forte
En PowerShell:
```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 4.3 Tester localement
1. Redémarre le backend: `cd backend; python main.py`
2. Redémarre le frontend: `cd frontend; npm run dev`
3. Va sur `http://localhost:5173/login`
4. Clique sur **"Continuer avec Google"**
5. Authentifie-toi avec Google
6. Tu devrais être redirigé vers le dashboard!

---

## 🚂 Étape 5: Configuration Railway (Production)

### 5.1 Ajouter les variables d'environnement
Dans Railway Dashboard → ton projet → **Variables**:

```
GOOGLE_CLIENT_ID=ton-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=ton-client-secret
SECRET_KEY=ta-cle-secrete-forte
FRONTEND_URL=https://ton-frontend.vercel.app
```

### 5.2 Mettre à jour les URIs autorisées
Retourne sur Google Cloud Console → Credentials → ton OAuth Client:

**Authorized redirect URIs:**
Ajoute l'URL Railway réelle:
```
https://ton-backend-production.railway.app/auth/google/callback
```

### 5.3 Mettre à jour frontend config
Édite `frontend/src/config.js`:

```javascript
export const config = {
  apiUrl: import.meta.env.PROD 
    ? 'https://ton-backend.railway.app'  // ← URL Railway backend
    : 'http://localhost:8000',
};
```

---

## ✅ Étape 6: Vérification

### 6.1 Tests à faire
- [ ] Login Google en local fonctionne
- [ ] Login Google en production fonctionne
- [ ] L'utilisateur est créé dans la base de données
- [ ] Le token JWT est généré correctement
- [ ] La redirection vers le dashboard fonctionne
- [ ] Les données utilisateur (nom, email) sont récupérées

### 6.2 Débugger
Si ça ne fonctionne pas:

1. **Vérifier les logs backend:**
   ```bash
   # Local
   Regarde la console où tu as lancé python main.py
   
   # Railway
   Railway Dashboard → Deployments → View logs
   ```

2. **Vérifier les URIs:**
   - Les redirect URIs dans Google Console doivent EXACTEMENT matcher
   - Pas de trailing slash: ✅ `/auth/google/callback` ❌ `/auth/google/callback/`

3. **Vérifier les variables d'environnement:**
   ```bash
   # Railway
   railway variables
   ```

4. **Console navigateur (F12):**
   - Regarde s'il y a des erreurs CORS
   - Vérifie que le token est bien reçu dans l'URL de callback

---

## 🔒 Sécurité

### Mode Production
Avant de mettre en production publique:

1. **Passer en "In production"** dans OAuth consent screen
2. **Soumettre pour vérification Google** (si nécessaire)
3. **Ajouter Privacy Policy & Terms of Service**
4. **Activer HTTPS partout**
5. **Restreindre les CORS origins**

### Bonnes pratiques
- ❌ Ne JAMAIS commit les credentials dans Git
- ✅ Utiliser des variables d'environnement
- ✅ Utiliser différents OAuth clients pour dev/prod
- ✅ Régulièrement vérifier les logs d'authentification

---

## 📞 Support

### Ressources
- [Google OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [Authlib Documentation](https://docs.authlib.org/)
- [FastAPI OAuth](https://fastapi.tiangolo.com/advanced/security/)

### Problèmes courants

**"redirect_uri_mismatch"**
→ Vérifie que l'URI dans Google Console match exactement

**"invalid_client"**
→ Vérifie GOOGLE_CLIENT_ID et GOOGLE_CLIENT_SECRET

**"access_denied"**
→ L'utilisateur a refusé l'accès ou n'est pas dans les test users

**CORS errors**
→ Vérifie la configuration CORS dans backend/main.py

---

## 🎉 C'est terminé!

Une fois configuré, les utilisateurs pourront:
- Se connecter avec leur compte Google
- Créer automatiquement un compte sur l'application
- Accéder directement au dashboard

**Prochaine étape:** Synchroniser la base de données vers Railway avec `sync_db_to_railway.py`

