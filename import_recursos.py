"""
Script to import recursos from text files and create cards via API
Usage: python import_recursos.py
"""

import os
import requests
import json

# API Configuration
API_BASE_URL = "http://localhost:8000"  # Change this to your deployed URL if needed
ADMIN_USERNAME = "admin"  # Update with your admin credentials
ADMIN_PASSWORD = "admin123"

# Style templates matching contenido cards
# Font: Source Sans Pro
# Couleurs: #6b745a (sage), #a28d72 (taupe), #cbcbcc (gray)
CARD_STYLES = {
    "intro": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">{title}</h1>
{content}
</div>""",
    
    "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.6em; margin-bottom: 16px; border-bottom: 2px solid #a28d72; padding-bottom: 10px;">{title}</h2>
{content}
</div>""",
    
    "section": """<div style="background: #f9f9f7; padding: 20px; border-left: 4px solid #a28d72; margin: 20px 0; font-family: 'Source Sans Pro', sans-serif;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">{title}</h3>
{content}
</div>""",
    
    "highlight": """<div style="background: #f5f5f0; padding: 20px; border: 1px solid #cbcbcc; border-radius: 8px; margin: 20px 0; font-family: 'Source Sans Pro', sans-serif;">
{content}
</div>""",
    
    "tip": """<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0; font-family: 'Source Sans Pro', sans-serif;">
<p style="margin: 0; color: #2d2d2d;"><strong>Tip:</strong> {content}</p>
</div>""",
    
    "list_item": """<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0; font-family: 'Source Sans Pro', sans-serif;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">{title}</h3>
{content}
</div>"""
}


def login_admin():
    """Login and get access token"""
    response = requests.post(
        f"{API_BASE_URL}/login",
        json={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Login failed: {response.text}")
        return None


def create_theme(token, module_id, title, description, order_number):
    """Create a theme of type 'resource'"""
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": title,
        "content": description,
        "order_number": order_number,
        "theme_type": "resource",
        "module_id": module_id
    }
    
    response = requests.post(
        f"{API_BASE_URL}/modules/{module_id}/themes",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to create theme: {response.text}")
        return None


def create_card(token, theme_id, title, content, card_type, order_number):
    """Create a card for a theme"""
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": title,
        "content": content,
        "card_type": card_type,
        "order_number": order_number,
        "theme_id": theme_id
    }
    
    response = requests.post(
        f"{API_BASE_URL}/themes/{theme_id}/cards",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to create card: {response.text}")
        return None


def parse_recurso_1(content):
    """Parse '¿Qué necesito realmente cuando me siento así?' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Las emociones no son el problema, son el mensaje. Cada vez que sientes tristeza, miedo, enojo o ansiedad, hay una necesidad profunda que no está siendo escuchada.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Esta guía te acompaña a identificar esa necesidad y a responderla con acciones concretas que te ayuden a sentirte más alineada contigo misma.</p>

<h3 style="color: #6b745a; margin-top: 25px; font-size: 1.3em;">¿Cómo usar esta guía?</h3>
<ol style="margin-left: 20px; line-height: 1.8;">
<li>Busca la emoción que estás sintiendo.</li>
<li>Lee las posibles necesidades que podrían estar detrás.</li>
<li>Elige una o más acciones prácticas para atenderte con compasión.</li>
</ol>

<p style="font-size: 1.1em; margin-top: 20px;">A continuación tendrás la lista de emociones más frecuentes o básicas, para que comprendas tus necesidades:</p>"""
    
    cards.append({
        "title": "¿Qué necesito realmente cuando me siento así?",
        "content": CARD_STYLES["intro"].format(
            title="¿Qué necesito realmente cuando me siento así?",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # Emotion cards
    emotions = [
        {
            "title": "Tristeza",
            "needs": [
                "Descanso emocional",
                "Apoyo y validación",
                "Procesar una pérdida o desilusión",
                "Espacio para sentir sin juicio"
            ],
            "actions": [
                "Escribir una carta de despedida o cierre",
                "Pedir compañía sin necesidad de hablar",
                "Permitir un día de calma sin exigencias",
                "Aceptar lo que sientes sin intentar 'arreglarlo' (lo vas arreglar después)"
            ],
            "order": 2
        },
        {
            "title": "Miedo",
            "needs": [
                "Seguridad",
                "Claridad o información",
                "Apoyo ante un cambio",
                "Tiempo para procesar"
            ],
            "actions": [
                "Establecer una rutina que te dé estabilidad",
                "Hacer una lista con lo que sí está bajo tu control",
                "Buscar información confiable o hablar con alguien que te dé confianza",
                "Visualizar un escenario posible y reconfortante"
            ],
            "order": 3
        },
        {
            "title": "Enojo",
            "needs": [
                "Sentirme respetad@",
                "Reconocer mis límites",
                "Expresar lo que me molesta",
                "Recuperar mi poder personal"
            ],
            "actions": [
                "Escribir lo que te molesta sin filtro (en privado)",
                "Establecer un límite claro en una relación",
                "Hacer una pausa antes de reaccionar",
                "Validar que tu enojo tiene un mensaje"
            ],
            "order": 4
        },
        {
            "title": "Ansiedad",
            "needs": [
                "Calma interior",
                "Presencia en el ahora",
                "Confianza en ti o en el proceso",
                "Soltar el control"
            ],
            "actions": [
                "Respiración consciente durante 3 minutos",
                "Conectar con tu cuerpo: caminar, estirarte",
                "Escribir todo lo que te preocupa y luego tachar lo que no puedes controlar",
                "Hacer una pausa digital: alejarte del celular por una hora"
            ],
            "order": 5
        },
        {
            "title": "Culpa",
            "needs": [
                "Reparar o enmendar",
                "Ser compasiv@ contigo mism@",
                "Distinguir entre culpa útil y culpa aprendida",
                "Reafirmar tus valores"
            ],
            "actions": [
                "Pedir disculpas si es necesario",
                "Escribir una carta de auto perdón",
                "Reflexionar si esa culpa viene de tus valores o de una expectativa externa",
                "Preguntarte: ¿Qué haré diferente la próxima vez?"
            ],
            "order": 6
        },
        {
            "title": "Frustración",
            "needs": [
                "Progreso real en algo importante",
                "Reconocimiento de mi esfuerzo",
                "Ajustar mis expectativas",
                "Claridad en mis metas"
            ],
            "actions": [
                "Celebrar un pequeño avance, por mínimo que sea",
                "Reescribir tus metas con mayor amabilidad",
                "Pedir feedback o expresar tu necesidad de reconocimiento",
                "Cambiar el enfoque del resultado al proceso"
            ],
            "order": 7
        }
    ]
    
    for emotion in emotions:
        needs_html = "<ul style='list-style-type: disc; margin-left: 20px; line-height: 1.8;'>\n"
        for need in emotion["needs"]:
            needs_html += f"<li>{need}</li>\n"
        needs_html += "</ul>"
        
        actions_html = "<ul style='list-style-type: disc; margin-left: 20px; line-height: 1.8;'>\n"
        for action in emotion["actions"]:
            actions_html += f"<li>{action}</li>\n"
        actions_html += "</ul>"
        
        emotion_content = f"""<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>¿Qué podrías estar necesitando?</strong></p>
{needs_html}

<p style="font-size: 1.1em; margin-top: 24px; margin-bottom: 16px;"><strong>¿Qué podrías hacer?</strong></p>
{actions_html}"""
        
        cards.append({
            "title": f"Emoción: {emotion['title']}",
            "content": CARD_STYLES["content"].format(
                title=f"Emoción: {emotion['title']}",
                content=emotion_content
            ),
            "card_type": "practical",
            "order_number": emotion["order"]
        })
    
    return cards


def parse_recurso_2(content):
    """Parse 'Emocionario' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Bienvenidos (as) al Emocionario, una herramienta sencilla para ayudarte a identificar y comprender tus emociones.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Las emociones no son ni buenas ni malas, simplemente existen para darnos información valiosa sobre cómo estamos viviendo y qué necesitamos.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Aquí aprenderás sobre las emociones primarias, secundarias, y terciarias, qué función tienen en nuestra vida y cómo se manifiestan en situaciones cotidianas.</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recomendación:</strong> Ver la película "Intensamente" también te ayudará a tener una gran noción sobre las emociones.</p>
</div>"""
    
    cards.append({
        "title": "Emocionario: Guía de las Emociones",
        "content": CARD_STYLES["intro"].format(
            title="Emocionario: Guía de las Emociones",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # Primary emotions card
    primary_emotions = [
        ("Alegría", "Motiva a repetir acciones o situaciones placenteras.", "Sientes alegría al ver a un amigo que no veías hace tiempo."),
        ("Tristeza", "Permite procesar una pérdida y buscar apoyo.", "Sentir tristeza tras la muerte de un ser querido."),
        ("Miedo", "Protege de peligros y amenazas.", "Sentir miedo al caminar solo en la oscuridad."),
        ("Enojo", "Proporciona energía para defenderse o corregir injusticias.", "Enfado al ser tratado injustamente."),
        ("Asco", "Protege de lo dañino, físico o emocional.", "Sentir asco ante comida en mal estado."),
        ("Sorpresa", "Prepara para procesar lo inesperado.", "Sorpresa al recibir una noticia inesperada, buena o mala.")
    ]
    
    primary_content = "<p style='font-size: 1.1em; margin-bottom: 20px;'>Las emociones primarias son las respuestas emocionales más básicas e instintivas que todos los seres humanos experimentan.</p>\n"
    for emotion, function, example in primary_emotions:
        primary_content += CARD_STYLES["list_item"].format(
            title=emotion,
            content=f"<p style='margin-bottom: 10px;'><strong>Función:</strong> {function}</p><p style='margin: 0;'><strong>Ejemplo:</strong> {example}</p>"
        )
    
    cards.append({
        "title": "Emociones Primarias",
        "content": CARD_STYLES["content"].format(
            title="Emociones Primarias",
            content=primary_content
        ),
        "card_type": "theory",
        "order_number": 2
    })
    
    # Secondary emotions card
    secondary_emotions = [
        ("Orgullo", "Refuerza la autoestima y la valoración de logros.", "Orgullo después de completar un proyecto importante."),
        ("Vergüenza", "Impulsa a ajustar el comportamiento para ser aceptado.", "Vergüenza tras hacer algo inapropiado en público."),
        ("Culpa", "Motiva a reparar acciones que dañaron a otros.", "Sentir culpa por herir los sentimientos de alguien."),
        ("Ansiedad", "Prepara para enfrentar situaciones estresantes.", "Ansiedad antes de dar una presentación importante."),
        ("Empatía", "Conecta con las emociones de los demás.", "Sentir empatía al escuchar a un amigo en dificultad."),
        ("Frustración", "Indica que algo no sale como se esperaba.", "Frustración al no poder completar un proyecto.")
    ]
    
    secondary_content = "<p style='font-size: 1.1em; margin-bottom: 20px;'>Las emociones secundarias surgen de combinaciones de las emociones primarias y del aprendizaje social.</p>\n"
    for emotion, function, example in secondary_emotions:
        secondary_content += CARD_STYLES["list_item"].format(
            title=emotion,
            content=f"<p style='margin-bottom: 10px;'><strong>Función:</strong> {function}</p><p style='margin: 0;'><strong>Ejemplo:</strong> {example}</p>"
        )
    
    cards.append({
        "title": "Emociones Secundarias",
        "content": CARD_STYLES["content"].format(
            title="Emociones Secundarias",
            content=secondary_content
        ),
        "card_type": "theory",
        "order_number": 3
    })
    
    # Tertiary emotions card
    tertiary_emotions = [
        ("Esperanza", "Mantiene la motivación hacia el futuro.", "Esperanza de que una situación difícil mejorará."),
        ("Resentimiento", "Informa sobre heridas emocionales no resueltas.", "Resentimiento hacia alguien que te lastimó en el pasado."),
        ("Compasión", "Impulsa a ayudar y apoyar a quienes sufren.", "Compasión hacia una persona en situación de calle."),
        ("Gratitud", "Conecta con el aprecio por las cosas buenas.", "Sentir gratitud por el apoyo de un amigo."),
        ("Nostalgia", "Conecta con momentos pasados y emociones significativas.", "Nostalgia al escuchar una canción de la infancia.")
    ]
    
    tertiary_content = "<p style='font-size: 1.1em; margin-bottom: 20px;'>Las emociones terciarias son más complejas y están profundamente influenciadas por nuestra cultura y experiencias personales.</p>\n"
    for emotion, function, example in tertiary_emotions:
        tertiary_content += CARD_STYLES["list_item"].format(
            title=emotion,
            content=f"<p style='margin-bottom: 10px;'><strong>Función:</strong> {function}</p><p style='margin: 0;'><strong>Ejemplo:</strong> {example}</p>"
        )
    
    cards.append({
        "title": "Emociones Terciarias",
        "content": CARD_STYLES["content"].format(
            title="Emociones Terciarias",
            content=tertiary_content
        ),
        "card_type": "theory",
        "order_number": 4
    })
    
    return cards


def parse_recurso_3(content):
    """Parse 'Técnicas de gestión emocional' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Gestionar tus emociones no tiene que ser complicado; se trata de tomar pequeñas acciones diarias que te ayuden a mantener el equilibrio emocional.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Aquí te dejo algunas técnicas simples, pero poderosas, que puedes aplicar para manejar tus emociones de manera efectiva.</p>"""
    
    cards.append({
        "title": "Técnicas de Gestión Emocional para el Día a Día",
        "content": CARD_STYLES["intro"].format(
            title="Técnicas de Gestión Emocional para el Día a Día",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # Techniques
    techniques = [
        {
            "num": "1",
            "title": "La Respiración Consciente",
            "what": "Tomarte unos minutos para respirar profundamente puede cambiar tu estado emocional.",
            "how": "Inhala profundamente por la nariz durante 4 segundos, retén el aire por 4 segundos y exhala lentamente por la boca durante otros 4 segundos. Hazlo 3-5 veces.",
            "tip": "Usa esta técnica antes de enfrentarte a una situación estresante o cuando te sientas abrumado/a.",
            "order": 2
        },
        {
            "num": "2",
            "title": "Etiqueta tus Emociones",
            "what": "Identificar lo que sientes te ayuda a reducir la intensidad de las emociones.",
            "how": "Cuando sientas algo intenso, detente y pregúntate: '¿Qué emoción estoy sintiendo ahora?' ¿Es tristeza, enojo, frustración o ansiedad? Nómbrala en voz alta o en tu mente.",
            "tip": "Esto te ayuda a ser consciente de tus emociones, en lugar de dejar que te dominen.",
            "order": 3
        },
        {
            "num": "3",
            "title": "Cambia tu Diálogo Interno",
            "what": "Hablarte con amabilidad puede transformar cómo te sientes en situaciones difíciles.",
            "how": "Si te enfrentas a una emoción desagradable, reemplaza los pensamientos críticos con afirmaciones más positivas o realistas. Por ejemplo, en vez de decir 'No puedo con esto', di 'Estoy haciendo lo mejor que puedo, un paso a la vez'.",
            "tip": "Hazlo un hábito diario. Al notar tus pensamientos negativos, cámbialos por algo más constructivo.",
            "order": 4
        },
        {
            "num": "4",
            "title": "El Espacio de Pausa",
            "what": "Crear un momento de pausa entre una emoción fuerte y tu reacción te ayuda a responder mejor.",
            "how": "Cuando te sientas emocionalmente cargado/a, en lugar de reaccionar de inmediato, tómate unos segundos para respirar, evaluar la situación y elegir cómo quieres responder.",
            "tip": "Aplícalo antes de una conversación difícil o en situaciones estresantes.",
            "order": 5
        },
        {
            "num": "5",
            "title": "Movimiento y Energía",
            "what": "El ejercicio físico ayuda a liberar emociones retenidas.",
            "how": "Dedica 10-15 minutos al día a una caminata rápida, estiramientos o alguna actividad que disfrutes. El movimiento libera endorfinas que te hacen sentir mejor.",
            "tip": "Usa este recurso cuando sientas emociones negativas acumuladas como estrés, ansiedad o enojo.",
            "order": 6
        },
        {
            "num": "6",
            "title": "Escribe lo que Sientes",
            "what": "La escritura emocional es una herramienta terapéutica que te permite liberar lo que llevas dentro.",
            "how": "Tómate 5-10 minutos cada noche para escribir cómo te sentiste durante el día. Identifica qué emociones aparecieron, por qué, y cómo las gestionaste.",
            "tip": "Esta práctica te permitirá ver patrones emocionales y mejorar tu autoconocimiento.",
            "order": 7
        },
        {
            "num": "7",
            "title": "Practica la Gratitud",
            "what": "Apreciar lo positivo en tu vida ayuda a contrarrestar las emociones desagradables.",
            "how": "Al final del día, escribe tres cosas por las que te sientas agradecido/a. Pueden ser tan simples como un café por la mañana o una conversación agradable.",
            "tip": "Haz de la gratitud un hábito diario. Verás cómo cambia tu perspectiva emocional y te sientes más equilibrado/a.",
            "order": 8
        },
        {
            "num": "8",
            "title": "Establece Límites Saludables",
            "what": "A veces, nuestras emociones se desbordan porque no hemos puesto límites claros con los demás.",
            "how": "Aprende a decir 'no' sin culpa. Si te sientes abrumado/a, identifica situaciones en las que necesitas espacio y comunícalo de manera asertiva.",
            "tip": "Practica diciendo 'no' en situaciones pequeñas. Esto te ayudará a evitar el agotamiento emocional.",
            "order": 9
        },
        {
            "num": "9",
            "title": "Usa el 'Tiempo Emocional Fuera'",
            "what": "Un 'tiempo emocional fuera' es una técnica que te permite ponerle límite a tus emociones.",
            "how": "Si te sientes emocionalmente desbordado/a, toma unos 5, 10, 15 minutos para sentir tu emoción y validarla. Después de ese tiempo, detén tu emoción usando algunas de las otras herramientas y continúa con tu rutina y tu día.",
            "tip": "Usa esta técnica en el trabajo o en casa, cuando sientas que una emoción fuerte te está controlando.",
            "order": 10
        },
        {
            "num": "10",
            "title": "Visualización Positiva",
            "what": "La visualización te ayuda a calmar la mente y cambiar tu estado emocional.",
            "how": "Cierra los ojos e imagina un lugar que te traiga paz (una playa, un bosque, etc.). Visualiza los detalles: los sonidos, los olores, la temperatura. Esto te llevará a un estado mental más relajado.",
            "tip": "Practica la visualización cuando te sientas abrumado/a o antes de situaciones que te generen ansiedad.",
            "order": 11
        },
        {
            "num": "11",
            "title": "La Técnica de 'Reencuadre'",
            "what": "Reinterpretar una situación negativa puede cambiar cómo la percibes emocionalmente.",
            "how": "Cuando algo te moleste, pregúntate: '¿Cómo puedo ver esto de una manera diferente o más positiva?'. Por ejemplo, si alguien te critica, piensa: 'Quizá esta persona está teniendo un mal día y no es personal'.",
            "tip": "Aplica el reencuadre cada vez que enfrentes una situación que te cause frustración o enojo.",
            "order": 12
        }
    ]
    
    for tech in techniques:
        tech_content = f"""<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Qué es:</strong> {tech['what']}</p>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Cómo hacerlo:</strong> {tech['how']}</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recomendación:</strong> {tech['tip']}</p>
</div>"""
        
        cards.append({
            "title": f"Técnica {tech['num']}: {tech['title']}",
            "content": CARD_STYLES["content"].format(
                title=f"Técnica {tech['num']}: {tech['title']}",
                content=tech_content
            ),
            "card_type": "practical",
            "order_number": tech['order']
        })
    
    # Conclusion
    conclusion_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Estas técnicas te permitirán enfrentar los desafíos emocionales del día a día de manera más consciente y efectiva.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Incorporarlas en tu rutina diaria te ayudará a mantener un equilibrio emocional duradero.</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recuerda:</strong> La práctica constante es clave. No se trata de ser perfecto, sino de ser consciente y compasivo contigo mismo.</p>
</div>"""
    
    cards.append({
        "title": "Conclusión",
        "content": CARD_STYLES["content"].format(
            title="Manteniendo tu Equilibrio Emocional",
            content=conclusion_content
        ),
        "card_type": "conclusion",
        "order_number": 13
    })
    
    return cards


def import_module1_recursos():
    """Main function to import all recursos for module 1"""
    
    # Login
    print("Logging in...")
    token = login_admin()
    if not token:
        print("Failed to login. Please check your credentials.")
        return
    
    print("✓ Logged in successfully")
    
    # Module 1 ID (assuming it's 1)
    module_id = 1
    
    # Get current themes count to determine order_number
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/modules/{module_id}", headers=headers)
    if response.status_code == 200:
        module_data = response.json()
        current_theme_count = len(module_data.get("themes", []))
        print(f"Current theme count: {current_theme_count}")
    else:
        current_theme_count = 0
    
    # Define recursos
    recursos = [
        {
            "title": "¿Qué necesito realmente cuando me siento así?",
            "description": "Guía práctica para identificar las necesidades detrás de tus emociones y tomar acciones concretas.",
            "parser": parse_recurso_1,
            "file": "assets/recurso_module1/Recurso_ ¿Qué necesito realmente cuando me siento así_.txt"
        },
        {
            "title": "Emocionario: Guía de las Emociones",
            "description": "Herramienta completa para identificar y comprender las emociones primarias, secundarias y terciarias.",
            "parser": parse_recurso_2,
            "file": "assets/recurso_module1/Recurso_ Emocionario.txt"
        },
        {
            "title": "Técnicas de Gestión Emocional para el Día a Día",
            "description": "11 técnicas prácticas y poderosas para manejar tus emociones de manera efectiva.",
            "parser": parse_recurso_3,
            "file": "assets/recurso_module1/Recurso_ Técnicas de gestión emocional para el día a día.txt"
        }
    ]
    
    # Create each recurso
    for idx, recurso in enumerate(recursos):
        order_number = current_theme_count + idx + 1
        
        print(f"\n{'='*60}")
        print(f"Creating recurso: {recurso['title']}")
        print(f"{'='*60}")
        
        # Read file content
        if os.path.exists(recurso['file']):
            with open(recurso['file'], 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            print(f"File not found: {recurso['file']}")
            continue
        
        # Create theme
        print("Creating theme...")
        theme = create_theme(
            token,
            module_id,
            recurso['title'],
            recurso['description'],
            order_number
        )
        
        if not theme:
            print(f"Failed to create theme for {recurso['title']}")
            continue
        
        theme_id = theme['id']
        print(f"✓ Theme created with ID: {theme_id}")
        
        # Parse content into cards
        print("Parsing content into cards...")
        cards = recurso['parser'](content)
        print(f"Generated {len(cards)} cards")
        
        # Create each card
        for card_data in cards:
            print(f"  Creating card: {card_data['title']}")
            card = create_card(
                token,
                theme_id,
                card_data['title'],
                card_data['content'],
                card_data['card_type'],
                card_data['order_number']
            )
            
            if card:
                print(f"  ✓ Card created: {card_data['title']}")
            else:
                print(f"  ✗ Failed to create card: {card_data['title']}")
        
        print(f"\n✓ Completed recurso: {recurso['title']}")
    
    print("\n" + "="*60)
    print("✓ All recursos imported successfully!")
    print("="*60)


if __name__ == "__main__":
    import_module1_recursos()

