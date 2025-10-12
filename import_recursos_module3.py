"""
Script to import recursos for Module 3
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


def parse_recurso_comunicacion(content):
    """Parse 'Comunicación' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Bienvenidos (as) al recurso de comunicación, una herramienta práctica para explorar y transformar la forma de comunicarte con los demás.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Este recurso integra dos enfoques fundamentales:</p>

<ul style="margin-left: 20px; line-height: 1.8;">
<li><strong>Comunicación No Violenta (CNV)</strong> de Marshall Rosenberg</li>
<li><strong>Los Jinetes del Apocalipsis</strong> de John Gottman</li>
</ul>"""
    
    cards.append({
        "title": "Comunicación",
        "content": CARD_STYLES["intro"].format(
            title="Comunicación",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # CNV Introduction
    cnv_intro = """<p style="font-size: 1.1em; margin-bottom: 16px;">La Comunicación No Violenta (CNV) es un enfoque de comunicación creado por Marshall Rosenberg que tiene como objetivo mejorar la conexión humana, eliminar malentendidos y reducir la violencia verbal.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">La CNV se basa en cuatro componentes clave:</p>"""
    
    cards.append({
        "title": "Comunicación No Violenta (CNV)",
        "content": CARD_STYLES["content"].format(
            title="Comunicación No Violenta (CNV)",
            content=cnv_intro
        ),
        "card_type": "theory",
        "order_number": 2
    })
    
    # CNV - 4 Components
    cnv_components = """<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">1. Observación sin juicio</h3>
<p style="margin-bottom: 10px;">Se trata de observar una situación sin hacer juicios ni críticas. Es importante enfocarse en lo que realmente ocurre, sin interpretar ni etiquetar.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> En lugar de decir "Siempre llegas tarde, no te importa", podrías decir "Hoy llegaste 15 minutos después de la hora acordada".</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">2. Identificación de sentimientos</h3>
<p style="margin-bottom: 10px;">El segundo paso es identificar y expresar tus emociones. Esto es crucial para entender lo que sientes realmente.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> En lugar de decir "Me haces sentir mal", puedes decir "Me siento frustrado y triste cuando no respetas los horarios que acordamos".</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">3. Reconocimiento de necesidades</h3>
<p style="margin-bottom: 10px;">Detrás de cada emoción hay una necesidad no satisfecha. En la CNV, aprender a identificar nuestras necesidades es clave para una comunicación eficaz.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> "Tengo la necesidad de sentirme respetado y saber que se valoran nuestros acuerdos".</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">4. Petición clara y positiva</h3>
<p style="margin-bottom: 10px;">En lugar de criticar, se pide algo concreto que satisfaga nuestra necesidad.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> En lugar de "No llegues tarde otra vez", podrías decir "Me gustaría que pudiéramos acordar una hora de llegada que ambos respetemos".</p>
</div>"""
    
    cards.append({
        "title": "Los 4 Componentes de la CNV",
        "content": CARD_STYLES["content"].format(
            title="Los 4 Componentes de la CNV",
            content=cnv_components
        ),
        "card_type": "theory",
        "order_number": 3
    })
    
    # CNV - Ejemplo práctico
    cnv_example = """<p style="font-size: 1.1em; margin-bottom: 16px;">Supón que tu pareja llega tarde a una cita. En lugar de recurrir a frases como "Siempre llegas tarde, no te importa", que probablemente generen un conflicto, usa la CNV:</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin: 0;"><strong>Observación:</strong> "Hoy llegaste 20 minutos después de la hora que acordamos."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin: 0;"><strong>Sentimiento:</strong> "Me siento frustrado y ansioso cuando no sé si llegarás a tiempo."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin: 0;"><strong>Necesidad:</strong> "Necesito sentir que nuestros compromisos son importantes para ambos."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin: 0;"><strong>Petición:</strong> "¿Podemos acordar juntos cómo hacer que podamos llegar a tiempo en el futuro?"</p>
</div>"""
    
    cards.append({
        "title": "CNV en la Práctica",
        "content": CARD_STYLES["content"].format(
            title="CNV en la Práctica",
            content=cnv_example
        ),
        "card_type": "practical",
        "order_number": 4
    })
    
    # Jinetes del Apocalipsis - Intro
    jinetes_intro = """<p style="font-size: 1.1em; margin-bottom: 16px;">Los Jinetes del Apocalipsis de John Gottman son cuatro comportamientos destructivos en las relaciones de pareja que, según él, predicen el final de una relación si no se abordan a tiempo.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Identificar estos comportamientos es el primer paso para evitarlos y construir relaciones más saludables.</p>"""
    
    cards.append({
        "title": "Los Jinetes del Apocalipsis de John Gottman",
        "content": CARD_STYLES["content"].format(
            title="Los Jinetes del Apocalipsis de John Gottman",
            content=jinetes_intro
        ),
        "card_type": "theory",
        "order_number": 5
    })
    
    # Los 4 Jinetes
    jinetes_content = """<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">1. Crítica</h3>
<p style="margin-bottom: 10px;">Se trata de atacar la personalidad o el carácter de la otra persona. Esto es diferente de hacer una observación específica sobre un comportamiento.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> En lugar de decir "Eres tan desorganizado", podrías decir "Me siento molesto cuando la casa está desordenada porque me cuesta concentrarme."</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">2. Desprecio</h3>
<p style="margin-bottom: 10px;">Este es el comportamiento más tóxico de todos. Implica tratar a la otra persona con desdén, sarcasmo o burlas.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> "Eres un desastre, ¿cómo no te das cuenta de lo que estás haciendo?" Esto puede hacer mucho daño a la relación, ya que crea un ambiente de humillación.</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">3. Defensividad</h3>
<p style="margin-bottom: 10px;">En lugar de tomar responsabilidad, la persona se pone a la defensiva y empieza a culpar al otro.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> "No es mi culpa, tú también llegaste tarde el viernes pasado". La defensividad impide que se resuelva el problema real.</p>
</div>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">4. Bloqueo o desconexión</h3>
<p style="margin-bottom: 10px;">También conocido como "stonewalling", consiste en cerrarse emocionalmente, no escuchar ni responder a la pareja.</p>
<p style="margin: 0;"><strong>Ejemplo:</strong> Si alguien te está hablando sobre un tema importante y tú simplemente dejas de contestar o te desconectas emocionalmente, estás bloqueando la comunicación.</p>
</div>"""
    
    cards.append({
        "title": "Los 4 Jinetes del Apocalipsis",
        "content": CARD_STYLES["content"].format(
            title="Los 4 Jinetes del Apocalipsis",
            content=jinetes_content
        ),
        "card_type": "theory",
        "order_number": 6
    })
    
    # Cómo evitar los jinetes
    evitar_jinetes = """<p style="font-size: 1.1em; margin-bottom: 16px;">Imagina que en una discusión, tu pareja te señala algo que no le gusta. Si reaccionas con crítica, esto probablemente desatará una serie de reproches y hará más difícil la resolución del conflicto.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">En cambio, si utilizas la CNV, puedes expresar cómo te sientes sin atacar, lo cual reduce la probabilidad de que surjan estos jinetes.</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">Crítica (Evitar)</h3>
<p style="margin: 0;">"Siempre dejas las luces encendidas."</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">Comunicación asertiva (Usar CNV)</h3>
<p style="margin: 0;">"Me siento molesto cuando dejo las luces encendidas porque aumenta nuestra factura de electricidad. ¿Podemos acordar apagar las luces al salir de una habitación?"</p>
</div>"""
    
    cards.append({
        "title": "Cómo Evitar los Jinetes",
        "content": CARD_STYLES["content"].format(
            title="Cómo Evitar los Jinetes",
            content=evitar_jinetes
        ),
        "card_type": "practical",
        "order_number": 7
    })
    
    # Conclusión
    conclusion = """<p style="font-size: 1.1em; margin-bottom: 16px;">La Comunicación No Violenta es una herramienta poderosa que te ayudará a expresar tus necesidades de manera respetuosa y empática.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">La conciencia de los Jinetes del Apocalipsis de Gottman te permitirá identificar comportamientos destructivos que pueden dañar tu relación.</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>Recuerda:</strong> Aprender a comunicarte conscientemente y evitar los jinetes negativos puede mejorar la calidad de tus relaciones y fomentar una conexión más profunda y saludable.</p>
</div>"""
    
    cards.append({
        "title": "Conclusión",
        "content": CARD_STYLES["content"].format(
            title="Transformando tu Comunicación",
            content=conclusion
        ),
        "card_type": "conclusion",
        "order_number": 8
    })
    
    return cards


def import_module3_recursos():
    """Main function to import all recursos for module 3"""
    
    # Login
    print("Logging in...")
    token = login_admin()
    if not token:
        print("Failed to login. Please check your credentials.")
        return
    
    print("✓ Logged in successfully")
    
    # Module 3 ID
    module_id = 3
    
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
            "title": "Comunicación",
            "description": "Herramientas prácticas de Comunicación No Violenta (CNV) y cómo evitar los Jinetes del Apocalipsis en tus relaciones.",
            "parser": parse_recurso_comunicacion,
            "file": "assets/recurso_module3/Recurso_ Comunicacion.txt"
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
    print("✓ All recursos for Module 3 imported successfully!")
    print("="*60)


if __name__ == "__main__":
    import_module3_recursos()

