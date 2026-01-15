import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database configuration - use PostgreSQL on Railway, SQLite locally
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    # Railway PostgreSQL (use short connect timeout to avoid startup hangs)
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        connect_args={
            "connect_timeout": 5,
        },
    )
else:
    # Local SQLite
    SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 