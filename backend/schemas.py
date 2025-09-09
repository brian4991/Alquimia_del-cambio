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

# Exercise Question schema (defined first to be used in other schemas)
class ExerciseQuestion(BaseModel):
    type: str = "text"  # "text" or "table"
    question: str
    table_config: Optional[dict] = None  # Only for table type questions

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
    # Exercise-specific fields (only populated when card_type = "exercise")
    exercise_instructions: Optional[str] = None
    exercise_questions: Optional[List[ExerciseQuestion]] = None
    # User responses for exercise cards (only for current user)
    user_responses: Optional[dict] = None  # {question_index: response_text}

class ThemeCardCreate(BaseModel):
    title: str
    content: str
    card_type: str = "content"
    order_number: int
    # Exercise-specific fields (optional, used when card_type = "exercise")
    # Note: These fields may not be available in all database versions
    exercise_instructions: Optional[str] = None
    exercise_questions: Optional[List[ExerciseQuestion]] = None

class ThemeCardUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    card_type: Optional[str] = None
    order_number: Optional[int] = None
    # Exercise-specific fields (optional, used when card_type = "exercise")
    exercise_instructions: Optional[str] = None
    exercise_questions: Optional[List[ExerciseQuestion]] = None

# Exercise schemas
class ExerciseCreate(BaseModel):
    title: str
    instructions: Optional[str] = None
    order_number: int
    sub_questions: List[str] = []

class ExerciseUpdate(BaseModel):
    title: Optional[str] = None
    instructions: Optional[str] = None
    order_number: Optional[int] = None
    sub_questions: Optional[List[str]] = None

class ExerciseResponseRequest(BaseModel):
    exercise_id: int
    response_text: str

# Sub-question response schema
class SubQuestionResponseRequest(BaseModel):
    exercise_id: int
    sub_question_index: int
    response_text: str

class ExerciseResponse(BaseModel):
    id: int
    title: str
    instructions: Optional[str]
    order_number: int
    theme_id: int
    sub_questions: List[str] = []
    user_response: Optional[str] = None
    sub_question_responses: dict = {}  # {index: response_text}

# Card Exercise Response schemas
class CardExerciseResponseRequest(BaseModel):
    card_id: int
    question_index: int
    response_text: str

class CardExerciseResponseUpdate(BaseModel):
    response_text: str

class CardExerciseResponse(BaseModel):
    id: int
    user_id: int
    card_id: int
    question_index: int
    response_text: str
    submitted_at: datetime
    updated_at: datetime

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
    is_accessible: bool = True
    progress: int = 0  # Pourcentage de progression (0-100)
    themes_count: int = 0  # Nombre total de thèmes

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