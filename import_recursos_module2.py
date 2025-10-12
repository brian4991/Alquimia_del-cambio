"""
Script to import recursos for Module 2
"""

import os
import requests
import json

# API Configuration
API_BASE_URL = "http://localhost:8000"
ADMIN_USERNAME = "admin"
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


def parse_recurso_creencias(content):
    """Parse 'Creencias' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Bienvenidos (as) al recurso de creencias, una herramienta práctica para explorar y transformar aquellas ideas limitantes que han influido en tu vida.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Las creencias no son ni buenas ni malas, simplemente son pensamientos que adoptamos con el tiempo, a menudo sin cuestionarlos. Estas creencias moldean la manera en que nos vemos a nosotros mismos, nuestras capacidades y el mundo que nos rodea.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Aquí aprenderás a identificar las creencias que te limitan y cómo reemplazarlas por pensamientos más empoderadores y positivos.</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recomendación:</strong> La lectura del libro "Los 4 acuerdos" de Miguel Ruiz puede ayudarte a profundizar en cómo las creencias que hemos aceptado desde la infancia impactan nuestra vida.</p>
</div>"""
    
    cards.append({
        "title": "Creencias",
        "content": CARD_STYLES["intro"].format(
            title="Creencias",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # 15 Creencias limitantes
    creencias = [
        {
            "num": 1,
            "title": "No soy lo suficientemente bueno",
            "desc": "Creer que no eres capaz o merecedor de éxito, amor o reconocimiento.",
            "positiva": "Soy suficiente tal como soy, y merezco lo mejor en la vida.",
            "order": 2
        },
        {
            "num": 2,
            "title": "Siempre tengo que ser perfecto",
            "desc": "La necesidad de cumplir con estándares imposibles, lo que genera una constante sensación de fracaso.",
            "positiva": "La imperfección es parte de ser humano. Mi valor no depende de la perfección.",
            "order": 3
        },
        {
            "num": 3,
            "title": "No merezco ser feliz",
            "desc": "Pensar que la felicidad no está destinada para ti debido a errores pasados o creencias limitantes.",
            "positiva": "Merezco ser feliz y disfrutar de la vida, independientemente de lo que haya sucedido antes.",
            "order": 4
        },
        {
            "num": 4,
            "title": "Debo complacer a los demás para ser querido",
            "desc": "Creer que solo a través de la aprobación externa podrás sentirte aceptado.",
            "positiva": "Soy valioso tal y como soy, sin necesidad de complacer a los demás.",
            "order": 5
        },
        {
            "num": 5,
            "title": "No soy valioso si no soy productivo",
            "desc": "Asumir que tu valor está ligado solo a tus logros y productividad.",
            "positiva": "Mi valor no depende de mi productividad. Soy valioso por mi ser, no solo por lo que hago.",
            "order": 6
        },
        {
            "num": 6,
            "title": "Es tarde para cambiar",
            "desc": "Creer que ya es demasiado tarde para hacer cambios importantes o crecer como persona.",
            "positiva": "Siempre estoy en el momento adecuado para comenzar a cambiar y crecer.",
            "order": 7
        },
        {
            "num": 7,
            "title": "Mis errores definen quién soy",
            "desc": "Dejar que los fracasos pasados definan tu identidad y tu valor personal.",
            "positiva": "Mis errores son oportunidades de aprendizaje. No definen quién soy, solo me ayudan a crecer.",
            "order": 8
        },
        {
            "num": 8,
            "title": "Si no soy perfecto, no soy digno de amor",
            "desc": "Pensar que el amor y la aceptación dependen de ser impecable o cumplir expectativas externas.",
            "positiva": "Soy digno de amor y aceptación tal como soy, con todas mis imperfecciones.",
            "order": 9
        },
        {
            "num": 9,
            "title": "Siempre debo tener el control",
            "desc": "La creencia de que no puedes permitirte la vulnerabilidad ni pedir ayuda, lo que te priva de aceptar tu humanidad.",
            "positiva": "Está bien no tener siempre el control. Pedir ayuda me fortalece y me permite crecer.",
            "order": 10
        },
        {
            "num": 10,
            "title": "No soy capaz de enfrentar los desafíos",
            "desc": "Sentir que no tienes las herramientas o la fuerza para superar las dificultades.",
            "positiva": "Tengo la capacidad de enfrentar los desafíos. Cada reto me da la oportunidad de desarrollar mi fortaleza.",
            "order": 11
        },
        {
            "num": 11,
            "title": "No soy digno de éxito",
            "desc": "Creer que el éxito es algo reservado solo para otros, pero no para ti.",
            "positiva": "Soy digno del éxito. Mi esfuerzo y dedicación me abren las puertas del éxito.",
            "order": 12
        },
        {
            "num": 12,
            "title": "Tengo que ser fuerte todo el tiempo",
            "desc": "La creencia de que debes estar siempre 'bien', ignorando tus necesidades emocionales.",
            "positiva": "Está bien mostrar vulnerabilidad. Ser auténtico y honesto sobre mis emociones me hace más fuerte.",
            "order": 13
        },
        {
            "num": 13,
            "title": "Las opiniones de los demás son más importantes que las mías",
            "desc": "Valorar más las expectativas de otros que tu propio bienestar y deseos.",
            "positiva": "Mis opiniones y necesidades son tan importantes como las de los demás. Mi bienestar es fundamental.",
            "order": 14
        },
        {
            "num": 14,
            "title": "Soy una persona débil si pido ayuda",
            "desc": "Pensar que aceptar ayuda o apoyo es un signo de debilidad.",
            "positiva": "Pedir ayuda es una muestra de sabiduría. Me fortalece aceptar el apoyo de los demás.",
            "order": 15
        },
        {
            "num": 15,
            "title": "Si fallo, me rechazo",
            "desc": "Relacionar el fracaso con la falta de valor, pensando que no mereces amor o aceptación si cometes errores.",
            "positiva": "El fracaso es solo una parte del proceso. Aprendo de él y me sigo valorando a pesar de los desafíos.",
            "order": 16
        }
    ]
    
    for creencia in creencias:
        creencia_content = f"""<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Creencia limitante:</strong></p>
<p style="font-size: 1.05em; margin-bottom: 16px;">{creencia['desc']}</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0; color: #2d2d2d;"><strong>Versión positiva:</strong> {creencia['positiva']}</p>
</div>"""
        
        cards.append({
            "title": f"{creencia['num']}. {creencia['title']}",
            "content": CARD_STYLES["content"].format(
                title=f"{creencia['num']}. {creencia['title']}",
                content=creencia_content
            ),
            "card_type": "practical",
            "order_number": creencia['order']
        })
    
    return cards


def parse_recurso_trec(content):
    """Parse 'TREC' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">¿Qué es el TREC?</h3>
<p style="font-size: 1.1em; margin-bottom: 16px;">Es una herramienta psicológica que nos ayuda a cambiar pensamientos automáticos e irracionales que generan malestar, por otros más realistas, saludables y funcionales.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Su creador, Albert Ellis, creía que <strong>no sufrimos por lo que nos pasa, sino por cómo interpretamos lo que nos pasa.</strong></p>"""
    
    cards.append({
        "title": "Transforma tus pensamientos con el modelo TREC",
        "content": CARD_STYLES["intro"].format(
            title="Transforma tus pensamientos con el modelo TREC",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # Modelo ABC
    abc_content = """<p style="font-size: 1.1em; margin-bottom: 20px;">El modelo ABC nos ayuda a entender cómo funciona nuestra mente:</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">A - Acontecimiento activador</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> "Mi pareja no me respondió el mensaje en todo el día."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">B - Creencia (belief)</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> "Seguramente ya no le importo. Siempre me dejan."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">C - Consecuencia emocional o conducta</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> Tristeza, ansiedad, necesidad de control, o evitar el vínculo</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>La clave está en la letra B (las creencias).</strong> Eso es lo que podemos cambiar para sanar y actuar diferente.</p>
</div>"""
    
    cards.append({
        "title": "El modelo ABC del TREC",
        "content": CARD_STYLES["content"].format(
            title="El modelo ABC del TREC",
            content=abc_content
        ),
        "card_type": "theory",
        "order_number": 2
    })
    
    # Transformación DEF
    def_content = """<p style="font-size: 1.1em; margin-bottom: 20px;">Agregamos tres pasos más al modelo para transformar nuestros pensamientos:</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">D - Disputar esa creencia</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> "¿Es 100% cierto? ¿Podría estar ocupado? ¿Siempre pasa esto?"</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">E - Nueva creencia racional y realista</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> "Tal vez solo tuvo un día ocupado. No significa que no me quiera."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">F - Nuevo sentimiento o resultado final</h3>
<p style="margin: 0;"><strong>Ejemplo:</strong> Calma, seguridad, menos necesidad de controlar, más claridad.</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0; font-style: italic;"><strong>Frase clave del TREC:</strong> "No son los hechos los que nos hacen sufrir, sino lo que nos decimos sobre ellos."</p>
</div>"""
    
    cards.append({
        "title": "¿Cómo transformarlo?",
        "content": CARD_STYLES["content"].format(
            title="¿Cómo transformarlo?",
            content=def_content
        ),
        "card_type": "theory",
        "order_number": 3
    })
    
    # Ejercicio práctico
    ejercicio_content = """<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>1. Piensa en una situación reciente que te causó malestar.</strong></p>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>2. Escribe:</strong></p>
<ul style="margin-left: 20px; line-height: 1.8;">
<li><strong>A:</strong> ¿Qué pasó?</li>
<li><strong>B:</strong> ¿Qué te dijiste?</li>
<li><strong>C:</strong> ¿Qué sentiste o hiciste?</li>
</ul>

<p style="font-size: 1.1em; margin-top: 20px; margin-bottom: 16px;"><strong>3. Ahora contesta:</strong></p>
<ul style="margin-left: 20px; line-height: 1.8;">
<li><strong>D:</strong> ¿Qué evidencia hay a favor y en contra de esa creencia?</li>
<li><strong>E:</strong> ¿Qué podrías pensar en su lugar que sea más realista y amable?</li>
<li><strong>F:</strong> ¿Cómo te sientes ahora con esta nueva visión?</li>
</ul>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recuerda:</strong> No se trata de "positivismo falso", sino de entrenar tu mente a ver con más claridad, para sentirte libre y actuar desde tu versión 2.0.</p>
</div>"""
    
    cards.append({
        "title": "Entrénate para dominar la herramienta",
        "content": CARD_STYLES["content"].format(
            title="Entrénate para dominar la herramienta (3 min)",
            content=ejercicio_content
        ),
        "card_type": "practical",
        "order_number": 4
    })
    
    return cards


def import_module2_recursos():
    """Main function to import all recursos for module 2"""
    
    # Login
    print("Logging in...")
    token = login_admin()
    if not token:
        print("Failed to login. Please check your credentials.")
        return
    
    print("✓ Logged in successfully")
    
    # Module 2 ID
    module_id = 2
    
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
            "title": "Creencias",
            "description": "Herramienta práctica para explorar y transformar aquellas ideas limitantes que han influido en tu vida.",
            "parser": parse_recurso_creencias,
            "file": "assets/recursos_modulke2/Recurso_ Creencias.txt"
        },
        {
            "title": "TREC - Transforma tus pensamientos",
            "description": "Modelo TREC (Terapia Racional Emotiva Conductual) para cambiar pensamientos automáticos e irracionales.",
            "parser": parse_recurso_trec,
            "file": "assets/recursos_modulke2/Recurso_ TREC .txt"
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
    print("✓ All recursos for Module 2 imported successfully!")
    print("="*60)


if __name__ == "__main__":
    import_module2_recursos()

