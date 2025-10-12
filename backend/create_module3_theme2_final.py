"""
Script pour ajouter les 2 DERNIERS subtemas du Thème 2 Module 3 - COMPLET
Subtemas 4-5: Mi persona equilibrio + Fundamentos de bienestar
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import ThemeCard

# Styles
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def add_final_subtemas(db: Session, theme_id: int):
    """Ajouter les 2 derniers subtemas (4 et 5)"""
    print("\n🎴 Création des subtemas 4-5 (FINAL du Thème 2)...")
    
    cards = []
    order = 19  # Commence après les 18 cards existantes
    
    # SUBTEMA 4: Mi persona equilibrio (cards 19-26)
    cards.extend([
        {
            "title": "Subtema 4: Mi Persona Equilibrio - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 4: Mi Persona Equilibrio</h1>

<p style="margin-bottom: 16px;">Hasta este punto, ya has trabajado en identificar patrones en tus relaciones, reconocer los duelos que no te pertenecen y definir tus necesidades emocionales.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Es Momento de Elegir Conscientemente</h3>
<p style="margin-bottom: 0;">Ahora, es momento de aplicar todo ese conocimiento para elegir conscientemente a una pareja que te guste, pero que también te haga bien.</p>
</div>

<p style="margin-bottom: 16px;">Muchas veces, al intentar alejarnos de patrones dañinos, caemos en la idea de que debemos renunciar a lo que nos atrae, como si sólo hubiera dos opciones:</p>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<ol style="padding-left: 20px;">
<li style="margin-bottom: 12px;"><strong>Elegir lo que nos gusta, aunque nos haga daño.</strong></li>
<li style="margin-bottom: 0;"><strong>Elegir lo saludable, aunque no nos emocione.</strong></li>
</ol>
</div>

<p style="margin-bottom: 16px; font-size: 1.1em; color: {C_ACCENT}; font-weight: 600;">Pero esto es un falso dilema.</p>

<p style="margin-bottom: 16px;">No se trata de renunciar a lo que te gusta, sino de aprender a elegirlo en una versión equilibrada.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Mi Persona Equilibrio - Atraído y Alineado",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. Atraído sí, pero también alineado</h2>

<p style="margin-bottom: 16px;">Es normal tener preferencias y sentirse atraído por ciertos rasgos en las personas. El problema surge cuando esos rasgos vienen acompañados de conductas que te han lastimado en el pasado.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Por ejemplo:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Si te gustan las personas extrovertidas y sociables, pero en el pasado sufriste por parejas que priorizaban la fiesta y la validación externa, puedes pensar que toda persona extrovertida es inestable o poco comprometida.</p>
<p style="margin-bottom: 0;">• Si te atraen las personas ambiciosas, pero antes estuviste con alguien que te hacía sentir en segundo plano por enfocarse solo en su éxito, podrías creer que cualquier persona con ambiciones es emocionalmente fría.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h4 style="margin-top: 0; color: white;">La Clave</h4>
<p style="margin-bottom: 0;">Sin embargo, el problema no es la característica en sí, sino cómo se manifiesta en la persona que eliges.</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo práctico:</h3>

<p style="margin-bottom: 12px;">En lugar de decir <em>"No puedo estar con alguien extrovertido porque me hará daño"</em>, reformula la idea:</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• ¿Cómo puedo encontrar a alguien extrovertido, pero que también valore el compromiso y la estabilidad?</p>
<p style="margin-bottom: 0;">• ¿Cómo se ve una persona que equilibra su vida social con su vida afectiva?</p>
</div>

<p style="margin-top: 20px; margin-bottom: 16px; font-weight: 600; color: {C_ACCENT};">Recomendación:</p>
<p style="margin-bottom: 16px;">No generalices tu experiencia pasada. Busca ejemplos de personas que encarnan esas características que te gustan de una manera más saludable.</p>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Mi Persona Equilibrio - Cómo Definir",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. ¿Cómo definir a mi persona equilibrio?</h2>

<p style="margin-bottom: 16px;">Para elegir bien, necesitas tener claridad sobre dos cosas:</p>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<ol style="padding-left: 20px;">
<li style="margin-bottom: 12px;"><strong>Las características que te atraen y te gustan.</strong></li>
<li style="margin-bottom: 0;"><strong>Las características que necesitas para tener una relación sana.</strong></li>
</ol>
</div>

<p style="margin-bottom: 16px; font-size: 1.1em;">Ambas pueden coexistir, pero es importante que las definas con precisión.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejercicio práctico:</h3>

<p style="margin-bottom: 16px;">Haz dos listas:</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• <strong>Lo que me gusta en una pareja</strong> (Ejemplo: carismático, independiente, con sentido del humor).</p>
<p style="margin-bottom: 0;">• <strong>Lo que necesito para una relación sana</strong> (Ejemplo: comprometido, emocionalmente disponible, respetuoso).</p>
</div>

<p style="margin-bottom: 16px;">Luego, encuentra el punto de equilibrio entre ambas. Pregúntate:</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• ¿Cómo se ve alguien que tiene lo que me gusta, pero también lo que necesito?</p>
<p style="margin-bottom: 0;">• ¿Cómo puedo identificar si esta persona encarna ambas cosas?</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<p style="margin-bottom: 16px;">Si te atraen las personas con energía social, pero necesitas estabilidad, podrías elegir a alguien que sea sociable, pero que tenga límites claros y priorice la relación.</p>

<p style="margin-top: 20px; font-style: italic; color: #5a5a5a;">*No necesitas tener todo claro ahora; haremos un ejercicio de este tipo donde podrás profundizar y crear tu persona equilibrio</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Mi Persona Equilibrio - Señales",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Señales de alerta y señales de equilibrio</h2>

<p style="margin-bottom: 16px;">Para asegurarte de que estás eligiendo desde el equilibrio y no desde el patrón aprendido, es importante reconocer las señales de alerta y las señales de alineación.</p>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🚩 Señales de alerta (cuando la atracción te aleja del bienestar):</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• La persona tiene lo que te atrae, pero ignora tus necesidades emocionales</p>
<p style="margin-bottom: 12px;">• Te sientes constantemente en incertidumbre o en una montaña rusa emocional</p>
<p style="margin-bottom: 0;">• Tienes que justificar o minimizar conductas que en el pasado ya te hicieron daño</p>
</div>

<h3 style="color: #5cb85c; margin-top: 24px; margin-bottom: 16px;">✅ Señales de equilibrio (cuando la atracción y la salud emocional se alinean):</h3>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• La persona tiene lo que te gusta, pero sin que eso comprometa la estabilidad de la relación</p>
<p style="margin-bottom: 12px;">• Hay emoción, pero también tranquilidad y confianza</p>
<p style="margin-bottom: 0;">• No tienes que forzarlo para que funcione, fluye de manera natural y respetuosa</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<p style="margin-bottom: 16px;">Si en el pasado te atrajeron personas que eran muy apasionadas pero poco comprometidas, ahora puedes buscar a alguien que mantenga la pasión y el entusiasmo, pero que también tenga estabilidad emocional y capacidad de construir un futuro contigo.</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "Mi Persona Equilibrio - Elección Consciente",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">4. Tu elección consciente: no más sacrificios, solo ajustes inteligentes</h2>

<p style="margin-bottom: 16px; font-size: 1.1em;">Elegir bien no significa conformarse con lo "seguro" pero aburrido, ni quedarse atrapado en lo emocionante pero dañino.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Verdadera Elección</h3>
<p style="margin-bottom: 0;">Significa tener la capacidad de ajustar tu elección para que incluya lo mejor de ambos mundos. 😉</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<p style="margin-bottom: 16px;">Si en el pasado elegiste parejas inestables porque te atraía su energía y espontaneidad, hoy puedes buscar a alguien que tenga esa chispa, pero que también tenga valores sólidos y coherencia en sus actos.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Reflexión:</h3>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-size: 1.1em; line-height: 1.9;">Amar no es un acto de sacrificio ni de renuncia. Es un acto de sabiduría. Cuando aprendes a elegir desde el equilibrio, descubres que no tienes que dejar de lado lo que te gusta; solo tienes que asegurarte de que también te haga bien.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Mi Persona Equilibrio",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Encuentra Claridad sobre tu Persona Equilibrio</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a encontrar claridad sobre tu persona equilibrio.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Fundamentos</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.4: Mi persona equilibrio</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        }
    ])
    
    order += 6
    
    # SUBTEMA 5: Fundamentos de bienestar (cards 25-33)
    cards.extend([
        {
            "title": "Subtema 5: Fundamentos de Bienestar - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 5: Fundamentos de Bienestar</h1>

<p style="margin-bottom: 16px;">Después de haber identificado patrones, soltado duelos del pasado, aprendido a negociar necesidades y elegido a una persona equilibrio, es momento de hablar sobre los valores esenciales que sostienen una relación saludable y duradera.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo Que Realmente Importa</h3>
<p style="margin-bottom: 0;">Muchas veces nos enfocamos en la atracción, la química o la compatibilidad superficial, pero lo que realmente define la calidad y estabilidad de una relación son los valores compartidos y el compromiso mutuo con el bienestar de la pareja.</p>
</div>

<p style="margin-bottom: 16px;">En este módulo, aprenderás cuáles son los pilares fundamentales para una relación sana y cómo identificar si están presentes en tus vínculos.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Fundamentos - Compromiso",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. Compromiso: La decisión diaria de construir juntos</h2>

<p style="margin-bottom: 16px;">El compromiso no es solo una promesa verbal ni un contrato invisible, sino una elección diaria de estar presente en la relación.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 0;">Imagina que el amor es como una planta. Si solo riegas la planta los primeros días porque te emociona verla crecer, pero luego te olvidas de cuidarla, terminará marchitándose. El compromiso es ese cuidado constante, incluso cuando la emoción inicial se estabiliza.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">¿Cómo se ve el compromiso en una relación sana?</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• La persona está disponible emocionalmente y no genera incertidumbre.</p>
<p style="margin-bottom: 12px;">• Sus palabras y acciones son coherentes.</p>
<p style="margin-bottom: 0;">• Ambos hacen esfuerzos para mantener la conexión y resolver conflictos de manera madura.</p>
</div>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🚩 Señales de alerta de falta de compromiso:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Evita definir la relación o se mantiene en una zona ambigua.</p>
<p style="margin-bottom: 12px;">• Sus acciones muestran falta de interés real en construir algo estable.</p>
<p style="margin-bottom: 0;">• Solo está presente cuando le conviene o cuando todo está bien.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Reflexión:</p>
<p style="margin: 8px 0 0 0;">No se trata solo de cuánto amor sientes, sino de qué estás dispuesto a hacer para cuidar ese amor.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Fundamentos - Respeto",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. Respeto: La base innegociable de cualquier relación</h2>

<p style="margin-bottom: 16px; font-size: 1.1em;">Sin respeto, no hay relación sana. Amar a alguien no significa perderse en él ni tolerar faltas que dañen la dignidad propia.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 0;">Piensa en una relación como una danza en pareja. Para que fluya, ambos deben moverse con armonía, sin pisarse ni empujar al otro fuera del ritmo. El respeto es esa armonía: permite que ambos sean libres sin invadir el espacio del otro.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">¿Cómo se ve el respeto en una relación sana?</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Se comunican sin humillar ni invalidar los sentimientos del otro.</p>
<p style="margin-bottom: 12px;">• Se sienten seguros expresando sus pensamientos sin miedo a ser juzgados.</p>
<p style="margin-bottom: 0;">• No hay manipulación ni intentos de controlar al otro.</p>
</div>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🚩 Señales de alerta de falta de respeto:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Burlas o comentarios que minimizan lo que sientes.</p>
<p style="margin-bottom: 12px;">• Falta de empatía cuando expresas tus emociones.</p>
<p style="margin-bottom: 0;">• Gritos, insultos o actitudes despectivas.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Reflexión:</p>
<p style="margin: 8px 0 0 0;">Puedes amar a alguien profundamente, pero si no hay respeto, esa relación no podrá ser sana ni sostenible.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Fundamentos - Admiración",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Admiración: Ver y valorar lo mejor del otro</h2>

<p style="margin-bottom: 16px;">Más allá del amor y la atracción, la admiración mutua es uno de los factores clave en las relaciones duraderas.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 0;">Imagina que tu pareja es como un compañero de equipo. Cuando lo admiras, no solo lo amas, sino que también respetas su esencia, valoras su crecimiento y te sientes orgulloso de quién es.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">¿Cómo se ve la admiración en una relación sana?</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Te inspira y te motiva a crecer en lugar de limitarte.</p>
<p style="margin-bottom: 12px;">• Valoras sus logros y apoyas sus sueños.</p>
<p style="margin-bottom: 0;">• Disfrutas aprender de la otra persona y reconoces sus cualidades.</p>
</div>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🚩 Señales de alerta de falta de admiración:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Sientes que tienes que disminuirte o esconder partes de ti para que el otro no se incomode.</p>
<p style="margin-bottom: 12px;">• En lugar de motivarte, la relación te drena o te hace sentir insuficiente.</p>
<p style="margin-bottom: 0;">• Te das cuenta de que no respetas profundamente quién es la otra persona.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Reflexión:</p>
<p style="margin: 8px 0 0 0;">El amor puede unir a las personas, pero la admiración las mantiene creciendo juntas.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 3
        },
        {
            "title": "Fundamentos - Valores Compartidos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">4. Valores compartidos: La brújula de la relación</h2>

<p style="margin-bottom: 16px;">No significa que deban ser idénticos, pero para que una relación funcione a largo plazo, es fundamental que compartan valores esenciales.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 0;">Piensa en una pareja como dos personas en un bote. Si ambos reman en direcciones opuestas, tarde o temprano se cansarán y el bote se estancará. Los valores compartidos aseguran que remen en la misma dirección.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">¿Cómo se ven los valores compartidos en una relación sana?</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Tienen visiones de vida similares o al menos compatibles (ejemplo: ideas sobre familia, fidelidad, crecimiento personal).</p>
<p style="margin-bottom: 12px;">• Respetan y valoran las creencias del otro sin necesidad de cambiarlas.</p>
<p style="margin-bottom: 0;">• Se apoyan en decisiones importantes y buscan acuerdos en temas fundamentales.</p>
</div>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">🚩 Señales de alerta de falta de valores compartidos:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Discusiones constantes sobre temas esenciales (hijos, dinero, proyectos de vida).</p>
<p style="margin-bottom: 12px;">• No te sientes alineado con su visión de futuro.</p>
<p style="margin-bottom: 0;">• Intentas convencer al otro de cambiar sus valores o sientes que te obligan a cambiar los tuyos.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Reflexión:</p>
<p style="margin: 8px 0 0 0;">La química y la atracción pueden ser intensas, pero si los valores fundamentales no están alineados, la relación eventualmente se volverá difícil.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Fundamentos de Bienestar",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Identifica los Fundamentos para tus Relaciones</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a identificar los fundamentos para tus relaciones.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Fundamentos</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.5: Fundamentos de bienestar</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        },
        {
            "title": "Conclusión del Tema 2",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 2: Cimientos de Conexión</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">Has recorrido un camino profundo de autoconocimiento y transformación:</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<ol style="padding-left: 20px; line-height: 1.9;">
<li style="margin-bottom: 12px;">Identificaste los <strong>patrones que se repiten</strong> en tus relaciones.</li>
<li style="margin-bottom: 12px;">Aprendiste a soltar los <strong>duelos que ya no te pertenecen</strong>.</li>
<li style="margin-bottom: 12px;">Descubriste cómo <strong>negociar tus necesidades</strong> de manera equilibrada.</li>
<li style="margin-bottom: 12px;">Definiste tu <strong>persona equilibrio</strong> - alguien que te guste Y te haga bien.</li>
<li style="margin-bottom: 0;">Reconociste los <strong>fundamentos esenciales</strong> de una relación sana: compromiso, respeto, admiración y valores compartidos.</li>
</ol>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 32px 0;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Ahora Estás Listo para el Siguiente Paso</h3>
<p style="margin-bottom: 0; font-size: 1.05em;">Con estos cimientos sólidos, estás preparado para construir relaciones más conscientes, equilibradas y genuinas. En el siguiente tema, exploraremos cómo llevar todo esto a la práctica en tu vida diaria.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": order + 6
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
    print(f"✅ {len(cards)} cards créées (Subtemas 4-5)")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 AJOUT FINAL - SUBTEMAS 4-5 DU THÈME 2 MODULE 3")
        print("=" * 70)
        
        THEME_ID = 11  # Thème 2 Module 3
        
        num_cards = add_final_subtemas(db, THEME_ID)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 2 COMPLET!")
        print("=" * 70)
        print(f"📚 {num_cards} cards ajoutées (Subtemas 4-5)")
        print(f"🎯 Total Thème 2: 18 + {num_cards} = {18 + num_cards} cards")
        print(f"\n✨ Prochaine étape: Créer le Thème 3 (Del amor propio al amor compartido)")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

