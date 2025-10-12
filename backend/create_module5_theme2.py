"""
Script pour créer le Thème 2 du Module 5 COMPLET
Thème 2: Esto ya no me pertenece (2 subtemas)
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
    """Cards du Thème 2: Esto ya no me pertenece"""
    print("\n🎴 Création des cards du Thème 2...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 2",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Esto Ya No Me Pertenece</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Para avanzar con libertad, no basta con saber lo que quieres; también necesitas reconocer lo que ya no tiene lugar en tu vida.</p>

<p style="margin-bottom: 16px;">Hay creencias, historias, miedos y responsabilidades que alguna vez fueron parte de ti, pero que hoy solo ocupan espacio y energía que podrías dedicar a lo que sí te impulsa.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Soltar con Consciencia</h3>
<p style="margin-bottom: 0;">Decir "esto ya no me pertenece" no es huir ni negar lo vivido. Es un acto consciente de soltar aquello que dejó de nutrirte: pensamientos que te frenan, juicios que no son tuyos, e incluso versiones antiguas de ti que ya cumplieron su función.</p>
</div>

<p style="margin-bottom: 16px;">Aquí aprenderás a identificar esas cargas invisibles, agradecer lo que te dejaron y reemplazarlas por un nuevo sistema de creencias y acciones que te sostengan en tu presente.</p>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Identificando mis creencias limitantes
    cards.extend([
        {
            "title": "Subtema 1: Identificando Mis Creencias Limitantes",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Identificando Mis Creencias Limitantes</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Cuando se trata de ir tras nuestros sueños, las creencias limitantes son como filtros invisibles que distorsionan lo que creemos posible.</p>

<p style="margin-bottom: 16px;">No importa cuán preparado estés o cuánta claridad tengas, si dentro de ti existe una idea arraigada que dice "no puedo", "no es para mí" o "es demasiado difícil", tu mente buscará confirmar esa historia y tu cuerpo actuará en consecuencia.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo Que Debes Saber</h3>
<p style="margin-bottom: 0;">En este punto del proceso, ya sabes que una creencia no es una verdad absoluta, sino una interpretación repetida tantas veces que terminó pareciendo real.</p>
</div>

<p style="margin-bottom: 16px;">Aquí el enfoque es ir más allá de las creencias generales y detectar aquellas específicas que bloquean tus metas y anhelos actuales.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Identificando Creencias Limitantes - Claves",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Claves para identificar creencias limitantes sobre tus sueños</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Escucha tus frases automáticas cuando piensas en tu meta</h4>
<p style="margin-bottom: 0;">Observa qué te dices sin filtrar: "No es el momento", "Necesito más experiencia", "Es muy arriesgado". Estas frases suelen aparecer antes incluso de dar el primer paso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Ubica la emoción que aparece</h4>
<p style="margin-bottom: 0;">Las creencias limitantes no solo viven en tu mente, también en tu cuerpo. Si al pensar en tu sueño sientes miedo, ansiedad o resignación, probablemente hay una creencia sosteniendo esa emoción.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Detecta de dónde viene la voz</h4>
<p style="margin-bottom: 0;">Pregúntate: ¿Esto lo aprendí por experiencia propia o es una idea heredada de mi familia, cultura o entorno? Muchas veces cargamos con límites que ni siquiera nos pertenecen.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Identifica el patrón de repetición</h4>
<p style="margin-bottom: 0;">Si una idea se presenta cada vez que quieres avanzar (ej. "no soy lo suficientemente buena"), esa es una señal clara de que está funcionando como freno interno.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Pon atención a las justificaciones "lógicas"</h4>
<p style="margin-bottom: 0;">Algunas creencias se disfrazan de sentido común: "No tengo tiempo", "Primero necesito X para empezar". Aunque parezcan razonables, si siempre aparecen antes de actuar, están funcionando como excusa.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Identificando Creencias Limitantes - Mensaje Clave",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Mensaje clave:</h2>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 16px; font-size: 1.1em;">En este momento del proceso, tu tarea no es luchar contra estas creencias, sino reconocerlas con precisión.</p>
<p style="margin-bottom: 0; font-size: 1.15em; font-weight: 600;">Porque lo que puedes ver, puedes transformar. Nombrarlas es el primer paso para quitarles el poder y abrir espacio a un nuevo sistema de creencias que respalde la vida que quieres crear.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Identificando Creencias Limitantes",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Identifica las Creencias que Limitan tus Anhelos</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a identificar las creencias que limitan tus anhelos.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Esto Ya No Me Pertenece</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.1: Identificando mis creencias limitantes</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # SUBTEMA 2: Mi nuevo mindset
    cards.extend([
        {
            "title": "Subtema 2: Mi Nuevo Mindset",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Mi Nuevo Mindset</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Una vez que identificas lo que te ha frenado, el siguiente paso es elegir conscientemente con qué mentalidad vas a avanzar.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">¿Qué es un Nuevo Mindset?</h3>
<p style="margin-bottom: 0;">Un nuevo mindset no es simplemente "pensar positivo" ni repetirte frases motivadoras, sino crear un sistema de creencias, pensamientos y hábitos que respalden tus objetivos y sueños.</p>
</div>

<p style="margin-bottom: 16px;">Aquí no se trata de borrar el pasado, sino de reemplazar las narrativas antiguas por otras más funcionales y alineadas con la persona que eres hoy.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Mindset como Software</h3>
<p style="margin-bottom: 0;">El mindset actúa como el software que dirige tus decisiones: si sigue programado con miedo, duda o escasez, tus acciones estarán limitadas; pero si lo programas con confianza, apertura y compromiso, tus decisiones se vuelven coherentes con la vida que quieres construir.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Mi Nuevo Mindset - Claves",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Claves para construir tu nuevo mindset</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Haz que tu mente trabaje a tu favor</h4>
<p style="margin-bottom: 0;">Entrena tu atención para enfocarte en lo que sí puedes controlar y en las oportunidades que surgen, en lugar de quedarte atrapado en lo que falta o lo que podría salir mal.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Reemplaza el "todo o nada" por el "progreso constante"</h4>
<p style="margin-bottom: 0;">Un nuevo mindset entiende que los grandes cambios son la suma de pequeñas acciones sostenidas. Avanzar imperfecto sigue siendo avanzar.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Integra creencias expansivas y realistas</h4>
<p style="margin-bottom: 0;">No basta con soñar en grande, también necesitas creencias que te impulsen a actuar: "Puedo aprender lo que me falta", "Cada paso cuenta", "Merezco lo que deseo". (recuerda como TREC es la herramienta por excelencia para identificar, cambiar y sostener creencias saludables.)</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Reprograma tus reacciones emocionales</h4>
<p style="margin-bottom: 0;">Un nuevo mindset no elimina los miedos, pero te entrena para que no sean ellos quienes decidan por ti. Puedes sentir temor y aún así seguir adelante.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Vincula tu mentalidad a tu propósito</h4>
<p style="margin-bottom: 0;">Tus nuevos pensamientos deben recordarte constantemente por qué empezaste. Esto mantiene tu energía estable incluso cuando enfrentas obstáculos.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Mi Nuevo Mindset - Mensaje Clave",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Mensaje clave:</h2>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 0; font-size: 1.1em; line-height: 1.8;">Tu nuevo mindset no es una máscara, es una elección consciente y sostenida. Es decidir, día tras día, alimentar pensamientos que te acerquen a tus metas y dejar de dar espacio a los que te devuelven al lugar del que ya decidiste salir.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Mi Nuevo Mindset",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Crea tu Nuevo Mindset</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a crear tu nuevo mindset.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Esto Ya No Me Pertenece</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.2: Mi nuevo mindset</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # Conclusion du Thème 2
    cards.append({
        "title": "Conclusión del Tema 2",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 2</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">En este punto, has hecho algo que muchas personas evitan: mirar de frente aquello que te ha limitado y reconocer que ya no es parte de quien decides ser.</p>

<p style="margin-bottom: 16px;">Has identificado las creencias que frenaban tus sueños y las has reemplazado por una mentalidad más coherente con la vida que quieres construir.</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px; font-weight: 600; color: {C_ACCENT};">Soltar no siempre significa olvidar; muchas de esas creencias nacieron para protegerte en momentos en los que lo necesitabas.</p>
<p style="margin-bottom: 0;">Pero hoy sabes que seguir cargándolas solo te mantiene en un lugar donde ya no encajas. Tu nuevo mindset no es una promesa vacía: es una herramienta que has creado tú, desde tu verdad, para sostenerte en cada paso que viene.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">A Partir de Aquí</h3>
<p style="margin-bottom: 0;">A partir de aquí, no se trata de no volver a sentir miedo o duda, sino de no dejar que ellos conduzcan tu camino. Ahora tienes la capacidad de elegir tus pensamientos, dirigir tu energía y actuar desde un lugar más libre y seguro. Lo que ayer te frenaba, hoy ya no te pertenece.</p>
</div>
</div>""",
        "card_type": "conclusion",
        "order_number": order
    })
    
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
        print("🚀 CRÉATION DU THÈME 2 - MODULE 5")
        print("=" * 70)
        
        MODULE_ID = 5
        
        # Créer le thème 2
        theme2 = Theme(
            title="Esto ya no me pertenece",
            content="Para avanzar con libertad, necesitas reconocer lo que ya no tiene lugar en tu vida. Aquí aprenderás a identificar esas cargas invisibles, agradecer lo que te dejaron y reemplazarlas por un nuevo sistema de creencias.",
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
        print(f"\n🎯 Prochain: Thème 3 (dernier thème)")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

