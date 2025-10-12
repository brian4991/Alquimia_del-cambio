"""
Script pour créer le Thème 3 du Module 5 - DERNIER THÈME
Thème 3: Energía en movimiento (3 subtemas)
FIDÉLITÉ 100% AU TEXTE
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

def create_theme3_cards(db: Session, theme_id: int):
    """Cards du Thème 3: Energía en movimiento"""
    print("\n🎴 Création des cards du Thème 3...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 3",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Energía en Movimiento</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Llegados a este punto, ya no se trata solo de saber qué quieres o de sentirte preparado para lograrlo. La verdadera transformación ocurre cuando toda esa claridad, tus nuevas creencias y tu propósito se convierten en movimiento.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¿Qué es la Energía en Movimiento?</h3>
<p style="margin-bottom: 0;">La energía en movimiento es acción con sentido. Es decidir cada día que lo que has aprendido no se quedará como una reflexión bonita o una idea motivadora, sino que será parte de tu forma de vivir.</p>
</div>

<p style="margin-bottom: 16px;">Cuando la energía se estanca, incluso las mejores intenciones pierden fuerza; pero cuando se canaliza hacia acciones concretas, se convierte en impulso y en resultados tangibles.</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px; font-weight: 600; color: {C_ACCENT};">Este es el momento en el que pasas de planear a ejecutar, de imaginar a experimentar, de querer a crear.</p>
<p style="margin-bottom: 0;">No hablamos de hacer por hacer, sino de elegir acciones que estén alineadas con tu visión y que puedas sostener en el tiempo. Es poner tu cuerpo, tu mente y tu corazón en dirección a lo que deseas, aunque no tengas todas las respuestas, aunque todavía haya miedo.</p>
</div>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 0; font-size: 1.15em; font-weight: 600;">La libertad no llega esperando el momento perfecto, sino moviéndote desde donde estás, con lo que tienes, hacia lo que sueñas.</p>
</div>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Plan de acción
    cards.extend([
        {
            "title": "Subtema 1: Plan de Acción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Plan de Acción</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Un plan de acción es la hoja de ruta que convierte tus ideas y objetivos en pasos concretos. No es una lista infinita de tareas, sino un mapa claro que te dice qué hacer, cuándo y cómo, de manera que puedas sostener el avance sin perder energía ni motivación.</p>

<p style="margin-bottom: 16px;">En este punto de tu proceso, ya tienes claridad sobre lo que quieres, has soltado creencias que te limitaban y has creado un nuevo mindset que te impulsa.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Lo Que Necesitas Ahora</h3>
<p style="margin-bottom: 0;">Ahora, lo que necesitas es organizar esa motivación en acciones estratégicas que te lleven de tu presente a tu objetivo.</p>
</div>

<p style="margin-bottom: 16px;">El error más común al crear un plan de acción es intentar abarcar demasiado o plantear pasos poco realistas para tu momento actual. Esto solo lleva a la frustración.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Cómo Funciona el Cerebro</h3>
<p style="margin-bottom: 0;">Nuestro cerebro funciona mejor cuando percibe que el objetivo es alcanzable: cada vez que completas una acción clara y posible, tu cerebro libera dopamina, el neurotransmisor de la motivación, lo que refuerza el deseo de seguir avanzando. Si el plan es irreal, el cerebro anticipa fracaso y reduce la energía y el compromiso.</p>
</div>

<p style="margin-bottom: 16px;">Por eso, un buen plan de acción parte de dos principios: <strong>simplicidad</strong> y <strong>coherencia</strong>. No se trata de correr más rápido, sino de construir un camino que tu mente y tu cuerpo puedan sostener con constancia.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Plan de Acción - Cómo Construir",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cómo construir tu plan de acción</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Empieza por el objetivo final</h4>
<p style="margin-bottom: 0;">Define con claridad qué quieres lograr y en qué plazo. Cuanto más específico, más fácil será trazar el camino.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Divide en etapas intermedias</h4>
<p style="margin-bottom: 0;">No intentes saltar de tu punto actual al resultado final de un solo paso. Divide el camino en fases que te permitan medir tu progreso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Asigna acciones concretas a cada etapa</h4>
<p style="margin-bottom: 0;">Cada acción debe ser clara y medible. En lugar de "mejorar mi salud", define "caminar 30 minutos 4 veces por semana" o "incorporar 2 raciones de verduras al día".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Pon fechas y orden</h4>
<p style="margin-bottom: 0;">El tiempo crea compromiso. Asigna un plazo realista a cada acción y ordénalas de forma lógica para que cada paso te acerque al siguiente.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Ajusta y revisa constantemente</h4>
<p style="margin-bottom: 0;">Un plan de acción no es rígido. Si algo no funciona, cámbialo. Lo importante es que el plan te sirva a ti, no que tú te adaptes a un plan imposible.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Plan de Acción - Mensaje Clave",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Mensaje clave:</h2>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 16px; font-size: 1.1em;">Un plan de acción es el puente entre lo que sueñas y lo que vives.</p>
<p style="margin-bottom: 0; font-size: 1.05em; line-height: 1.8;">Cuando es realista y sostenible, tu cerebro lo percibe como posible, refuerza tu motivación y te permite avanzar con constancia. No se trata de hacer más cosas, sino de hacer lo que realmente importa, de forma ordenada y sostenible, para que tus objetivos dejen de ser una idea y se conviertan en tu nueva realidad.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Plan de Acción",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Crea tu Propio Plan de Acción</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a crear tu propio plan de acción.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Energía en Movimiento</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Momento de accionar y Ejercicio 3.1: Plan de acción</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # SUBTEMA 2: Diseño de productividad - JE CONTINUE DANS LA SUITE CAR C'EST TROP LONG
    
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
    print(f"✅ {len(cards)} cards créées pour le Thème 3 (partie 1/2)")
    return len(cards), order  # Retourne aussi l'ordre pour continuer

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 3 PARTIE 1 - MODULE 5")
        print("=" * 70)
        
        MODULE_ID = 5
        
        # Créer le thème 3
        theme3 = Theme(
            title="Energía en movimiento",
            content="La verdadera transformación ocurre cuando toda esa claridad, tus nuevas creencias y tu propósito se convierten en movimiento. Es acción con sentido.",
            order_number=3,
            module_id=MODULE_ID
        )
        db.add(theme3)
        db.flush()
        print(f"✅ Thème 3 créé (ID: {theme3.id})")
        
        # Créer les cards du thème 3 (partie 1)
        num_cards, _ = create_theme3_cards(db, theme3.id)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 3 PARTIE 1 CRÉÉE!")
        print("=" * 70)
        print(f"📚 Thème 3 ID: {theme3.id} ({num_cards} cards)")
        print(f"\n⚠️  Manque encore 2 subtemas (Diseño de productividad + El maestro del equilibrio)")
        print("🎯 Je crée maintenant la partie 2")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

