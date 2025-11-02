# 🔧 Correction du problème OAuth avec le nouveau domaine

## Problème

L'erreur `mismatching_state: CSRF Warning! State not equal in request and response` se produit parce que :
1. Le nouveau domaine `www.nicoleramirezpsicoach.com` n'est pas configuré dans Google OAuth Console
2. Les cookies de session ne sont pas partagés correctement entre les domaines

## ✅ Solutions à appliquer

### 1. Configuration Google OAuth Console (OBLIGATOIRE)

**Vous devez modifier votre configuration Google OAuth Console :**

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Sélectionnez votre projet
3. Menu ☰ → **"APIs & Services"** → **"Credentials"**
4. Cliquez sur votre **OAuth Client ID** existant

#### Modifier les Authorized JavaScript origins :

Ajoutez ces URLs :
```
https://www.nicoleramirezpsicoach.com
https://nicoleramirezpsicoach.com
https://api.nicoleramirezpsicoach.com
https://alquimiadel-cambio-production.up.railway.app
```

#### Modifier les Authorized redirect URIs :

Ajoutez ces URLs (les redirect URIs doivent se terminer par `/auth/google/callback`) :
```
https://api.nicoleramirezpsicoach.com/auth/google/callback
https://alquimiadel-cambio-production.up.railway.app/auth/google/callback
http://localhost:8000/auth/google/callback
```

⚠️ **IMPORTANT** : Le redirect URI doit correspondre EXACTEMENT à l'URL de votre backend API. Si votre backend est sur Railway avec l'URL `alquimiadel-cambio-production.up.railway.app`, utilisez cette URL. Si vous avez un domaine personnalisé pour l'API (`api.nicoleramirezpsicoach.com`), utilisez celui-ci.

### 2. Variables d'environnement Railway

Assurez-vous que ces variables sont configurées dans Railway :

```
BACKEND_URL=https://alquimiadel-cambio-production.up.railway.app
# OU si vous avez un domaine personnalisé pour l'API :
# BACKEND_URL=https://api.nicoleramirezpsicoach.com

FRONTEND_URL=https://www.nicoleramirezpsicoach.com

SECRET_KEY=votre-secret-key-tres-securise-et-unique
```

### 3. Vérification du domaine API

Le frontend utilise `api.nicoleramirezpsicoach.com` (voir `frontend/src/config.js`). Vérifiez que :
- Ce domaine pointe vers votre backend Railway
- Le redirect URI dans Google OAuth Console correspond à ce domaine

### 4. Test

Après avoir modifié la configuration Google OAuth Console :
1. Attendez quelques minutes (Google peut prendre du temps pour propager les changements)
2. Essayez de vous connecter avec Google
3. Vérifiez que la redirection fonctionne correctement

## 🔍 Diagnostic

Si le problème persiste, vérifiez :

1. **Les logs Railway** : Regardez les erreurs dans les logs du backend
2. **La console navigateur** : Vérifiez les cookies et les requêtes réseau
3. **Le redirect URI** : Il doit correspondre EXACTEMENT à celui configuré dans Google OAuth Console

## 📝 Notes importantes

- Le paramètre `state` utilisé pour la protection CSRF est stocké dans la session du backend
- Les cookies de session doivent être accessibles entre le frontend et le backend
- Le `same_site="lax"` permet les requêtes cross-site nécessaires pour OAuth
- En production avec HTTPS, `https_only=True` est activé automatiquement

