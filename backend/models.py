from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user", nullable=False)  # "admin" or "user"  
    provider = Column(String(50), nullable=True)  # "google", "facebook", "local"
    provider_id = Column(String(100), nullable=True)  # ID from OAuth provider
    is_active = Column(Boolean, default=True)
    is_validated = Column(Boolean, default=False)  # Admin validation required for normal progression
    validated_modules = Column(JSON, nullable=True, default="[]")  # List of validated module IDs
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    user_responses = relationship("UserResponseDB", back_populates="user")
    user_progress = relationship("UserProgress", back_populates="user")

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    objective = Column(Text, nullable=True)
    belief_to_transform = Column(Text, nullable=True)
    expected_results = Column(Text, nullable=True)
    recommended_book = Column(Text, nullable=True)
    audio_file = Column(String(255), nullable=True)
    order_number = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    themes = relationship("Theme", back_populates="module", cascade="all, delete-orphan")

class Theme(Base):
    __tablename__ = "themes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)  # Kept for backward compatibility
    order_number = Column(Integer, nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    theme_type = Column(String(50), default="theme")  # "theme" or "resource"
    
    # Relationships
    module = relationship("Module", back_populates="themes")
    exercises = relationship("Exercise", back_populates="theme", cascade="all, delete-orphan")
    cards = relationship("ThemeCard", back_populates="theme", cascade="all, delete-orphan")

class ThemeCard(Base):
    __tablename__ = "theme_cards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    card_type = Column(String(50), default="content")  # content, theory, practical, resources, conclusion, intro, exercise
    order_number = Column(Integer, nullable=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    is_editable = Column(Boolean, default=True)
    
    # Exercise-specific fields
    exercise_instructions = Column(Text, nullable=True)
    exercise_questions = Column(JSON, nullable=True, default="[]")
    exercise_sections = Column(JSON, nullable=True, default="[]")
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    theme = relationship("Theme", back_populates="cards")

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    parent_title = Column(String(200), nullable=True)  # Titre du groupe d'exercices (ex: "Ejercicio #1: Historia")
    instructions = Column(Text, nullable=True)
    sub_questions = Column(JSON, nullable=True, default="[]")
    order_number = Column(Integer, nullable=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    
    # Exercise-specific fields (same as cards)
    exercise_instructions = Column(Text, nullable=True)
    exercise_questions = Column(JSON, nullable=True, default="[]")
    exercise_sections = Column(JSON, nullable=True, default="[]")
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    theme = relationship("Theme", back_populates="exercises")
    user_responses = relationship("UserResponseDB", back_populates="exercise")

class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=True)
    completed = Column(Boolean, default=False)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="user_progress")

class UserResponseDB(Base):
    __tablename__ = "user_responses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    response_text = Column(Text, nullable=True)
    submitted_at = Column(DateTime, default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="user_responses")
    exercise = relationship("Exercise", back_populates="user_responses")

class UserSubQuestionResponseDB(Base):
    __tablename__ = "user_sub_question_responses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    sub_question_index = Column(Integer, nullable=False)
    response_text = Column(Text, nullable=True)
    submitted_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("User")
    exercise = relationship("Exercise")
