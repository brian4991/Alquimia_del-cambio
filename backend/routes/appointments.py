from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel

from auth import get_current_user, get_current_admin_user
from database import get_db
from models import User, Appointment, AdminCalendarSettings
from services.google_calendar import GoogleCalendarService
from services.email import EmailService


router = APIRouter(tags=["appointments"])


# ============================================
# PUBLIC ROUTES
# ============================================

@router.get("/appointments/admin-info")
def get_admin_info(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get the admin user info for booking (any authenticated user can access)"""
    admin = db.query(User).filter(User.role == "admin").first()
    
    if not admin:
        raise HTTPException(status_code=404, detail="No admin found")
    
    # Check if admin has calendar connected
    settings = db.query(AdminCalendarSettings).filter(
        AdminCalendarSettings.admin_id == admin.id
    ).first()
    
    return {
        "admin_id": admin.id,
        "admin_name": admin.username,
        "has_calendar": settings is not None and settings.google_refresh_token is not None
    }


# Pydantic schemas
class AppointmentCreate(BaseModel):
    admin_id: int
    start_time: str  # ISO format datetime
    end_time: str
    notes: Optional[str] = None


class AppointmentUpdate(BaseModel):
    status: str  # pending, confirmed, cancelled


class AppointmentResponse(BaseModel):
    id: int
    user_id: int
    user_name: str
    user_email: str
    admin_id: int
    admin_name: str
    start_time: str
    end_time: str
    status: str
    notes: Optional[str]
    created_at: str
    
    class Config:
        from_attributes = True


class AvailabilitySlot(BaseModel):
    start: str
    end: str
    duration_minutes: int


class CalendarSettingsResponse(BaseModel):
    has_calendar_connected: bool
    slot_duration: int
    availability_buffer: int


class CalendarSettingsUpdate(BaseModel):
    slot_duration: Optional[int] = None
    availability_buffer: Optional[int] = None


# ============================================
# ADMIN CALENDAR SETUP ROUTES
# ============================================

@router.get("/admin/calendar/connect")
def connect_google_calendar(
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Generate OAuth URL for admin to connect Google Calendar"""
    calendar_service = GoogleCalendarService(db)
    auth_url = calendar_service.get_authorization_url(current_admin.id)
    
    return {
        "authorization_url": auth_url,
        "message": "Redirect admin to this URL to authorize calendar access"
    }


@router.get("/admin/calendar/callback")
def google_calendar_callback(
    code: str = Query(...),
    state: str = Query(...),
    db: Session = Depends(get_db)
):
    """Handle OAuth callback from Google"""
    from fastapi.responses import RedirectResponse
    import os
    
    frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:5173')
    
    try:
        admin_id = int(state)
        calendar_service = GoogleCalendarService(db)
        
        success = calendar_service.handle_oauth_callback(code, admin_id)
        
        if success:
            # Redirect to admin panel with success message
            return RedirectResponse(url=f"{frontend_url}/admin?calendar=connected")
        else:
            return RedirectResponse(url=f"{frontend_url}/admin?calendar=error")
            
    except Exception as e:
        print(f"Calendar callback error: {e}")
        return RedirectResponse(url=f"{frontend_url}/admin?calendar=error")


@router.get("/admin/calendar/settings", response_model=CalendarSettingsResponse)
def get_calendar_settings(
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get admin's calendar settings"""
    settings = db.query(AdminCalendarSettings).filter(
        AdminCalendarSettings.admin_id == current_admin.id
    ).first()
    
    if settings:
        return CalendarSettingsResponse(
            has_calendar_connected=settings.google_refresh_token is not None,
            slot_duration=settings.slot_duration,
            availability_buffer=settings.availability_buffer
        )
    else:
        return CalendarSettingsResponse(
            has_calendar_connected=False,
            slot_duration=60,
            availability_buffer=60
        )


@router.put("/admin/calendar/settings")
def update_calendar_settings(
    settings_update: CalendarSettingsUpdate,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Update admin's calendar settings"""
    settings = db.query(AdminCalendarSettings).filter(
        AdminCalendarSettings.admin_id == current_admin.id
    ).first()
    
    if not settings:
        settings = AdminCalendarSettings(admin_id=current_admin.id)
        db.add(settings)
    
    if settings_update.slot_duration is not None:
        settings.slot_duration = settings_update.slot_duration
    if settings_update.availability_buffer is not None:
        settings.availability_buffer = settings_update.availability_buffer
    
    db.commit()
    
    return {"message": "Settings updated successfully"}


@router.post("/admin/calendar/disconnect")
def disconnect_google_calendar(
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Disconnect Google Calendar"""
    settings = db.query(AdminCalendarSettings).filter(
        AdminCalendarSettings.admin_id == current_admin.id
    ).first()
    
    if settings:
        settings.google_refresh_token = None
        settings.google_access_token = None
        settings.token_expiry = None
        db.commit()
    
    return {"message": "Calendar disconnected successfully"}


# ============================================
# AVAILABILITY ROUTES
# ============================================

@router.get("/appointments/availability")
def get_available_slots(
    admin_id: int = Query(...),
    start_date: str = Query(...),  # ISO format
    end_date: str = Query(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get available time slots for booking"""
    try:
        start_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")
    
    calendar_service = GoogleCalendarService(db)
    slots = calendar_service.get_available_slots(admin_id, start_dt, end_dt)
    
    return {
        "slots": slots,
        "admin_id": admin_id,
        "start_date": start_date,
        "end_date": end_date
    }


# ============================================
# APPOINTMENT BOOKING ROUTES (USER)
# ============================================

@router.post("/appointments/book")
def book_appointment(
    appointment: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Book an appointment with admin"""
    # Verify admin exists
    admin = db.query(User).filter(
        User.id == appointment.admin_id,
        User.role == "admin"
    ).first()
    
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    # Parse datetime
    try:
        start_dt = datetime.fromisoformat(appointment.start_time.replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(appointment.end_time.replace('Z', '+00:00'))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format")
    
    # Check if slot is still available (no overlapping appointments)
    overlapping = db.query(Appointment).filter(
        Appointment.admin_id == appointment.admin_id,
        Appointment.status.in_(["pending", "confirmed"]),
        or_(
            and_(Appointment.start_time <= start_dt, Appointment.end_time > start_dt),
            and_(Appointment.start_time < end_dt, Appointment.end_time >= end_dt),
            and_(Appointment.start_time >= start_dt, Appointment.end_time <= end_dt)
        )
    ).first()
    
    if overlapping:
        raise HTTPException(status_code=409, detail="This time slot is no longer available")
    
    # Create appointment
    new_appointment = Appointment(
        user_id=current_user.id,
        admin_id=appointment.admin_id,
        start_time=start_dt,
        end_time=end_dt,
        notes=appointment.notes,
        status="pending"
    )
    
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    
    # Create Google Calendar event
    calendar_service = GoogleCalendarService(db)
    event_id = calendar_service.create_calendar_event(
        admin_id=appointment.admin_id,
        start_time=start_dt,
        end_time=end_dt,
        summary=f"Rendez-vous avec {current_user.username}",
        description=f"Rendez-vous demandé par {current_user.username}\n\nNotes: {appointment.notes or 'Aucune'}",
        attendee_email=current_user.email
    )
    
    if event_id:
        new_appointment.google_event_id = event_id
        db.commit()
    
    # Send email notifications
    EmailService.send_new_appointment_to_admin(
        admin_email=admin.email,
        admin_name=admin.username,
        user_name=current_user.username,
        user_email=current_user.email,
        start_time=start_dt,
        end_time=end_dt,
        notes=appointment.notes
    )
    
    EmailService.send_appointment_confirmation_to_user(
        user_email=current_user.email,
        user_name=current_user.username,
        admin_name=admin.username,
        start_time=start_dt,
        end_time=end_dt,
        status="pending"
    )
    
    return {
        "message": "Appointment booked successfully",
        "appointment_id": new_appointment.id,
        "status": "pending"
    }


@router.get("/appointments/my", response_model=List[AppointmentResponse])
def get_my_appointments(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user's appointments"""
    appointments = db.query(Appointment).filter(
        Appointment.user_id == current_user.id
    ).order_by(Appointment.start_time.desc()).all()
    
    result = []
    for apt in appointments:
        admin = db.query(User).filter(User.id == apt.admin_id).first()
        result.append(AppointmentResponse(
            id=apt.id,
            user_id=apt.user_id,
            user_name=current_user.username,
            user_email=current_user.email,
            admin_id=apt.admin_id,
            admin_name=admin.username if admin else "Unknown",
            start_time=apt.start_time.isoformat(),
            end_time=apt.end_time.isoformat(),
            status=apt.status,
            notes=apt.notes,
            created_at=apt.created_at.isoformat()
        ))
    
    return result


@router.delete("/appointments/{appointment_id}")
def cancel_my_appointment(
    appointment_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cancel user's own appointment"""
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.user_id == current_user.id
    ).first()
    
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    # Can only cancel if not already cancelled
    if appointment.status == "cancelled":
        raise HTTPException(status_code=400, detail="Appointment already cancelled")
    
    appointment.status = "cancelled"
    db.commit()
    
    # Delete from Google Calendar
    if appointment.google_event_id:
        calendar_service = GoogleCalendarService(db)
        calendar_service.delete_calendar_event(appointment.admin_id, appointment.google_event_id)
    
    # Send notification
    admin = db.query(User).filter(User.id == appointment.admin_id).first()
    if admin:
        EmailService.send_appointment_confirmation_to_user(
            user_email=current_user.email,
            user_name=current_user.username,
            admin_name=admin.username,
            start_time=appointment.start_time,
            end_time=appointment.end_time,
            status="cancelled"
        )
    
    return {"message": "Appointment cancelled successfully"}


# ============================================
# ADMIN APPOINTMENT MANAGEMENT ROUTES
# ============================================

@router.get("/admin/appointments", response_model=List[AppointmentResponse])
def get_all_appointments(
    status: Optional[str] = Query(None),
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get all appointments for admin"""
    query = db.query(Appointment).filter(Appointment.admin_id == current_admin.id)
    
    if status:
        query = query.filter(Appointment.status == status)
    
    appointments = query.order_by(Appointment.start_time.desc()).all()
    
    result = []
    for apt in appointments:
        user = db.query(User).filter(User.id == apt.user_id).first()
        result.append(AppointmentResponse(
            id=apt.id,
            user_id=apt.user_id,
            user_name=user.username if user else "Unknown",
            user_email=user.email if user else "Unknown",
            admin_id=apt.admin_id,
            admin_name=current_admin.username,
            start_time=apt.start_time.isoformat(),
            end_time=apt.end_time.isoformat(),
            status=apt.status,
            notes=apt.notes,
            created_at=apt.created_at.isoformat()
        ))
    
    return result


@router.get("/admin/appointments/count")
def get_pending_appointments_count(
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get count of pending appointments (for badge)"""
    count = db.query(Appointment).filter(
        Appointment.admin_id == current_admin.id,
        Appointment.status == "pending"
    ).count()
    
    return {"pending_count": count}


@router.put("/admin/appointments/{appointment_id}/status")
def update_appointment_status(
    appointment_id: int,
    status_update: AppointmentUpdate,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Update appointment status (confirm/cancel)"""
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.admin_id == current_admin.id
    ).first()
    
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    # Validate status
    if status_update.status not in ["pending", "confirmed", "cancelled"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    old_status = appointment.status
    appointment.status = status_update.status
    db.commit()
    
    # If cancelling, delete from Google Calendar
    if status_update.status == "cancelled" and appointment.google_event_id:
        calendar_service = GoogleCalendarService(db)
        calendar_service.delete_calendar_event(appointment.admin_id, appointment.google_event_id)
    
    # Send notification to user
    user = db.query(User).filter(User.id == appointment.user_id).first()
    if user and old_status != status_update.status:
        EmailService.send_appointment_confirmation_to_user(
            user_email=user.email,
            user_name=user.username,
            admin_name=current_admin.username,
            start_time=appointment.start_time,
            end_time=appointment.end_time,
            status=status_update.status
        )
    
    return {
        "message": f"Appointment status updated to {status_update.status}",
        "appointment_id": appointment_id,
        "status": status_update.status
    }


@router.get("/admin/appointments/{appointment_id}", response_model=AppointmentResponse)
def get_appointment_details(
    appointment_id: int,
    current_admin: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get detailed appointment information"""
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.admin_id == current_admin.id
    ).first()
    
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    user = db.query(User).filter(User.id == appointment.user_id).first()
    
    return AppointmentResponse(
        id=appointment.id,
        user_id=appointment.user_id,
        user_name=user.username if user else "Unknown",
        user_email=user.email if user else "Unknown",
        admin_id=appointment.admin_id,
        admin_name=current_admin.username,
        start_time=appointment.start_time.isoformat(),
        end_time=appointment.end_time.isoformat(),
        status=appointment.status,
        notes=appointment.notes,
        created_at=appointment.created_at.isoformat()
    )

