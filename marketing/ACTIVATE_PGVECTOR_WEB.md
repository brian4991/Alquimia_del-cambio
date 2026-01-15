# Activer pgvector via Railway Web (Sans CLI)

## 🎯 Solution la plus simple - Pas besoin de CLI !

### Étapes

1. **Va sur Railway Dashboard**
   - https://railway.app
   - Connecte-toi avec ton compte

2. **Sélectionne ton projet**
   - Clique sur ton projet "Alquimia" (ou le nom de ton projet)

3. **Va dans Database**
   - Dans le menu latéral, clique sur **Database** ou **Postgres**

4. **Ouvre Query Editor**
   - Clique sur **Query** ou **SQL Editor**

5. **Exécute cette commande SQL** :
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

6. **Vérifie que c'est activé** :
   ```sql
   SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';
   ```

   Tu devrais voir :
   ```
   extname | extversion
   --------+------------
   vector  | 0.5.1
   ```

7. **C'est fait ! ✅**

## Alternative : Via psql direct

Si Railway Dashboard ne fonctionne pas, tu peux aussi utiliser un client PostgreSQL :

1. Installe **pgAdmin** ou **DBeaver** (gratuit)
2. Connecte-toi avec ta `DATABASE_URL` :
   ```
   Host: yamanote.proxy.rlwy.net
   Port: 31448
   Database: railway
   User: postgres
   Password: auFAOILcQZPfnKycrzcJRgIsruWuJObt
   ```
3. Exécute : `CREATE EXTENSION IF NOT EXISTS vector;`

## Vérification depuis Python

Une fois activé, teste depuis ton code :

```python
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector';"))
    row = result.fetchone()
    if row:
        print(f"✅ pgvector activé: version {row[1]}")
    else:
        print("❌ pgvector non activé")
```
