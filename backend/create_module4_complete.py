"""
Script pour créer le Module 4: De la expectativa a la realidad
Avec ses 3 thèmes et toutes les cartes
Font: Source Sans Pro
Couleurs: #a28d72, #cbcbcc, #6b745a
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Module, Theme, ThemeCard

def create_module4(db: Session):
    """Créer le Module 4 complet"""
    
    print("\n" + "=" * 70)
    print("🚀 CRÉATION DU MODULE 4: De la expectativa a la realidad")
    print("=" * 70)
    
    # Créer le module
    module = Module(
        title="De la expectativa a la realidad",
        description="Resignifica el 'deber ser' por el 'deseo ser', yendo más allá de las expectativas externas.",
        objective="El propósito de este módulo es que resignifiques el 'deber ser' por el 'deseo ser', yendo más allá de las expectativas externas, para enfocarte y elegir lo que realmente quieres o deseas",
        belief_to_transform="Siempre me detengo a pensar en lo que los demás dirán, aunque me suelo negar aceptarlo, y eso no me deja hacer lo que realmente quiero.",
        expected_results="* Logras ir más allá de las expectativas externas y enfocarte en lo que realmente deseas (entender qué es eso)\n* Te permites vivir una vida más alineada con lo que te entrega sentido y plenitud",
        recommended_book=None,
        audio_file=None,
        order_number=4,
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module 4 créé (ID: {module.id})")
    
    # THÈME 1: Rompiendo barreras
    print("\n📚 Création du Thème 1: Rompiendo barreras...")
    theme1 = Theme(
        title="Rompiendo barreras",
        content="Identificar las barreras mentales que nos limitan, cuestionarlas y reemplazarlas por creencias que realmente nos ayuden a vivir desde nuestra autenticidad.",
        order_number=1,
        module_id=module.id
    )
    db.add(theme1)
    db.flush()
    print(f"  ✅ Thème 1 créé (ID: {theme1.id})")
    
    # Cartes du Thème 1
    theme1_cards = [
        {
            "title": "Bienvenida al Tema 1",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Rompiendo Barreras</h1>

<p style="font-size: 1.1em; margin-bottom: 16px;">A lo largo de nuestra vida, absorbemos <strong>creencias, normas y expectativas</strong> que moldean nuestra forma de ver el mundo y de relacionarnos con los demás.</p>

<p style="margin-bottom: 16px;">Muchas de estas ideas vienen de nuestra familia, escuela, cultura y sociedad, y sin darnos cuenta, terminamos actuando bajo reglas que ni siquiera hemos elegido conscientemente.</p>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Este módulo se trata de:</h3>
<p style="margin-bottom: 10px;">✓ Identificar esas barreras mentales</p>
<p style="margin-bottom: 10px;">✓ Cuestionarlas</p>
<p style="margin-bottom: 0;">✓ Reemplazarlas por creencias que realmente nos ayuden a vivir desde nuestra autenticidad</p>
</div>

<blockquote style="border-left: 4px solid #6b745a; padding-left: 20px; margin: 24px 0; font-style: italic; color: #555;">
"Lo que nos detiene no es lo que somos, sino lo que creemos que somos."
</blockquote>

<p style="margin-bottom: 16px;">El primer paso para cualquier cambio es <strong>reconocer las barreras</strong> que hemos construido, muchas veces sin darnos cuenta. No somos conscientes de los acuerdos internos que hemos hecho con nosotros mismos ni de las voces internas que influyen en nuestras decisiones.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Mis Acuerdos",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Mis Acuerdos</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Imagina que tu mente es como una casa llena de <strong>contratos firmados</strong>. Algunos acuerdos los hiciste de forma consciente, pero la mayoría los heredaste sin cuestionarlos.</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 8px 0;">✅ "Merezco amor y respeto."</p>
<p style="margin: 8px 0;">❌ "Si me equivoco, soy un fracaso."</p>
<p style="margin: 8px 0;">✅ "Puedo ser auténtico sin miedo."</p>
<p style="margin: 8px 0;">❌ "Tengo que ser como los demás esperan."</p>
</div>

<p style="margin-bottom: 16px;"><strong>Si un contrato ya no te sirve, ¿qué harías?</strong> Exacto, lo rompes y escribes uno nuevo.</p>

<p style="margin-bottom: 16px;">Desde que nacemos, aprendemos a hacer acuerdos con la vida y con los demás. Muchos de ellos son positivos, pero otros pueden convertirse en limitaciones que nos frenan.</p>
</div>""",
            "card_type": "content",
            "order_number": 2
        },
        {
            "title": "Los 4 Acuerdos de Miguel Ruiz",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Los Cuatro Acuerdos</h2>

<p style="margin-bottom: 16px;">Miguel Ruiz nos invita a romper con aquellos acuerdos que nos generan sufrimiento y reemplazarlos por cuatro principios que nos ayudarán a vivir con mayor libertad y bienestar:</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">1. Sé impecable con tus palabras</h3>
<p style="margin-bottom: 0;">Las palabras tienen un poder enorme. Nos pueden sanar o herir, tanto a nosotros como a los demás. Ser impecable con nuestras palabras significa hablarnos con amor y respeto, tanto a nosotros mismos como a los demás.</p>
</div>

<p style="margin-bottom: 12px; padding: 12px; background: #f8f8f8; border-radius: 6px;"><strong>Ejemplo:</strong> En lugar de decir "Soy un desastre en las relaciones", podemos cambiarlo por "Estoy aprendiendo a relacionarme de una manera más sana".</p>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">2. No te tomes nada personal</h3>
<p style="margin-bottom: 0;">Lo que los demás dicen o hacen es un reflejo de su propia realidad, no de la nuestra. Sin embargo, tendemos a interpretar sus acciones como ataques personales, cuando en realidad responden a sus propias creencias y emociones.</p>
</div>

<p style="margin-bottom: 12px; padding: 12px; background: #f8f8f8; border-radius: 6px;"><strong>Ejemplo:</strong> Si alguien critica nuestro trabajo, en lugar de asumir que "no somos lo suficientemente buenos", podemos recordar que esa opinión es de la otra persona y no define nuestro valor.</p>
</div>""",
            "card_type": "content",
            "order_number": 3
        },
        {
            "title": "Los 4 Acuerdos (continuación)",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<div style="background: #cbcbcc; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: #2d2d2d;">3. No hagas suposiciones</h3>
<p style="margin-bottom: 0;">Muchas veces sufrimos porque asumimos lo que los demás piensan o sienten sin preguntar. Creamos historias en nuestra mente y reaccionamos en función de esas suposiciones. Aprender a comunicar nuestras dudas y necesidades puede evitar muchos malentendidos y conflictos.</p>
</div>

<p style="margin-bottom: 12px; padding: 12px; background: #f8f8f8; border-radius: 6px;"><strong>Ejemplo:</strong> Si un amigo no nos responde un mensaje, en lugar de asumir que está enojado con nosotros, podemos simplemente preguntarle si todo está bien.</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">4. Haz siempre lo mejor que puedas</h3>
<p style="margin-bottom: 0;">Nuestro "mejor" cambia según el día, el contexto y nuestro estado emocional. A veces, nuestro mejor esfuerzo será alto; otras veces, simplemente podremos hacer lo mínimo. Lo importante es dar lo mejor de nosotros según nuestras posibilidades en cada momento, sin castigarnos por no ser perfectos.</p>
</div>

<p style="margin-bottom: 12px; padding: 12px; background: #f8f8f8; border-radius: 6px;"><strong>Ejemplo:</strong> Si hoy no nos sentimos con energía para hacer ejercicio, en lugar de culparnos, podemos reconocer que descansar también es parte del proceso, lo importante es la constancia.</p>

<p style="margin-top: 24px; font-size: 1.1em;">Romper barreras implica darnos cuenta de que muchas de las creencias que nos limitan no son nuestras, sino que fueron aprendidas. Al aplicar los Cuatro Acuerdos, comenzamos a ver nuestra vida desde una perspectiva más libre, eligiendo conscientemente cómo queremos pensar, hablar y actuar.</p>
</div>""",
            "card_type": "content",
            "order_number": 4
        },
        {
            "title": "La Voz Interior",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">La Voz Interior a la que Sirvo</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Nuestra <strong>voz interior</strong> es la narradora constante de nuestra vida. Es esa conversación interna que nunca se detiene y que, en muchas ocasiones, define la manera en que nos percibimos a nosotros mismos y al mundo que nos rodea.</p>

<p style="margin-bottom: 16px;">Pero, ¿alguna vez te has detenido a escucharla con atención?</p>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¿De dónde viene nuestra voz interior?</h3>
<p style="margin-bottom: 0;">Desde pequeños, absorbemos las palabras de figuras de autoridad como nuestros padres, maestros y la sociedad en general. Si hemos crecido en un ambiente donde se enfatizaban más los errores que los logros, es probable que nuestra voz interior sea dura y crítica.</p>
</div>

<p style="margin-bottom: 16px;">Por ejemplo, si en la infancia escuchaste frases como:</p>
<ul style="list-style: none; padding-left: 0;">
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px; margin-bottom: 8px;">"No eres suficiente."</li>
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px; margin-bottom: 8px;">"No puedes cometer errores."</li>
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px;">"No hagas el ridículo."</li>
</ul>

<p style="margin-top: 24px;">Es posible que hoy, como adulto, repitas estas ideas en tu mente sin cuestionarlas. <strong>Lo importante es entender que esta voz no es una verdad absoluta, sino una construcción que podemos modificar.</strong></p>
</div>""",
            "card_type": "content",
            "order_number": 5
        },
        {
            "title": "Impacto de la Voz Interior",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">El Impacto de la Voz Interior</h2>

<p style="margin-bottom: 16px;">La manera en que nos hablamos influye directamente en nuestra confianza, nuestras acciones y nuestra capacidad de asumir riesgos.</p>

<p style="margin-bottom: 16px;">Si nuestra voz interior está dominada por el miedo y la autocrítica, tenderemos a:</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 8px 0;">❌ Evitar desafíos por miedo al fracaso</p>
<p style="margin: 8px 0;">❌ Dudar de nuestras capacidades</p>
<p style="margin: 8px 0;">❌ Procrastinar proyectos importantes</p>
<p style="margin: 8px 0;">❌ Sentirnos atrapados en patrones de autosabotaje</p>
</div>

<p style="margin-bottom: 16px;">En cambio, cuando cultivamos una voz interior compasiva y alentadora, nos permitimos crecer, aprender de los errores y construir una vida más auténtica.</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Cómo Transformar la Voz Crítica</h3>
<p style="margin-bottom: 10px;"><strong>1. Identifica el tipo de voz</strong><br>Durante un día, pon atención a cómo te hablas. ¿Es una voz de apoyo o de juicio?</p>
<p style="margin-bottom: 10px;"><strong>2. Cuestiona su veracidad</strong><br>¿De dónde viene esta creencia? ¿Es un pensamiento basado en hechos o en el miedo?</p>
<p style="margin-bottom: 10px;"><strong>3. Redefine tu diálogo interno</strong><br>Si tu voz dice "No eres lo suficientemente bueno", reformúlala: "Estoy aprendiendo y mejorando cada día"</p>
<p style="margin-bottom: 0;"><strong>4. Crea afirmaciones</strong><br>Escribe frases que refuercen tu confianza y repítelas diariamente.</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 6
        }
    ]
    
    for card_data in theme1_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme1.id
        )
        db.add(card)
    
    db.flush()
    print(f"  ✅ {len(theme1_cards)} cartes créées pour le Thème 1")
    
    # THÈME 2: Despertar auténtico
    print("\n📚 Création du Thème 2: Despertar auténtico...")
    theme2 = Theme(
        title="Despertar auténtico",
        content="Cuestionar las capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura.",
        order_number=2,
        module_id=module.id
    )
    db.add(theme2)
    db.flush()
    print(f"  ✅ Thème 2 créé (ID: {theme2.id})")
    
    # Cartes du Thème 2
    theme2_cards = [
        {
            "title": "Bienvenida al Tema 2",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Despertar Auténtico</h1>

<blockquote style="border-left: 4px solid #a28d72; padding-left: 20px; margin: 24px 0; font-style: italic; color: #555;">
"Ser tú mismo en un mundo que constantemente intenta hacerte otra persona es el mayor logro." – Ralph Waldo Emerson
</blockquote>

<p style="font-size: 1.1em; margin-bottom: 16px;"><strong>La autenticidad no es algo que se encuentra, es algo que se cultiva.</strong></p>

<p style="margin-bottom: 16px;">Despertar a nuestro verdadero ser significa cuestionar esas capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura.</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0;">Es un proceso de <strong>exploración y desaprendizaje</strong>, que nos lleva a reconocer quiénes somos más allá de las etiquetas, expectativas y miedos.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Tu Verdadero Ser",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Tu Verdadero Ser</h2>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Error Más Común</h3>
<p style="margin-bottom: 0;">Vivir desde lo aprendido y no desde lo auténtico</p>
</div>

<p style="margin-bottom: 16px;">Muchas personas pasan gran parte de su vida siendo quienes "deberían ser" en lugar de quienes realmente son. Esto sucede porque desde la infancia absorbemos mensajes sobre lo que es aceptable o deseable.</p>

<p style="margin-bottom: 16px;">Es un proceso normal, los seres humanos necesitamos de otros humanos para sobrevivir, nos adaptamos para encajar, pero en el proceso, podemos perder de vista nuestra verdadera esencia.</p>

<p style="font-size: 1.2em; color: #6b745a; margin: 24px 0; padding: 16px; background: #f8f8f8; border-radius: 8px;">La pregunta clave es: <strong>¿Estoy viviendo desde mi autenticidad o desde lo que me dijeron que debía ser?</strong></p>
</div>""",
            "card_type": "content",
            "order_number": 2
        },
        {
            "title": "Yo Aprendido vs Yo Auténtico",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">La Diferencia Entre el "Yo Aprendido" y el "Yo Auténtico"</h2>

<p style="margin-bottom: 16px;">Desde la infancia, comenzamos a moldearnos según lo que creemos que es aceptable o esperado. Adoptamos ciertas actitudes para encajar, para evitar el rechazo o para recibir amor.</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0;">
<div style="background: #cbcbcc; padding: 20px; border-radius: 10px;">
<h3 style="margin-top: 0; color: #2d2d2d;">Yo Aprendido</h3>
<p style="margin: 8px 0;">• Me adapto para agradar a los demás</p>
<p style="margin: 8px 0;">• Tomo decisiones basadas en lo que se espera de mí</p>
<p style="margin: 8px 0;">• Busco aprobación constante</p>
<p style="margin: 8px 0;">• Evito mostrar mis emociones o vulnerabilidad</p>
</div>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px;">
<h3 style="margin-top: 0; color: white;">Yo Auténtico</h3>
<p style="margin: 8px 0;">• Expreso lo que realmente siento y pienso</p>
<p style="margin: 8px 0;">• Tomo decisiones alineadas con lo que deseo</p>
<p style="margin: 8px 0;">• Confío en mi propio criterio</p>
<p style="margin: 8px 0;">• Me permito sentir y expresarme libremente</p>
</div>
</div>

<p style="margin-top: 24px; font-size: 1.1em;">La clave para despertar a tu verdadero ser es comenzar a identificar qué partes de ti se originan en el deseo de encajar y cuáles provienen de tu autenticidad. 😊</p>
</div>""",
            "card_type": "content",
            "order_number": 3
        },
        {
            "title": "Señales de Desconexión",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Señales de Desconexión con tu Verdadero Ser</h2>

<p style="margin-bottom: 16px;">Algunas señales de que estamos desconectados de nuestro yo auténtico incluyen:</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 12px 0;">❌ Sentir que constantemente estamos actuando para complacer a otros</p>
<p style="margin: 12px 0;">❌ Experimentar insatisfacción o vacío a pesar de lograr objetivos externos</p>
<p style="margin: 12px 0;">❌ Tener miedo de mostrar nuestras emociones reales</p>
<p style="margin: 12px 0;">❌ Percibir una falta de dirección o un sentido de "estar perdidos"</p>
</div>

<p style="margin-bottom: 16px;">Por otro lado, cuando nos alineamos con nuestro verdadero ser, experimentamos:</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 12px 0;">✓ Mayor claridad sobre lo que queremos y valoramos</p>
<p style="margin: 12px 0;">✓ Relaciones más genuinas y significativas</p>
<p style="margin: 12px 0;">✓ Una sensación de paz interna al actuar desde nuestra verdad</p>
<p style="margin: 12px 0;">✓ Un flujo natural en nuestras decisiones y acciones</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 4
        },
        {
            "title": "Cultivando la Autoconciencia",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Cultivando la Autoconciencia</h2>

<p style="font-size: 1.1em; margin-bottom: 16px;">Vivir de manera auténtica requiere una profunda comprensión de quiénes somos más allá de nuestras experiencias y roles.</p>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Problema: Desconexión</h3>
<p style="margin-bottom: 0;">Cuando olvidamos quiénes somos o no tenemos claridad de esto, se nos dificulta más conectarnos con nuestra esencia y por ende vivimos desconectados de nosotros mismos y de nuestros más profundos deseos (metas o sueños).</p>
</div>

<p style="margin-bottom: 16px;"><strong>Señales de desconexión:</strong></p>
<ul style="list-style: none; padding-left: 0;">
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px; margin-bottom: 8px;">Sensación de vacío o insatisfacción, aunque todo parezca estar "bien"</li>
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px; margin-bottom: 8px;">Miedo a decepcionar a los demás al expresar nuestras verdaderas opiniones</li>
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px; margin-bottom: 8px;">Decisiones basadas en lo que se espera de nosotros</li>
<li style="padding: 8px 0; border-left: 4px solid #cbcbcc; padding-left: 16px;">Búsqueda constante de validación externa</li>
</ul>

<p style="margin-top: 24px;">Este alejamiento de nuestra esencia genera confusión, ansiedad y la sensación de estar viviendo una vida que no nos pertenece del todo.</p>
</div>""",
            "card_type": "content",
            "order_number": 5
        },
        {
            "title": "El Camino de Regreso",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">El Camino de Regreso: Despertar la Autoconciencia</h2>

<p style="margin-bottom: 16px;">La buena noticia es que la autoconciencia es una habilidad que se puede cultivar. No se trata de convertirse en alguien nuevo, sino de <strong>recordar quién eres</strong> más allá de las etiquetas y creencias aprendidas.</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong style="color: #6b745a;">🔹 Observar sin juzgar</strong><br>
La autoconciencia comienza con la capacidad de notar nuestros pensamientos, emociones y comportamientos sin etiquetarlos como "buenos" o "malos".</p>

<p style="margin-bottom: 12px;"><strong style="color: #6b745a;">🔹 Reconocer patrones limitantes</strong><br>
Identificar en qué momentos nos alejamos de nuestra autenticidad y por qué.</p>

<p style="margin-bottom: 12px;"><strong style="color: #6b745a;">🔹 Diferenciar lo que deseas de lo que aprendiste a desear</strong><br>
Muchas veces perseguimos metas que no nos llenan porque nos enseñaron que "eso es lo correcto".</p>

<p style="margin-bottom: 0;"><strong style="color: #6b745a;">🔹 Aceptar todas las partes de ti</strong><br>
La autoconciencia también implica abrazar nuestras luces y sombras. No se trata de ser perfectos, sino de aceptar todo lo que somos con compasión.</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 6
        },
        {
            "title": "Abrazando la Vulnerabilidad",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Abrazando la Vulnerabilidad</h2>

<p style="margin-bottom: 16px;">¿Cuántas veces has sentido que mostrarte vulnerable es sinónimo de debilidad? Que si dejas que los demás vean tus miedos, tus dudas o tu dolor, podrían usarlos en tu contra.</p>

<p style="margin-bottom: 16px;">La sociedad nos ha enseñado que ser fuerte es "aguantarse todo", no llorar y siempre demostrar que tenemos el control. Pero... <strong>¿y si en realidad la vulnerabilidad fuera una fortaleza?</strong></p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0;">La psicóloga Brené Brown, experta en el tema, dice que <strong>la vulnerabilidad es el pegamento que une a las personas</strong>. Es la capacidad de mostrarnos tal y como somos, sin máscaras, sin aparentar que todo está bien cuando no lo está. Es lo que nos permite conectar de verdad con los demás.</p>
</div>

<p style="margin-bottom: 16px;">Piensa en esto: ¿qué hace que te sientas cercano a alguien? Probablemente no sea que todo en su vida es perfecto, sino que ha compartido contigo sus luchas, sus emociones reales.</p>

<p style="font-size: 1.1em; margin-top: 24px;"><strong>Nos conectamos más con la autenticidad que con la perfección.</strong></p>
</div>""",
            "card_type": "content",
            "order_number": 7
        },
        {
            "title": "Qué Pasa Cuando Evitamos la Vulnerabilidad",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">¿Qué Pasa Cuando Evitamos Ser Vulnerables?</h2>

<p style="margin-bottom: 16px;">Cuando evitamos la vulnerabilidad, caemos en mecanismos de defensa que nos alejan de los demás y de nosotros mismos.</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 12px 0;"><strong>❌ La armadura emocional</strong><br>
Nos ponemos una coraza y actuamos como si nada nos afectara. "Estoy bien, todo bien", aunque por dentro sintamos lo contrario.</p>

<p style="margin: 12px 0;"><strong>❌ El perfeccionismo</strong><br>
Creemos que si somos lo suficientemente "buenos", no nos rechazarán. Nos exigimos más de la cuenta para evitar sentirnos inadecuados.</p>

<p style="margin: 12px 0;"><strong>❌ El distanciamiento</strong><br>
En lugar de arriesgarnos a ser heridos, evitamos la cercanía con los demás. Nos volvemos fríos o independientes en exceso.</p>
</div>

<p style="margin-top: 24px; font-size: 1.1em;">El problema es que, aunque estos mecanismos nos protejan del dolor, también nos impiden sentir amor, conexión y autenticidad.</p>
</div>""",
            "card_type": "content",
            "order_number": 8
        },
        {
            "title": "Cómo Abrazar la Vulnerabilidad",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">¿Cómo Abrazar la Vulnerabilidad?</h2>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">1. Cambia tu perspectiva</h3>
<p style="margin-bottom: 0;">La vulnerabilidad no es un defecto, es una habilidad que nos hace más humanos. Pregúntate: "¿Qué pasaría si en lugar de esconder mi vulnerabilidad, la acepto y la comparto con quienes confío?"</p>
</div>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">2. Practica expresar lo que sientes</h3>
<p style="margin-bottom: 0;">En vez de decir "Nada, no pasa nada", prueba con "Me siento triste porque esperaba otra respuesta y no sé cómo manejarlo".</p>
</div>

<div style="background: #cbcbcc; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: #2d2d2d;">3. Rodéate de personas seguras</h3>
<p style="margin-bottom: 0;">No todos merecen ver tu vulnerabilidad. Comparte tus emociones con personas que te escuchen sin juzgar, que te hagan sentir en un espacio seguro.</p>
</div>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">4. Atrévete a pedir ayuda</h3>
<p style="margin-bottom: 0;">Aceptar que necesitas apoyo no te hace débil, te hace humano. Si estás pasando por un momento difícil, hablar con alguien puede ser un gran paso.</p>
</div>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">5. Acepta tus imperfecciones</h3>
<p style="margin-bottom: 0;">Nadie es perfecto. En lugar de castigarte por lo que no puedes controlar, date permiso de ser quien eres, con tus luces y sombras.</p>
</div>

<p style="margin-top: 24px; font-size: 1.1em;">La vulnerabilidad es el camino hacia la conexión, el amor y la autenticidad. No necesitas ser perfecto para ser amado, solo necesitas ser tú.</p>
</div>""",
            "card_type": "content",
            "order_number": 9
        }
    ]
    
    for card_data in theme2_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme2.id
        )
        db.add(card)
    
    db.flush()
    print(f"  ✅ {len(theme2_cards)} cartes créées pour le Thème 2")
    
    # THÈME 3: Mapa de acción hacia la autenticidad
    print("\n📚 Création du Thème 3: Mapa de acción hacia la autenticidad...")
    theme3 = Theme(
        title="Mapa de acción hacia la autenticidad",
        content="Aprender a alinear tus acciones con tu esencia y construir la vida que realmente deseas.",
        order_number=3,
        module_id=module.id
    )
    db.add(theme3)
    db.flush()
    print(f"  ✅ Thème 3 créé (ID: {theme3.id})")
    
    # Cartes du Thème 3
    theme3_cards = [
        {
            "title": "Bienvenida al Tema 3",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Mapa de Acción hacia la Autenticidad</h1>

<p style="font-size: 1.1em; margin-bottom: 16px;">Ser auténtico es uno de los mayores actos de valentía que podemos hacer en nuestra vida. No porque sea difícil en sí mismo, sino porque desde pequeños hemos aprendido a adaptarnos para ser aceptados.</p>

<p style="margin-bottom: 16px;">Nos enseñaron a encajar, a no hacer demasiado ruido, a seguir ciertas reglas sociales sin cuestionarlas.</p>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Conflicto</h3>
<p style="margin-bottom: 0;">Queremos ser fieles a nosotros mismos, pero también tememos ser rechazados, juzgados o incomprendidos. Entonces, ¿cómo se empieza a vivir con autenticidad?</p>
</div>

<p style="margin-top: 24px; font-size: 1.1em;">La respuesta no está en hacer cambios radicales de la noche a la mañana, sino en <strong>aprender a alinear tus acciones con tu esencia</strong>.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Construir la Vida que Sí Quiero",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Construir la Vida que Sí Quiero</h2>

<p style="margin-bottom: 16px;">Muchas veces pensamos que nuestra vida está determinada por las circunstancias, por lo que nos pasó en el pasado, por la familia en la que nacimos o las oportunidades que tuvimos (o no tuvimos).</p>

<p style="margin-bottom: 16px;">Sin embargo, en realidad, <strong>nuestra vida se construye día a día, con cada decisión, con cada pequeño paso que tomamos</strong>.</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0;">Construir la vida que sí queremos no es un acto de suerte ni algo que ocurre de repente. Es un <strong>proceso intencional</strong>, un camino que requiere claridad, compromiso y acción. No significa que todo saldrá perfecto ni que no habrá obstáculos, sino que, a pesar de ellos, elegimos avanzar hacia algo que realmente nos haga sentido.</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 2
        },
        {
            "title": "Por Qué No Elegimos la Vida que Queremos",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">¿Por Qué a Veces No Elegimos la Vida que Queremos?</h2>

<p style="margin-bottom: 16px;">Muchas veces vivimos en "piloto automático", atrapados en una rutina que no elegimos del todo. Esto puede pasar por varias razones:</p>

<div style="background: #f8f8f8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin: 12px 0;"><strong style="color: #a28d72;">🔹 Creencias limitantes</strong><br>
Pensamos cosas como "no soy suficiente", "es demasiado tarde para cambiar" o "eso no es para mí". Estas ideas nos frenan antes de siquiera intentarlo.</p>

<p style="margin: 12px 0;"><strong style="color: #a28d72;">🔹 Miedo al cambio</strong><br>
Aunque no estemos felices con nuestra vida actual, al menos es familiar. A veces nos quedamos donde estamos porque nos da miedo lo desconocido.</p>

<p style="margin: 12px 0;"><strong style="color: #a28d72;">🔹 Expectativas externas</strong><br>
La sociedad, la familia y los amigos opinan sobre lo que deberíamos hacer. Muchas veces, tomamos decisiones para complacerlos en lugar de pensar en lo que realmente queremos.</p>

<p style="margin: 12px 0;"><strong style="color: #a28d72;">🔹 Falta de claridad</strong><br>
Sentimos que algo no está bien en nuestra vida, pero no sabemos exactamente qué cambiar o hacia dónde ir.</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 3
        },
        {
            "title": "Pequeñas Acciones, Grandes Cambios",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Pequeñas Acciones, Grandes Cambios</h2>

<p style="margin-bottom: 16px;">Construir la vida que quieres <strong>no significa cambiarlo todo de golpe</strong>. No necesitas dejar tu trabajo, mudarte de país o tomar una decisión radical de un día para otro.</p>

<p style="margin-bottom: 16px;"><strong>Los cambios más importantes comienzan con pequeños pasos.</strong></p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 8px 0;">🔹 Si quieres más tranquilidad en tu vida, empieza por crear momentos de calma en tu día.</p>
<p style="margin: 8px 0;">🔹 Si quieres rodearte de personas más alineadas contigo, empieza a poner límites a quienes te desgastan.</p>
<p style="margin: 8px 0;">🔹 Si quieres cambiar de trabajo, investiga opciones, actualiza tu CV o toma un curso.</p>
</div>

<p style="margin-top: 24px; font-size: 1.1em;">No necesitas tenerlo todo claro para empezar. Lo que realmente transforma la vida es la capacidad de <strong>dar un paso, luego otro, y otro más</strong>.</p>
</div>""",
            "card_type": "content",
            "order_number": 4
        },
        {
            "title": "Ejemplo de Transformación",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.7em; margin-bottom: 15px; border-bottom: 2px solid #a28d72; padding-bottom: 8px;">Ejemplo de un Pequeño Cambio</h2>

<div style="background: #cbcbcc; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px;">Imagina a alguien que ha pasado años en un trabajo que no le gusta, pero que no se atreve a salir porque le da miedo no encontrar algo mejor.</p>

<p style="margin-bottom: 16px;">Un día, en lugar de seguir esperando, decide hacer algo pequeño: <strong>inscribirse en un curso, actualizar su currículum o hablar con alguien que trabaja en un área que le interesa</strong>.</p>

<p style="margin-bottom: 16px;">Ese paso le da confianza. Poco a poco, empieza a ver nuevas oportunidades.</p>

<p style="margin-bottom: 0;"><strong>Meses después, consigue un trabajo que le apasiona.</strong> No cambió todo en un día, pero comenzó a moverse en la dirección correcta.</p>
</div>

<div style="background: #a28d72; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">💡 Paso de Acción</h3>
<p style="margin-bottom: 12px;">La vida que sí quieres no es un sueño imposible. Es algo que se construye con cada decisión que tomas.</p>
<p style="margin-bottom: 12px;">No importa cuánto tiempo hayas pasado en un camino que no te hace feliz. Siempre puedes elegir moverte hacia algo que realmente resuene contigo.</p>
<p style="margin-bottom: 0;"><strong>No esperes el momento perfecto. Empieza hoy. Un paso, una elección, un cambio a la vez.</strong> 💙</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 5
        },
        {
            "title": "Felicidades",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; text-align: center;">¡Felicidades por Completar el Módulo 4!</h1>

<div style="background: linear-gradient(135deg, #6b745a 0%, #a28d72 100%); color: white; padding: 40px; border-radius: 15px; margin: 24px 0; text-align: center;">
<p style="font-size: 1.3em; margin: 0;">🎉 Has dado un paso enorme hacia tu autenticidad 🎉</p>
</div>

<p style="font-size: 1.1em; text-align: center; margin: 24px 0;">Ahora estás más conectado/a con tu verdadero ser y tienes las herramientas para construir la vida que realmente deseas.</p>

<p style="text-align: center; margin-top: 32px; color: #6b745a; font-size: 1.2em;"><strong>¡Continúa tu transformación! ✨</strong></p>
</div>""",
            "card_type": "content",
            "order_number": 6
        }
    ]
    
    for card_data in theme3_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme3.id
        )
        db.add(card)
    
    db.flush()
    print(f"  ✅ {len(theme3_cards)} cartes créées pour le Thème 3")
    
    db.commit()
    
    print("\n" + "=" * 70)
    print("✅ MODULE 4 CRÉÉ AVEC SUCCÈS!")
    print("=" * 70)
    print(f"📚 Thème 1 (Rompiendo barreras): {len(theme1_cards)} cartes")
    print(f"📚 Thème 2 (Despertar auténtico): {len(theme2_cards)} cartes")
    print(f"📚 Thème 3 (Mapa de acción): {len(theme3_cards)} cartes")
    print(f"\n✨ Total: {len(theme1_cards) + len(theme2_cards) + len(theme3_cards)} cartes créées!")
    print("\n🎯 Prochaine étape: Créer les exercices du Module 4")

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        create_module4(db)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

