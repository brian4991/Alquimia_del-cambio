"""
Email Service for Appointment Notifications
Handles sending email notifications to admin and users
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Optional


# Email configuration from environment variables
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
FROM_EMAIL = os.getenv('FROM_EMAIL', SMTP_USER)
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5173')


class EmailService:
    """Service to send email notifications"""
    
    @staticmethod
    def _send_email(to_email: str, subject: str, html_body: str, text_body: str = "") -> bool:
        """
        Send an email
        
        Args:
            to_email: Recipient email address
            subject: Email subject
            html_body: HTML content of the email
            text_body: Plain text fallback
            
        Returns:
            True if successful, False otherwise
        """
        if not SMTP_USER or not SMTP_PASSWORD:
            print("Email not configured. Set SMTP_USER and SMTP_PASSWORD in environment.")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = FROM_EMAIL
            msg['To'] = to_email
            
            # Attach text and HTML versions
            if text_body:
                part1 = MIMEText(text_body, 'plain')
                msg.attach(part1)
            
            part2 = MIMEText(html_body, 'html')
            msg.attach(part2)
            
            # Send email
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    @staticmethod
    def send_new_appointment_to_admin(
        admin_email: str,
        admin_name: str,
        user_name: str,
        user_email: str,
        start_time: datetime,
        end_time: datetime,
        notes: Optional[str] = None
    ) -> bool:
        """
        Notify admin of a new appointment request
        
        Args:
            admin_email: Admin's email address
            admin_name: Admin's name
            user_name: User's name
            user_email: User's email
            start_time: Appointment start time
            end_time: Appointment end time
            notes: Optional notes from user
            
        Returns:
            True if successful, False otherwise
        """
        subject = f"Nouvelle demande de rendez-vous - {user_name}"
        
        # Format dates
        start_formatted = start_time.strftime("%d/%m/%Y à %H:%M")
        end_formatted = end_time.strftime("%H:%M")
        
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
                    .appointment-details {{ background: white; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #667eea; }}
                    .button {{ display: inline-block; padding: 12px 30px; background: #667eea; color: white; text-decoration: none; border-radius: 5px; margin: 10px 5px; }}
                    .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Nouvelle demande de rendez-vous</h1>
                    </div>
                    <div class="content">
                        <p>Bonjour {admin_name},</p>
                        <p><strong>{user_name}</strong> a demandé un rendez-vous avec vous.</p>
                        
                        <div class="appointment-details">
                            <h3>Détails du rendez-vous</h3>
                            <p><strong>Date et heure:</strong> {start_formatted} - {end_formatted}</p>
                            <p><strong>Participant:</strong> {user_name} ({user_email})</p>
                            {f'<p><strong>Notes:</strong> {notes}</p>' if notes else ''}
                        </div>
                        
                        <p>Veuillez confirmer ou annuler ce rendez-vous depuis votre panneau d'administration.</p>
                        
                        <div style="text-align: center; margin: 30px 0;">
                            <a href="{FRONTEND_URL}/admin" class="button">Voir dans le panneau admin</a>
                        </div>
                        
                        <div class="footer">
                            <p>Alquimia del Cambio - Système de gestion des rendez-vous</p>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
        
        text_body = f"""
        Nouvelle demande de rendez-vous
        
        Bonjour {admin_name},
        
        {user_name} a demandé un rendez-vous avec vous.
        
        Détails:
        - Date et heure: {start_formatted} - {end_formatted}
        - Participant: {user_name} ({user_email})
        {f'- Notes: {notes}' if notes else ''}
        
        Veuillez confirmer ou annuler ce rendez-vous depuis votre panneau d'administration:
        {FRONTEND_URL}/admin
        
        Alquimia del Cambio
        """
        
        return EmailService._send_email(admin_email, subject, html_body, text_body)
    
    @staticmethod
    def send_appointment_confirmation_to_user(
        user_email: str,
        user_name: str,
        admin_name: str,
        start_time: datetime,
        end_time: datetime,
        status: str = "pending"
    ) -> bool:
        """
        Send appointment confirmation to user
        
        Args:
            user_email: User's email address
            user_name: User's name
            admin_name: Admin's name
            start_time: Appointment start time
            end_time: Appointment end time
            status: Appointment status (pending, confirmed, cancelled)
            
        Returns:
            True if successful, False otherwise
        """
        status_text = {
            "pending": "en attente de confirmation",
            "confirmed": "confirmé",
            "cancelled": "annulé"
        }.get(status, status)
        
        subject = f"Rendez-vous {status_text} avec {admin_name}"
        
        # Format dates
        start_formatted = start_time.strftime("%d/%m/%Y à %H:%M")
        end_formatted = end_time.strftime("%H:%M")
        
        color = "#667eea" if status == "confirmed" else "#f59e0b" if status == "pending" else "#ef4444"
        
        html_body = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, {color} 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
                    .appointment-details {{ background: white; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid {color}; }}
                    .button {{ display: inline-block; padding: 12px 30px; background: {color}; color: white; text-decoration: none; border-radius: 5px; margin: 10px 5px; }}
                    .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Rendez-vous {status_text}</h1>
                    </div>
                    <div class="content">
                        <p>Bonjour {user_name},</p>
                        <p>Votre rendez-vous avec <strong>{admin_name}</strong> est <strong>{status_text}</strong>.</p>
                        
                        <div class="appointment-details">
                            <h3>Détails du rendez-vous</h3>
                            <p><strong>Date et heure:</strong> {start_formatted} - {end_formatted}</p>
                            <p><strong>Avec:</strong> {admin_name}</p>
                            <p><strong>Statut:</strong> {status_text.upper()}</p>
                        </div>
                        
                        {f'<p>Vous recevrez une autre notification lorsque votre rendez-vous sera confirmé.</p>' if status == "pending" else ''}
                        
                        <div style="text-align: center; margin: 30px 0;">
                            <a href="{FRONTEND_URL}/booking" class="button">Voir mes rendez-vous</a>
                        </div>
                        
                        <div class="footer">
                            <p>Alquimia del Cambio</p>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
        
        text_body = f"""
        Rendez-vous {status_text}
        
        Bonjour {user_name},
        
        Votre rendez-vous avec {admin_name} est {status_text}.
        
        Détails:
        - Date et heure: {start_formatted} - {end_formatted}
        - Avec: {admin_name}
        - Statut: {status_text.upper()}
        
        {f'Vous recevrez une autre notification lorsque votre rendez-vous sera confirmé.' if status == "pending" else ''}
        
        Voir mes rendez-vous: {FRONTEND_URL}/booking
        
        Alquimia del Cambio
        """
        
        return EmailService._send_email(user_email, subject, html_body, text_body)

