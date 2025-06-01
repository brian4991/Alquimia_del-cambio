from sqlalchemy.orm import Session
from models import Module, Theme, Exercise, ThemeCard
from card_creator import create_theme_cards

def init_database(db: Session):
    """Initialize database with Module 1 content using cards system"""
    
    # Check if data already exists
    existing_module = db.query(Module).first()
    if existing_module:
        print("Database already initialized")
        return
    
    print("Initializing database with Module 1 content...")
    
    # Create Module 1
    module1 = Module(
        title="El Mapa de tus Emociones",
        description="Aprende a gestionar tu mundo emocional y expresar lo que sientes y necesitas.",
        objective="El propósito de este módulo es que aprendas a gestionar tu mundo emocional y expresar lo que sientes y necesitas, con una mayor consciencia y asertividad.",
        belief_to_transform="Expresar lo que siento me hace débil y vulnerable",
        expected_results="Logras gestionar y regular tu sentir y tus emociones. Logras escuchar tus necesidades y expresarlas con seguridad y asertividad.",
        recommended_book="Inteligencia emocional de Daniel Goleman (lo encuentras en la carpeta de Bonus)",
        audio_file="modulo-1-intro.mp3",
        order_number=1,
        is_active=True
    )
    db.add(module1)
    db.flush()  # Get the ID
    
    # Create themes
    theme1 = Theme(
        title="Explorando mi historia emocional",
        content="El propósito de este tema es guiarte a través de la exploración consciente de tu historia emocional.",
        order_number=1,
        module_id=module1.id
    )
    
    theme2 = Theme(
        title="Autoconocimiento emocional profundo", 
        content="Profundizaremos en la identificación de tus emociones primarias y en el reconocimiento de las necesidades emocionales.",
        order_number=2,
        module_id=module1.id
    )
    
    theme3 = Theme(
        title="Gestionando y expresando emociones",
        content="Aprenderás a gestionar y expresar tus emociones de manera saludable y efectiva.",
        order_number=3,
        module_id=module1.id
    )
    
    db.add_all([theme1, theme2, theme3])
    db.flush()  # Get the IDs
    
    # Create theme cards using the card creator
    create_theme_cards(db, [theme1, theme2, theme3])
    
    # Create exercises
    exercises = [
        # Theme 1 exercises
        Exercise(
            title="Historia y Exploración Emocional",
            question="Describe tu historia emocional desde la infancia hasta ahora. ¿Qué eventos o relaciones han marcado tu forma de sentir y expresar emociones?",
            instructions="Escribe con sinceridad y detalle. No hay respuestas correctas o incorrectas. Este es un espacio seguro para explorar tu historia.",
            order_number=1,
            theme_id=theme1.id
        ),
        Exercise(
            title="Reconociendo Patrones Emocionales",
            question="¿Qué patrones emocionales reconoces en ti? ¿En qué situaciones o con qué personas tiendes a reaccionar de manera similar?",
            instructions="Reflexiona sobre situaciones recurrentes y tus respuestas automáticas. Identifica al menos 3 patrones emocionales.",
            order_number=2,
            theme_id=theme1.id
        ),
        Exercise(
            title="Raíces Emocionales",
            question="¿Cuáles crees que son las raíces de tus principales patrones emocionales? ¿Qué experiencias tempranas pueden haber influido en cómo manejas tus emociones hoy?",
            instructions="Explora con compasión las experiencias que te han formado. Recuerda que el objetivo es comprender, no juzgar.",
            order_number=3,
            theme_id=theme1.id
        ),
        
        # Theme 2 exercises  
        Exercise(
            title="Identificar Emociones Primarias",
            question="Durante una semana, lleva un registro de tus emociones primarias (miedo, tristeza, alegría, enojo, sorpresa, asco). ¿Cuáles experimentas más frecuentemente y en qué contextos?",
            instructions="Anota al menos una emoción por día con el contexto en que apareció. Sé específico sobre la situación y la intensidad de la emoción.",
            order_number=1,
            theme_id=theme2.id
        ),
        Exercise(
            title="Reconocer Necesidades Emocionales",
            question="Para cada emoción que identificaste en el ejercicio anterior, pregúntate: ¿Qué necesidad emocional me está señalando esta emoción? ¿Qué requiero en este momento?",
            instructions="Conecta cada emoción con su necesidad subyacente. Por ejemplo: enojo = necesidad de respeto, tristeza = necesidad de consuelo.",
            order_number=2,
            theme_id=theme2.id
        ),
        Exercise(
            title="Plan para Satisfacer Necesidades",
            question="Crea un plan concreto para satisfacer las necesidades emocionales que identificaste. ¿Qué acciones específicas puedes tomar para atender mejor tus necesidades?",
            instructions="Sé específico y realista. Define acciones concretas que puedes implementar en tu vida diaria para satisfacer tus necesidades emocionales.",
            order_number=3,
            theme_id=theme2.id
        ),
        
        # Theme 3 exercises
        Exercise(
            title="Técnicas de Regulación Emocional",
            question="De las 7 técnicas de regulación emocional presentadas, ¿cuáles resuenan más contigo? Describe una situación reciente donde podrías haber aplicado una de estas técnicas.",
            instructions="Elige al menos 3 técnicas que consideres más útiles para ti y explica cómo las implementarías en situaciones específicas de tu vida.",
            order_number=1,
            theme_id=theme3.id
        ),
        Exercise(
            title="Comunicación Asertiva",
            question="Piensa en una situación reciente donde no expresaste una necesidad o emoción importante. ¿Cómo podrías haber comunicado esto de manera asertiva? Reescribe la conversación.",
            instructions="Usa las técnicas de comunicación asertiva: habla en primera persona, sé claro y directo, respeta al otro. Practica el nuevo diálogo.",
            order_number=2,
            theme_id=theme3.id
        ),
        Exercise(
            title="Mi Caja de Herramientas Emocionales",
            question="Crea tu caja de herramientas emocionales personal. ¿Qué técnicas, frases, recordatorios o actividades incluirías para gestionar mejor tus emociones?",
            instructions="Organiza tu caja en categorías: técnicas rápidas (para crisis), herramientas diarias (mantenimiento), estrategias a largo plazo (crecimiento). Incluye al menos 2 elementos por categoría.",
            order_number=3,
            theme_id=theme3.id
        ),
    ]
    
    db.add_all(exercises)
    db.commit()
    
    print("✅ Database initialized successfully with Module 1 content and cards system!")
    print(f"   - 1 Module created")
    print(f"   - 3 Themes created")
    print(f"   - {len(exercises)} Exercises created")
    
    # Count cards
    total_cards = db.query(ThemeCard).count()
    print(f"   - {total_cards} Cards created")
    
    print("🎯 Module 1: 'El Mapa de tus Emociones' is ready!")
    print("🔗 Cards system implemented for better content management!") 