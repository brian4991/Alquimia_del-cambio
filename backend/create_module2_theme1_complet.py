"""
Script pour créer le Module 2 avec le Thème 1 COMPLET - fidèle au texte original
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

def create_module2(db: Session):
    """Créer le module 2"""
    print("\n📦 Création du Module 2...")
    module = Module(
        title="Celebra tu ser",
        description="Aprende a valorar profundamente todo lo que eres, más allá de tus logros.",
        objective="El propósito de este módulo es que logres ir más allá de la autoexigencia para valorar de manera profunda todo lo que eres, y reconocer el valor detrás de tus experiencias de logro y aprendizaje.",
        belief_to_transform="Solo valgo por lo que hago o logro; mis imperfecciones me restan valor.",
        expected_results="Te liberas del exceso de autoexigencia y crítica personal. Aprendes a valorarte y amarte sin codependencias, reconociendo todo lo que ya eres y has logrado.",
        recommended_book="El poder del espejo de Louis Hay (lo encuentras en la carpeta de Bonus)",
        audio_file=None,
        order_number=2,
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module créé (ID: {module.id})")
    return module

def create_theme1(db: Session, module_id: int):
    """Thème 1: Reconociendo tu valor interno"""
    print("\n📚 Création du Thème 1...")
    theme = Theme(
        title="Reconociendo tu valor interno",
        content="Este tema está diseñado para guiarte hacia una comprensión más profunda de quién eres y por qué eres valioso, independientemente de tus logros o resultados.",
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
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Reconociendo tu Valor Interno</h1>

<p style="margin-bottom: 16px;">Este tema está diseñado para guiarte hacia una comprensión más profunda de <strong>quién eres</strong> y <strong>por qué eres valioso</strong>, independientemente de tus logros o resultados.</p>

<p style="margin-bottom: 16px;">Muchas veces, la sociedad nos enseña a medir nuestro valor por lo que hacemos, pero aquí aprenderás a enfocarte en lo que eres y a cultivar una relación más compasiva contigo mismo.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: Identificación de Fortalezas - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Identificación de Fortalezas</h1>

<p style="margin-bottom: 16px;">Reconocer tu valor interno es un proceso de mirar más allá de lo que haces o logras para conectar con quién eres en esencia.</p>

<p style="margin-bottom: 16px;">Desde la psicología, sabemos que gran parte de nuestra autoestima está influida por creencias aprendidas a lo largo de nuestra vida: mensajes que recibimos sobre lo que "deberíamos" ser o hacer para sentirnos valiosos.</p>

<p style="margin-bottom: 16px;">Sin embargo, el valor personal no depende de cumplir expectativas externas; surge de reconocer tus cualidades, fortalezas y singularidad como ser humano.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">¿Qué es el Valor Interno?</h3>
<p style="margin-bottom: 0;">Cuando hablamos de valor interno, nos referimos a esa parte de ti que no cambia con los errores, los éxitos o las opiniones de los demás. Es el núcleo de tu identidad, el lugar donde residen tus capacidades, tus intenciones y tu potencial.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "Identificación de Fortalezas - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Las Fortalezas Personales</h2>

<p style="margin-bottom: 16px;">Las fortalezas personales son esas cualidades intrínsecas que te permiten superar obstáculos, crear relaciones significativas y aportar al mundo de manera única.</p>

<p style="margin-bottom: 16px;">Pero aquí hay algo crucial: no siempre somos conscientes de ellas. Muchas veces, pasamos tanto tiempo enfocándonos en nuestras debilidades o errores que dejamos de ver las cualidades que ya poseemos.</p>

<p style="margin-bottom: 16px;">Reconocer tus fortalezas implica salir de un enfoque de "déficit" (donde buscas lo que falta) y entrar en un enfoque de "reconocimiento" (donde valoras lo que ya está).</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Poder del Cambio</h3>
<p style="margin-bottom: 0;">Este cambio es poderoso porque activa en el cerebro un estado de gratitud y confianza, lo que fortalece nuestra capacidad de enfrentar desafíos.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        
        {
            "title": "Tres Acciones que Limitan tus Fortalezas",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Tres Acciones que Limitan Nuestra Capacidad</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">1. Creencias limitantes</h3>
<p style="margin-bottom: 0;">Las creencias internas negativas, como "no soy lo suficientemente bueno" o "no merezco el éxito". Estas creencias nos hacen dudar de nuestra capacidad y nos impiden aprovechar todo nuestro potencial.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">2. Perfeccionismo</h3>
<p style="margin-bottom: 0;">El deseo de hacer las cosas "perfectas" puede ser un obstáculo. Nos centramos tanto en evitar fallos que terminamos bloqueándonos o procrastinando.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">3. Comparación constante con los demás</h3>
<p style="margin-bottom: 0;">Compararse continuamente con los demás puede desvalorizarnos. Al centrarnos en lo que otros tienen o hacen, perdemos de vista nuestras propias fortalezas y nos sentimos incapaces de destacar.</p>
</div>

<p style="margin-bottom: 16px; margin-top: 24px;">A veces, las limitaciones que sentimos no provienen de una falta de capacidad, sino de cómo hemos aprendido a vernos a nosotros mismos a lo largo del tiempo. Al reconocer estas creencias limitantes, podemos empezar a liberar todo nuestro potencial y actuar con confianza en nuestras verdaderas fortalezas.</p>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        
        {
            "title": "Ejercicio: Identificación de Fortalezas",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Reconoce tu Valor</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu valor.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Mi valor</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.1: Identificación de fortalezas</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 5
        },
        
        {
            "title": "Subtema 2: Una Mirada al Interior - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Una Mirada al Interior</h1>

<p style="margin-bottom: 16px;">Imagina que cada experiencia que has vivido es como una capa sobre tu ser interior. Con el tiempo, esas capas se acumulan, formando una especie de "coraza" que a veces nos impide ver quiénes somos realmente en el fondo.</p>

<p style="margin-bottom: 16px;">Estas capas no son malas; son parte de lo que nos ha formado, pero muchas veces nos desconectan de nuestra esencia y nos dificultan reconocer nuestras verdaderas fortalezas.</p>

<p style="margin-bottom: 16px;">El primer paso es empezar a mirar hacia adentro con honestidad, sin juzgar lo que encontramos. Es como cuando revisamos el interior de un armario desordenado. Al principio, puede ser incómodo ver todo lo que hemos guardado allí: miedos, inseguridades, creencias limitantes.</p>

<p style="margin-bottom: 16px;">Pero solo cuando decidimos abrir esa puerta y mirar, podemos empezar a entender qué hay dentro y cómo eso influye en nuestra forma de vernos a nosotros mismos.</p>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        
        {
            "title": "Una Mirada al Interior - Parte 2: ¿Cómo Hacerlo?",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo Hacerlo?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Observa sin juzgar</h3>
<p style="margin-bottom: 0;">Tómate un momento para ser consciente de lo que sientes y piensas, sin intentar cambiarlo inmediatamente. Pregúntate: ¿qué pensamientos aparecen cuando me pienso a mí mismo? A menudo, lo que encontramos no es la verdad absoluta, sino una interpretación de experiencias pasadas que han quedado grabadas en nuestra mente.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Diferencia entre lo que eres y lo que sientes que eres</h3>
<p style="margin-bottom: 0;">Un concepto clave en psicología es entender que nuestras emociones no siempre reflejan la realidad. Lo que sentimos, por ejemplo, cuando nos criticamos, no siempre es lo que realmente somos. Si te sientes insuficiente, eso no significa que seas insuficiente. Es una emoción que puede estar influenciada por experiencias pasadas, no por tus capacidades actuales.</p>
</div>

<p style="margin-bottom: 16px; margin-top: 24px;">Al aprender a mirar al interior de manera objetiva y compasiva, podemos comenzar a ver nuestras fortalezas de una manera más clara y libre de las influencias del pasado. Cuando empezamos a reconocernos sin las capas de juicio, podemos ver que esas fortalezas siempre han estado allí, solo que a veces estaban cubiertas por la crítica y el perfeccionismo.</p>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        
        {
            "title": "Ejercicio: Una Mirada al Interior",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Observa sin Juzgar</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu valor.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Mi valor</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.2: Una mirada al interior</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 8
        },
        
        {
            "title": "Subtema 3: Aceptación y Compasión - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Aceptación y Compasión</h1>

<p style="margin-bottom: 16px;">Piensa por un momento en tu amiga más cercana. Esta amiga, en muchas ocasiones, se siente insegura o insuficiente, se critica por sus errores y tiene dificultades para reconocer sus logros.</p>

<p style="margin-bottom: 16px;">Si ella te pidiera consejo, ¿la rechazarías por sentirse así? ¿O la abrazarías con comprensión, recordándole lo valiosa que es a pesar de sus dudas?</p>

<p style="margin-bottom: 16px;">La mayoría de nosotros respondería con compasión, sin juzgarla. Sin embargo, cuando se trata de nosotros mismos, solemos ser mucho más duros y exigentes.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Los Cimientos</h3>
<p style="margin-bottom: 0;">La aceptación y la compasión son los cimientos para empezar a valorarnos de una manera profunda. Aceptarnos no significa conformarnos, sino reconocer quiénes somos, con nuestras fortalezas y debilidades, y tratarnos con la misma amabilidad que ofreceríamos a un ser querido.</p>
</div>

<p style="margin-bottom: 16px;">A través de esta aceptación, podemos permitirnos ser humanos, con la seguridad de que nuestros errores no nos definen, pero nuestras capacidades y nuestra esencia sí.</p>
</div>""",
            "card_type": "theory",
            "order_number": 9
        },
        
        {
            "title": "Aceptación y Compasión - Parte 2: ¿Por Qué son Clave?",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Por Qué la Aceptación y Compasión son Clave?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Aceptar no significa rendirse</h3>
<p style="margin-bottom: 0;">Aceptar no significa rendirse ante nuestras limitaciones, sino más bien reconocer nuestras áreas de crecimiento y tener la disposición de trabajarlas. Es como mirar un mapa: sabemos dónde estamos, qué caminos podemos tomar y qué nos falta por recorrer, pero sin juzgar nuestra posición actual. Cuando nos aceptamos, podemos empezar a entender nuestras fortalezas reales, porque dejamos de compararnos con los demás y dejamos de buscar una perfección inalcanzable.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">La compasión es el ingrediente</h3>
<p style="margin-bottom: 0;">La compasión es el ingrediente que nos permite acercarnos a nosotros mismos con amabilidad, sobre todo cuando cometemos errores. Nos ayuda a recordar que ser humano implica equivocarse, y no por ello dejamos de ser valiosos o capaces. Al ser compasivos con nosotros mismos, podemos reconocer nuestras debilidades sin caer en la autocrítica destructiva.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 10
        },
        
        {
            "title": "Aceptación y Compasión - Parte 3: Cómo Practicar",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo Practicar la Aceptación y la Compasión?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">1. Diálogo interno saludable</h3>
<p style="margin-bottom: 0;">Cuando te enfrentes a un reto o una dificultad, observa tu voz interna. ¿Es amable o crítica? Si es negativa, intenta transformarla en algo más comprensivo. En lugar de pensar "No soy capaz de hacer esto", puedes pensar "Estoy aprendiendo y puedo intentar de nuevo". Este cambio en la forma de pensar no se trata de ignorar la realidad, sino de ser más amable y realista con nosotros mismos.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">2. La importancia de la autocompasión</h3>
<p style="margin-bottom: 0;">Un ejercicio muy útil es practicar la autocompasión a través de la meditación o la escritura. Por ejemplo, cuando sientas frustración o miedo por no estar a la altura, toma unos minutos para escribir una carta a ti mismo/a, como si fueras tu propio mejor amigo. Reconoce tus esfuerzos, valida tus sentimientos y recuerda que está bien no ser perfecto.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">3. Haz las paces con la imperfección</h3>
<p style="margin-bottom: 0;">Aceptar y practicar la compasión también implica abrazar la imperfección. Todos tenemos áreas en las que podemos mejorar, pero esto no significa que no seamos valiosos ahora mismo. Cuando reconocemos nuestras debilidades sin rechazo, podemos aprender de ellas de una manera más eficaz, en lugar de temerles.</p>
</div>

<p style="margin-bottom: 16px; margin-top: 24px;">Al aprender a mirar al interior de manera objetiva y compasiva, podemos comenzar a ver nuestras fortalezas de una manera más clara y libre de las influencias del pasado. Cuando empezamos a reconocernos sin las capas de juicio, podemos ver que esas fortalezas siempre han estado allí, solo que a veces estaban cubiertas por la crítica y el perfeccionismo.</p>
</div>""",
            "card_type": "practical",
            "order_number": 11
        },
        
        {
            "title": "Ejercicio: Aceptación y Compasión",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cultiva la Compasión</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu valor.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Mi valor</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.3: Aceptación y compasión</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 12
        },
        
        {
            "title": "Conclusión del Tema 1",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 1</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">Este tema es la base para desarrollar una <strong>conexión más profunda contigo mismo</strong>.</p>

<p style="margin-bottom: 16px;">Al identificar tus fortalezas, comienzas a reconocer tus capacidades innatas y lo que te hace único, mientras que mirar al interior te permite comprender las influencias pasadas que han formado tu forma de pensar y sentir.</p>

<p style="margin-bottom: 16px;">La aceptación y compasión son esenciales para aceptar tanto tus logros como tus imperfecciones sin juicio.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<p style="margin: 0;">Este proceso de autoconocimiento te brinda la oportunidad de abrazar tu valor interno, facilitando decisiones más conscientes y un crecimiento personal más auténtico y empoderado.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Siguiente Paso</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Continúa al Tema 2: Transformando la autoexigencia y perfeccionismo</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 13
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
        print("🚀 CRÉATION DU MODULE 2: THÈME 1 COMPLET")
        print("=" * 70)
        
        # Créer le module
        module = create_module2(db)
        
        # Créer le thème 1
        theme1 = create_theme1(db, module.id)
        num_cards1 = create_theme1_cards(db, theme1.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 2 THÈME 1 CRÉÉ")
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

