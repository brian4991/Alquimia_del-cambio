from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

# Theme Card schemas
class ThemeCardResponse(BaseModel):
    id: int
    title: str
    content: str
    card_type: str
    order_number: int
    theme_id: int
    is_editable: bool
    created_at: datetime
    updated_at: datetime

class ThemeCardCreate(BaseModel):
    title: str
    content: str
    card_type: str = "content"
    order_number: int

class ThemeCardUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    card_type: Optional[str] = None
    order_number: Optional[int] = None

# Exercise schemas
class ExerciseCreate(BaseModel):
    title: str
    question: str
    instructions: Optional[str] = None
    order_number: int

class ExerciseUpdate(BaseModel):
    title: Optional[str] = None
    question: Optional[str] = None
    instructions: Optional[str] = None
    order_number: Optional[int] = None

class ExerciseResponseRequest(BaseModel):
    exercise_id: int
    response_text: str

class ExerciseResponse(BaseModel):
    id: int
    title: str
    question: str
    instructions: Optional[str]
    order_number: int
    theme_id: int
    user_response: Optional[str] = None

# Module schemas
class ModuleCreate(BaseModel):
    title: str
    description: Optional[str] = None
    objective: Optional[str] = None
    belief_to_transform: Optional[str] = None
    expected_results: Optional[str] = None
    recommended_book: Optional[str] = None
    audio_file: Optional[str] = None
    order_number: int

class ModuleUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    objective: Optional[str] = None
    belief_to_transform: Optional[str] = None
    expected_results: Optional[str] = None
    recommended_book: Optional[str] = None
    audio_file: Optional[str] = None
    order_number: Optional[int] = None
    is_active: Optional[bool] = None

class ModuleResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    objective: Optional[str]
    belief_to_transform: Optional[str]
    expected_results: Optional[str]
    recommended_book: Optional[str]
    audio_file: Optional[str]
    order_number: int
    is_completed: bool = False

# Theme schemas
class ThemeCreate(BaseModel):
    title: str
    content: str = ""
    order_number: int

class ThemeUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    order_number: Optional[int] = None

class ThemeResponse(BaseModel):
    id: int
    title: str
    content: str  # Kept for backward compatibility
    order_number: int
    module_id: int
    is_completed: bool = False
    is_unlocked: bool = False
    total_cards: int = 0  # Number of cards in this theme 