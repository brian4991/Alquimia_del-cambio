"""
Google Calendar API Service
Handles OAuth2 flow and calendar operations for admin appointments
"""
import os
from datetime import datetime, timedelta, timezone
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
            
            # Format dates properly for Google Calendar API
            # Remove any existing timezone info and format as RFC3339
            time_min = start_date.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
            time_max = end_date.strftime('%Y-%m-%dT%H:%M:%S') + 'Z'
            
            print(f"[CALENDAR] Querying freeBusy: timeMin={time_min}, timeMax={time_max}")
            
            # Get busy times from calendar
            body = {
                "timeMin": time_min,
                "timeMax": time_max,
                "items": [{"id": settings.calendar_id or "primary"}]
            }
            
            events_result = service.freebusy().query(body=body).execute()
            busy_times = events_result['calendars'][settings.calendar_id or "primary"]['busy']
            print(f"[CALENDAR] Found {len(busy_times)} busy periods")
            for i, busy in enumerate(busy_times):
                print(f"[CALENDAR] Busy {i}: {busy['start']} -> {busy['end']}")
            
            # Generate available slots
            available_slots = []
            slot_duration = timedelta(minutes=settings.slot_duration)
            buffer = timedelta(minutes=settings.availability_buffer)
            
            # Make start_date naive (remove timezone info) for comparison
            if hasattr(start_date, 'tzinfo') and start_date.tzinfo is not None:
                start_date = start_date.replace(tzinfo=None)
            if hasattr(end_date, 'tzinfo') and end_date.tzinfo is not None:
                end_date = end_date.replace(tzinfo=None)
            
            # Start from now + buffer or start_date (whichever is later)
            now_plus_buffer = datetime.utcnow() + buffer
            current_time = max(now_plus_buffer, start_date)
            
            # Round to next hour for cleaner slots
            if current_time.minute > 0:
                current_time = current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
            
            # Generate slots for all days and hours (no restrictions)
            while current_time < end_date:
                slot_end = current_time + slot_duration
                
                # Check if slot conflicts with busy times
                is_available = True
                for busy in busy_times:
                    # Parse busy times - handle both Z and +offset formats
                    busy_start_str = busy['start']
                    busy_end_str = busy['end']
                    
                    # Convert to datetime and make naive (UTC)
                    if busy_start_str.endswith('Z'):
                        busy_start = datetime.fromisoformat(busy_start_str.replace('Z', '+00:00'))
                    else:
                        busy_start = datetime.fromisoformat(busy_start_str)
                    
                    if busy_end_str.endswith('Z'):
                        busy_end = datetime.fromisoformat(busy_end_str.replace('Z', '+00:00'))
                    else:
                        busy_end = datetime.fromisoformat(busy_end_str)
                    
                    # Convert to UTC naive for comparison
                    if busy_start.tzinfo is not None:
                        busy_start = busy_start.astimezone(timezone.utc).replace(tzinfo=None)
                    if busy_end.tzinfo is not None:
                        busy_end = busy_end.astimezone(timezone.utc).replace(tzinfo=None)
                    
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

