# Assets - Organisation des fichiers multimédias

## Structure des dossiers

### 📁 `images/`
Contient toutes les images du projet, organisées par catégorie :

#### 📁 `backgrounds/` 
Images de fond et visuels d'ambiance
- `kendal-TW2bfT_tWDI-unsplash.jpg` (1.7MB)
- `kendal-ZrCLoDQTFUI-unsplash.jpg` (2.0MB)
- `pawel-czerwinski-lWBZ01XRRoI-unsplash.jpg` (1.3MB)
- `josh-calabrese-XXpbdU_31Sg-unsplash.jpg` (655KB)

#### 📁 `photography/`
Photos personnelles et portraits
- `Copia de _DSC1351.jpg` (7.3MB)
- `Copia de _DSC1497.jpg` (8.2MB)
- `Copia de _DSC1725.jpg` (9.3MB)
- `Copia de _DSC1730.jpg` (8.6MB)
- `Copia de _DSC1911.jpg` (10.0MB)

#### 📁 `interface/`
Captures d'écran et éléments d'interface
- `exercices.png` (152KB) - Capture d'écran des exercices
- `module.png` (163KB) - Capture d'écran d'un module
- `panel.png` (171KB) - Capture d'écran du panel admin

## Convention de nommage

- **Backgrounds** : `nom-descriptif-source.jpg`
- **Photography** : Conserver les noms originaux pour traçabilité
- **Interface** : `nom-fonctionnalite.png`

## Utilisation dans le code

Pour référencer ces images dans votre application :

```jsx
// Images de fond
import backgroundImage from '/assets/images/backgrounds/kendal-TW2bfT_tWDI-unsplash.jpg';

// Images d'interface
import moduleScreenshot from '/assets/images/interface/module.png';
```

---
*Dossier organisé automatiquement le 8 juin 2025* 