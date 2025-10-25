# FIX VIDEOS MOBILE - Landing Page Retiro

## Problème
Les vidéos en format `.mov` ne s'affichent pas sur mobile (Android et certains iOS).

## Solution

### 1. Installer FFmpeg (si pas déjà installé)

**Option A - Winget (recommandé):**
```powershell
winget install ffmpeg
```

**Option B - Chocolatey:**
```powershell
choco install ffmpeg
```

**Option C - Manuel:**
Télécharger depuis https://ffmpeg.org/download.html et ajouter au PATH

### 2. Convertir les vidéos

Exécuter le script de conversion :
```powershell
.\convert_videos_simple.ps1
```

Ce script va convertir les 3 vidéos de `.mov` vers `.mp4` avec :
- Codec H.264 (compatible tous navigateurs)
- Codec audio AAC
- Optimisation mobile (faststart)
- Qualité CRF 23 (bon compromis taille/qualité)

### 3. Vérifier les fichiers

Après la conversion, vous devriez avoir dans `frontend/public/`:
- `video-para-ti.mp4` (nouveau)
- `video-retiro-1.mp4` (nouveau)
- `video-retiro-2.mp4` (nouveau)

### 4. Code déjà mis à jour

Le code JSX a déjà été mis à jour pour utiliser les fichiers `.mp4` :
- ✅ Logo transparent ajouté
- ✅ Vidéos changées de `.mov` à `.mp4`
- ✅ Attributs vidéo optimisés pour mobile
- ✅ Code simplifié avec `loop` automatique

### Attributs vidéo utilisés pour mobile :
```jsx
<video 
  autoPlay      // Lecture automatique
  muted         // Muet (requis pour autoplay mobile)
  loop          // Boucle automatique
  playsInline   // Lecture dans la page (pas fullscreen iOS)
  preload="auto" // Préchargement
  poster=""     // Pas de poster pour éviter flash
>
  <source src="/video-para-ti.mp4" type="video/mp4" />
</video>
```

### Test
Une fois les vidéos converties :
1. Tester sur desktop (Chrome, Firefox, Safari)
2. Tester sur mobile (Chrome Android, Safari iOS)
3. Vérifier que les vidéos jouent automatiquement en boucle

## Alternative si FFmpeg ne fonctionne pas

Vous pouvez utiliser un convertisseur en ligne :
- https://cloudconvert.com/mov-to-mp4
- https://www.freeconvert.com/mov-to-mp4

Paramètres recommandés :
- Codec vidéo: H.264
- Codec audio: AAC
- Qualité: Élevée
- Optimisation: Web/Streaming

