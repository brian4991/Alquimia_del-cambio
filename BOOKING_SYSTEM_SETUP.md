# Système de Rendez-vous avec Google Calendar - Guide de Configuration

## Installation Complète

Tous les fichiers ont été créés. Suivez ces étapes pour activer le système de rendez-vous:

## 1. Backend - Installation des dépendances

```bash
cd backend
pip install -r requirements.txt
```

Les nouvelles dépendances installées:
- `google-api-python-client`: API Google Calendar
- `google-auth-httplib2`: Authentification Google
- `google-auth-oauthlib`: OAuth2 pour Google

## 2. Migration de la base de données

Créer les nouvelles tables `appointments` et `admin_calendar_settings`:

```bash
python migrate_appointments.py
```

Ou redémarrer le backend (les tables seront créées automatiquement au démarrage):

```bash
python main.py
```

## 3. Configuration des variables d'environnement

Ajoutez ces variables dans `backend/.env`:

```env
# Configuration Email (pour les notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre-email@gmail.com
SMTP_PASSWORD=votre-mot-de-passe-app
FROM_EMAIL=votre-email@gmail.com

# Google Calendar OAuth (utiliser les mêmes credentials que pour l'auth Google)
GOOGLE_CLIENT_ID=votre-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=votre-client-secret
CALENDAR_REDIRECT_URI=http://localhost:8000/admin/calendar/callback

# Pour la production (Railway)
# CALENDAR_REDIRECT_URI=https://votre-backend.railway.app/admin/calendar/callback
```

### Configuration SMTP Gmail

Pour Gmail, utilisez un "App Password":
1. Allez sur https://myaccount.google.com/security
2. Activez la validation en 2 étapes
3. Créez un "App Password" pour l'application
4. Utilisez ce mot de passe dans `SMTP_PASSWORD`

## 4. Configuration Google OAuth

Le système utilise les mêmes credentials OAuth que pour l'authentification Google existante. Il faut simplement ajouter les scopes supplémentaires:

### Dans Google Cloud Console:

1. Allez sur https://console.cloud.google.com/
2. Sélectionnez votre projet
3. APIs & Services → OAuth consent screen
4. Ajoutez les scopes:
   - `https://www.googleapis.com/auth/calendar.readonly`
   - `https://www.googleapis.com/auth/calendar.events`

### Ajoutez les redirect URIs:

Dans "Credentials" → votre OAuth Client ID → "Authorized redirect URIs":
- `http://localhost:8000/admin/calendar/callback` (local)
- `https://votre-backend.railway.app/admin/calendar/callback` (production)

## 5. Frontend - Aucune installation requise

Les composants React utilisent uniquement les dépendances déjà présentes (Heroicons, React Router).

## 6. Test du système

### A. En tant qu'Admin:

1. Connectez-vous en tant qu'admin
2. Allez sur "Panel Admin" → onglet "Rendez-vous"
3. Cliquez sur "Paramètres" → "Connecter" Google Calendar
4. Autorisez l'accès à votre Google Calendar
5. Configurez la durée des créneaux (30, 60, 90 min)
6. Configurez le délai minimum avant réservation

### B. En tant qu'User:

1. Connectez-vous en tant qu'utilisateur normal
2. Cliquez sur "Rendez-vous" dans le menu
3. Vous verrez les créneaux disponibles basés sur le calendrier de l'admin
4. Sélectionnez un créneau et réservez
5. Vous recevrez un email de confirmation

### C. Notifications:

- **User réserve** → Admin reçoit un email + notification in-app
- **Admin confirme** → User reçoit un email de confirmation
- **Admin annule** → User reçoit un email d'annulation
- **User annule** → L'événement est supprimé du Google Calendar

## 7. Fonctionnalités

### Pour les Users:
- Voir les créneaux disponibles (synchronisés avec Google Calendar de l'admin)
- Réserver un rendez-vous
- Ajouter des notes lors de la réservation
- Voir leurs rendez-vous (en attente, confirmés, annulés)
- Annuler leurs rendez-vous

### Pour l'Admin:
- Connecter Google Calendar
- Configurer la durée des créneaux
- Configurer le délai minimum avant réservation
- Voir tous les rendez-vous
- Filtrer par statut (tous, en attente, confirmés, annulés)
- Badge avec le nombre de demandes en attente
- Confirmer ou annuler des rendez-vous
- Synchronisation automatique avec Google Calendar

## 8. Architecture

### Backend:
- **Models**: `Appointment`, `AdminCalendarSettings` (dans `backend/models.py`)
- **Routes**: `backend/routes/appointments.py` (14 endpoints)
- **Services**:
  - `backend/services/google_calendar.py` (intégration Google Calendar)
  - `backend/services/email.py` (envoi d'emails)

### Frontend:
- **BookingPage.jsx**: Page de réservation pour les users
- **AdminAppointments.jsx**: Gestion des RDV pour l'admin
- Intégré dans `App.jsx`, `AdminPanel.jsx`, `Layout.jsx`

## 9. Routes API disponibles

### User endpoints:
- `GET /appointments/availability` - Obtenir les créneaux disponibles
- `POST /appointments/book` - Réserver un rendez-vous
- `GET /appointments/my` - Mes rendez-vous
- `DELETE /appointments/{id}` - Annuler mon rendez-vous

### Admin endpoints:
- `GET /admin/calendar/connect` - Obtenir l'URL OAuth Google
- `GET /admin/calendar/callback` - Callback OAuth
- `GET /admin/calendar/settings` - Paramètres du calendrier
- `PUT /admin/calendar/settings` - Mettre à jour les paramètres
- `POST /admin/calendar/disconnect` - Déconnecter Google Calendar
- `GET /admin/appointments` - Tous les rendez-vous (filtrable par status)
- `GET /admin/appointments/count` - Nombre de rendez-vous en attente
- `PUT /admin/appointments/{id}/status` - Confirmer/annuler un rendez-vous
- `GET /admin/appointments/{id}` - Détails d'un rendez-vous

## 10. Troubleshooting

### Les créneaux ne s'affichent pas:
- Vérifiez que l'admin a bien connecté Google Calendar
- Vérifiez les scopes OAuth (calendar.readonly, calendar.events)
- Vérifiez les logs backend pour les erreurs d'API Google

### Les emails ne s'envoient pas:
- Vérifiez les variables SMTP dans .env
- Pour Gmail, utilisez un App Password (pas le mot de passe normal)
- Vérifiez les logs backend

### Erreur OAuth:
- Vérifiez que les redirect URIs sont correctement configurés
- Vérifiez que les credentials Google sont valides
- Vérifiez que les scopes sont autorisés

## 11. Production (Railway)

Ajoutez ces variables d'environnement dans Railway:

```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre-email@gmail.com
SMTP_PASSWORD=votre-app-password
FROM_EMAIL=votre-email@gmail.com
CALENDAR_REDIRECT_URI=https://votre-backend.railway.app/admin/calendar/callback
```

Et mettez à jour les redirect URIs dans Google Cloud Console.

## 12. Sécurité

- Les tokens Google sont stockés chiffrés dans la base de données
- Les refresh tokens permettent de maintenir l'accès sans re-authentification
- Les emails sont envoyés uniquement aux utilisateurs concernés
- Seuls les admins peuvent voir tous les rendez-vous

---

## Support

Le système est maintenant complètement fonctionnel et prêt à être utilisé!

