# 🔧 Guide du Système d'Administration - Alquimia del Cambio

## 🎯 Vue d'ensemble

Vous disposez maintenant d'un **système d'administration complet** qui vous permet de créer et gérer tout le contenu de votre application depuis l'interface web, sans avoir besoin de toucher au code ou à la base de données.

## 🚀 Accès au Panneau d'Administration

### Comment y accéder :
1. **Connectez-vous** à votre application
2. Dans la navigation, cliquez sur **"Administration"** (icône d'engrenage)
3. Vous arrivez sur le panneau d'administration avec 4 onglets

## 📋 Fonctionnalités Disponibles

### 1. 📚 **Gestion des Modules**
- **Créer** de nouveaux modules
- **Modifier** les modules existants
- **Supprimer** des modules
- **Organiser** l'ordre des modules

#### Champs disponibles :
- **Titre** (obligatoire)
- **Description**
- **Objectif**
- **Croyance à transformer**
- **Résultats attendus**
- **Livre recommandé**
- **Fichier audio**
- **Numéro d'ordre**

### 2. 🎯 **Gestion des Thèmes**
- **Créer** des thèmes dans un module sélectionné
- **Modifier** les thèmes existants
- **Supprimer** des thèmes
- **Organiser** l'ordre des thèmes

#### Champs disponibles :
- **Titre** (obligatoire)
- **Contenu** (description du thème)
- **Numéro d'ordre**

### 3. 📄 **Gestion des Cartes**
- **Créer** des cartes de contenu dans un thème sélectionné
- **Modifier** les cartes existantes
- **Supprimer** des cartes
- **Organiser** l'ordre des cartes

#### Types de cartes disponibles :
- 🎯 **Introduction** (bleu)
- 📚 **Théorie** (violet)
- 🛠️ **Pratique** (vert)
- 📖 **Ressources** (orange)
- ✨ **Conclusion** (rose)
- 📄 **Contenu général** (gris)

#### Champs disponibles :
- **Titre** (obligatoire)
- **Contenu** (obligatoire - supporte le markdown)
- **Type de carte**
- **Numéro d'ordre**

### 4. 🎯 **Gestion des Exercices**
- **Créer** des exercices dans un thème sélectionné
- **Modifier** les exercices existants
- **Supprimer** des exercices
- **Organiser** l'ordre des exercices

#### Champs disponibles :
- **Titre** (obligatoire)
- **Question principale** (obligatoire)
- **Instructions complémentaires** (optionnel)
- **Numéro d'ordre**

## 🔄 Flux de Travail Recommandé

### Étape 1 : Créer un Module
1. Allez dans l'onglet **"Modules"**
2. Cliquez sur **"Nouveau Module"**
3. Remplissez les informations du module
4. **Sauvegardez**

### Étape 2 : Créer des Thèmes
1. **Sélectionnez** le module créé (cliquez dessus)
2. Allez dans l'onglet **"Thèmes"**
3. Cliquez sur **"Nouveau Thème"**
4. Remplissez les informations du thème
5. **Sauvegardez**

### Étape 3 : Créer des Cartes
1. **Sélectionnez** le thème créé
2. Allez dans l'onglet **"Cartes"**
3. Cliquez sur **"Nouvelle Carte"**
4. Choisissez le **type de carte** approprié
5. Rédigez le **contenu** (markdown supporté)
6. **Sauvegardez**

### Étape 4 : Créer des Exercices
1. **Sélectionnez** le thème
2. Allez dans l'onglet **"Exercices"**
3. Cliquez sur **"Nouvel Exercice"**
4. Formulez la **question principale**
5. Ajoutez des **instructions** si nécessaire
6. **Sauvegardez**

## 🎨 Bonnes Pratiques

### Pour les Modules :
- Utilisez des **titres clairs** et motivants
- Définissez des **objectifs SMART**
- Numérotez logiquement (1, 2, 3...)

### Pour les Thèmes :
- **3-5 thèmes** par module idéalement
- Titres **progressifs** et logiques
- Contenu **introductif** dans la description

### Pour les Cartes :
- **Variez les types** pour un contenu riche
- Commencez par une carte **Introduction**
- Terminez par une carte **Conclusion**
- **5-10 cartes** par thème recommandé

### Pour les Exercices :
- Questions **ouvertes** et introspectives
- Instructions **claires** et bienveillantes
- **1-3 exercices** par thème recommandé

## 📖 Support Markdown

Les cartes supportent le **markdown** pour un contenu riche :

```markdown
# Titre principal
## Sous-titre
**Texte en gras**
*Texte en italique*
- Liste à puces
1. Liste numérotée
> Citation
```

## 🔒 Sécurité

- Seuls les **utilisateurs connectés** peuvent accéder au panneau
- Toutes les actions sont **loggées**
- **Confirmations** avant suppression
- **Sauvegarde automatique** des modifications

## 🆘 Résolution de Problèmes

### Problème : "Aucun module sélectionné"
**Solution** : Allez d'abord dans l'onglet "Modules" et cliquez sur un module

### Problème : "Aucun thème sélectionné" 
**Solution** : Allez dans l'onglet "Thèmes" et cliquez sur un thème

### Problème : Contenu non sauvegardé
**Solution** : Vérifiez votre connexion internet et réessayez

### Problème : Erreur lors de la création
**Solution** : Vérifiez que tous les champs obligatoires (*) sont remplis

## 📊 APIs Disponibles

Le système utilise les APIs REST suivantes :

### Modules :
- `GET /api/modules` - Liste des modules
- `POST /api/modules` - Créer un module
- `PUT /api/modules/{id}` - Modifier un module
- `DELETE /api/modules/{id}` - Supprimer un module

### Thèmes :
- `GET /api/modules/{id}/themes` - Thèmes d'un module
- `POST /api/modules/{id}/themes` - Créer un thème
- `PUT /api/themes/{id}` - Modifier un thème
- `DELETE /api/themes/{id}` - Supprimer un thème

### Cartes :
- `GET /api/themes/{id}/cards` - Cartes d'un thème
- `POST /api/themes/{id}/cards` - Créer une carte
- `PUT /api/cards/{id}` - Modifier une carte
- `DELETE /api/cards/{id}` - Supprimer une carte

### Exercices :
- `GET /api/themes/{id}/exercises` - Exercices d'un thème
- `POST /api/themes/{id}/exercises` - Créer un exercice
- `PUT /api/exercises/{id}` - Modifier un exercice
- `DELETE /api/exercises/{id}` - Supprimer un exercice

## 🎉 Félicitations !

Vous avez maintenant **toutes les clés** pour créer et gérer votre contenu de manière autonome. Le système est **intuitif**, **sécurisé** et **complet**.

**Amusez-vous** à créer du contenu inspirant pour vos utilisateurs ! 🌟 