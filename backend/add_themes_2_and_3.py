"""
Script pour ajouter les Thèmes 2 et 3 au Module 1
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Theme, ThemeCard

# Styles communs
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def create_theme2(db: Session, module_id: int):
    """Créer le Thème 2"""
    print("\n📚 Création du Thème 2...")
    theme = Theme(
        title="Autoconocimiento emocional profundo",
        content="Profundizaremos en la identificación de tus emociones primarias y en el reconocimiento de las necesidades emocionales.",
        order_number=2,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 2 créé (ID: {theme.id})")
    return theme

def create_theme2_cards(db: Session, theme_id: int):
    """Créer les cards du thème 2"""
    print("\n🎴 Création des cards du Thème 2...")
    
    cards = [
        {
            "title": "Bienvenida al Tema 2",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Autoconocimiento Emocional Profundo</h1>

<p style="margin-bottom: 16px;">En este tema, profundizaremos en la <strong>identificación de tus emociones primarias</strong> y en el <strong>reconocimiento de las necesidades emocionales</strong>.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Es crucial entender</h3>
<p style="margin-bottom: 0;">Nuestras emociones no solo son respuestas inmediatas a los eventos, sino que también son señales que nos indican nuestras necesidades internas no satisfechas.</p>
</div>

<p style="margin-bottom: 16px;">Al desarrollar un mayor autoconocimiento emocional, podrás identificar estas señales y actuar de manera más consciente.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: Identificar Emociones Primarias",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Identificar Emociones Primarias</h1>

<p style="margin-bottom: 16px;">Las emociones primarias son las respuestas emocionales más básicas e instintivas que todos los seres humanos experimentan.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Las 6 Emociones Primarias</h3>
<p style="margin-bottom: 0;">Miedo, tristeza, alegría, enojo, sorpresa y asco. Estas emociones tienen una función evolutiva: nos ayudan a responder a nuestro entorno de manera rápida para sobrevivir y adaptarnos.</p>
</div>

<p style="margin-bottom: 16px;">Es importante aprender a identificar estas emociones a medida que surgen, sin juicio ni represión, ya que cada una de ellas contiene información valiosa sobre lo que necesitamos en ese momento.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "Beneficios de Identificar Emociones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Beneficios de identificar las emociones primarias</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Consciencia emocional</h3>
<p style="margin-bottom: 0;">Al ser más conscientes de tus emociones primarias, puedes actuar de manera más alineada con tus valores y deseos, en lugar de reaccionar impulsivamente.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Prevención de conflictos</h3>
<p style="margin-bottom: 0;">Al identificar las emociones en el momento en que surgen, puedes evitar que escalen en situaciones conflictivas o dañinas.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Desarrollo de empatía</h3>
<p style="margin-bottom: 0;">Cuando reconoces tus propias emociones, también te vuelves más empático hacia las emociones de los demás, lo que mejora las relaciones interpersonales.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 3
        },
        
        {
            "title": "Paul Ekman y las Emociones Universales",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Las Emociones son Universales</h2>

<div style="background: {C_BG_GRAY}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Paul Ekman</h3>
<p style="margin-bottom: 12px;">Según Paul Ekman, un reconocido psicólogo en el campo de las emociones, las emociones primarias son universales y están presentes en todas las culturas.</p>
<p style="margin-bottom: 0;">Esto sugiere que, aunque las expresiones emocionales pueden variar entre diferentes sociedades, la experiencia interna de estas emociones es compartida por todos los seres humanos.</p>
</div>

<p style="margin-bottom: 16px;">Ekman también señala que identificar y regular estas emociones es fundamental para el bienestar psicológico, ya que nos permiten procesar nuestras experiencias de manera efectiva.</p>
</div>""",
            "card_type": "theory",
            "order_number": 4
        },
        
        {
            "title": "Ejercicio: Identificar Emociones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Explora tus Emociones Primarias</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a explorar tus emociones primarias.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2 Emociones</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.1: Identificar emociones</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 5
        },
        
        {
            "title": "Subtema 2: Reconocer Necesidades Emocionales",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Reconocer Necesidades Emocionales</h1>

<p style="margin-bottom: 16px;">Cada emoción primaria está conectada a una necesidad emocional. Las emociones actúan como un sistema de alerta que nos indica si nuestras necesidades están siendo satisfechas o no.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Ejemplos</h3>
<p style="margin-bottom: 8px;"><strong>Miedo</strong> puede señalar una necesidad de seguridad</p>
<p style="margin-bottom: 8px;"><strong>Tristeza</strong> puede revelar una necesidad de apoyo o consuelo</p>
<p style="margin-bottom: 0;"><strong>Enojo</strong> puede indicar que sentimos que se ha violado un límite importante</p>
</div>

<p style="margin-bottom: 16px;">Al identificar estas necesidades, puedes empezar a tomar acciones más efectivas para satisfacerlas y evitar quedarte atrapado en ciclos emocionales insalubres.</p>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        
        {
            "title": "Beneficios de Reconocer Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Beneficios de reconocer necesidades emocionales</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Satisfacción personal</h3>
<p style="margin-bottom: 0;">Ser consciente de tus necesidades emocionales te permite satisfacerlas de manera efectiva, lo que lleva a una mayor sensación de bienestar.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Reducción del estrés</h3>
<p style="margin-bottom: 0;">Al entender y abordar tus necesidades emocionales, puedes reducir la ansiedad y el estrés relacionados con la insatisfacción emocional.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Mejora en las relaciones</h3>
<p style="margin-bottom: 0;">Reconocer tus propias necesidades emocionales también te permite comunicarte mejor con los demás y establecer relaciones más saludables y auténticas.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        
        {
            "title": "Carl Rogers y la Persona Completa",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">La Teoría de Carl Rogers</h2>

<div style="background: {C_BG_GRAY}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">La Persona Completa</h3>
<p style="margin-bottom: 12px;">Carl Rogers destacó la importancia de las necesidades emocionales en su teoría de la "persona completa".</p>
<p style="margin-bottom: 0;">Cuando las personas son conscientes de sus necesidades y trabajan activamente para satisfacerlas, tienden a ser más equilibradas y felices. En cambio, cuando estas necesidades se ignoran o se niegan, surgen conflictos internos.</p>
</div>

<p style="margin-bottom: 16px;">El reconocimiento y la satisfacción de las necesidades emocionales son esenciales para la autoaceptación y la autorrealización.</p>
</div>""",
            "card_type": "theory",
            "order_number": 8
        },
        
        {
            "title": "Ejercicio: Reconocer Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Reconoce tus Necesidades Emocionales</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a reconocer tus necesidades emocionales.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2 Emociones</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.2: Reconocer necesidades emocionales</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 9
        },
        
        {
            "title": "Ejercicio: Plan para Satisfacer Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Tu Plan de Acción</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">El día de mañana no habrá lectura en la guía, pero sí tienes una tarea muy importante.</p>

<div style="background: {C_BG_GRAY}; border: 2px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 8px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Compromiso contigo mismo/a</h3>
<p style="margin-bottom: 0;">Como parte del aprendizaje y compromiso contigo mismo/a, vas a realizar el ejercicio de crear un plan concreto para satisfacer tus necesidades emocionales.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2 Emociones</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.3: Creando un Plan para satisfacer mis necesidades</p>
</div>
</div>""",
            "card_type": "exercise",
            "order_number": 10
        },
        
        {
            "title": "Conclusión del Tema 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conexión Profunda Contigo Mismo/a</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">Este tema te llevará a un nivel más profundo de conexión contigo mismo/a.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo que has logrado:</h3>
<p style="margin-bottom: 12px;">Identificar tus emociones primarias y las necesidades emocionales que subyacen a estas es un paso crucial para entender por qué reaccionas de ciertas maneras.</p>
<p style="margin-bottom: 0;">Al desarrollar este nivel de autoconocimiento emocional, estarás mejor equipado/a para responder de manera más intencional y saludable en tu vida diaria.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Siguiente Paso</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Continúa al Tema 3: Gestionando y expresando emociones</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 11
        }
    ]
    
    for card_data in cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme_id
        )
        db.add(card)
    
    db.commit()
    print(f"✅ {len(cards)} cards créées pour le Thème 2")
    return len(cards)

def create_theme3(db: Session, module_id: int):
    """Créer le Thème 3"""
    print("\n📚 Création du Thème 3...")
    theme = Theme(
        title="Gestionando y expresando emociones",
        content="Aprenderás cómo gestionar y expresar tus emociones de manera saludable y efectiva.",
        order_number=3,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 3 créé (ID: {theme.id})")
    return theme

def create_theme3_cards(db: Session, theme_id: int):
    """Créer les cards du thème 3 (partie 1/2)"""
    print("\n🎴 Création des cards du Thème 3...")
    
    cards = [
        {
            "title": "Bienvenida al Tema 3",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Gestionando y Expresando Emociones</h1>

<p style="margin-bottom: 16px;">En esta última parte del módulo, nos adentraremos en cómo <strong>gestionar y expresar nuestras emociones</strong> de manera saludable y efectiva.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Siguiente Nivel</h3>
<p style="margin-bottom: 0;">Saber identificar nuestras emociones es un primer paso esencial, pero ser capaces de regularlas y expresarlas de manera asertiva es lo que realmente nos permite avanzar hacia una vida más equilibrada y consciente.</p>
</div>

<p style="margin-bottom: 16px;">Este tema se enfoca en proporcionarte las herramientas necesarias para gestionar las emociones más difíciles y comunicar lo que sientes y necesitas de una manera clara, respetuosa y efectiva.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: Técnicas de Regulación Emocional",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Técnicas de Regulación Emocional</h1>

<p style="margin-bottom: 16px;">Las emociones, especialmente las intensas, pueden ser abrumadoras si no sabemos cómo manejarlas.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">¿Por qué es importante?</h3>
<p style="margin-bottom: 0;">La regulación emocional es la capacidad de manejar y responder a una experiencia emocional de manera saludable. Quienes desarrollan esta habilidad son más capaces de mantener relaciones interpersonales satisfactorias, tienen menos niveles de estrés, y gozan de mayor bienestar general.</p>
</div>

<p style="margin-bottom: 16px;">Este subtema explora diversas técnicas basadas en la investigación psicológica que han demostrado ser efectivas para regular las emociones.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "Estrategias de Regulación Emocional",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Estrategias Efectivas</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Reevaluación del pensamiento</h3>
<p style="margin-bottom: 0;">Consiste en reinterpretar una situación para cambiar su impacto emocional. En lugar de ver un evento como una amenaza, puedes aprender a verlo como un desafío o una oportunidad de crecimiento.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Mindfulness y atención plena</h3>
<p style="margin-bottom: 0;">Nos ayuda a observar nuestras emociones sin juzgarlas, reduciendo su intensidad y permitiéndonos responder con mayor claridad.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Respiración y relajación</h3>
<p style="margin-bottom: 0;">El control de la respiración es muy efectivo para disminuir la activación fisiológica asociada con el estrés o la ira. La respiración diafragmática reduce la respuesta del sistema nervioso simpático.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 3
        },
    ]
    
    # Continuer dans le même script...
    cards_part2 = [
        {
            "title": "Consejos Prácticos para el Día a Día",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">7 Consejos Prácticos</h2>

<p style="margin-bottom: 16px;"><strong>1. Reconoce y valida tus emociones:</strong> Acéptalas sin juzgarte.</p>
<p style="margin-bottom: 16px;"><strong>2. Practica la respiración consciente:</strong> 4 segundos inhalando, 4 sosteniendo, 4 exhalando.</p>
<p style="margin-bottom: 16px;"><strong>3. Etiqueta tus emociones:</strong> "Estoy molesto porque siento que no me están escuchando".</p>
<p style="margin-bottom: 16px;"><strong>4. Redirige la energía:</strong> Ejercicio, escritura, actividades creativas.</p>
<p style="margin-bottom: 16px;"><strong>5. Cuida tus pensamientos:</strong> Identifica pensamientos limitantes y reemplázalos.</p>
<p style="margin-bottom: 16px;"><strong>6. Establece límites emocionales:</strong> Aprende a decir "no".</p>
<p style="margin-bottom: 16px;"><strong>7. Autocuidado:</strong> Dormir, alimentarte bien, momentos de relajación.</p>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        
        {
            "title": "Ejercicio: Técnicas de Regulación",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Prepárate para Gestionar</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a prepararte para lograr gestionar tus emociones.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3 Gestión Emocional</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.1: Técnicas de Regulación Emocional</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 5
        },
        
        {
            "title": "Subtema 2: Comunicación Asertiva",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Comunicación Asertiva de las Necesidades</h1>

<p style="margin-bottom: 16px;">Gestionar las emociones también implica la capacidad de <strong>expresar lo que sientes y necesitas</strong> de manera efectiva.</p>

<div style="background: {C_BG_GRAY}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">¿Qué es la comunicación asertiva?</h3>
<p style="margin-bottom: 0;">Es una habilidad interpersonal clave que permite expresar nuestras emociones y necesidades de manera honesta y directa, respetando tanto tus necesidades como las de los demás.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        
        {
            "title": "Características de la Comunicación Asertiva",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Características Clave</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Claridad</h3>
<p style="margin-bottom: 0;">Expresar lo que sientes y necesitas de manera directa y sin ambigüedades. En lugar de evitar el conflicto, la asertividad se enfoca en resolverlo desde la comprensión mutua.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Uso de "Yo" en lugar de "Tú"</h3>
<p style="margin-bottom: 0;">"Me siento ignorado cuando no respondes a mis mensajes" en lugar de "Nunca respondes a mis mensajes".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Equilibrio entre expresión y escucha</h3>
<p style="margin-bottom: 0;">Ser asertivo implica no solo expresar lo que necesitas, sino también estar dispuesto a escuchar y comprender las necesidades del otro.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        
        {
            "title": "Beneficios de la Comunicación Asertiva",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Beneficios Comprobados</h2>

<p style="margin-bottom: 16px;">✓ Promueve relaciones más honestas y abiertas</p>
<p style="margin-bottom: 16px;">✓ Mejora la satisfacción personal y profesional</p>
<p style="margin-bottom: 16px;">✓ Reduce el malestar emocional (frustración y resentimiento)</p>
<p style="margin-bottom: 16px;">✓ Ayuda a prevenir conflictos</p>
<p style="margin-bottom: 16px;">✓ Aumenta la autoconfianza y disminuye la ansiedad</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin-top: 24px;">
<p style="margin: 0;">Las personas que se comunican asertivamente tienden a sentirse más seguras de sí mismas, lo que reduce su nivel de ansiedad en situaciones sociales o profesionales.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 8
        },
        
        {
            "title": "Ejercicio: Comunicación Asertiva",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Aprende a Comunicar Asertivamente</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a prepararte para lograr comunicar de manera asertiva tus emociones y por ende tus necesidades.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3 Gestión Emocional</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.2: Comunicación asertiva de las necesidades</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 9
        },
        
        {
            "title": "Subtema 3: Caja de Herramientas Emocionales",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Construcción de mi Caja de Herramientas Emocionales</h1>

<p style="margin-bottom: 16px;">Este subtema es el cierre del trabajo emocional realizado a lo largo de este módulo.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Tu Caja Personal</h3>
<p style="margin-bottom: 0;">Aquí vas a reunir todas las herramientas que has aprendido en una caja de recursos emocionales que te acompañará en tu día a día.</p>
</div>

<p style="margin-bottom: 16px;">Esta caja es simbólica y puede contener diferentes estrategias que te ayuden a regular tus emociones y expresarlas de forma más consciente.</p>
</div>""",
            "card_type": "theory",
            "order_number": 10
        },
        
        {
            "title": "Qué Incluir en tu Caja",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Ejemplos de Herramientas</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin: 0;">✓ Técnicas de respiración o relajación que te ayuden a calmarte en momentos de estrés</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin: 0;">✓ Recordatorios de frases asertivas que te ayuden a comunicarte mejor</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin: 0;">✓ Un diario de emociones donde puedas escribir tus pensamientos y sentimientos</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin: 0;">✓ Visualizaciones o imágenes mentales que te inspiren calma o fortaleza</p>
</div>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin-top: 24px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Por qué es importante</h3>
<p style="margin: 0;">Al tener una colección clara de herramientas, sabes que siempre puedes recurrir a ellas cuando las emociones se vuelven abrumadoras. Las personas que tienen recursos concretos para gestionar el estrés son más resilientes.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 11
        },
        
        {
            "title": "Ejercicio: Tu Caja de Herramientas",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Construye tu Caja</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a poner en práctica cómo gestionar tu mundo emocional.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3 Gestión Emocional</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.3: Construcción de mi caja de herramientas emocionales</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 12
        },
        
        {
            "title": "Reflexión Final del Módulo",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Reflexión Final del Módulo</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A lo largo de este módulo, has aprendido que <strong>cada emoción tiene un propósito y un mensaje</strong>.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0;">
<h3 style="margin-top: 0; color: white;">El Verdadero Crecimiento</h3>
<p style="margin-bottom: 12px;">El verdadero crecimiento personal radica en ser capaces de escuchar nuestras emociones, atender nuestras necesidades y tener el coraje de expresarlas de manera honesta y respetuosa.</p>
<p style="margin-bottom: 0;">Cuando logramos este equilibrio, no solo resolvemos conflictos o reducimos el estrés; creamos un espacio para vivir de manera más auténtica, plena y consciente.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Recuerda</h3>
<p style="margin-bottom: 0;">Gestionar tus emociones no significa controlarlas o reprimirlas, sino aprender a navegar por ellas con sabiduría y compasión. La práctica continua de estas herramientas te permitirá enfrentar cualquier desafío emocional que la vida te presente, con mayor claridad y confianza.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 13
        },
        
        {
            "title": "¡Felicidades por Completar el Módulo 1!",
            "content": f"""<div style="{css()}">
<div style="background: {C_TITLE}; color: white; padding: 40px; border-radius: 15px; text-align: center; margin: 40px 0;">
<h1 style="margin-top: 0; color: white; font-size: 2.5em;">¡Felicidades!</h1>
<h2 style="color: white; margin-bottom: 20px;">Has completado el Módulo 1: El Mapa de tus Emociones</h2>
<p style="font-size: 1.2em; margin-bottom: 0;">Has dado un paso enorme en tu desarrollo personal y emocional. Estamos muy orgullosos de ti.</p>
</div>

<div style="background: {C_BG_GRAY}; padding: 30px; border-radius: 10px; margin: 30px 0;">
<h3 style="color: {C_TITLE}; margin-top: 0; text-align: center;">Lo que has logrado:</h3>
<p style="text-align: center; margin-bottom: 16px;">✓ Exploraste tu historia emocional</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Identificaste tus patrones y raíces emocionales</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Reconociste tus emociones primarias y necesidades</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Aprendiste técnicas de regulación emocional</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Desarrollaste comunicación asertiva</p>
<p style="text-align: center; margin-bottom: 0;">✓ Construiste tu caja de herramientas emocionales</p>
</div>

<p style="text-align: center; font-style: italic; color: #5a5a5a; margin-top: 40px;">Continúa tu viaje de transformación en los próximos módulos.</p>
</div>""",
            "card_type": "conclusion",
            "order_number": 14
        }
    ]
    
    for card_data in cards + cards_part2:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme_id
        )
        db.add(card)
    
    db.commit()
    print(f"✅ {len(cards) + len(cards_part2)} cards créées pour le Thème 3")
    return len(cards) + len(cards_part2)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 AJOUT DES THÈMES 2 ET 3 AU MODULE 1")
        print("=" * 70)
        
        MODULE_ID = 1
        
        # Créer le thème 2
        theme2 = create_theme2(db, MODULE_ID)
        num_cards2 = create_theme2_cards(db, theme2.id)
        
        # Créer le thème 3
        theme3 = create_theme3(db, MODULE_ID)
        num_cards3 = create_theme3_cards(db, theme3.id)
        
        print("\n" + "=" * 70)
        print("✅ CRÉATION TERMINÉE AVEC SUCCÈS")
        print("=" * 70)
        print(f"📚 Thème 2 ID: {theme2.id} ({num_cards2} cards)")
        print(f"📚 Thème 3 ID: {theme3.id} ({num_cards3} cards)")
        print(f"\n🎯 Le Module 1 complet est prêt!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

