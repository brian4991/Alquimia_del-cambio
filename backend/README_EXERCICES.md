# 📚 Système de Gestion des Exercices

## 🎯 Structure Hiérarchique des Exercices

Le système utilise maintenant une **structure à deux niveaux** pour les exercices:

### Niveau 1: Groupe d'Exercices (PARENT_TITLE)
- **Exemple:** `"Ejercicio #1: Historia"`
- **Affichage:** En haut de la page utilisateur (grand titre H1)
- **Usage:** Partagé par tous les sous-exercices du même groupe (1.1, 1.2, 1.3...)
- **Format:** `"Ejercicio #X: Nom du groupe"`

### Niveau 2: Sous-Exercice (TITLE)
- **Exemple:** `"Ejercicio 1.1: Explorando mi historia Emocional"`
- **Affichage:** Dans la sidebar à droite (liste des exercices) + titre secondaire (H2)
- **Format:** `"Ejercicio X.X: [Titre]"`

### Où sont affichés les titres?

**Page utilisateur:**
```
┌──────────────────────────────────────┐
│  [EN HAUT - H1]                      │
│  Ejercicio #1: Historia              │ ← PARENT_TITLE
│                                      │
│  [Carte principale - H2]             │
│  Ejercicio 1.1: Explorando...        │ ← TITLE
│  [Contenu de l'exercice]             │
└──────────────────────────────────────┘

[SIDEBAR DROITE]
① Ejercicio 1.1: Explorando... ← TITLE
② Ejercicio 1.2: Reconociendo... ← TITLE
③ Ejercicio 1.3: Raíces... ← TITLE
```

## 📊 Exemple Concret

**Groupe:** Ejercicio #1: Historia

- **Ejercicio 1.1:** Explorando mi historia Emocional
- **Ejercicio 1.2:** Reconociendo Patrones Emocionales
- **Ejercicio 1.3:** Raíces Emocionales

Tous ces sous-exercices affichent "Ejercicio #1: Historia" en haut, mais ont leurs titres spécifiques dans la sidebar.

## 🛠️ Fichiers Disponibles

### Pour Créer des Exercices
- **`TEMPLATE_create_exercise.py`** - Template à copier pour créer de nouveaux exercices
- **`GUIDE_CREATION_EXERCICES.md`** - Guide complet étape par étape

### Scripts de Migration (déjà exécutés)
- **`add_parent_title_to_exercises.py`** - Ajoute le champ parent_title à la BD

## 📝 Comment Créer un Nouvel Exercice

### Méthode Rapide

1. Copier `TEMPLATE_create_exercise.py`
2. Renommer en `create_ejercicio_X_X.py`
3. Modifier les variables:
```python
THEME_ID = 13
EXERCISE_NUMBER = "2.1"
EXERCISE_TITLE = "Ton titre"                    # Titre du sous-exercice
PARENT_TITLE = "Ejercicio #2: Nom du groupe"    # Titre du groupe (partagé)
ORDER_NUMBER = 4
```

**Exemple pour le groupe "Historia" (Ejercicio #1):**
```python
# Ejercicio 1.1
PARENT_TITLE = "Ejercicio #1: Historia"
EXERCISE_TITLE = "Explorando mi historia Emocional"

# Ejercicio 1.2
PARENT_TITLE = "Ejercicio #1: Historia"          # ← MÊME parent_title!
EXERCISE_TITLE = "Reconociendo Patrones Emocionales"

# Ejercicio 1.3
PARENT_TITLE = "Ejercicio #1: Historia"          # ← MÊME parent_title!
EXERCISE_TITLE = "Raíces Emocionales"
```
4. Copier-coller les sections du fichier .txt
5. Exécuter: `python create_ejercicio_2_1.py`

### Documentation Complète

Voir `GUIDE_CREATION_EXERCICES.md` pour:
- Instructions détaillées
- Règles importantes
- Exemples complets
- Checklist de vérification

## ✅ Règles Essentielles

1. **Parent title (groupe)** format: `"Ejercicio #X: Nom"`
   - Partagé par tous les sous-exercices du même groupe
   - Affiché EN HAUT de la page utilisateur
   
2. **Titre du sous-exercice** format: `"Ejercicio X.X: Titre"`
   - Doit inclure le numéro complet (X.X)
   - Affiché dans la sidebar à droite
   
3. **Questions multiples** séparées par `\n\n`
   
4. **Fidélité au texte** original (ne pas modifier)

## 🔄 Migrations Effectuées

- ✅ Ajout du champ `parent_title` à la table `exercises`
- ✅ Mise à jour des 3 exercices du Thème 1
- ✅ Frontend mis à jour pour afficher la hiérarchie

## 📞 Support

En cas de problème, consulter:
1. `GUIDE_CREATION_EXERCICES.md` - Documentation complète
2. `TEMPLATE_create_exercise.py` - Exemple fonctionnel
3. Les logs de la base de données

