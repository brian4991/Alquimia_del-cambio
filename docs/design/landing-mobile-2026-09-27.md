# Landing de Nicole — adaptation mobile, 27 septembre 2026

Surface : `/` et `/nicole`. Mode : Persuade. Identité : charte de couleurs et logos fournis par l'utilisateur, Playfair Display Bold pour les titres et Montserrat Regular pour le texte, photographies de Nicole et boutons arrondis. Cette version est préparée pour une publication ciblée de la landing sur main.

## Charte de marque et logos

Référence actuelle : manuel « BRANDBOOK_NR », fichier fourni `7dc0b903-1c67-456c-8c55-746f0147c949.pdf`, pages 23 et 31–32 pour les couleurs, 43–44 pour leurs applications. Les couleurs servent de référence visuelle ; le texte de la landing et les choix de typographie de l'utilisateur restent inchangés.

| Couleur | Valeur | Rôle sur la landing |
| --- | --- | --- |
| Marfil | `#EDEADF` | Fond dominant et texte sur le fond forêt |
| Salvia | `#A2A683` | Fonds des objectifs et du public concerné ; nuances dans les cartes et titres secondaires |
| Bosque | `#303E2D` | Titre principal, textes, boutons et conclusion |
| Claridad | `#99AFC1` | Sélection de texte ; nuance claire `#D1DBE3` pour le bloc de prestations |
| Terracota | `#7F4A32` | Une phrase de mise en relief après les situations vécues |
| Arena | `#B37A4B` | Petit séparateur photographique |

Les codes Marfil, Salvia, Claridad et Terracota sont ceux imprimés page 31. Bosque et Arena n'ont pas de code imprimé : les valeurs ci-dessus sont relevées dans le rendu RGB des aplats page 32. Leur conversion dépend du profil du PDF ; ce ne sont pas des codes explicitement spécifiés par le manuel.

### Application des règles d'usage (page 32)

- **Marfil, principal (60 % indiqué)** : fond de la page et des grands espaces de lecture. Les surfaces des cartes/FAQ sont une variation ivoire `#F6F3EA` ; il n'y a plus d'alternance de grands fonds blancs hors palette.
- **Salvia, secondaire (25 % indiqué)** : aplats des sections « Lo que vas a lograr » et « ¿Es para vos? ». Une nuance claire `#E2E5D5` porte les cartes d'identification et le bloc migration ; une nuance sombre `#65734F` porte les titres secondaires lisibles.
- **Bosque, profondeur (15 % indiqué)** : titre principal entièrement forêt, paragraphes et boutons. Les boutons gardent cette famille au survol/à la pression (`#233020`). Le seul grand aplat forêt est la conclusion, avec texte ivoire.
- **Claridad, complément (10 % indiqué)** : nuance claire `#D1DBE3` du bloc « ¿Qué incluye? », unique mise en avant bleue. Aucune dispersion de bleu dans les autres cartes ou les titres ; il sert aussi à la sélection de texte.
- **Terracota, accent (5 % indiqué)** : seulement la phrase « El duelo también es un proceso de adaptarte a lo nuevo mientras procesás aquello que dejaste atrás. ». Pas de grandes surfaces terracotta et pas de changement de famille des boutons au survol.
- **Arena, soutien (2 % indiqué)** : seulement le petit séparateur de la légende photographique.

Les pourcentages imprimés totalisent 117 %. Ils sont appliqués comme une hiérarchie de dominante/secondaire/accents, sans prétendre mesurer des parts exactes de pixels. La page 31 autorise une utilisation flexible des nuances : les variantes de sauge et d'ivoire conservent les teintes de la marque et assurent la lecture sur écran.

Contrastes calculés : forêt/ivoire 9,41:1 ; sauge sombre/ivoire 4,23:1 pour les grands titres gras ; texte `#303B2A` sur Salvia 4,66:1 et sur le Claridad original 5,19:1 (le fond des prestations a ensuite été éclairci) ; terracotta/ivoire 5,95:1 ; bouton au survol 11,51:1. Les petits textes restent foncés. Les logos utilisent l'association sauge/ivoire montrée page 23 ; ils ne sont pas recolorés.

Les deux JPEG fournis restent intacts dans `public/assets/landing/nicole-wordmark-brand.jpg` et `nicole-monogram-brand.jpg`. Le monogramme NR est dans l'en-tête, centré sur téléphone, et le logo horizontal dans le pied de page. Des cadres SVG avec `viewBox` masquent les marges blanches ; `mix-blend-mode: multiply` les intègre au fond ivoire. Les proportions sont conservées. Le lien d'en-tête garde son nom accessible « Nicole Ramírez · Inicio ».

## Typographie

- Playfair Display Bold, style droit à 700, est la police des titres de la landing. Elle remplace l'essai LE AMALFI à la demande de l'utilisateur. Montserrat Regular à 400 reste utilisé pour les paragraphes, les commandes, les questions de FAQ et les informations secondaires. Les emphases courtes du corps de texte gardent Montserrat Black.
- La graisse 700 de Playfair Display est déjà chargée dans `index.html` via Google Fonts, avec `display=swap`. La synthèse artificielle reste désactivée. Aucun téléchargement supplémentaire de police ni paquet ajouté ; le fichier de démonstration LE AMALFI reste uniquement dans la copie locale, hors commit, et n'est plus référencé ni chargé par la page.
- Corps de texte à 16 px et interligne 1,7, largeur de lecture limitée à 70 caractères. Titres principaux fluides de 2 à 3,35 rem, titres de section de 1,75 à 2,5 rem. Approche nulle et interligne de 1,18 pour le titre principal. Les titres des cartes d'identification restent à 1,25 rem.
- Les écarts signalés par le détecteur avec la grille globale Inter de `DESIGN.md` sont intentionnels pour cette landing : les familles et la hiérarchie sont documentées ici. Cette exception ne modifie pas le système de la plateforme connectée.

## Contenu

La nouvelle rédaction provient du fichier fourni `29e520fa-dfab-4bda-abae-67c55020de75/Texte collé.txt`. Après les ajustements demandés, les neuf sections suivent cet ordre : introduction, situations vécues, présentation de Nicole, objectifs, programme, public concerné, points différenciants, FAQ et conclusion. Le pied de page reprend les deux nouvelles lignes de présentation.

Les anciennes sections sur la compréhension du mal-être et l'appel de clarté sont remplacées par les objectifs et les critères du programme. Les quatre axes « Regular / Reconectar / Comprender / Reconstruir » sont remplacés par les quatre points différenciants fournis. Les anciens développements de FAQ et les anciennes lignes de formation ne sont pas conservés en supplément. La biographie reprend la mention TCC, ACT et EMDR telle que fournie, sans ajouter d'affirmation.

La durée reste de 17 semaines. Les cinq emplacements de réservation fournis sont présents, en plus du bouton mobile fixe existant. L'ordre des photos, les liens de réservation et de navigation, les logos, les polices et les rôles de couleurs restent conservés. Les titres de section prennent une casse de lecture plutôt que les majuscules du document. La coquille « Psicologa » est corrigée en « Psicóloga ».

Le titre SEO et la meta description fournis sont renseignés dans `frontend/index.html`, sans apparaître comme contenu dans la page. Le H1 reste unique et identique au texte demandé.

Les ajustements finaux placent la spécialité en petit au-dessus du H1, puis « Soy Nicole Ramírez » juste avant « Lo que vas a lograr ». La phrase sur le deuil et celle sur le travail entre les séances sont centrées avec leur bouton de réservation. Le bloc « ¿Qué incluye? » utilise désormais le bleu éclairci `#D1DBE3`. Les liens Instagram et TikTok `@nicoleramirezpsicologa` figurent sous le courriel dans le pied de page et ouvrent un nouvel onglet.

## Parcours mobile et composants

- En-tête réduit à l'identité sur téléphone ; navigation supplémentaire sur ordinateur. L'accès au programme reste dans le pied de page, conformément à la suppression du bouton d'en-tête demandée.
- Message et réservation avant la photo. La photo de Nicole à son bureau ouvre la page ; le portrait debout accompagne « Soy Nicole Ramírez ».
- Les composants shadcn/ui existants sont réutilisés : `Card`, `CardHeader`, `CardTitle`, `CardContent`, `Button` et `Accordion`. Aucun nouveau paquet ni modification des composants partagés.
- Les six situations sont présentées sur des cartes sauge clair. Les quatre points différenciants occupent des cartes ivoire clair, arrondies, avec une ombre légère ; une colonne sur téléphone et deux à partir de 600 px.
- Le bloc « ¿Qué incluye? » utilise une nuance claire du bleu Claridad, avec une liste de prestations bien séparées. Sur ordinateur, il accompagne la présentation du programme à droite.
- La FAQ utilise l'accordéon Radix/shadcn : plusieurs réponses peuvent rester ouvertes, les déclencheurs sont utilisables au clavier et leur focus est visible.
- Le bouton « Reserva una llamada de claridad » utilise `Button` avec `asChild` pour conserver un vrai lien vers le Calendly existant. Navigation dans le même onglet, sans popup ni intégration tierce chargée sur la landing.
- Un bouton fixe apparaît après le défilement du premier appel à l'action, et s'efface lorsque celui de conclusion devient visible. Il respecte la zone de sécurité inférieure du téléphone ; le pied de page garde un espace suffisant.
- Les styles sont limités à `.nicole-landing` et aux classes préfixées `nl-`. Aucun changement des exercices, des rendez-vous ou de la landing du séjour. Les préférences de réduction des animations sont respectées.

## Ressources

Les originaux fournis restent intacts. Les variantes WebP distribuées par cette page sont :

| Ressource | Dimensions | Taille |
| --- | --- | --- |
| Nicole au bureau, mobile | 480 × 312 | 15 170 octets |
| Nicole au bureau, haute résolution | 960 × 625 | 43 802 octets |
| Portrait debout, mobile | 480 × 720 | 23 610 octets |
| Portrait debout, haute résolution | 960 × 1440 | 67 792 octets |

Les deux photographies utilisent `srcset`. La seconde est chargée à la demande ; son cadrage garde le visage visible. Les variantes sont des redimensionnements/compressions des photographies fournies, sans génération de visage ni retouche créative.

L'entrée locale `frontend/iphone-preview.html` affiche la vraie landing dans un cadre de téléphone avec un viewport interne de 390 px. C'est une simulation visuelle Chromium, pas un émulateur Safari/iOS. Cette entrée n'est pas ajoutée au build de production.

## Validation de cette présentation shadcn

- ESLint et compilation de production réussis ; `git diff --check` sans erreur de contenu.
- Contrôles Chromium à 320, 768 et 1440 px sans débordement horizontal, plus inspection de l'aperçu iPhone à 390 px.
- Composition des cartes inspectée sur téléphone, tablette et ordinateur. Les boutons se mettent sur plusieurs lignes au besoin : 56 px de haut sur ordinateur, 72 px sur l'écran de 320 px.
- Ouverture et fermeture de la FAQ au clavier vérifiées ; focus de 3 px visible. Réponse mobile vérifiée dans l'aperçu iPhone.
- Photographies chargées dans l'ordre demandé. Lien de réservation conservé sur toutes les actions. Aucune erreur ni avertissement de console dans l'onglet de contrôle.
- Les contrastes de cette première présentation shadcn ont ensuite été revérifiés avec la palette de marque ci-dessus.
- Aucun test sur un appareil physique, Safari iOS ou le navigateur intégré de TikTok.

Le parcours Calendly avait été consulté lors de la première livraison jusqu'aux questions précédant la confirmation. Aucune donnée saisie, aucun rendez-vous réservé ; ce contrôle externe n'a pas été répété pour la présentation shadcn.

## Point externe à harmoniser

Le lien existant est `https://calendly.com/contacto-nicoleramirezpsicoach/24horas`. Lors de sa consultation précédente, il affichait bien « Llamada de Claridad » et des questions avant confirmation, mais sa description indiquait encore 15 semaines et l'une de ses questions 16 semaines. Ces textes externes restent à aligner avec les 17 semaines du texte fourni. Cette livraison ne modifie pas le compte Calendly.
## Publication indépendante sur main

La landing finale du commit local `22e6be3` est transférée sur `ce9a7fb` (main), sans les commits intermédiaires du programme, de ses exercices ou de Google Calendar. Les composants shadcn et leurs dépendances existent déjà sur cette base ; aucun paquet ni changement de backend n'est nécessaire.

Deux adaptations assurent son autonomie : les styles du lien « Saltar al contenido » sont intégrés au CSS de la landing ; les pages publiques `/informacion` et `/privacidad` sont portées dans `LandingInformation.jsx` avec leurs deux routes. Ces pages reprennent les informations applicables à main, sans importer les services de suivi, les brouillons ou la synchronisation Calendar encore locaux. Les routes protégées restent inchangées.

Validation de cette intégration : installation avec le lockfile de main, build Vite 5 réussi, ESLint ciblé réussi. Vérification Chromium à 1440 et 390 px sans débordement, chargement des photos, FAQ au clavier, liens Calendly conservés et navigation vers les informations, la confidentialité et la connexion. Aucune erreur de console dans ces parcours. Le build signale la taille du bundle historique et des données de compatibilité anciennes ; les dépendances du programme ne sont pas modifiées dans cette publication.
