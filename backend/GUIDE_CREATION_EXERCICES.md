# Guide de Création d'Exercices

Ce guide explique comment créer des exercices à partir de fichiers .txt pour l'application Alquimia del Cambio.

## 📋 Prérequis

- Un fichier .txt avec le contenu de l'exercice
- Python et la base de données configurée
- Accès au dossier `backend`

## 🎯 Méthode Recommandée: Template Manuel

### Étape 1: Préparer le fichier .txt

Assurez-vous que votre fichier .txt suit la structure:
```
Ejercicio X.X: [Titre]
Paso a Paso:
[Instructions générales]

1. [Titre Section 1]:
[Instructions section]
¿Question 1?
¿Question 2?

2. [Titre Section 2]:
...

Tiempo estimado: XX minutos
```

### Étape 2: Copier le Template

1. Copier le fichier `TEMPLATE_create_exercise.py`
2. Renommer en `create_ejercicio_X_X.py` (ex: `create_ejercicio_2_1.py`)

### Étape 3: Remplir les Données

Modifier les variables en haut du fichier:

```python
THEME_ID = 13  # ID du thème dans la BD
EXERCISE_NUMBER = "2.1"  # Numéro de l'exercice
EXERCISE_TITLE = "Titre de l'exercice"  # SANS le numéro
PARENT_TITLE = "Ejercicio #2: Nom du groupe"  # Titre du groupe (affiché en haut)
ORDER_NUMBER = 4  # Position dans le thème
```

**Important:** 
- `PARENT_TITLE` est le titre du **GROUPE** d'exercices (ex: "Ejercicio #1: Historia")
  - ✅ Affiché **EN HAUT** de la page (grand titre)
  - ✅ Partagé par tous les sous-exercices du même groupe (1.1, 1.2, 1.3...)
- `EXERCISE_TITLE` est le titre du **SOUS-exercice** spécifique (ex: "Explorando mi historia Emocional")
  - ✅ Titre complet: "Ejercicio X.X: [EXERCISE_TITLE]"
  - ✅ Affiché dans la **sidebar** (liste à droite)
  
**Exemple:**
```
Exercice 1.1, 1.2, 1.3 → Même PARENT_TITLE: "Ejercicio #1: Historia"
Exercice 2.1, 2.2     → Même PARENT_TITLE: "Ejercicio #2: Autre groupe"
```

### Étape 4: Copier les Instructions

Copier les instructions générales du .txt:

```python
INSTRUCTIONS = """[Copier-coller les instructions du fichier .txt]

Temps estimé: XX minutos"""
```

### Étape 5: Créer les Sections

Pour chaque section du .txt, ajouter un dictionnaire:

```python
SECTIONS = [
    {
        "title": "1. Titre de la section",
        "instructions": "Instructions de la section...",
        "questions": "¿Question 1?\n\n¿Question 2?\n\n¿Question 3?"
    },
    {
        "title": "2. Deuxième section",
        "instructions": "...",
        "questions": "..."
    },
]
```

**IMPORTANT:** 
- Questions multiples = les séparer par `\n\n` (double retour à la ligne)
- Rester FIDÈLE au texte original
- Ne PAS modifier ou inventer des questions

### Étape 6: Exécuter le Script

```bash
cd Alquimia_del-cambio/backend
python create_ejercicio_2_1.py
```

## ⚠️ Règles Importantes

### Format du Titre
**Structure à deux niveaux:**

✅ **PARENT_TITLE (en haut):** `"Ejercicio #1: Historia"`
- Titre du GROUPE d'exercices
- Affiché en haut de la page (grand titre)
- Partagé par tous les sous-exercices du même groupe

✅ **TITLE (dans la sidebar):** `"Ejercicio 1.1: Explorando mi historia Emocional"`
- Titre du SOUS-exercice spécifique
- Affiché dans la liste des exercices à droite
- Format: "Ejercicio X.X: [Titre]"

❌ **INCORRECT:** `"Explorando mi historia Emocional"` (manque le numéro "Ejercicio X.X:")

### Questions Multiples
Quand une section a plusieurs questions, les regrouper:

✅ **CORRECT:**
```python
"questions": "¿Question 1?\n\n¿Question 2?\n\n¿Question 3?"
```

❌ **INCORRECT:**
```python
"questions": ["¿Question 1?", "¿Question 2?", "¿Question 3?"]
```

### Fidélité au Texte
- ✅ Copier-coller exactement le texte du .txt
- ❌ Ne PAS paraphraser
- ❌ Ne PAS modifier les questions
- ❌ Ne PAS ajouter de questions

## 📝 Exemple Complet

Voir le fichier `TEMPLATE_create_exercise.py` pour un exemple complet et fonctionnel.

## 🔧 Scripts Disponibles

### Scripts de Correction
- `fix_exercises_faithful.py` - Corriger les exercices du thème 1
- `fix_exercise_titles.py` - Ajouter les numéros aux titres
- `fix_exercise_questions.py` - Corriger la structure des questions

### Template
- `TEMPLATE_create_exercise.py` - Template pour créer de nouveaux exercices

## 📞 Support

En cas de problème:
1. Vérifier que le format du .txt est correct
2. Vérifier que THEME_ID existe dans la BD
3. Vérifier les erreurs dans le terminal
4. Contacter le développeur si nécessaire

## ✅ Checklist de Vérification

Avant de créer un exercice:

- [ ] Le fichier .txt est bien structuré
- [ ] THEME_ID est correct
- [ ] EXERCISE_NUMBER est correct (format "X.X")
- [ ] **PARENT_TITLE** est défini (format "Ejercicio #X: Nom")
- [ ] PARENT_TITLE est **partagé** par tous les sous-exercices du même groupe
- [ ] ORDER_NUMBER est correct
- [ ] Instructions copiées fidèlement
- [ ] Toutes les sections sont présentes
- [ ] Questions multiples séparées par `\n\n`
- [ ] Aucune modification du texte original
- [ ] Le titre inclut le numéro: "Ejercicio X.X: Titre"

### Vérification après création:

- [ ] Le **PARENT_TITLE** s'affiche **en haut** de la page
- [ ] Le **TITLE complet** s'affiche dans la **sidebar** à droite
- [ ] Les questions sont bien regroupées avec retours à la ligne

---

**Dernière mise à jour:** $(date)

