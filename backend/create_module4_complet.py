"""
Script pour créer le Module 4 COMPLET
Module 4: De la expectativa a la realidad (3 thèmes)
FIDÈLE à 100% au texte original
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

def create_module(db: Session):
    """Créer le Module 4"""
    print("\n📚 Création du Module 4...")
    module = Module(
        title="De la expectativa a la realidad",
        description="Resignifica el 'deber ser' por el 'deseo ser'",
        objective="El propósito de este módulo es que resignifiques el 'deber ser' por el 'deseo ser', yendo más allá de las expectativas externas, para enfocarte y elegir lo que realmente quieres o deseas",
        belief_to_transform="Siempre me detengo a pensar en lo que los demás dirán, aunque me suelo negar aceptarlo, y eso no me deja hacer lo que realmente quiero.",
        expected_results="* Logras ir más allá de las expectativas externas y enfocarte en lo que realmente deseas (entender qué es eso)\n* Te permites vivir una vida más alineada con lo que te entrega sentido y plenitud",
        recommended_book="Los cuatro acuerdos de Miguel Ruiz (lo encuentras en la carpeta de Bonus)",
        audio_file=None,
        order_number=4,
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module 4 créé (ID: {module.id})")
    return module

def create_theme1_cards(db: Session, theme_id: int):
    """Cards du Thème 1: Rompiendo barreras"""
    print("\n🎴 Création des cards du Thème 1...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 1",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Rompiendo Barreras</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">A lo largo de nuestra vida, absorbemos creencias, normas y expectativas que moldean nuestra forma de ver el mundo y de relacionarnos con los demás.</p>

<p style="margin-bottom: 16px;">Muchas de estas ideas vienen de nuestra familia, escuela, cultura y sociedad, y sin darnos cuenta, terminamos actuando bajo reglas que ni siquiera hemos elegido conscientemente.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Propósito de Este Módulo</h3>
<p style="margin-bottom: 0;">Identificar esas barreras mentales, cuestionarlas y reemplazarlas por creencias que realmente nos ayuden a vivir desde nuestra autenticidad.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin: 0; font-size: 1.1em; font-style: italic;">"Lo que nos detiene no es lo que somos, sino lo que creemos que somos."</p>
</div>

<p style="margin-bottom: 16px;">El primer paso para cualquier cambio es reconocer las barreras que hemos construido, muchas veces sin darnos cuenta. No somos conscientes de los acuerdos internos que hemos hecho con nosotros mismos ni de las voces internas que influyen en nuestras decisiones.</p>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Mis acuerdos
    cards.extend([
        {
            "title": "Subtema 1: Mis Acuerdos - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Mis Acuerdos</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">Imagina que tu mente es como una casa llena de contratos firmados. Algunos acuerdos los hiciste de forma consciente, pero la mayoría los heredaste sin cuestionarlos.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Algunos de esos acuerdos dicen:</h3>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong style="color: #5cb85c;">✅ "Merezco amor y respeto."</strong></p>
<p style="margin-bottom: 12px;"><strong style="color: #d9534f;">❌ "Si me equivoco, soy un fracaso."</strong></p>
<p style="margin-bottom: 12px;"><strong style="color: #5cb85c;">✅ "Puedo ser auténtico sin miedo."</strong></p>
<p style="margin-bottom: 0;"><strong style="color: #d9534f;">❌ "Tengo que ser como los demás esperan."</strong></p>
</div>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">Una Pregunta Clave</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Si un contrato ya no te sirve, ¿qué harías? Exacto, lo rompes y escribes uno nuevo.</p>
</div>

<p style="margin-bottom: 16px;">Desde que nacemos, aprendemos a hacer acuerdos con la vida y con los demás. Muchos de ellos son positivos, pero otros pueden convertirse en limitaciones que nos frenan.</p>

<p style="margin-bottom: 16px;">Miguel Ruiz nos invita a romper con aquellos acuerdos que nos generan sufrimiento y reemplazarlos por cuatro principios que nos ayudarán a vivir con mayor libertad y bienestar:</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Mis Acuerdos - Acuerdo 1",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">1. Sé impecable con tus palabras</h2>

<p style="margin-bottom: 16px;">Las palabras tienen un poder enorme. Nos pueden sanar o herir, tanto a nosotros como a los demás.</p>

<p style="margin-bottom: 16px;">Muchas veces, hemos interiorizado mensajes negativos desde la infancia: "No eres lo suficientemente bueno", "No puedes hacer eso". Estas frases se quedan grabadas en nuestra mente y nos condicionan.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Principio</h3>
<p style="margin-bottom: 0;">Ser impecable con nuestras palabras significa hablarnos con amor y respeto, tanto a nosotros mismos como a los demás.</p>
</div>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong>En lugar de decir:</strong> "Soy un desastre en las relaciones"</p>
<p style="margin-bottom: 0;"><strong>Podemos cambiarlo por:</strong> "Estoy aprendiendo a relacionarme de una manera más sana"</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Mis Acuerdos - Acuerdo 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">2. No te tomes nada personal</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">Lo que los demás dicen o hacen es un reflejo de su propia realidad, no de la nuestra.</p>

<p style="margin-bottom: 16px;">Sin embargo, tendemos a interpretar sus acciones como ataques personales, cuando en realidad responden a sus propias creencias y emociones.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">Si alguien critica nuestro trabajo, en lugar de asumir que "no somos lo suficientemente buenos", podemos recordar que esa opinión es de la otra persona y no define nuestro valor.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Mis Acuerdos - Acuerdo 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">3. No hagas suposiciones</h2>

<p style="margin-bottom: 16px;">Muchas veces sufrimos porque asumimos lo que los demás piensan o sienten sin preguntar.</p>

<p style="margin-bottom: 16px;">Creamos historias en nuestra mente y reaccionamos en función de esas suposiciones. Aprender a comunicar nuestras dudas y necesidades puede evitar muchos malentendidos y conflictos.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">Si un amigo no nos responde un mensaje, en lugar de asumir que está enojado con nosotros, podemos simplemente preguntarle si todo está bien.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 3
        },
        {
            "title": "Mis Acuerdos - Acuerdo 4",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">4. Haz siempre lo mejor que puedas</h2>

<p style="margin-bottom: 16px;">Nuestro "mejor" cambia según el día, el contexto y nuestro estado emocional.</p>

<p style="margin-bottom: 16px;">A veces, nuestro mejor esfuerzo será alto; otras veces, simplemente podremos hacer lo mínimo. Lo importante es dar lo mejor de nosotros según nuestras posibilidades en cada momento, sin castigarnos por no ser perfectos.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Ejemplo:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin-bottom: 0;">Si hoy no nos sentimos con energía para hacer ejercicio, en lugar de culparnos, podemos reconocer que descansar también es parte del proceso, lo importante es la constancia.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        },
        {
            "title": "Mis Acuerdos - Conclusión",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Rompiendo Barreras</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">Romper barreras implica darnos cuenta de que muchas de las creencias que nos limitan no son nuestras, sino que fueron aprendidas.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Camino hacia la Libertad</h3>
<p style="margin-bottom: 0;">Al aplicar los Cuatro Acuerdos, comenzamos a ver nuestra vida desde una perspectiva más libre, eligiendo conscientemente cómo queremos pensar, hablar y actuar.</p>
</div>

<p style="margin-bottom: 16px;">Este es un proceso que lleva tiempo, pero cada pequeño paso que damos nos acerca a una versión más auténtica y en paz con nosotros mismos.</p>
</div>""",
            "card_type": "theory",
            "order_number": order + 5
        },
        {
            "title": "Ejercicio: Mis Acuerdos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Identifica tus Acuerdos</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a identificar tus acuerdos.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Rompiendo Barreras</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Acuerdos</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 6
        }
    ])
    order += 7
    
    # SUBTEMA 2: La voz interior
    cards.extend([
        {
            "title": "Subtema 2: La Voz Interior a la que Sirvo",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: La Voz Interior a la que Sirvo</h1>

<p style="margin-bottom: 16px; font-size: 1.1em;">Nuestra voz interior es la narradora constante de nuestra vida. Es esa conversación interna que nunca se detiene y que, en muchas ocasiones, define la manera en que nos percibimos a nosotros mismos y al mundo que nos rodea.</p>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 0; font-size: 1.1em;">Pero, ¿alguna vez te has detenido a escucharla con atención?</p>
</div>

<p style="margin-bottom: 16px;">La voz interior se forma a partir de nuestras experiencias, creencias, educación y la influencia de quienes nos rodean.</p>

<p style="margin-bottom: 16px;">En muchos casos, sin darnos cuenta, le damos más poder a una voz crítica y limitante, en lugar de fortalecer aquella que nos impulsa y nos da confianza.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "La Voz Interior - Origen",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿De dónde viene nuestra voz interior?</h2>

<p style="margin-bottom: 16px;">Desde pequeños, absorbemos las palabras de figuras de autoridad como nuestros padres, maestros y la sociedad en general. Si hemos crecido en un ambiente donde se enfatizaban más los errores que los logros, es probable que nuestra voz interior sea dura y crítica.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Por ejemplo, si en la infancia escuchaste frases como:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin: 20px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">• "No eres suficiente."</p>
<p style="margin-bottom: 12px;">• "No puedes cometer errores."</p>
<p style="margin-bottom: 0;">• "No hagas el ridículo."</p>
</div>

<p style="margin-bottom: 16px;">Es posible que hoy, como adulto, repitas estas ideas en tu mente sin cuestionarlas.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo Importante</h3>
<p style="margin-bottom: 0;">Lo importante es entender que esta voz no es una verdad absoluta, sino una construcción que podemos modificar.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "La Voz Interior - Impacto",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El impacto de la voz interior en nuestras decisiones</h2>

<p style="margin-bottom: 16px;">La manera en que nos hablamos influye directamente en nuestra confianza, nuestras acciones y nuestra capacidad de asumir riesgos.</p>

<h3 style="color: #d9534f; margin-top: 24px; margin-bottom: 16px;">Si nuestra voz interior está dominada por el miedo y la autocrítica, tenderemos a:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Evitar desafíos por miedo al fracaso</p>
<p style="margin-bottom: 12px;">• Dudar de nuestras capacidades</p>
<p style="margin-bottom: 12px;">• Procrastinar proyectos importantes</p>
<p style="margin-bottom: 0;">• Sentirnos atrapados en patrones de autosabotaje</p>
</div>

<h3 style="color: #5cb85c; margin-top: 24px; margin-bottom: 16px;">En cambio, cuando cultivamos una voz interior compasiva y alentadora:</h3>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<p style="margin-bottom: 0;">Nos permitimos crecer, aprender de los errores y construir una vida más auténtica.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "La Voz Interior - Transformación",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cómo transformar la voz crítica en una voz aliada</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Identifica el tipo de voz que predomina en ti</h4>
<p style="margin-bottom: 8px;">Durante un día, pon atención a cómo te hablas a ti mism@. ¿Es una voz de apoyo o de juicio?</p>
<p style="margin-bottom: 0;">Escribe las frases más recurrentes que te dices a ti mism@.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Cuestiona su veracidad</h4>
<p style="margin-bottom: 8px;">• ¿De dónde viene esta creencia?</p>
<p style="margin-bottom: 8px;">• ¿Es un pensamiento basado en hechos o en el miedo?</p>
<p style="margin-bottom: 0;">• ¿Le hablaría de la misma manera a un ser querido?</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Redefine tu diálogo interno</h4>
<p style="margin-bottom: 8px;">• Si tu voz interior dice: "No eres lo suficientemente bueno", reformúlala en: "Estoy aprendiendo y mejorando cada día"</p>
<p style="margin-bottom: 0;">• Si te dices: "Siempre fracaso", cambia a: "Cada error me acerca a una nueva oportunidad"</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Crea afirmaciones</h4>
<p style="margin-bottom: 8px;">Escribe frases que refuercen tu confianza y repítelas diariamente.</p>
<p style="margin-bottom: 0;"><strong>Ejemplo:</strong> "Confío en mi capacidad para tomar decisiones".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Rodéate de mensajes positivos</h4>
<p style="margin-bottom: 8px;">• Escucha contenido que refuerce una mentalidad positiva</p>
<p style="margin-bottom: 0;">• Evita entornos donde predomine la crítica constante</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "Ejercicio: La Voz Interior",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Identifica tu Voz Interior</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a identificar tu voz interior.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Rompiendo Barreras</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.2: La Voz Interior</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 4
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
    print(f"✅ {len(cards)} cards créées pour le Thème 1")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU MODULE 4 + THÈME 1")
        print("=" * 70)
        
        # Créer le module
        module = create_module(db)
        
        # Créer le thème 1
        theme1 = Theme(
            title="Rompiendo barreras",
            content="A lo largo de nuestra vida, absorbemos creencias, normas y expectativas que moldean nuestra forma de ver el mundo y de relacionarnos con los demás.",
            order_number=1,
            module_id=module.id
        )
        db.add(theme1)
        db.flush()
        print(f"✅ Thème 1 créé (ID: {theme1.id})")
        
        # Créer les cards du thème 1
        num_cards = create_theme1_cards(db, theme1.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 4 + THÈME 1 CRÉÉS!")
        print("=" * 70)
        print(f"📚 Module 4 ID: {module.id}")
        print(f"📚 Thème 1 ID: {theme1.id} ({num_cards} cards)")
        print(f"\n🎯 Prochain: Créer les Thèmes 2 et 3")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

