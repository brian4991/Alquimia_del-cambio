# Activer pgvector - Solution Rapide (2 minutes)

## 🚀 Via Railway Dashboard (Le plus simple)

### Étapes

1. **Ouvre Railway Dashboard**
   - https://railway.app
   - Connecte-toi

2. **Sélectionne ton projet**
   - Clique sur ton projet "Alquimia" (ou le nom de ton projet)

3. **Va dans Database**
   - Dans le menu latéral → **Database** ou **Postgres**

4. **Ouvre Query Editor**
   - Clique sur **Query** ou **SQL Editor** ou **Connect**

5. **Copie-colle cette commande** :
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

6. **Clique sur "Run" ou "Execute"**

7. **Vérifie** (optionnel) :
   ```sql
   SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';
   ```

8. **✅ C'est fait !**

## ⏱️ Temps total : ~2 minutes

Beaucoup plus rapide que d'attendre une connexion Python qui peut timeout.
