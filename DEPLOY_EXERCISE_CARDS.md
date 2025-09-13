# Déploiement des Cartes d'Exercice

## 📋 Résumé des changements

Cette mise à jour ajoute la fonctionnalité complète des cartes d'exercice au système :

### ✅ Fonctionnalités ajoutées :
- **Création de cartes d'exercice** avec instructions et questions
- **Support des questions texte et tableau** avec configuration personnalisée
- **Prévisualisation complète** dans le panel admin
- **Édition des cartes existantes** avec sauvegarde des questions
- **Rendu utilisateur** des exercices avec interface interactive

### 🔧 Modifications techniques :

#### Backend :
- ✅ Ajout colonnes `exercise_instructions` et `exercise_questions` à `theme_cards`
- ✅ Mise à jour des modèles Pydantic pour supporter les données d'exercice
- ✅ Correction des endpoints de création/modification de cartes
- ✅ Support JSON pour les configurations de tableau

#### Frontend :
- ✅ Interface complète de création d'exercices dans le panel admin
- ✅ Prévisualisation en temps réel des cartes d'exercice
- ✅ Gestion des questions texte et tableau
- ✅ Édition des cartes existantes avec chargement des données

## 🚂 Migration Railway

### 1. Exécuter la migration
```bash
# Sur Railway, le script sera exécuté automatiquement
python backend/migrate_railway_exercise_cards.py
```

### 2. Vérifications post-déploiement
- [ ] Créer une carte d'exercice avec questions
- [ ] Vérifier la prévisualisation
- [ ] Modifier une carte existante
- [ ] Tester l'interface utilisateur

### 3. Structure de base de données

#### Nouvelles colonnes `theme_cards` :
```sql
ALTER TABLE theme_cards ADD COLUMN exercise_instructions TEXT NULL;
ALTER TABLE theme_cards ADD COLUMN exercise_questions JSON NULL DEFAULT '[]';
```

#### Nouvelle table `user_card_responses` :
```sql
CREATE TABLE user_card_responses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    card_id INTEGER NOT NULL,
    question_index INTEGER NOT NULL,
    response_text TEXT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (card_id) REFERENCES theme_cards(id) ON DELETE CASCADE
);
```

## 📊 Format des données

### Structure des questions d'exercice :
```json
[
  {
    "type": "text",
    "question": "Quelle est votre réflexion sur ce sujet ?"
  },
  {
    "type": "table",
    "question": "Complétez le tableau suivant :",
    "table_config": {
      "columns": [
        {"title": "Jour", "type": "text"},
        {"title": "Émotion", "type": "text"},
        {"title": "Intensité", "type": "number"}
      ],
      "rows": 7
    }
  }
]
```

## 🔍 Tests recommandés

1. **Panel Admin :**
   - Créer une carte d'exercice avec questions texte
   - Créer une carte avec questions tableau
   - Prévisualiser les cartes
   - Modifier des cartes existantes

2. **Interface Utilisateur :**
   - Affichage des instructions d'exercice
   - Rendu des questions texte
   - Rendu des tableaux configurés
   - Sauvegarde des réponses

## 🚀 Commandes de déploiement

```bash
# 1. Commit des changements
git add .
git commit -m "feat: Add complete exercise cards system with questions and tables"

# 2. Push vers Railway
git push origin main

# 3. Railway redéploiera automatiquement
# 4. Exécuter la migration si nécessaire
```

## 📝 Notes importantes

- Les anciennes données sont préservées
- Les cartes existantes sans questions restent fonctionnelles  
- La migration est sécurisée et réversible
- Compatibilité avec les formats de données existants
