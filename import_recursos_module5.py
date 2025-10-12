"""
Script to import recursos for Module 5
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


def parse_recurso_smart(content):
    """Parse 'Objetivos SMART' into cards"""
    cards = []
    
    # Intro card
    intro_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Un objetivo SMART es una manera estructurada y clara de definir lo que quieres lograr.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">La palabra SMART viene del inglés y representa cinco características esenciales que debe tener un objetivo bien formulado.</p>

<p style="font-size: 1.1em; margin-bottom: 16px;">Este método te ayudará a transformar ideas vagas en metas concretas y alcanzables.</p>"""
    
    cards.append({
        "title": "Objetivos SMART",
        "content": CARD_STYLES["intro"].format(
            title="¿Cómo crear objetivos SMART?",
            content=intro_content
        ),
        "card_type": "intro",
        "order_number": 1
    })
    
    # S - Específico
    s_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">Un objetivo debe ser claro y concreto, no algo vago</h3>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Pregúntate:</strong> ¿Qué quiero lograr exactamente?</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo NO SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero hacer más ejercicio"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero salir a correr 3 veces por semana durante 30 minutos"</p>
</div>"""
    
    cards.append({
        "title": "S - Específico (Specific)",
        "content": CARD_STYLES["content"].format(
            title="S - Específico (Specific)",
            content=s_content
        ),
        "card_type": "theory",
        "order_number": 2
    })
    
    # M - Medible
    m_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">Debe ser cuantificable o tener un indicador para saber si lo lograste</h3>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Pregúntate:</strong> ¿Cómo sabré que lo he conseguido?</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo NO SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero ahorrar dinero"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero ahorrar 200 € en 2 meses"</p>
</div>"""
    
    cards.append({
        "title": "M - Medible (Measurable)",
        "content": CARD_STYLES["content"].format(
            title="M - Medible (Measurable)",
            content=m_content
        ),
        "card_type": "theory",
        "order_number": 3
    })
    
    # A - Alcanzable
    a_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">Debe ser realista y posible según tus recursos y tu situación</h3>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Pregúntate:</strong> ¿Es un objetivo que puedo cumplir con lo que tengo ahora?</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo NO SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero correr una maratón mañana"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero correr 5 km en 2 meses, entrenando 3 veces por semana"</p>
</div>"""
    
    cards.append({
        "title": "A - Alcanzable (Achievable)",
        "content": CARD_STYLES["content"].format(
            title="A - Alcanzable (Achievable)",
            content=a_content
        ),
        "card_type": "theory",
        "order_number": 4
    })
    
    # R - Relevante
    r_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">Debe tener sentido y conexión con tus metas a largo plazo o valores</h3>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Pregúntate:</strong> ¿Este objetivo me acerca a lo que realmente quiero?</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo NO SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero aprender a tocar guitarra solo porque sí"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero mejorar mi inglés para conseguir un empleo internacional"</p>
</div>"""
    
    cards.append({
        "title": "R - Relevante (Relevant)",
        "content": CARD_STYLES["content"].format(
            title="R - Relevante (Relevant)",
            content=r_content
        ),
        "card_type": "theory",
        "order_number": 5
    })
    
    # T - Tiempo definido
    t_content = """<h3 style="color: #6b745a; margin-top: 0; font-size: 1.3em;">Necesita un plazo límite para no quedar en el aire</h3>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>Pregúntate:</strong> ¿Cuándo quiero lograrlo?</p>

<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo NO SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Algún día quiero escribir un libro"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<p style="margin-bottom: 10px;"><strong>Ejemplo SMART:</strong></p>
<p style="margin: 0; font-style: italic;">"Quiero escribir el primer borrador de mi libro en 6 meses"</p>
</div>"""
    
    cards.append({
        "title": "T - Tiempo definido (Time-bound)",
        "content": CARD_STYLES["content"].format(
            title="T - Tiempo definido (Time-bound)",
            content=t_content
        ),
        "card_type": "theory",
        "order_number": 6
    })
    
    # Resumen
    resumen_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Un objetivo SMART responde a:</p>

<ul style="margin-left: 20px; line-height: 1.8;">
<li><strong>Qué</strong> quiero lograr</li>
<li><strong>Cómo</strong> voy a medirlo</li>
<li><strong>Si</strong> es posible de alcanzar</li>
<li><strong>Por qué</strong> es importante</li>
<li><strong>Cuándo</strong> lo voy a lograr</li>
</ul>"""
    
    cards.append({
        "title": "Resumen",
        "content": CARD_STYLES["content"].format(
            title="Resumen",
            content=resumen_content
        ),
        "card_type": "theory",
        "order_number": 7
    })
    
    # Ejemplo completo
    ejemplo_content = """<div style="background: #f9f9f7; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">NO SMART</h3>
<p style="margin: 0; font-style: italic;">"Quiero estar más saludable"</p>
</div>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 16px 0;">
<h3 style="color: #6b745a; margin-top: 0; font-size: 1.2em;">SMART</h3>
<p style="margin: 0; font-style: italic;">"Quiero perder 5 kg en 3 meses, yendo al gimnasio 4 veces por semana y siguiendo un plan de alimentación saludable, porque deseo tener más energía y sentirme mejor conmigo mismo."</p>
</div>

<p style="font-size: 1.1em; margin-top: 20px;">Este ejemplo cumple con todos los criterios SMART:</p>

<ul style="margin-left: 20px; line-height: 1.8;">
<li><strong>Específico:</strong> Perder 5 kg</li>
<li><strong>Medible:</strong> Puedo medir mi peso</li>
<li><strong>Alcanzable:</strong> Es realista con 4 días de gimnasio + alimentación saludable</li>
<li><strong>Relevante:</strong> Tiene un propósito claro (más energía y bienestar)</li>
<li><strong>Tiempo definido:</strong> 3 meses</li>
</ul>"""
    
    cards.append({
        "title": "Ejemplo Completo",
        "content": CARD_STYLES["content"].format(
            title="Ejemplo Completo",
            content=ejemplo_content
        ),
        "card_type": "practical",
        "order_number": 8
    })
    
    # Conclusión
    conclusion_content = """<p style="font-size: 1.1em; margin-bottom: 16px;">Ahora que conoces la metodología SMART, estás listo para transformar tus deseos en objetivos concretos y alcanzables.</p>

<div style="background: #fdfdf8; padding: 18px; border-left: 4px solid #6b745a; margin: 20px 0;">
<p style="margin: 0;"><strong>¡Ahora es tu turno!</strong> Toma un objetivo que tengas en mente y aplícale el método SMART. Verás cómo se transforma en algo mucho más claro y alcanzable.</p>
</div>"""
    
    cards.append({
        "title": "A la Acción",
        "content": CARD_STYLES["content"].format(
            title="¡Ahora es tu turno!",
            content=conclusion_content
        ),
        "card_type": "conclusion",
        "order_number": 9
    })
    
    return cards


def import_module5_recursos():
    """Main function to import all recursos for module 5"""
    
    # Login
    print("Logging in...")
    token = login_admin()
    if not token:
        print("Failed to login. Please check your credentials.")
        return
    
    print("✓ Logged in successfully")
    
    # Module 5 ID
    module_id = 5
    
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
            "title": "Objetivos SMART",
            "description": "Aprende a crear objetivos específicos, medibles, alcanzables, relevantes y con tiempo definido.",
            "parser": parse_recurso_smart,
            "file": "assets/recurso_module5/Recurso_ Objetivos SMART.txt"
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
    print("✓ All recursos for Module 5 imported successfully!")
    print("="*60)


if __name__ == "__main__":
    import_module5_recursos()

