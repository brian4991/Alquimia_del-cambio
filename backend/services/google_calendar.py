"""
Google Calendar API Service
Handles OAuth2 flow and calendar operations for admin appointments
"""
import os
from datetime import datetime, timedelta
from typing import List, Optional, Dict
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sqlalchemy.orm import Session

from models import AdminCalendarSettings


# Google Calendar API scopes
SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events'
]

# OAuth2 configuration
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = os.getenv('CALENDAR_REDIRECT_URI', 'http://localhost:8000/admin/calendar/callback')


class GoogleCalendarService:
    """Service to interact with Google Calendar API"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_authorization_url(self, admin_id: int) -> str:
        """
        Generate Google OAuth2 authorization URL for calendar access
        
        Args:
            admin_id: ID of the admin user
            
        Returns:
            Authorization URL to redirect the admin to
        """
        from google_auth_oauthlib.flow import Flow
        
        flow = Flow.from_client_config(
            {
                "web": {
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": [REDIRECT_URI]
                }
            },
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        
        # Add state parameter to verify callback
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent',
            state=str(admin_id)
        )
        
        return authorization_url
    
    def handle_oauth_callback(self, code: str, admin_id: int) -> bool:
        """
        Handle OAuth2 callback and store credentials
        
        Args:
            code: Authorization code from Google
            admin_id: ID of the admin user
            
        Returns:
            True if successful, False otherwise
        """
        try:
            import requests
            
            # Exchange code for tokens directly (avoid scope mismatch issues)
            token_response = requests.post(
                'https://oauth2.googleapis.com/token',
                data={
                    'code': code,
                    'client_id': GOOGLE_CLIENT_ID,
                    'client_secret': GOOGLE_CLIENT_SECRET,
                    'redirect_uri': REDIRECT_URI,
                    'grant_type': 'authorization_code'
                }
            )
            
            if token_response.status_code != 200:
                print(f"Token exchange failed: {token_response.text}")
                return False
            
            tokens = token_response.json()
            
            access_token = tokens.get('access_token')
            refresh_token = tokens.get('refresh_token')
            expires_in = tokens.get('expires_in', 3600)
            
            # Calculate expiry
            from datetime import datetime, timedelta
            token_expiry = datetime.utcnow() + timedelta(seconds=expires_in)
            
            # Store or update settings
            settings = self.db.query(AdminCalendarSettings).filter(
                AdminCalendarSettings.admin_id == admin_id
            ).first()
            
            if settings:
                settings.google_refresh_token = refresh_token or settings.google_refresh_token
                settings.google_access_token = access_token
                settings.token_expiry = token_expiry
            else:
                settings = AdminCalendarSettings(
                    admin_id=admin_id,
                    google_refresh_token=refresh_token,
                    google_access_token=access_token,
                    token_expiry=token_expiry
                )
                self.db.add(settings)
            
            self.db.commit()
            return True
            
        except Exception as e:
            print(f"Error handling OAuth callback: {e}")
            return False
    
    def get_credentials(self, admin_id: int) -> Optional[Credentials]:
        """
        Get valid credentials for an admin
        
        Args:
            admin_id: ID of the admin user
            
        Returns:
            Valid Credentials object or None
        """
        settings = self.db.query(AdminCalendarSettings).filter(
            AdminCalendarSettings.admin_id == admin_id
        ).first()
        
        if not settings or not settings.google_refresh_token:
            return None
        
        credentials = Credentials(
            token=settings.google_access_token,
            refresh_token=settings.google_refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=GOOGLE_CLIENT_ID,
            client_secret=GOOGLE_CLIENT_SECRET,
            scopes=SCOPES
        )
        
        # Refresh if expired
        if credentials.expired:
            try:
                credentials.refresh(Request())
                settings.google_access_token = credentials.token
                settings.token_expiry = credentials.expiry
                self.db.commit()
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                return None
        
        return credentials
    
    def get_available_slots(
        self, 
        admin_id: int, 
        start_date: datetime, 
        end_date: datetime
    ) -> List[Dict]:
        """
        Get available time slots for booking based on admin's calendar
        
        Args:
            admin_id: ID of the admin user
            start_date: Start of the date range
            end_date: End of the date range
            
        Returns:
            List of available time slots
        """
        credentials = self.get_credentials(admin_id)
        if not credentials:
            return []
        
        settings = self.db.query(AdminCalendarSettings).filter(
            AdminCalendarSettings.admin_id == admin_id
        ).first()
        
        if not settings:
            return []
        
        try:
            service = build('calendar', 'v3', credentials=credentials)
            
            # Get busy times from calendar
            body = {
                "timeMin": start_date.isoformat() + 'Z',
                "timeMax": end_date.isoformat() + 'Z',
                "items": [{"id": settings.calendar_id or "primary"}]
            }
            
            events_result = service.freebusy().query(body=body).execute()
            busy_times = events_result['calendars'][settings.calendar_id or "primary"]['busy']
            
            # Generate available slots
            available_slots = []
            slot_duration = timedelta(minutes=settings.slot_duration)
            buffer = timedelta(minutes=settings.availability_buffer)
            
            # Start from now + buffer or start_date (whichever is later)
            current_time = max(datetime.utcnow() + buffer, start_date)
            
            # Working hours: 9 AM to 6 PM (can be made configurable)
            while current_time < end_date:
                # Skip weekends
                if current_time.weekday() >= 5:  # 5=Saturday, 6=Sunday
                    current_time += timedelta(days=1)
                    current_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
                    continue
                
                # Only check during working hours
                if current_time.hour < 9:
                    current_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
                    continue
                elif current_time.hour >= 18:
                    current_time += timedelta(days=1)
                    current_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
                    continue
                
                slot_end = current_time + slot_duration
                
                # Check if slot conflicts with busy times
                is_available = True
                for busy in busy_times:
                    busy_start = datetime.fromisoformat(busy['start'].replace('Z', '+00:00'))
                    busy_end = datetime.fromisoformat(busy['end'].replace('Z', '+00:00'))
                    
                    if (current_time < busy_end and slot_end > busy_start):
                        is_available = False
                        break
                
                if is_available:
                    available_slots.append({
                        'start': current_time.isoformat(),
                        'end': slot_end.isoformat(),
                        'duration_minutes': settings.slot_duration
                    })
                
                # Move to next slot (30 min intervals)
                current_time += timedelta(minutes=30)
            
            return available_slots
            
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []
    
    def create_calendar_event(
        self,
        admin_id: int,
        start_time: datetime,
        end_time: datetime,
        summary: str,
        description: str = "",
        attendee_email: Optional[str] = None
    ) -> Optional[str]:
        """
        Create a calendar event
        
        Args:
            admin_id: ID of the admin user
            start_time: Event start time
            end_time: Event end time
            summary: Event title
            description: Event description
            attendee_email: Optional attendee email
            
        Returns:
            Event ID if successful, None otherwise
        """
        credentials = self.get_credentials(admin_id)
        if not credentials:
            return None
        
        settings = self.db.query(AdminCalendarSettings).filter(
            AdminCalendarSettings.admin_id == admin_id
        ).first()
        
        if not settings:
            return None
        
        try:
            service = build('calendar', 'v3', credentials=credentials)
            
            event = {
                'summary': summary,
                'description': description,
                'start': {
                    'dateTime': start_time.isoformat(),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': end_time.isoformat(),
                    'timeZone': 'UTC',
                },
            }
            
            if attendee_email:
                event['attendees'] = [{'email': attendee_email}]
            
            event = service.events().insert(
                calendarId=settings.calendar_id or "primary",
                body=event
            ).execute()
            
            return event.get('id')
            
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
    
    def delete_calendar_event(self, admin_id: int, event_id: str) -> bool:
        """
        Delete a calendar event
        
        Args:
            admin_id: ID of the admin user
            event_id: Google Calendar event ID
            
        Returns:
            True if successful, False otherwise
        """
        credentials = self.get_credentials(admin_id)
        if not credentials:
            return False
        
        settings = self.db.query(AdminCalendarSettings).filter(
            AdminCalendarSettings.admin_id == admin_id
        ).first()
        
        if not settings:
            return False
        
        try:
            service = build('calendar', 'v3', credentials=credentials)
            service.events().delete(
                calendarId=settings.calendar_id or "primary",
                eventId=event_id
            ).execute()
            return True
            
        except HttpError as error:
            print(f"An error occurred: {error}")
            return False

