from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.sql import func
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import List, Optional
import jwt
from datetime import datetime, timedelta
import os

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
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
    audio_file = Column(String(255), nullable=True)  # nom du fichier audio
    order_number = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    themes = relationship("Theme", back_populates="module", cascade="all, delete-orphan")

class Theme(Base):
    __tablename__ = "themes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    order_number = Column(Integer, nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    
    # Relationships
    module = relationship("Module", back_populates="themes")
    exercises = relationship("Exercise", back_populates="theme", cascade="all, delete-orphan")

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    question = Column(Text, nullable=False)
    instructions = Column(Text, nullable=True)
    order_number = Column(Integer, nullable=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    
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

# Create tables
Base.metadata.create_all(bind=engine)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI app
app = FastAPI(title="Alquimia del Cambio", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Pydantic models
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

class ExerciseResponseRequest(BaseModel):
    exercise_id: int
    response_text: str

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

class ThemeResponse(BaseModel):
    id: int
    title: str
    content: str
    order_number: int
    module_id: int
    is_completed: bool = False
    is_unlocked: bool = False

class ExerciseResponse(BaseModel):
    id: int
    title: str
    question: str
    instructions: Optional[str]
    order_number: int
    theme_id: int
    user_response: Optional[str] = None

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# Initialize database with Módulo 1 content
def init_database(db: Session):
    # Check if data already exists
    if db.query(Module).first():
        return
    
    # Create Módulo 1 with complete information from module1.txt
    module1 = Module(
        title="El Mapa de tus Emociones",
        description="El propósito de este módulo es que aprendas a gestionar tu mundo emocional y expresar lo que sientes y necesitas, con una mayor consciencia y asertividad.",
        objective="Gestionar tu mundo emocional y expresar lo que sientes y necesitas con mayor consciencia y asertividad",
        belief_to_transform="Expresar lo que siento me hace débil y vulnerable",
        expected_results="Logras gestionar y regular tu sentir y tus emociones. Logras escuchar tus necesidades y expresarlas con seguridad y asertividad.",
        recommended_book="Inteligencia emocional de Daniel Goleman (lo encuentras en la carpeta de Bonus)",
        audio_file="modulo-1-intro.mp3",
        order_number=1
    )
    db.add(module1)
    db.flush()
    
    # ===============================
    # TEMA 1: Explorando mi historia emocional
    # ===============================
    theme1 = Theme(
        title="Explorando mi historia emocional",
        content="""El propósito de este tema es guiarte a través de la exploración consciente de tu historia emocional. A lo largo de nuestra vida, vamos acumulando experiencias que moldean la forma en que sentimos, reaccionamos y gestionamos nuestras emociones. Al reconocer los patrones emocionales y descubrir las raíces de estos, podrás comprender mejor cómo las experiencias pasadas siguen influyendo en tu presente. Este autoconocimiento es fundamental para aprender a gestionar las emociones de manera más consciente y efectiva.

**Subtemas:**
• Reconocer patrones emocionales
• Raíces emocionales

**Recursos:**
- Mi carta de aceptación y compromiso
- Emocionario, técnicas de gestión emocional para el día a día y ¿qué necesito realmente cuando me siento así?

Antes de empezar a profundizar en los temas y después de haber completado "La carta de aceptación y compromiso" quiero que empecemos por dos ejercicios muy valiosos que son el punto de partida y reconectar con tu historia, que es la que hoy te ha permitido llegar hasta aquí pero que sin duda podremos contar desde otra perspectiva.

¡Ah! Y no olvides tu carta de aceptación y compromiso: es lo primero antes de comenzar. Disfruta el viaje que te espera.

**Subtema 1: Reconocer patrones emocionales**

Los patrones emocionales son respuestas automáticas que repetimos en situaciones similares a lo largo de nuestra vida. Estas respuestas se forman a partir de nuestras primeras experiencias emocionales y las conexiones que hacemos entre emociones y eventos específicos.

Por ejemplo: si en nuestra infancia asociamos la crítica con el miedo al rechazo, es probable que, en la vida adulta, respondamos a cualquier forma de crítica con ansiedad o inseguridad.

Desde el campo de la psicología cognitiva, se ha demostrado que nuestras emociones están en gran parte influenciadas por esquemas mentales, o "mapas" que desarrollamos a lo largo del tiempo, y que nos ayudan a interpretar el mundo. Estos esquemas emocionales son patrones de pensamientos y emociones que guían nuestras reacciones.

Por ejemplo: si creciste en un ambiente donde la expresión emocional era reprimida, es probable que desarrolles un patrón de evitación emocional en tu vida adulta, donde tiendes a ignorar o minimizar tus propias emociones.

Identificar estos patrones es esencial para desactivarlos. La neurociencia nos muestra que el cerebro puede cambiar sus conexiones, lo que significa que podemos "reprogramar" cómo reaccionamos emocionalmente a través del autoconocimiento y la práctica consciente. Este proceso se conoce como neuroplasticidad, y es lo que nos permite adoptar nuevas formas de gestionar nuestras emociones una vez que somos conscientes de los patrones emocionales que hemos desarrollado.

**Señales de patrones emocionales recurrentes:**
• Reacciones exageradas a ciertas situaciones: A veces, cuando alguien nos critica o dice algo que no nos gusta, podemos sentirnos muy enojados o muy tristes, incluso si lo que dijeron no era tan grave. Esto pasa porque hemos aprendido a reaccionar así en el pasado.
• Sentir las mismas emociones en situaciones parecidas: Puede que te sientas frustrado o nervioso en ciertos lugares o con ciertas personas, como en el trabajo o en una reunión social. Esto ocurre porque esas situaciones te recuerdan a otras donde ya te sentiste así antes.
• Evitar ciertos temas o emociones: Si hay cosas que prefieres no hablar o sentir, como el miedo o la tristeza, podrías intentar ignorarlas. En lugar de enfrentarlas, quizás optes por aislarte o discutir con los demás para no sentirte vulnerable.

Al identificar estos patrones, podemos empezar a comprender que nuestras emociones no siempre reflejan la realidad del presente, sino que están condicionadas por experiencias anteriores.

**Subtema 2: Raíces emocionales**

Las raíces emocionales son las experiencias pasadas, a menudo en la infancia o adolescencia, que forman la base de nuestros patrones emocionales actuales. Estas experiencias tempranas, tanto positivas como negativas, juegan un papel crucial en el desarrollo de nuestro sistema emocional. En psicología del desarrollo, el modelo del apego propuesto por John Bowlby sostiene que nuestras primeras relaciones, particularmente con los cuidadores primarios, influyen en cómo formamos relaciones y regulamos nuestras emociones en el futuro.

Por ejemplo: si en nuestra infancia aprendimos que expresar tristeza no era aceptado o no recibía la validación necesaria, podríamos haber desarrollado una tendencia a reprimir esa emoción. Este patrón de represión emocional puede perdurar en la vida adulta, resultando en una incapacidad para expresar o incluso identificar correctamente sentimientos de tristeza. De manera similar, experiencias traumáticas o momentos de gran tensión emocional, como la pérdida de un ser querido o una ruptura familiar, también pueden formar raíces emocionales que influyen en nuestra respuesta a situaciones de estrés o pérdida en el presente.

**Impacto de las raíces emocionales:**
• Apego inseguro: Puede generar dependencia emocional o dificultades para confiar en los demás.
• Experiencias de rechazo: Pueden llevar a una sensibilidad exagerada ante la crítica o el conflicto.
• Ambientes familiares poco expresivos emocionalmente: Pueden resultar en la incapacidad de expresar necesidades emocionales de manera asertiva.
• Momentos traumáticos: Pueden generar reacciones desproporcionadas ante situaciones de pérdida o estrés en la vida adulta.

Explorar estas raíces no solo es importante para comprender por qué reaccionamos de cierta manera, sino que también nos permite tomar el control sobre cómo queremos responder en el futuro. El autoconocimiento de nuestras raíces emocionales nos da el poder de cambiar nuestras narrativas emocionales y romper patrones que ya no nos sirven.

**Conclusión del Tema 1**

Este tema es el fundamento para construir un mayor entendimiento de ti mismo a nivel emocional. Reconocer tus patrones emocionales es el primer paso para observar cómo respondes a situaciones y relaciones, mientras que explorar las raíces emocionales te permitirá entender por qué reaccionas de esa manera. Con este conocimiento, comenzarás a tomar decisiones más conscientes sobre cómo gestionar tus emociones y evitarás caer en respuestas automáticas que no contribuyen a tu bienestar.

Es crucial recordar que las emociones no se generan en el vacío; están profundamente conectadas a nuestra historia y a las experiencias que nos han moldeado. Este proceso de autoexploración te brinda una visión más clara de esas conexiones, permitiéndote tomar las riendas de tu mundo emocional con mayor comprensión y compasión.""",
        order_number=1,
        module_id=module1.id
    )
    db.add(theme1)
    db.flush()
    
    # Ejercicios del Tema 1 - Historia
    exercises_theme1 = [
        Exercise(
            title="Explorando mi historia Emocional",
            question="Describe tu historia emocional desde la infancia hasta ahora. ¿Qué eventos significativos han marcado tu relación con las emociones?",
            instructions="""Tómate el tiempo necesario para reflexionar sobre tu historia emocional. Escribe con detalles sobre experiencias que consideres importantes en tu desarrollo emocional. 

Este ejercicio es el punto de partida para reconectar con tu historia, que es la que hoy te ha permitido llegar hasta aquí pero que sin duda podremos contar desde otra perspectiva.

Ve al Ejercicio #1: Historia y escribe todo lo que puedas con detalles.""",
            order_number=1,
            theme_id=theme1.id
        ),
        Exercise(
            title="Reconociendo Patrones Emocionales",
            question="¿Qué patrones emocionales reconoces en ti? ¿Hay situaciones que siempre te generan las mismas emociones?",
            instructions="""Los patrones emocionales son respuestas automáticas que repetimos en situaciones similares a lo largo de nuestra vida. Identifica patrones de comportamiento emocional que se repiten en tu vida.

Señales de patrones emocionales recurrentes:
• Reacciones exageradas a ciertas situaciones
• Sentir las mismas emociones en situaciones parecidas  
• Evitar ciertos temas o emociones

Reflexiona sobre situaciones similares y cómo reaccionas emocionalmente. Al identificar estos patrones, podemos empezar a comprender que nuestras emociones no siempre reflejan la realidad del presente, sino que están condicionadas por experiencias anteriores.

A continuación vas a empezar a armar tu mapa emocional interno.""",
            order_number=2,
            theme_id=theme1.id
        ),
        Exercise(
            title="Raíces Emocionales",
            question="¿Cuáles consideras que son las raíces de tus patrones emocionales? ¿Qué experiencias tempranas los originaron?",
            instructions="""Las raíces emocionales son las experiencias pasadas, a menudo en la infancia o adolescencia, que forman la base de nuestros patrones emocionales actuales.

Explora las experiencias de tu infancia y adolescencia que pueden haber formado tus patrones emocionales actuales:
• Apego inseguro: puede generar dependencia emocional
• Experiencias de rechazo: sensibilidad ante la crítica
• Ambientes familiares poco expresivos emocionalmente
• Momentos traumáticos: reacciones desproporcionadas

Explorar estas raíces no solo es importante para comprender por qué reaccionamos de cierta manera, sino que también nos permite tomar el control sobre cómo queremos responder en el futuro.

A continuación vas a comprender la raíz de tus emociones.""",
            order_number=3,
            theme_id=theme1.id
        )
    ]
    
    for exercise in exercises_theme1:
        db.add(exercise)
    
    # ===============================
    # TEMA 2: Autoconocimiento emocional profundo
    # ===============================
    theme2 = Theme(
        title="Autoconocimiento emocional profundo",
        content="""En este tema, profundizaremos en la identificación de tus emociones primarias y en el reconocimiento de las necesidades emocionales. Es crucial entender que nuestras emociones no solo son respuestas inmediatas a los eventos, sino que también son señales que nos indican nuestras necesidades internas no satisfechas. Al desarrollar un mayor autoconocimiento emocional, podrás identificar estas señales y actuar de manera más consciente, evitando respuestas automáticas o reactivas que podrían perpetuar patrones no deseados.

**Subtema 1: Identificar emociones primarias**

Las emociones primarias son las respuestas emocionales más básicas e instintivas que todos los seres humanos experimentan. Las emociones primarias incluyen el miedo, la tristeza, la alegría, el enojo, la sorpresa y el asco. Estas emociones tienen una función evolutiva: nos ayudan a responder a nuestro entorno de manera rápida para sobrevivir y adaptarnos. Sin embargo, a menudo no estamos completamente conscientes de estas emociones, y es común que las disfrazamos o las racionalicemos en lugar de experimentarlas plenamente.

Es importante aprender a identificar estas emociones a medida que surgen, sin juicio ni represión, ya que cada una de ellas contiene información valiosa sobre lo que necesitamos en ese momento.

**Beneficios de identificar las emociones primarias:**
• Consciencia emocional: Al ser más conscientes de tus emociones primarias, puedes actuar de manera más alineada con tus valores y deseos, en lugar de reaccionar impulsivamente.
• Prevención de conflictos: Al identificar las emociones en el momento en que surgen, puedes evitar que escalen en situaciones conflictivas o dañinas.
• Desarrollo de empatía: Cuando reconoces tus propias emociones, también te vuelves más empático hacia las emociones de los demás, lo que mejora las relaciones interpersonales.

Según Paul Ekman, un reconocido psicólogo en el campo de las emociones, las emociones primarias son universales y están presentes en todas las culturas. Esto sugiere que, aunque las expresiones emocionales pueden variar entre diferentes sociedades, la experiencia interna de estas emociones es compartida por todos los seres humanos. Ekman también señala que identificar y regular estas emociones es fundamental para el bienestar psicológico, ya que nos permiten procesar nuestras experiencias de manera efectiva.

**Subtema 2: Reconocer necesidades emocionales**

Cada emoción primaria está conectada a una necesidad emocional. Las emociones actúan como un sistema de alerta que nos indica si nuestras necesidades están siendo satisfechas o no. Por ejemplo, el miedo puede señalar una necesidad de seguridad, la tristeza puede revelar una necesidad de apoyo o consuelo, y el enojo puede indicar que sentimos que se ha violado un límite importante. Al identificar estas necesidades, puedes empezar a tomar acciones más efectivas para satisfacerlas y evitar quedarte atrapado en ciclos emocionales insalubres.

El reconocimiento de las necesidades emocionales es una habilidad esencial para el autoconocimiento. Sin este reconocimiento, corremos el riesgo de malinterpretar nuestras emociones y responder de manera incorrecta a ellas. A menudo, cuando ignoramos nuestras necesidades, nos sentimos desbordados, desconectados de nosotros mismos y de los demás, lo que puede llevar a la frustración, el agotamiento emocional e incluso a problemas físicos.

**Beneficios de reconocer necesidades emocionales:**
• Satisfacción personal: Ser consciente de tus necesidades emocionales te permite satisfacerlas de manera efectiva, lo que lleva a una mayor sensación de bienestar y satisfacción.
• Reducción del estrés: Al entender y abordar tus necesidades emocionales, puedes reducir la ansiedad y el estrés relacionados con la insatisfacción emocional.
• Mejora en las relaciones: Reconocer tus propias necesidades emocionales también te permite comunicarte mejor con los demás y establecer relaciones más saludables y auténticas.

Carl Rogers, uno de los fundadores de la psicología humanista, destacó la importancia de las necesidades emocionales en su teoría de la "persona completa". Rogers sostuvo que cuando las personas son conscientes de sus necesidades y trabajan activamente para satisfacerlas, tienden a ser más equilibradas y felices. En cambio, cuando estas necesidades se ignoran o se niegan, surgen conflictos internos y disfunciones en las relaciones. Rogers sugirió que el reconocimiento y la satisfacción de las necesidades emocionales son esenciales para la autoaceptación y la autorrealización.

Además, investigaciones recientes en el campo de la psicología positiva, sugieren que la identificación de las necesidades emocionales y la capacidad de satisfacerlas son claves para el desarrollo de resiliencia emocional y la construcción de recursos psicológicos a largo plazo.

**Conclusión del Tema 2**

Este tema te llevará a un nivel más profundo de conexión contigo mismo/a. Identificar tus emociones primarias y las necesidades emocionales que subyacen a estas es un paso crucial para entender por qué reaccionas de ciertas maneras en situaciones cotidianas y cómo puedes tomar decisiones más alineadas con tu bienestar. Al desarrollar este nivel de autoconocimiento emocional, estarás mejor equipado/a para responder de manera más intencional y saludable en tu vida diaria, creando un equilibrio emocional más sólido.

En la próxima sección, te guiaré a través de ejercicios específicos que te ayudarán a poner en práctica esta identificación de emociones y el reconocimiento de tus necesidades emocionales, haciendo que el proceso de autoconocimiento sea claro y aplicable.""",
        order_number=2,
        module_id=module1.id
    )
    db.add(theme2)
    db.flush()
    
    # Ejercicios del Tema 2 - Emociones
    exercises_theme2 = [
        Exercise(
            title="Identificar emociones primarias",
            question="Durante una semana, registra las emociones primarias que experimentas cada día. ¿Cuáles son las más frecuentes?",
            instructions="""Las emociones primarias son las respuestas emocionales más básicas: miedo, tristeza, alegría, enojo, sorpresa y asco.

Lleva un diario emocional durante una semana. Anota las emociones que sientes y en qué contextos aparecen.

Beneficios de identificar las emociones primarias:
• Consciencia emocional: actuar alineado con tus valores
• Prevención de conflictos: evitar escaladas emocionales
• Desarrollo de empatía: mejores relaciones interpersonales

Es importante aprender a identificar estas emociones a medida que surgen, sin juicio ni represión, ya que cada una contiene información valiosa sobre lo que necesitamos en ese momento.

A continuación vas a explorar tus emociones primarias.""",
            order_number=1,
            theme_id=theme2.id
        ),
        Exercise(
            title="Reconocer necesidades emocionales",
            question="Para cada emoción que identificaste, reflexiona: ¿qué necesidad emocional está comunicando esta emoción?",
            instructions="""Cada emoción primaria está conectada a una necesidad emocional:
• El miedo puede señalar una necesidad de seguridad
• La tristeza puede revelar una necesidad de apoyo o consuelo  
• El enojo puede indicar que se ha violado un límite importante

Conecta cada emoción con la necesidad subyacente que está tratando de comunicar.

Beneficios de reconocer necesidades emocionales:
• Satisfacción personal y mayor bienestar
• Reducción del estrés y la ansiedad
• Mejora en las relaciones interpersonales
• Construcción de resiliencia emocional

Sin este reconocimiento, corremos el riesgo de malinterpretar nuestras emociones y responder de manera incorrecta.

A continuación vas a reconocer tus necesidades emocionales.""",
            order_number=2,
            theme_id=theme2.id
        ),
        Exercise(
            title="Creando un Plan para satisfacer mis necesidades",
            question="Basándote en las necesidades emocionales identificadas, ¿qué acciones concretas puedes tomar para satisfacerlas?",
            instructions="""Diseña un plan de acción específico para atender tus necesidades emocionales de manera saludable.

Al identificar estas necesidades, puedes empezar a tomar acciones más efectivas para satisfacerlas y evitar quedarte atrapado en ciclos emocionales insalubres.

Como parte del aprendizaje y compromiso contigo mismo/a, este ejercicio es una tarea muy importante para desarrollar tu autoconocimiento emocional.

Cuando las personas son conscientes de sus necesidades y trabajan activamente para satisfacerlas, tienden a ser más equilibradas y felices. En cambio, cuando estas necesidades se ignoran o se niegan, surgen conflictos internos y disfunciones en las relaciones.

El día de mañana no habrá lectura en la guía, pero sí tienes una tarea muy importante. Como parte del aprendizaje y compromiso contigo misma(o), vas a realizar este ejercicio.""",
            order_number=3,
            theme_id=theme2.id
        )
    ]
    
    for exercise in exercises_theme2:
        db.add(exercise)
    
    # ===============================
    # TEMA 3: Gestionando y expresando emociones
    # ===============================
    theme3 = Theme(
        title="Gestionando y expresando emociones",
        content="""En esta última parte del módulo, nos adentraremos en cómo gestionar y expresar nuestras emociones de manera saludable y efectiva. Saber identificar nuestras emociones es un primer paso esencial, pero ser capaces de regularlas y expresarlas de manera asertiva es lo que realmente nos permite avanzar hacia una vida más equilibrada y consciente. Este tema se enfoca en proporcionarte las herramientas necesarias para gestionar las emociones más difíciles y comunicar lo que sientes y necesitas de una manera clara, respetuosa y efectiva.

**Subtema 1: Técnicas de regulación emocional**

Las emociones, especialmente las intensas, pueden ser abrumadoras si no sabemos cómo manejarlas. Este subtema explora diversas técnicas basadas en la investigación psicológica que han demostrado ser efectivas para regular las emociones, permitiéndote responder a las situaciones difíciles de manera más adaptativa, en lugar de reaccionar de forma impulsiva.

**¿Por qué es importante la regulación emocional?**

La regulación emocional es la capacidad de manejar y responder a una experiencia emocional de manera saludable. La teoría de James Gross sobre la regulación emocional, ha mostrado que quienes desarrollan esta habilidad son más capaces de mantener relaciones interpersonales satisfactorias, tienen menos niveles de estrés, y gozan de mayor bienestar general.

**La regulación emocional implica diversas estrategias:**
• **Reevaluación del pensamiento**: Esta técnica consiste en reinterpretar una situación para cambiar su impacto emocional. En lugar de ver un evento como una amenaza, puedes aprender a verlo como un desafío o una oportunidad de crecimiento.
• **Mindfulness y atención plena**: La práctica de mindfulness, o atención plena, nos ayuda a observar nuestras emociones sin juzgarlas, reduciendo su intensidad y permitiéndonos responder con mayor claridad. Las investigaciones han demostrado que el mindfulness mejora la capacidad de autorregulación emocional y disminuye los niveles de ansiedad y depresión.
• **Respiración y técnicas de relajación**: El control de la respiración es una herramienta muy efectiva para disminuir la activación fisiológica asociada con el estrés o la ira. Ejercicios como la respiración diafragmática han demostrado reducir la respuesta del sistema nervioso simpático, ayudándonos a calmarnos en momentos de tensión.

**Cómo aplicar la regulación emocional en la vida diaria:**

**1. Reconoce y valida tus emociones**
Uno de los primeros pasos en la regulación emocional es ser consciente de lo que sientes. En lugar de ignorar tus emociones o juzgarte por sentirlas, tómate un momento para reconocerlas y aceptarlas.

Ejemplo: Si estás frustrado después de un día difícil en el trabajo, en lugar de decir "No debería sentirme así", trata de decir "Es normal sentirme frustrad@ después de un día así". Esta validación te permitirá tomar decisiones más sabias sobre cómo manejar la emoción.

**2. Practica la respiración consciente**
Cuando sientas que una emoción intensa, como la ansiedad o la ira, está aumentando, una técnica rápida y efectiva es la respiración profunda. Esto ayuda a calmar el sistema nervioso y te da tiempo para procesar lo que estás sintiendo antes de reaccionar impulsivamente.

Tip: Haz una pausa y respira profundamente, inhalando por la nariz durante 4 segundos, sosteniendo el aire por 4 segundos y exhalando lentamente por la boca durante otros 4 segundos, repite este ciclo 3 o 4 veces.

**3. Etiqueta tus emociones**
Identificar y ponerle nombre a lo que estás sintiendo es otra forma de regulación emocional. Al etiquetar la emoción, puedes distanciarte de ella y evitar que te controle.

**4. Redirige la energía de las emociones intensas**
A veces, las emociones intensas necesitan ser canalizadas. En lugar de actuar impulsivamente, busca formas constructivas de liberar esa energía.

**5. Cuida tus pensamientos**
Nuestras emociones están fuertemente ligadas a nuestros pensamientos. Si alimentamos pensamientos negativos o catastróficos, nuestras emociones se intensificarán.

**6. Establece límites emocionales**
Aprender a decir "no" o a poner límites con los demás también es una forma de regular tus emociones.

**7. Utiliza el autocuidado como herramienta de regulación**
Cuando cuidas de ti mismo regularmente, creas una base sólida para enfrentar los desafíos emocionales.

**Subtema 2: Comunicación asertiva de las necesidades**

Gestionar las emociones también implica la capacidad de expresar lo que sientes y necesitas de manera efectiva. La comunicación asertiva es un estilo de comunicación que te permite defender tus derechos y expresar tus emociones sin ser agresivo o pasivo, respetando tanto tus necesidades como las de los demás.

**¿Qué es la comunicación asertiva?**

La comunicación asertiva es una habilidad interpersonal clave que permite expresar nuestras emociones y necesidades de manera honesta y directa, respetando al mismo tiempo los derechos y sentimientos de los demás. Según estudios del psicólogo Albert Ellis, la falta de asertividad puede llevar a la acumulación de frustración, resentimiento y conflictos interpersonales.

**Características de la comunicación asertiva:**
• **Claridad**: Expresar lo que sientes y necesitas de manera directa y sin ambigüedades. En lugar de evitar el conflicto, la asertividad se enfoca en resolverlo desde la comprensión mutua.
• **Uso de "Yo" en lugar de "Tú"**: Cuando expresamos nuestras emociones en primera persona, evitamos culpar a los demás y tomamos responsabilidad por lo que sentimos. Por ejemplo: "Me siento ignorado cuando no respondes a mis mensajes" en lugar de "Nunca respondes a mis mensajes".
• **Equilibrio entre expresión y escucha**: Ser asertivo implica no solo expresar lo que necesitas, sino también estar dispuesto a escuchar y comprender las necesidades del otro.

**Beneficios de la comunicación asertiva:**
• Promueve relaciones más honestas y abiertas: La comunicación asertiva fomenta un entorno de confianza y sinceridad en las relaciones.
• Mejora la satisfacción personal y profesional: la asertividad está vinculada a una mayor satisfacción en las interacciones personales y en el ámbito laboral.
• Reduce el malestar emocional: Al expresar las necesidades de manera clara y respetuosa, las personas asertivas experimentan menos frustración y resentimiento.
• Ayuda a prevenir conflictos: La asertividad facilita una comunicación directa y constructiva, minimizando malentendidos y desacuerdos.
• Aumenta la autoconfianza y disminuye la ansiedad: Las personas que se comunican asertivamente tienden a sentirse más seguras de sí mismas, lo que reduce su nivel de ansiedad en situaciones sociales o profesionales.

**Subtema 3: Construcción de mi caja de herramientas emocionales**

Este subtema es el cierre del trabajo emocional realizado a lo largo de este módulo. Aquí vas a reunir todas las herramientas que has aprendido en una caja de recursos emocionales que te acompañará en tu día a día. Esta caja es simbólica y puede contener diferentes estrategias que te ayuden a regular tus emociones y expresarlas de forma más consciente.

**¿Qué es una caja de herramientas emocionales?**

Es una recopilación personal de técnicas, estrategias y recordatorios que puedes utilizar para gestionar tus emociones y navegar los desafíos emocionales de manera más efectiva. Está basada en los recursos que mejor funcionen para ti, y puede incluir tanto técnicas de regulación como métodos de comunicación asertiva.

**Ejemplos de lo que puedes incluir en tu caja de herramientas emocionales:**
• Técnicas de respiración o relajación que te ayuden a calmarte en momentos de estrés.
• Recordatorios de frases asertivas que te ayuden a comunicarte mejor con los demás.
• Un diario de emociones donde puedas escribir tus pensamientos y sentimientos en situaciones difíciles.
• Visualizaciones o imágenes mentales que te inspiren calma o fortaleza en momentos complicados.

**Por qué es importante tener una caja de herramientas emocionales:**

Al tener una colección clara de herramientas, sabes que siempre puedes recurrir a ellas cuando las emociones se vuelven abrumadoras o cuando necesitas expresar algo importante. La investigación en psicología sugiere que las personas que tienen recursos concretos para gestionar el estrés y las emociones intensas son más resilientes y manejan mejor los desafíos de la vida.

**Reflexión final del módulo**

A lo largo de este módulo, has aprendido que cada emoción tiene un propósito y un mensaje, y que no gestionarlas puede llevarnos a patrones destructivos o estancamiento emocional. Por eso, aprender a regularlas y expresarlas asertivamente no solo nos permite conectar mejor con los demás, sino también con nosotros mismos.

El verdadero crecimiento personal radica en ser capaces de escuchar nuestras emociones, atender nuestras necesidades y tener el coraje de expresarlas de manera honesta y respetuosa. Cuando logramos este equilibrio, no solo resolvemos conflictos o reducimos el estrés; creamos un espacio para vivir de manera más auténtica, plena y consciente. Es este dominio sobre nuestras emociones lo que nos permite tomar decisiones alineadas con nuestro bienestar, construir relaciones más significativas y avanzar con mayor seguridad en la vida.

Recuerda, gestionar tus emociones no significa controlarlas o reprimirlas, sino aprender a navegar por ellas con sabiduría y compasión. La práctica continua de estas herramientas te permitirá enfrentar cualquier desafío emocional que la vida te presente, con mayor claridad y confianza.""",
        order_number=3,
        module_id=module1.id
    )
    db.add(theme3)
    db.flush()
    
    # Ejercicios del Tema 3 - Gestión Emocional
    exercises_theme3 = [
        Exercise(
            title="Técnicas de Regulación Emocional",
            question="¿Qué técnicas de regulación emocional has probado y cuáles te resultan más efectivas? Describe tu experiencia con técnicas como respiración, mindfulness, reevaluación cognitiva.",
            instructions="""Las emociones, especialmente las intensas, pueden ser abrumadoras si no sabemos cómo manejarlas. La regulación emocional es la capacidad de manejar y responder a una experiencia emocional de manera saludable.

Estrategias de regulación emocional:
• **Reevaluación del pensamiento**: reinterpretar una situación para cambiar su impacto emocional
• **Mindfulness**: observar nuestras emociones sin juzgarlas, reduciendo su intensidad
• **Respiración y relajación**: controlar la respiración para calmar el sistema nervioso
• **Reconocer y validar emociones**: aceptar lo que sientes sin juzgarte
• **Etiquetar emociones**: identificar específicamente lo que sientes
• **Redirección de energía**: canalizar emociones intensas de forma constructiva

Experimenta con diferentes técnicas y documenta tu experiencia. ¿Cuáles te funcionan mejor en diferentes situaciones?

A continuación vas a prepararte para lograr gestionar tus emociones.""",
            order_number=1,
            theme_id=theme3.id
        ),
        Exercise(
            title="Comunicación asertiva de las necesidades",
            question="Practica expresar una necesidad emocional de manera asertiva. ¿Cómo te sientes al hacerlo? Describe una situación específica donde aplicarías comunicación asertiva.",
            instructions="""La comunicación asertiva es un estilo de comunicación que te permite defender tus derechos y expresar tus emociones sin ser agresivo o pasivo, respetando tanto tus necesidades como las de los demás.

Características de la comunicación asertiva:
• **Claridad**: expresar lo que sientes sin ambigüedades
• **Uso de "Yo"**: "Me siento ignorado cuando..." en lugar de "Nunca respondes..."
• **Equilibrio**: expresar tus necesidades Y escuchar las del otro

Beneficios:
• Relaciones más honestas y abiertas
• Mayor satisfacción personal y profesional  
• Reducción del malestar emocional
• Prevención de conflictos
• Aumento de autoconfianza

Identifica una situación reciente donde necesitabas expresar algo importante y practica cómo lo harías de manera asertiva.

A continuación vas a prepararte para lograr comunicar de manera asertiva tus emociones y por ende tus necesidades.""",
            order_number=2,
            theme_id=theme3.id
        ),
        Exercise(
            title="Construcción de mi caja de herramientas emocionales",
            question="Crea tu caja de herramientas emocionales personal. ¿Qué técnicas, recordatorios y estrategias incluirás? ¿Cómo la vas a organizar para tenerla siempre disponible?",
            instructions="""Este es el cierre del trabajo emocional realizado a lo largo de este módulo. Aquí vas a reunir todas las herramientas que has aprendido en una caja de recursos emocionales que te acompañará en tu día a día.

¿Qué es una caja de herramientas emocionales?
Es una recopilación personal de técnicas, estrategias y recordatorios que puedes utilizar para gestionar tus emociones y navegar los desafíos emocionales de manera más efectiva.

Ejemplos de lo que puedes incluir:
• Técnicas de respiración o relajación para momentos de estrés
• Recordatorios de frases asertivas para comunicarte mejor
• Un diario de emociones para escribir pensamientos y sentimientos
• Visualizaciones o imágenes mentales que te inspiren calma
• Estrategias específicas que has descubierto que funcionan para ti

La práctica continua de estas herramientas te permitirá enfrentar cualquier desafío emocional que la vida te presente, con mayor claridad y confianza.

Recopila todas las herramientas que has aprendido en este módulo y crea tu kit personal de gestión emocional.

A continuación vas a poner en práctica cómo gestionar tu mundo emocional.

¡Felicidades por completar el Módulo 1!""",
            order_number=3,
            theme_id=theme3.id
        )
    ]
    
    for exercise in exercises_theme3:
        db.add(exercise)
    
    db.commit()

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        init_database(db)
    finally:
        db.close()

# API Endpoints
@app.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create access token
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return UserResponse(username=current_user.username, email=current_user.email, id=current_user.id)

@app.get("/modules", response_model=List[ModuleResponse])
def get_modules(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    result = []
    for module in modules:
        # Check if module is completed
        module_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.module_id == module.id,
            UserProgress.completed == True
        ).first()
        
        result.append(ModuleResponse(
            id=module.id,
            title=module.title,
            description=module.description,
            objective=module.objective,
            belief_to_transform=module.belief_to_transform,
            expected_results=module.expected_results,
            recommended_book=module.recommended_book,
            audio_file=module.audio_file,
            order_number=module.order_number,
            is_completed=module_progress is not None
        ))
    
    return result

@app.get("/modules/{module_id}/themes", response_model=List[ThemeResponse])
def get_module_themes(module_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    themes = db.query(Theme).filter(Theme.module_id == module_id).order_by(Theme.order_number).all()
    
    result = []
    for i, theme in enumerate(themes):
        # Check if theme is completed
        theme_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.theme_id == theme.id,
            UserProgress.completed == True
        ).first()
        
        # Theme is unlocked if it's the first one or if the previous theme is completed
        is_unlocked = i == 0  # First theme is always unlocked
        if i > 0:
            prev_theme = themes[i-1]
            prev_progress = db.query(UserProgress).filter(
                UserProgress.user_id == current_user.id,
                UserProgress.theme_id == prev_theme.id,
                UserProgress.completed == True
            ).first()
            is_unlocked = prev_progress is not None
        
        result.append(ThemeResponse(
            id=theme.id,
            title=theme.title,
            content=theme.content,
            order_number=theme.order_number,
            module_id=theme.module_id,
            is_completed=theme_progress is not None,
            is_unlocked=is_unlocked
        ))
    
    return result

@app.get("/themes/{theme_id}/exercises", response_model=List[ExerciseResponse])
def get_theme_exercises(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).order_by(Exercise.order_number).all()
    
    result = []
    for exercise in exercises:
        # Get user's response if it exists
        user_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        result.append(ExerciseResponse(
            id=exercise.id,
            title=exercise.title,
            question=exercise.question,
            instructions=exercise.instructions,
            order_number=exercise.order_number,
            theme_id=exercise.theme_id,
            user_response=user_response.response_text if user_response else None
        ))
    
    return result

@app.post("/submit-response")
def submit_response(response: ExerciseResponseRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Check if response already exists
    existing_response = db.query(UserResponseDB).filter(
        UserResponseDB.user_id == current_user.id,
        UserResponseDB.exercise_id == response.exercise_id
    ).first()
    
    if existing_response:
        # Update existing response
        existing_response.response_text = response.response_text
        existing_response.submitted_at = func.now()
    else:
        # Create new response
        db_response = UserResponseDB(
            user_id=current_user.id,
            exercise_id=response.exercise_id,
            response_text=response.response_text
        )
        db.add(db_response)
    
    db.commit()
    return {"message": "Response submitted successfully"}

@app.post("/complete-theme/{theme_id}")
def complete_theme(theme_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Get the theme to access module_id
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    # Check if all exercises in the theme have responses
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme_id).all()
    
    for exercise in exercises:
        response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        if not response:
            raise HTTPException(status_code=400, detail="All exercises must be completed before marking theme as complete")
    
    # Mark theme as completed
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.theme_id == theme_id
    ).first()
    
    if progress:
        progress.completed = True
        progress.completed_at = func.now()
    else:
        progress = UserProgress(
            user_id=current_user.id,
            module_id=theme.module_id,
            theme_id=theme_id,
            completed=True,
            completed_at=func.now()
        )
        db.add(progress)
    
    db.commit()
    return {"message": "Theme completed successfully"}

# Legacy endpoints for compatibility
@app.get("/steps", response_model=List[dict])
def get_steps_legacy(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint for compatibility with old frontend"""
    modules = db.query(Module).filter(Module.is_active == True).order_by(Module.order_number).all()
    
    result = []
    for module in modules:
        # Check if module is completed
        module_progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.module_id == module.id,
            UserProgress.completed == True
        ).first()
        
        result.append({
            "id": module.id,
            "title": module.title,
            "description": module.description,
            "completed": module_progress is not None
        })
    
    return result

@app.get("/steps/{step_id}/exercises")
def get_step_exercises_legacy(step_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint - returns exercises from the first theme of the module"""
    # Get first theme of the module
    theme = db.query(Theme).filter(
        Theme.module_id == step_id,
        Theme.order_number == 1
    ).first()
    
    if not theme:
        return []
    
    exercises = db.query(Exercise).filter(Exercise.theme_id == theme.id).order_by(Exercise.order_number).all()
    
    result = []
    for exercise in exercises:
        user_response = db.query(UserResponseDB).filter(
            UserResponseDB.user_id == current_user.id,
            UserResponseDB.exercise_id == exercise.id
        ).first()
        
        result.append({
            "id": exercise.id,
            "question": exercise.question,
            "user_response": user_response.response_text if user_response else None
        })
    
    return result

@app.post("/complete-step/{step_id}")
def complete_step_legacy(step_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Legacy endpoint - completes the first theme of the module"""
    theme = db.query(Theme).filter(
        Theme.module_id == step_id,
        Theme.order_number == 1
    ).first()
    
    if theme:
        return complete_theme(theme.id, current_user, db)
    
    return {"message": "Step completed successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 