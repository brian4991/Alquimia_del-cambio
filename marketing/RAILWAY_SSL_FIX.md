# Fix Erreur SSL Railway CLI - Windows

## Problème

```
Failed to fetch: error sending request for url (https://backboard.railway.com/graphql/v2)
Caused by: invalid peer certificate: UnknownIssuer
```

## Solutions

### Solution 1: Script automatique (recommandé)

```bash
python marketing/railway_login_fix_ssl.py
```

### Solution 2: Token manuel (plus sûr)

1. Va sur: https://railway.app/account/tokens
2. Crée un nouveau token
3. Copie le token
4. Ajoute dans ton `.env`:
   ```bash
   RAILWAY_TOKEN=ton-token-ici
   ```

### Solution 3: Désactiver SSL temporairement (DEV uniquement)

```bash
# Windows PowerShell
$env:RUSTLS_NO_VERIFY="1"
railway login

# Ou dans CMD
set RUSTLS_NO_VERIFY=1
railway login
```

### Solution 4: Configurer les certificats Windows

Si tu es dans un environnement d'entreprise avec proxy:

1. Exporte le certificat de ton entreprise
2. Ajoute-le aux certificats Windows:
   - Win + R → `certmgr.msc`
   - Importe le certificat dans "Trusted Root Certification Authorities"

### Solution 5: Utiliser Railway Web UI

Si le CLI ne fonctionne toujours pas:

1. Va sur: https://railway.app
2. Connecte-toi via le navigateur
3. Utilise l'interface web pour gérer tes projets
4. Pour pgvector, utilise directement SQL via Railway Dashboard → Database → Query

## Pour activer pgvector sans CLI

Si le CLI ne fonctionne pas, tu peux activer pgvector directement:

1. Va sur Railway Dashboard
2. Sélectionne ton projet
3. Va dans **Database** → **Query**
4. Exécute:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```
5. Vérifie:
   ```sql
   SELECT * FROM pg_extension WHERE extname = 'vector';
   ```

## Vérification

Après avoir configuré le token ou résolu le SSL:

```bash
railway whoami
```

Tu devrais voir ton email Railway.
