"""
Script pour créer le Thème 2 du Module 4 COMPLET
Thème 2: Despertar auténtico (3 subtemas)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Theme, ThemeCard

# Styles
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def create_theme2_cards(db: Session, theme_id: int):
    """Cards du Thème 2: Despertar auténtico"""
    print("\n🎴 Création des cards du Thème 2...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 2",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Despertar Auténtico</h1>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin: 0; font-size: 1.1em; font-style: italic;">"Ser tú mismo en un mundo que constantemente intenta hacerte otra persona es el mayor logro." – Ralph Waldo Emerson</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Autenticidad</h3>
<p style="margin-bottom: 0;">La autenticidad no es algo que se encuentra, es algo que se cultiva.</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">Despertar a nuestro verdadero ser significa cuestionar esas capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura.</p>

<p style="margin-bottom: 16px;">Es un proceso de exploración y desaprendizaje, que nos lleva a reconocer quiénes somos más allá de las etiquetas, expectativas y miedos.</p>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Tu verdadero ser
    cards.extend([
        {
            "title": "Subtema 1: Tu Verdadero Ser",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Tu Verdadero Ser</h1>

<h2 style="color: {C_ACCENT}; font-size: 1.6em; margin-bottom: 16px;">El error más común: vivir desde lo aprendido y no desde lo auténtico</h2>

<p style="margin-bottom: 16px;">Muchas personas pasan gran parte de su vida siendo quienes "deberían ser" en lugar de quienes realmente son.</p>

<p style="margin-bottom: 16px;">Esto sucede porque desde la infancia absorbemos mensajes sobre lo que es aceptable o deseable. Es un proceso normal, los seres humanos, necesitamos de otros humanos para sobrevivir, nos adaptamos para encajar, pero en el proceso, podemos perder de vista nuestra verdadera esencia.</p>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">La pregunta clave es:</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">¿Estoy viviendo desde mi autenticidad o desde lo que me dijeron que debía ser?</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Tu Verdadero Ser - Yo Aprendido vs Yo Auténtico",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">La diferencia entre el "yo aprendido" y el "yo auténtico"</h2>

<p style="margin-bottom: 16px;">Desde la infancia, comenzamos a moldearnos según lo que creemos que es aceptable o esperado. Adoptamos ciertas actitudes para encajar, para evitar el rechazo o para recibir amor. A esto lo llamamos el <strong>"yo aprendido"</strong>, la versión de nosotros mismos que hemos construido para adaptarnos.</p>

<p style="margin-bottom: 16px;">En contraste, el <strong>"yo auténtico"</strong> es aquella parte de nosotros que existe sin esfuerzo, sin necesidad de validación externa. Es nuestra verdadera esencia, libre de condicionamientos y llena de posibilidades, con esta versión es la que necesitas conectarte.</p>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">Algunas señales de que estamos desconectados de nuestro yo auténtico incluyen:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Sentir que constantemente estamos actuando para complacer a otros.</p>
<p style="margin-bottom: 12px;">• Experimentar insatisfacción o vacío a pesar de lograr objetivos externos.</p>
<p style="margin-bottom: 12px;">• Tener miedo de mostrar nuestras emociones reales.</p>
<p style="margin-bottom: 0;">• Percibir una falta de dirección o un sentido de "estar perdidos".</p>
</div>

<h3 style="color: #5cb85c; margin-top: 24px; margin-bottom: 16px;">Por otro lado, cuando nos alineamos con nuestro verdadero ser, experimentamos:</h3>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Mayor claridad sobre lo que queremos y valoramos.</p>
<p style="margin-bottom: 12px;">• Relaciones más genuinas y significativas.</p>
<p style="margin-bottom: 12px;">• Una sensación de paz interna al actuar desde nuestra verdad.</p>
<p style="margin-bottom: 0;">• Un flujo natural en nuestras decisiones y acciones.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Tu Verdadero Ser - Tabla Comparativa",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cómo empezar a reconectar contigo mismo/a</h2>

<p style="margin-bottom: 16px;">Para entender quién eres realmente, primero necesitas diferenciar entre lo que has aprendido de los demás y lo que proviene de ti mismo/a. Observemos estas diferencias:</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
<th style="padding: 12px; text-align: left; border-bottom: 2px solid {C_ACCENT}; color: {C_TITLE}; font-size: 1.1em;">Yo aprendido</th>
<th style="padding: 12px; text-align: left; border-bottom: 2px solid {C_ACCENT}; color: {C_TITLE}; font-size: 1.1em;">Yo auténtico</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Me adapto para agradar a los demás</td>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Expreso lo que realmente siento y pienso</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Tomo decisiones basadas en lo que se espera de mí</td>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Tomo decisiones alineadas con lo que deseo</td>
</tr>
<tr>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Busco aprobación constante</td>
<td style="padding: 12px; border-bottom: 1px solid #ddd;">Confío en mi propio criterio</td>
</tr>
<tr>
<td style="padding: 12px;">Evito mostrar mis emociones o vulnerabilidad</td>
<td style="padding: 12px;">Me permito sentir y expresarme libremente</td>
</tr>
</tbody>
</table>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0; text-align: center;">
<p style="margin: 0; font-size: 1.05em;">La clave para despertar a tu verdadero ser es comenzar a identificar qué partes de ti se originan en el deseo de encajar y cuáles provienen de tu autenticidad. ☺️</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        }
    ])
    order += 3
    
    # SUBTEMA 2: Cultivando la autoconciencia
    cards.extend([
        {
            "title": "Subtema 2: Cultivando la Autoconciencia",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Cultivando la Autoconciencia</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Vivir de manera auténtica requiere una profunda comprensión de quiénes somos más allá de nuestras experiencias y roles.</p>

<p style="margin-bottom: 16px;">Sin embargo, en un mundo que constantemente nos dice cómo deberíamos ser, muchas veces nos alejamos de nuestra esencia sin darnos cuenta.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Autoconciencia</h3>
<p style="margin-bottom: 0;">Es el puente que nos permite regresar a nuestro ser genuino y vivir en coherencia con lo que realmente sentimos y valoramos.</p>
</div>

<h2 style="color: {C_ACCENT}; font-size: 1.6em; margin-top: 28px; margin-bottom: 16px;">El Problema: Desconexión con el verdadero ser</h2>

<p style="margin-bottom: 16px;">Cuando olvidamos quienes somos o peor aún no tenemos claridad de esto, se nos dificulta más conectarnos con nuestra esencia y por ende vivimos desconectados de nosotros mismos y de nuestros más profundos deseos (metas o sueños).</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Cultivando la Autoconciencia - Señales",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Señales de desconexión con el verdadero ser</h2>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin: 20px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">✅ Sensación de vacío o insatisfacción, aunque todo parezca estar "bien".</p>
<p style="margin-bottom: 12px;">✅ Miedo a decepcionar a los demás al expresar nuestras verdaderas opiniones y decisiones</p>
<p style="margin-bottom: 12px;">✅ Decisiones basadas en lo que se espera de nosotros y no en lo que realmente queremos</p>
<p style="margin-bottom: 0;">✅ Búsqueda constante de validación externa para sentirnos valiosos</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">Este alejamiento de nuestra esencia genera confusión, ansiedad y la sensación de estar viviendo una vida que no nos pertenece del todo.</p>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Cultivando la Autoconciencia - Esencia Humana",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El reconocimiento de la esencia humana</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">Para despertar la autoconciencia, es fundamental recordar que somos más que nuestros pensamientos, emociones y circunstancias. Somos seres espirituales teniendo una experiencia humana.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Este reconocimiento nos permite:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• <strong>Liberarnos del apego a la identidad social:</strong> Entender que nuestro valor no depende de cómo nos perciben los demás.</p>
<p style="margin-bottom: 12px;">• <strong>Ver más allá de la mente reactiva:</strong> Identificar cuánto de lo que pensamos y sentimos viene del condicionamiento y no de nuestra verdadera naturaleza.</p>
<p style="margin-bottom: 0;">• <strong>Reconectar con lo que siempre hemos sido:</strong> Antes de que las expectativas y exigencias del mundo nos moldearan, había una esencia en nosotros libre y espontánea.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-size: 1.05em;">Cuando empezamos a vivir desde la conciencia de nuestra esencia, nuestras decisiones y acciones se vuelven más alineadas con nuestra verdad interna.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Cultivando la Autoconciencia - Camino de Regreso",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El camino de regreso: despertar la autoconciencia</h2>

<p style="margin-bottom: 16px;">La buena noticia es que la autoconciencia es una habilidad que se puede cultivar. No se trata de convertirse en alguien nuevo, sino de recordar quién eres más allá de las etiquetas y creencias aprendidas.</p>

<p style="margin-bottom: 16px;">A través de la observación y la reflexión, podemos recuperar nuestra conexión con la esencia y vivir desde un lugar de autenticidad.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;"><strong>🔹 Observar sin juzgar:</strong> La autoconciencia comienza con la capacidad de notar nuestros pensamientos, emociones y comportamientos sin etiquetarlos como "buenos" o "malos". Pregúntate: ¿De dónde vienen estas ideas sobre mí mismo/a? ¿Son realmente mías o las he aprendido de otros?</p>
<p style="margin-bottom: 12px;"><strong>🔹 Reconocer patrones limitantes:</strong> Identificar en qué momentos nos alejamos de nuestra autenticidad y por qué. ¿Cuáles son las situaciones en las que sientes que no puedes ser tú mismo/a? ¿Qué temes que pase si lo eres?</p>
<p style="margin-bottom: 12px;"><strong>🔹 Diferenciar lo que deseas de lo que aprendiste a desear:</strong> Muchas veces perseguimos metas que no nos llenan porque nos enseñaron que "eso es lo correcto". Reflexiona sobre lo que realmente quieres en lo más profundo de tu ser.</p>
<p style="margin-bottom: 0;"><strong>🔹 Aceptar todas las partes de ti:</strong> La autoconciencia también implica abrazar nuestras luces y sombras. No se trata de ser perfectos, sino de aceptar todo lo que somos con compasión y sin rechazo</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # SUBTEMA 3: Abrazando la vulnerabilidad
    cards.extend([
        {
            "title": "Subtema 3: Abrazando la Vulnerabilidad",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Abrazando la Vulnerabilidad</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">¿Cuántas veces has sentido que mostrarte vulnerable es sinónimo de debilidad? Que si dejas que los demás vean tus miedos, tus dudas o tu dolor, podrían usarlos en tu contra.</p>

<p style="margin-bottom: 16px;">La sociedad nos ha enseñado que ser fuerte es "aguantarse todo", no llorar y siempre demostrar que tenemos el control.</p>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">Pero... ¿y si en realidad la vulnerabilidad fuera una fortaleza?</h3>
</div>

<p style="margin-bottom: 16px;">La psicóloga Brené Brown, experta en el tema, dice que la vulnerabilidad es el pegamento que une a las personas. Es la capacidad de mostrarnos tal y como somos, sin máscaras, sin aparentar que todo está bien cuando no lo está. Es lo que nos permite conectar de verdad con los demás.</p>

<p style="margin-bottom: 16px;">Piensa en esto: ¿qué hace que te sientas cercano a alguien? Probablemente no sea que todo en su vida es perfecto, sino que ha compartido contigo sus luchas, sus emociones reales. Nos conectamos más con la autenticidad que con la perfección.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Verdadero Coraje</h3>
<p style="margin-bottom: 0;">La vulnerabilidad no es debilidad, es coraje. Significa atreverte a ser visto, a decir "esto me duele", "esto me da miedo", "esto me emociona". Y hacerlo sin la certeza de cómo responderán los demás.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Abrazando la Vulnerabilidad - Lo que Evitamos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué pasa cuando evitamos ser vulnerables?</h2>

<p style="margin-bottom: 16px;">Cuando evitamos la vulnerabilidad, caemos en mecanismos de defensa que nos alejan de los demás y de nosotros mismos.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Estos son algunos ejemplos:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;"><strong>❌ La armadura emocional:</strong> Nos ponemos una coraza y actuamos como si nada nos afectara. "Estoy bien, todo bien", aunque por dentro sintamos lo contrario.</p>
<p style="margin-bottom: 12px;"><strong>❌ El perfeccionismo:</strong> Creemos que si somos lo suficientemente "buenos", no nos rechazarán. Nos exigimos más de la cuenta para evitar sentirnos inadecuados.</p>
<p style="margin-bottom: 0;"><strong>❌ El distanciamiento:</strong> En lugar de arriesgarnos a ser heridos, evitamos la cercanía con los demás. Nos volvemos fríos o independientes en exceso.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">El problema es que, aunque estos mecanismos nos protejan del dolor, también nos impiden sentir amor, conexión y autenticidad.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Abrazando la Vulnerabilidad - Cómo Abrazar",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo abrazar la vulnerabilidad?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Cambia tu perspectiva</h4>
<p style="margin-bottom: 0;">La vulnerabilidad no es un defecto, es una habilidad que nos hace más humanos. Pregúntate: "¿Qué pasaría si en lugar de esconder mi vulnerabilidad, la acepto y la comparto con quienes confío?"</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Practica expresar lo que sientes</h4>
<p style="margin-bottom: 8px;">Si algo te duele o te preocupa, en lugar de callarlo, intenta decirlo con honestidad.</p>
<p style="margin-bottom: 0;"><strong>Ejemplo:</strong> En vez de decir "Nada, no pasa nada", prueba con "Me siento triste porque esperaba otra respuesta y no sé cómo manejarlo".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Rodéate de personas seguras</h4>
<p style="margin-bottom: 0;">No todos merecen ver tu vulnerabilidad. Comparte tus emociones con personas que te escuchen sin juzgar, que te hagan sentir en un espacio seguro.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Atrévete a pedir ayuda</h4>
<p style="margin-bottom: 0;">Aceptar que necesitas apoyo no te hace débil, te hace humano. Si estás pasando por un momento difícil, hablar con alguien (amigo, terapeuta, mentor) puede ser un gran paso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Acepta tus imperfecciones</h4>
<p style="margin-bottom: 0;">Nadie es perfecto, ni tú ni nadie. En lugar de castigarte por lo que no puedes controlar, date permiso de ser quien eres, con tus luces y sombras.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 28px 0;">
<p style="margin: 0; font-size: 1.05em;">La vulnerabilidad es el camino hacia la conexión, el amor y la autenticidad. No necesitas ser perfecto para ser amado, solo necesitas ser tú. Cuando te atreves a mostrarte tal como eres, abres la puerta a relaciones más reales y significativas.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Abrazando la Vulnerabilidad",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Conecta con tu Versión más Vulnerable</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a conectar con tu versión más vulnerable.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Despertar Auténtico</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.3: Ser</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    
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

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 2 - MODULE 4")
        print("=" * 70)
        
        MODULE_ID = 4
        
        # Créer le thème 2
        theme2 = Theme(
            title="Despertar auténtico",
            content="La autenticidad no es algo que se encuentra, es algo que se cultiva. Despertar a nuestro verdadero ser significa cuestionar esas capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura.",
            order_number=2,
            module_id=MODULE_ID
        )
        db.add(theme2)
        db.flush()
        print(f"✅ Thème 2 créé (ID: {theme2.id})")
        
        # Créer les cards du thème 2
        num_cards = create_theme2_cards(db, theme2.id)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 2 CRÉÉ!")
        print("=" * 70)
        print(f"📚 Thème 2 ID: {theme2.id} ({num_cards} cards)")
        print(f"\n🎯 Prochain: Créer le Thème 3")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

