"""
Migration script to add Appointment and AdminCalendarSettings tables
Run this after pulling the booking system changes
"""
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import models
from models import Base, Appointment, AdminCalendarSettings

# Get database URL
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')

# Create engine
engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

# Check if tables exist
existing_tables = inspector.get_table_names()

print("Existing tables:", existing_tables)
print("\nCreating new tables if they don't exist...")

# Create all tables (will only create missing ones)
Base.metadata.create_all(engine)

# Verify new tables
inspector = inspect(engine)
new_tables = inspector.get_table_names()

if 'appointments' in new_tables:
    print("✓ appointments table created successfully")
    # Show columns
    columns = inspector.get_columns('appointments')
    print(f"  Columns: {', '.join([col['name'] for col in columns])}")
else:
    print("✗ appointments table not found")

if 'admin_calendar_settings' in new_tables:
    print("✓ admin_calendar_settings table created successfully")
    # Show columns
    columns = inspector.get_columns('admin_calendar_settings')
    print(f"  Columns: {', '.join([col['name'] for col in columns])}")
else:
    print("✗ admin_calendar_settings table not found")

print("\nMigration complete!")

