# Comment lancer le Frontend

## 🚀 Option 1 : Mode Dev (Recommandé pour développement)

Le frontend tourne séparément avec Vite en mode dev (hot reload).

### 1. Lance le backend

```bash
cd backend
python main.py
```

Le backend tourne sur `http://localhost:8000`

### 2. Lance le frontend (dans un autre terminal)

```bash
cd frontend
npm run dev
```

Le frontend tourne sur `http://localhost:5173` (ou un autre port si 5173 est occupé)

### 3. Accède à l'app

Va sur `http://localhost:5173`

Le frontend en mode dev se connecte automatiquement au backend sur `http://localhost:8000`

## 🏗️ Option 2 : Build statique (Production)

Le backend sert le frontend buildé.

### 1. Build le frontend

```bash
cd frontend
npm install  # Si pas déjà fait
npm run build
```

Ça crée le dossier `frontend/dist/`

### 2. Lance le backend

```bash
cd backend
python main.py
```

### 3. Accède à l'app

Va sur `http://localhost:8000`

Le backend sert automatiquement le frontend depuis `frontend/dist/`

## ⚙️ Configuration Frontend

Le frontend se connecte au backend via `frontend/src/config.js` :

```javascript
export const config = {
  apiUrl: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  // ...
};
```

En mode dev, Vite utilise cette config. En production, utilise la variable d'environnement `VITE_API_URL`.

## ✅ Vérification

### Mode Dev
- Frontend : `http://localhost:5173`
- Backend : `http://localhost:8000`
- Les deux tournent séparément

### Mode Build
- Tout sur : `http://localhost:8000`
- Backend sert le frontend buildé

## 🐛 Problèmes courants

### Frontend ne se connecte pas au backend

Vérifie que :
1. Le backend tourne sur `http://localhost:8000`
2. La config dans `frontend/src/config.js` pointe vers le bon URL
3. Pas de CORS errors dans la console

### Port déjà utilisé

Si le port 5173 est occupé, Vite utilisera automatiquement un autre port (5174, etc.)

### Build échoue

```bash
cd frontend
rm -rf node_modules dist
npm install
npm run build
```
