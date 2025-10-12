"""
Script pour créer le Thème 3 du Module 4 - DERNIER THÈME
Thème 3: Mapa de acción hacia la autenticidad
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
    """Cards du Thème 3: Mapa de acción hacia la autenticidad"""
    print("\n🎴 Création des cards du Thème 3...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 3",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Mapa de Acción hacia la Autenticidad</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Ser auténtico es uno de los mayores actos de valentía que podemos hacer en nuestra vida. No porque sea difícil en sí mismo, sino porque desde pequeños hemos aprendido a adaptarnos para ser aceptados.</p>

<p style="margin-bottom: 16px;">Nos enseñaron a encajar, a no hacer demasiado ruido, a seguir ciertas reglas sociales sin cuestionarlas.</p>

<div style="background: {C_ACCENT}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.3em;">Pero, ¿qué pasa cuando lo que la sociedad espera de ti no encaja con quién realmente eres?</h3>
</div>

<p style="margin-bottom: 16px;">Aquí es donde surge el conflicto: queremos ser fieles a nosotros mismos, pero también tememos ser rechazados, juzgados o incomprendidos.</p>

<p style="margin-bottom: 16px;">Entonces, ¿cómo se empieza a vivir con autenticidad?</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Respuesta</h3>
<p style="margin-bottom: 0;">La respuesta no está en hacer cambios radicales de la noche a la mañana, sino en aprender a alinear tus acciones con tu esencia.</p>
</div>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Construir la vida que sí quiero
    cards.extend([
        {
            "title": "Subtema 1: Construir la Vida que Sí Quiero",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Construir la Vida que Sí Quiero</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Muchas veces pensamos que nuestra vida está determinada por las circunstancias, por lo que nos pasó en el pasado, por la familia en la que nacimos o las oportunidades que tuvimos (o no tuvimos).</p>

<p style="margin-bottom: 16px;">Sin embargo, en realidad, nuestra vida se construye día a día, con cada decisión, con cada pequeño paso que tomamos.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo Importante</h3>
<p style="margin-bottom: 0;">Construir la vida que sí queremos no es un acto de suerte ni algo que ocurre de repente. Es un proceso intencional, un camino que requiere claridad, compromiso y acción.</p>
</div>

<p style="margin-bottom: 16px;">No significa que todo saldrá perfecto ni que no habrá obstáculos, sino que, a pesar de ellos, elegimos avanzar hacia algo que realmente nos haga sentido.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Construir la Vida que Sí Quiero - Por Qué No Elegimos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Por qué a veces no elegimos la vida que queremos?</h2>

<p style="margin-bottom: 16px;">Muchas veces vivimos en "piloto automático" atrapados en una rutina que no elegimos del todo.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Esto puede pasar por varias razones:</h3>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;"><strong>🔹 Creencias limitantes</strong> – Pensamos cosas como "no soy suficiente", "es demasiado tarde para cambiar" o "eso no es para mí". Estas ideas nos frenan antes de siquiera intentarlo.</p>
<p style="margin-bottom: 12px;"><strong>🔹 Miedo al cambio</strong> – Aunque no estemos felices con nuestra vida actual, al menos es familiar. A veces nos quedamos donde estamos porque nos da miedo lo desconocido.</p>
<p style="margin-bottom: 12px;"><strong>🔹 Expectativas externas</strong> – La sociedad, la familia y los amigos opinan sobre lo que deberíamos hacer. Muchas veces, tomamos decisiones para complacerlos en lugar de pensar en lo que realmente queremos.</p>
<p style="margin-bottom: 0;"><strong>🔹 Falta de claridad</strong> – Sentimos que algo no está bien en nuestra vida, pero no sabemos exactamente qué cambiar o hacia dónde ir.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Construir la Vida que Sí Quiero - Pequeñas Acciones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Pequeñas acciones, grandes cambios</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">Construir la vida que quieres no significa cambiarlo todo de golpe. No necesitas dejar tu trabajo, mudarte de país o tomar una decisión radical de un día para otro.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Clave</h3>
<p style="margin-bottom: 0;">Los cambios más importantes comienzan con pequeños pasos.</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<p style="margin-bottom: 12px;">🔹 Si quieres más tranquilidad en tu vida, empieza por crear momentos de calma en tu día.</p>
<p style="margin-bottom: 12px;">🔹 Si quieres rodearte de personas más alineadas contigo, empieza a poner límites a quienes te desgastan.</p>
<p style="margin-bottom: 0;">🔹 Si quieres cambiar de trabajo, investiga opciones, actualiza tu CV o toma un curso.</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">No necesitas tenerlo todo claro para empezar. Lo que realmente transforma la vida es la capacidad de dar un paso, luego otro, y otro más.</p>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Construir la Vida que Sí Quiero - Ejemplo",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Ejemplo de un pequeño cambio</h2>

<div style="background: {C_BG_GRAY}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 12px;">Imagina a alguien que ha pasado años en un trabajo que no le gusta, pero que no se atreve a salir porque le da miedo no encontrar algo mejor.</p>

<p style="margin-bottom: 12px;">Un día, en lugar de seguir esperando, decide hacer algo pequeño: inscribirse en un curso, actualizar su currículum o hablar con alguien que trabaja en un área que le interesa.</p>

<p style="margin-bottom: 12px;">Ese paso le da confianza. Poco a poco, empieza a ver nuevas oportunidades.</p>

<p style="margin-bottom: 0;"><strong>Meses después, consigue un trabajo que le apasiona.</strong> No cambió todo en un día, pero comenzó a moverse en la dirección correcta.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 3
        },
        {
            "title": "Construir la Vida que Sí Quiero - Paso de Acción",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Paso de acción</h2>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">💡 La vida que sí quieres no es un sueño imposible.</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Es algo que se construye con cada decisión que tomas.</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">No importa cuánto tiempo hayas pasado en un camino que no te hace feliz. Siempre puedes elegir moverte hacia algo que realmente resuene contigo.</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<h3 style="color: {C_ACCENT}; margin-top: 0; font-size: 1.3em;">No esperes el momento perfecto. Empieza hoy.</h3>
<p style="margin-bottom: 0; font-size: 1.05em;">Un paso, una elección, un cambio a la vez. 💙</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Construir la Vida que Sí Quiero",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Empieza a Construir la Vida que Sí Quieres</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a construir la vida que si quieres.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Mapa de Acción</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Realidad</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        }
    ])
    order += 6
    
    # Conclusion du module
    cards.append({
        "title": "¡Felicidades por completar el Módulo 4!",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2.2em; margin-bottom: 20px; text-align: center;">¡Felicidades por completar el Módulo 4!</h1>

<div style="background: linear-gradient(135deg, {C_TITLE} 0%, {C_ACCENT} 100%); color: white; padding: 32px; border-radius: 15px; margin: 32px 0; text-align: center;">
<h2 style="margin-top: 0; color: white; font-size: 1.8em;">🎉 ¡Lo lograste!</h2>
<p style="font-size: 1.15em; margin-bottom: 0; line-height: 1.7;">Has completado un viaje profundo de transformación, rompiendo barreras, despertando a tu ser auténtico y creando un mapa de acción hacia la vida que realmente deseas vivir.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 32px; margin-bottom: 16px; font-size: 1.5em;">Lo Que Has Logrado:</h3>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px;">✅ <strong>Rompiste barreras mentales</strong> al cuestionar los acuerdos limitantes y transformar tu voz interior</p>
<p style="margin-bottom: 16px;">✅ <strong>Despertaste a tu verdadero ser</strong> al reconectar con tu autenticidad, cultivar la autoconciencia y abrazar tu vulnerabilidad</p>
<p style="margin-bottom: 0;">✅ <strong>Creaste un mapa de acción</strong> para construir la vida que realmente quieres, paso a paso</p>
</div>

<div style="background: {C_ACCENT}; color: white; padding: 28px; border-radius: 10px; margin: 32px 0;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Recuerda</h3>
<p style="margin-bottom: 0; font-size: 1.05em; line-height: 1.8;">Este no es el final, es el comienzo de una vida más auténtica y alineada con quien realmente eres. Cada día es una nueva oportunidad para elegir ser tú, sin máscaras, sin expectativas ajenas. Confía en tu proceso y sigue avanzando con valentía.</p>
</div>

<p style="text-align: center; font-size: 1.2em; color: {C_TITLE}; margin-top: 32px; font-weight: 600;">🌟 ¡Sigue brillando con tu luz única! 🌟</p>
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
    print(f"✅ {len(cards)} cards créées pour le Thème 3")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 3 - MODULE 4 (DERNIER THÈME)")
        print("=" * 70)
        
        MODULE_ID = 4
        
        # Créer le thème 3
        theme3 = Theme(
            title="Mapa de acción hacia la autenticidad",
            content="Ser auténtico es uno de los mayores actos de valentía que podemos hacer en nuestra vida. La respuesta no está en hacer cambios radicales de la noche a la mañana, sino en aprender a alinear tus acciones con tu esencia.",
            order_number=3,
            module_id=MODULE_ID
        )
        db.add(theme3)
        db.flush()
        print(f"✅ Thème 3 créé (ID: {theme3.id})")
        
        # Créer les cards du thème 3
        num_cards = create_theme3_cards(db, theme3.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 4 COMPLÈTEMENT TERMINÉ!")
        print("=" * 70)
        print(f"📚 Thème 3 ID: {theme3.id} ({num_cards} cards)")
        print(f"\n🎉 RÉCAPITULATIF MODULE 4:")
        print(f"   • Thème 1: Rompiendo barreras (13 cards)")
        print(f"   • Thème 2: Despertar auténtico (12 cards)")
        print(f"   • Thème 3: Mapa de acción hacia la autenticidad ({num_cards} cards)")
        print(f"\n✨ Total: {13 + 12 + num_cards} cards pour le Module 4!")
        print(f"\n🏆 TOUS LES 4 MODULES SONT MAINTENANT COMPLETS!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

