"""
Script pour créer le Module 3 avec le Thème 1 COMPLET - fidèle au texte original
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Module, Theme, ThemeCard

# Styles
FONT = "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
C_TEXT = "#2d2d2d"
C_TITLE = "#6b745a"
C_ACCENT = "#a28d72"
C_BG_LIGHT = "#f5f5f0"
C_BG_GRAY = "#cbcbcc"

def css():
    return f'color: {C_TEXT}; font-family: {FONT}; line-height: 1.8; max-width: 800px;'

def create_module3(db: Session):
    """Créer le module 3"""
    print("\n📦 Création du Module 3...")
    module = Module(
        title="El Arte de Amar",
        description="Aprende a sostener relaciones personales asertivas y equilibrar tu individualidad para generar mayor estabilidad en tus vínculos.",
        objective="El propósito de este módulo es que aprendas a sostener relaciones personales asertivas, y equilibrar tu individualidad, de tal manera que logres generar una mayor estabilidad en tus vínculos",
        belief_to_transform="Siempre elijo a las personas equivocadas, parece que estoy destinado a relaciones que no funcionan.",
        expected_results="Logras generar un equilibrio y estabilidad entre la experiencia individual (El Yo) y la experiencia relacional (El Nosotr@s). Aprendes a relacionarte de manera asertiva con tus vínculos, y ser más selectiv@ con las personas que atraes a tu vida.",
        recommended_book="Siete reglas de oro para vivir en pareja de John M Gottman (lo encuentras en la carpeta de Bonus)",
        audio_file=None,
        order_number=3,
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module créé (ID: {module.id})")
    return module

def create_theme1(db: Session, module_id: int):
    """Thème 1"""
    print("\n📚 Création du Thème 1...")
    theme = Theme(
        title="Espejos del alma",
        content="Este tema te invita a reflexionar sobre cómo tus experiencias pasadas, tus patrones de apego y tus necesidades no satisfechas influyen en tus relaciones actuales.",
        order_number=1,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 1 créé (ID: {theme.id})")
    return theme

def create_theme1_cards(db: Session, theme_id: int):
    """Cards du thème 1 - CONTENU COMPLET"""
    print("\n🎴 Création des cards du Thème 1...")
    
    cards = [
        {
            "title": "Bienvenida al Tema 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Espejos del Alma</h1>

<p style="margin-bottom: 16px;">Este tema te invita a reflexionar sobre cómo tus experiencias pasadas, tus patrones de apego y tus necesidades no satisfechas influyen en tus relaciones actuales.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¿Por qué es importante?</h3>
<p style="margin-bottom: 0;">Comprender estas dinámicas no solo te ayuda a construir relaciones más sanas, sino que también te permite sanar partes de ti mismo que aún buscan equilibrio y conexión.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: ¿De Dónde Vengo y a Dónde Voy? - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: ¿De Dónde Vengo y a Dónde Voy?</h1>

<p style="margin-bottom: 16px;">Las relaciones personales, especialmente las más cercanas, son como espejos que reflejan quiénes somos y las experiencias que hemos acumulado a lo largo de la vida.</p>

<p style="margin-bottom: 16px;">Desde una perspectiva psicológica, estas experiencias pasadas influyen profundamente en cómo percibimos el amor, cómo manejamos la cercanía y cómo establecemos vínculos con los demás.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">¿De dónde vengo?</h3>
<p style="margin-bottom: 0;">Todo comienza en la infancia. Es en este período donde aprendemos nuestras primeras lecciones sobre el amor y las relaciones. Estas lecciones no siempre se transmiten con palabras; muchas veces, las aprendemos observando cómo nuestros cuidadores se relacionan entre sí y con nosotros. ¿Había seguridad y calidez en esas interacciones, o había distancia y conflicto? Estas experiencias iniciales moldean nuestras expectativas sobre las relaciones futuras.</p>
</div>

<p style="margin-bottom: 16px;">Por ejemplo, si creciste en un hogar donde los conflictos no se resolvían o se evitaban, es posible que hayas aprendido a temer las confrontaciones. Esto puede llevarte, en la adultez, a evitar abordar problemas en tus relaciones, dejando que se acumulen hasta que se vuelvan inmanejables.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "¿De Dónde Vengo y a Dónde Voy? - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿A dónde voy?</h2>

<p style="margin-bottom: 16px;">El otro lado de esta reflexión es mirar hacia el futuro: entender cómo nuestras experiencias pasadas nos han moldeado no significa que estemos condenados a repetirlas.</p>

<p style="margin-bottom: 16px;">La psicología nos enseña que tenemos la capacidad de elegir, cambiar y sanar. Este proceso comienza cuando tomamos conciencia de cómo nuestras vivencias pasadas están influyendo en nuestras decisiones y relaciones actuales.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo común</h4>
<p style="margin-bottom: 0;">Alguien que, al reflexionar sobre su historia, se da cuenta de que tiende a buscar relaciones con personas emocionalmente inaccesibles porque, en su infancia, el amor y la atención no siempre estaban disponibles. Al comprender esta conexión, puede empezar a tomar decisiones más conscientes, buscando vínculos que le ofrezcan seguridad y reciprocidad.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        
        {
            "title": "¿De Dónde Vengo y a Dónde Voy? - Parte 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El Poder de la Conciencia</h2>

<p style="margin-bottom: 16px;">Reconocer de dónde vienes no se trata de culpar a nadie, sino de comprender. Al explorar tu historia, puedes identificar patrones que ya no te sirven y que puedes cambiar.</p>

<p style="margin-bottom: 16px;">Esto es importante porque, como seres humanos, tendemos a repetir lo familiar, incluso cuando no nos beneficia. Pero cuando te permites hacer una pausa y reflexionar, puedes romper ciclos y construir relaciones más saludables y equilibradas.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Un ejemplo cotidiano</h4>
<p style="margin-bottom: 0;">Piensa en cómo reaccionas cuando alguien no responde a un mensaje tuyo de inmediato. Si te invade la ansiedad o la sensación de rechazo, puede ser un reflejo de una experiencia pasada donde no te sentiste importante o priorizado. Al identificar esta conexión, puedes recordar que tu valor no depende de la respuesta inmediata de los demás, sino de cómo tú eliges interpretarlo y gestionarlo.</p>
</div>

<p style="margin-bottom: 16px;">Tu historia no define tu destino, pero sí te ofrece valiosas pistas sobre lo que necesitas para sanar y crecer. Entender de dónde vienes y hacia dónde quieres ir es un paso esencial para transformar tus relaciones. Este proceso no es lineal, pero con cada reflexión y elección consciente, te acercas más a construir vínculos más estables, auténticos y satisfactorios.</p>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        
        {
            "title": "Ejercicio: De Dónde Vengo y a Dónde Voy",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Conecta con tus Bases del Amor</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a conectar con tus bases del amor.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Bases</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.1: De dónde vengo y a dónde voy?</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 5
        },
        
        {
            "title": "Subtema 2: Mi Estilo de Apego - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Mi Estilo de Apego</h1>

<p style="margin-bottom: 16px;">¿Te has preguntado por qué algunas personas parecen sentirse cómodas con la cercanía emocional, mientras que otras prefieren mantener cierta distancia, o incluso luchan con miedos de abandono?</p>

<p style="margin-bottom: 16px;">La forma en que nos relacionamos con los demás tiene raíces profundas que se remontan a nuestras primeras experiencias de vida. A esto se le llama <strong>estilo de apego</strong>, y es como una "huella emocional" que determina cómo percibimos el amor, la confianza y la seguridad en nuestras relaciones.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Entendiendo tu estilo de apego</h3>
<p style="margin-bottom: 0;">Desde pequeños, todos desarrollamos un sistema de apego basado en cómo nuestros cuidadores respondieron a nuestras necesidades emocionales y físicas. Este sistema es como un mapa interno que nos guía en nuestras relaciones.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        
        {
            "title": "Mi Estilo de Apego - Parte 2: Apego Seguro",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. Apego Seguro</h2>

<p style="margin-bottom: 16px;">Si en la infancia recibiste cuidado constante y amor incondicional, es probable que tengas un apego seguro. Este estilo permite confiar en los demás, sentirte cómodo con la cercanía emocional y manejar los conflictos sin miedo a perder la relación.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo en una relación de pareja</h4>
<p style="margin-bottom: 0;">Ana y su pareja tienen un desacuerdo sobre cómo organizar un viaje. Aunque la conversación se pone tensa, Ana se siente segura de que podrán resolverlo juntos. Hablan sobre sus diferencias, llegan a un acuerdo y terminan sintiéndose más conectados.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Ejemplo en una amistad</h4>
<p style="margin-bottom: 0;">Marcos no ha hablado con su mejor amigo en varias semanas porque ambos han estado ocupados. En lugar de preocuparse o pensar que algo está mal, le envía un mensaje casual para ponerse al día. No necesita constante contacto para sentir que la amistad sigue fuerte.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        
        {
            "title": "Mi Estilo de Apego - Parte 3: Apego Ansioso",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. Apego Ansioso</h2>

<p style="margin-bottom: 16px;">Si experimentaste respuestas impredecibles de tus cuidadores, quizás aprendiste a buscar validación constante. En este caso, puedes sentir miedo al abandono y tender a ser muy sensible a señales de rechazo, incluso cuando no están allí.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo en una relación de pareja</h4>
<p style="margin-bottom: 0;">Sofía envía un mensaje a su pareja y no recibe respuesta durante una hora. Empieza a pensar: "¿Por qué no me responde? ¿Habrá pasado algo? ¿Estará molesto conmigo?". Sofía se siente ansiosa y envía más mensajes buscando una confirmación de que todo está bien.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Ejemplo en una amistad</h4>
<p style="margin-bottom: 0;">Carlos organiza una reunión y su amigo cancela en el último minuto. Carlos empieza a pensar que su amigo ya no lo valora y se preocupa de que la amistad se esté enfriando. Esto le lleva a buscar validación constantemente, preguntándole si hizo algo mal.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 8
        },
        
        {
            "title": "Mi Estilo de Apego - Parte 4: Apego Evitativo",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Apego Evitativo</h2>

<p style="margin-bottom: 16px;">Si tus cuidadores fueron emocionalmente distantes o inconsistentes, podrías haber aprendido a valerte por ti mismo y evitar la cercanía como una forma de protegerte del dolor. Aunque valoras la independencia, esto puede dificultar establecer vínculos profundos.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo en una relación de pareja</h4>
<p style="margin-bottom: 0;">Luis siente que su pareja está siendo "demasiado emocional" al expresar sus sentimientos sobre algo que le molesta. En lugar de escuchar y conectar, Luis se distancia y cambia de tema, evitando cualquier conversación profunda porque le hace sentir incómodo.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Ejemplo en una amistad</h4>
<p style="margin-bottom: 0;">Andrea recibe un mensaje de una amiga que quiere hablar de un problema personal. Aunque Andrea se preocupa por su amiga, siente que la conversación podría ser "demasiado intensa" y decide posponer la respuesta para no involucrarse emocionalmente.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 9
        },
        
        {
            "title": "Mi Estilo de Apego - Parte 5: Apego Desorganizado",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">4. Apego Desorganizado</h2>

<p style="margin-bottom: 16px;">Este estilo suele surgir de experiencias tempranas de trauma o abandono. Es una mezcla de deseo de cercanía y miedo a ella, lo que puede llevar a relaciones intensas y caóticas.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo en una relación de pareja</h4>
<p style="margin-bottom: 0;">Marta quiere sentirse cerca de su pareja, pero al mismo tiempo tiene miedo de que la lastimen. Por eso, a veces busca atención desesperadamente y, otras veces, empuja a su pareja lejos, confundiendo a ambos. Este comportamiento suele generar conflictos en la relación.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">Ejemplo en una amistad</h4>
<p style="margin-bottom: 0;">Jorge tiene una amistad cercana, pero siempre teme que lo traicionen o lo abandonen. A veces, es muy cariñoso con su amigo y busca constante conexión, pero en otras ocasiones actúa de forma distante o incluso agresiva sin razón aparente.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 10
        },
        
        {
            "title": "Mi Estilo de Apego - Parte 6: ¿Por Qué es Importante?",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Por Qué es Importante Conocer tu Estilo de Apego?</h2>

<p style="margin-bottom: 16px;">Tu estilo de apego no es un destino fijo, pero sí es un punto de partida. Entender cómo te relacionas emocionalmente te da claridad sobre patrones que podrías estar repitiendo.</p>

<p style="margin-bottom: 16px;">Por ejemplo, si tienes un apego ansioso, puede que encuentres difícil confiar en que tu pareja estará para ti, lo que puede llevarte a comportamientos que, sin querer, terminan alejando a la otra persona.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Empoderamiento</h3>
<p style="margin-bottom: 0;">Saber esto no es para culparte ni para justificar comportamientos, sino para empoderarte. Al identificar tu estilo de apego, puedes comenzar a trabajar en los aspectos que te limitan y desarrollar herramientas para construir relaciones más seguras y equilibradas.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 11
        },
        
        {
            "title": "Ejercicio: Mi Estilo de Apego",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Conoce tu Tipo de Apego</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a conocer tu tipo de apego.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Bases</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.2: Mi estilo de apego</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 12
        },
        
        {
            "title": "Subtema 3: Soy el Adulto que Necesité - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Soy el Adulto que Necesité</h1>

<p style="margin-bottom: 16px;">A lo largo de nuestras vidas, muchas de las inseguridades y dificultades que enfrentamos en nuestras relaciones tienen raíces en necesidades emocionales que no fueron satisfechas en nuestra infancia.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Un Acto de Amor Propio</h3>
<p style="margin-bottom: 0;">Ser "el adulto que necesitaste" no significa borrar el pasado ni culpar a quienes nos criaron, sino tomar conciencia de lo que faltó y aprender a ofrecerte ahora aquello que siempre buscaste en los demás. Es un acto de amor propio y de responsabilidad emocional.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 13
        },
        
        {
            "title": "Soy el Adulto que Necesité - Parte 2: Reconociendo las Necesidades",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Reconociendo las Necesidades No Satisfechas</h2>

<p style="margin-bottom: 16px;">Cuando éramos niños, dependíamos completamente de los adultos a nuestro alrededor para recibir amor, validación y protección. Si esas necesidades no se cubrieron de manera consistente, es posible que hayamos crecido con ciertas carencias emocionales.</p>

<p style="margin-bottom: 16px;">Tal vez aprendiste que era más seguro esconder tus emociones para evitar conflictos, o quizá sentiste que debías "ganarte" el afecto de los demás siendo perfecto o complaciente.</p>

<p style="margin-bottom: 16px;">Estos patrones de respuesta pueden haber funcionado en tu infancia para protegerte, pero en la adultez suelen convertirse en barreras para relacionarte de manera auténtica y satisfactoria. Reconocer qué necesitaste en el pasado te ayuda a comprender por qué actúas como lo haces hoy.</p>
</div>""",
            "card_type": "theory",
            "order_number": 14
        },
        
        {
            "title": "Soy el Adulto que Necesité - Parte 3: Aprendiendo a Ser tu Propio Sostén",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Aprendiendo a Ser tu Propio Sostén Emocional</h2>

<p style="margin-bottom: 16px;">Ser el adulto que necesitaste significa asumir la responsabilidad de tu bienestar emocional. Nadie puede llenar completamente los vacíos que quedaron en tu interior, pero tú puedes aprender a ser el sostén que siempre has buscado.</p>

<p style="margin-bottom: 16px;">Esto implica desarrollar habilidades para cuidarte, validarte y amarte incondicionalmente, independientemente de lo que los demás puedan ofrecerte.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Recomendaciones para empezar:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Valida tus emociones</h4>
<p style="margin-bottom: 0;">Cuando sientas tristeza, enojo o miedo, en lugar de ignorarlas o juzgarlas, reconoce lo que estás experimentando. Dite a ti mismo/a: "Es válido sentir esto. Estoy aquí para mí." (sigue poniendo en práctica todo lo que aprendiste en el módulo #1)</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Crea un espacio seguro interno</h4>
<p style="margin-bottom: 12px;">Piensa en lo que un adulto cariñoso te habría dicho cuando eras niño/a para consolarte. Ahora, sé tú quien te hable con esas palabras.</p>
<p style="margin-bottom: 0;"><strong>Por ejemplo:</strong> "Está bien cometer errores. Lo importante es que sigas aprendiendo y creciendo."</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 15
        },
        
        {
            "title": "Soy el Adulto que Necesité - Parte 4: Establece Límites Saludables",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. Establece Límites Saludables</h2>

<p style="margin-bottom: 16px;">Aprender a decir "no" y proteger tu espacio emocional es un acto de autocuidado. Si te cuesta hacerlo, recuerda que tus necesidades también son importantes y que tienes derecho a priorizarlas.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo: Estableciendo límites con un amigo, pareja o familiar</h4>
<p style="margin-bottom: 12px;">Imagina que la persona X (elige el nombre de la persona con la que más te cuesta poner límites) te pide ayuda con un proyecto en un momento en el que ya te sientes sobrecargado/a con tus propias responsabilidades. Aunque quieres apoyarlo, sabes que decir "sí" pondría en riesgo tu bienestar emocional o físico.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Cómo decir "no" de manera clara y respetuosa</h4>
<p style="margin-bottom: 0;">"Me encantaría ayudarte, pero en este momento no puedo porque ya tengo muchas cosas en mi agenda. Espero que puedas entenderlo."</p>
</div>

<p style="margin-bottom: 12px;">Este tipo de respuesta:</p>
<ul style="margin-bottom: 16px; padding-left: 24px;">
<li style="margin-bottom: 8px;"><strong>Es clara y honesta:</strong> Explica tu límite sin dar excusas innecesarias.</li>
<li style="margin-bottom: 8px;"><strong>Respeta al otro:</strong> Muestra empatía al reconocer su necesidad.</li>
<li style="margin-bottom: 8px;"><strong>Respeta tus necesidades:</strong> Prioriza tu bienestar sin sentir culpa.</li>
</ul>

<p style="margin-bottom: 16px;">Establecer límites como este refuerza la idea de que cuidar de ti mismo/a no es egoísmo, sino una forma de asegurarte de que puedes estar presente para los demás desde un lugar auténtico y equilibrado. 🙂</p>
</div>""",
            "card_type": "practical",
            "order_number": 16
        },
        
        {
            "title": "Soy el Adulto que Necesité - Parte 5: Transformando tu Relación Contigo Mismo",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Transformando tu Relación Contigo Mismo</h2>

<p style="margin-bottom: 16px;">Cuando comienzas a atender tus propias necesidades, algo cambia. Dejas de buscar en los demás lo que puedes darte a ti mismo/a y te relacionas desde un lugar de abundancia, no de carencia.</p>

<p style="margin-bottom: 16px;">Esto no significa que dejes de necesitar a las personas, sino que las eliges para compartir tu vida, no para llenarte.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">Ejemplo</h4>
<p style="margin-bottom: 0;">Una persona que ha aprendido a validarse emocionalmente podrá aceptar el desacuerdo de un amigo o pareja sin sentir que su valor personal está en juego. Esto genera relaciones más equilibradas y menos reactivas.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 17
        },
        
        {
            "title": "Conclusión del Tema 1",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 1</h2>

<p style="margin-bottom: 16px;">Entender cómo nos relacionamos con los demás comienza con mirar hacia dentro y reflexionar sobre nuestras experiencias pasadas. Todo lo que vivimos, especialmente en nuestros primeros vínculos, deja huellas que influyen en cómo percibimos el amor, la confianza y la cercanía.</p>

<p style="margin-bottom: 16px;">Al reconocer esas raíces, podemos entender por qué actuamos de cierta manera en nuestras relaciones y empezar a cambiar los patrones que ya no nos sirven.</p>

<p style="margin-bottom: 16px;">A lo largo de este proceso, también aprendemos que no necesitamos buscar en otros lo que podemos darnos a nosotros mismos. Tomar la responsabilidad de atender nuestras propias necesidades emocionales es un acto de amor propio que no solo sana nuestras heridas, sino que también transforma la manera en que nos vinculamos con quienes nos rodean.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Camino a Seguir</h3>
<p style="margin-bottom: 0;">Cuando conectamos con nuestro pasado y nos damos permiso de crecer desde ahí, empezamos a construir relaciones más conscientes, equilibradas y auténticas, basadas en la seguridad y el respeto mutuo. Este es el camino para crear el espacio emocional que siempre hemos buscado, primero dentro de nosotros y luego en los demás.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 18
        },
        
        {
            "title": "Ejercicio: Soy el Adulto que Necesité",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Date Todo lo que Necesitas</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a darte todo lo que necesitas.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Bases</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.3: Soy el adulto que necesité</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 19
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
    print(f"✅ {len(cards)} cards créées pour le Thème 1")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU MODULE 3: THÈME 1 COMPLET")
        print("=" * 70)
        
        # Créer le module
        module = create_module3(db)
        
        # Créer le thème 1
        theme1 = create_theme1(db, module.id)
        num_cards1 = create_theme1_cards(db, theme1.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 3 THÈME 1 CRÉÉ")
        print("=" * 70)
        print(f"📦 Module ID: {module.id}")
        print(f"📚 Thème 1 ID: {theme1.id} ({num_cards1} cards)")
        print("\n🎯 Exécute maintenant les scripts pour les thèmes 2 et 3")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

