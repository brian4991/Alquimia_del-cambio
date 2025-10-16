# Guide des Placeholders d'Images - Landing Page

Ce document liste tous les codes des placeholders d'images utilisés dans la landing page et leur description.

## Logo et En-tête
- **LOGO-001** : Logo "Alquimia del Cambio" (32x12 - largeur x hauteur en unités de mesure)

## Images Principales

### Section Hero
- **IMG-HERO-001** : Image principale du retiro - femmes en méditation au bord de la mer (grande bannière)

### Section Localisation
- **IMG-LOCATION-001** : Vue aérienne de l'île de Barú avec plage paradisiaque

### Section Hébergement
- **IMG-ROOM-001** : Chambre d'hôtel avec vue sur la mer
- **IMG-ROOM-002** : Intérieur de chambre luxueuse

## Section "Pourquoi Nous Sommes Différents"

- **IMG-DIFF-001** : EXPERIENCIA DE LUJO - Image représentant le luxe et l'attention aux détails
- **IMG-DIFF-002** : LA RÁPIDA TRANSFORMACIÓN - Image de transformation personnelle
- **IMG-DIFF-003** : EL PODER DE LA AUTENTICIDAD - Image d'authenticité et d'introspection
- **IMG-DIFF-004** : LAS SESIONES GRUPALES A DIARIO - Image de session de groupe
- **IMG-DIFF-005** : LAS AMISTADES ETERNAS - Image de femmes créant des liens
- **IMG-DIFF-006** : CONEXIÓN CON LA NATURALEZA - Image de connexion avec la nature (plage, forêt)
- **IMG-DIFF-007** : ESPIRITUALIDAD - Image de méditation ou pratiques spirituelles
- **IMG-DIFF-008** : NUESTRO EQUIPO - Photo de l'équipe du retiro

## Section Fondatrice
- **IMG-FOUNDER-001** : Photo professionnelle de Victoria Novoa (portrait vertical de haute qualité)

## Section Témoignages
- **IMG-TESTIMONIAL-001** : Photo de la participante (témoignage 1)
- **IMG-TESTIMONIAL-002** : Photo de la participante (témoignage 2)
- **IMG-TESTIMONIAL-003** : Photo de la participante (témoignage 3)
- **IMG-TESTIMONIAL-004** : Photo de la participante (témoignage 4)
- **IMG-TESTIMONIAL-005** : Photo de la participante (témoignage 5)
- **IMG-TESTIMONIAL-006** : Photo de la participante (témoignage 6)

## Image Promotionnelle
- **IMG-PROMO-001** : Image promotionnelle du retiro avec groupe de femmes heureuses

---

## Instructions pour remplacer les placeholders

1. Préparez vos images avec les dimensions appropriées
2. Placez-les dans le dossier `Alquimia_del-cambio/frontend/public/landing/`
3. Remplacez les divs de placeholder par des balises `<img>` avec le bon chemin
4. Exemple de remplacement :

**Avant:**
```jsx
<div className="w-full h-96 bg-gray-200 rounded-2xl flex items-center justify-center text-gray-600">
  [IMG-HERO-001: Image principale du retiro - femmes en méditation au bord de la mer]
</div>
```

**Après:**
```jsx
<img 
  src="/landing/hero-main.jpg" 
  alt="Retiro Ámate - Femmes en méditation au bord de la mer"
  className="w-full h-96 object-cover rounded-2xl"
/>
```

## Dimensions Recommandées

- **LOGO-001** : 400x150px (PNG avec fond transparent)
- **IMG-HERO-001** : 1920x600px (format large)
- **IMG-LOCATION-001** : 1600x900px
- **IMG-ROOM-001/002** : 800x600px
- **IMG-DIFF-001 à 008** : 600x400px
- **IMG-FOUNDER-001** : 800x1000px (portrait vertical)
- **IMG-TESTIMONIAL-001 à 006** : 400x400px (carré)
- **IMG-PROMO-001** : 1200x600px

## Notes
- Toutes les images doivent être optimisées pour le web (format JPG ou WebP)
- Assurez-vous que les images soient de haute qualité mais compressées
- Utilisez des images qui reflètent l'esprit du retiro : sérénité, connexion, transformation

