"""
Script pour créer le Module 5 + Thème 1 COMPLET
Module 5: Libertad en Acción
Thème 1: Claridad y sentido (2 subtemas)
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
    """Créer le Module 5"""
    print("\n📚 Création du Module 5...")
    module = Module(
        title="Libertad en Acción",
        description="Si puedo empezar, solo necesito dar el siguiente paso para llegar al otro lado de la vida que anhelo",
        objective="El propósito de este módulo es ayudarte a fortalecer tu confianza interna y obtener claridad sobre tus próximos pasos, para que puedas avanzar con seguridad hacia la vida que deseas crear.",
        belief_to_transform="Si no lo hago perfecto, mejor no empiezo",
        expected_results="* Regulas el exceso de duda, y te permites ser una persona que acciona y avanza con lo que quiere\n* Determinas los siguientes pasos que te acercan a la vida que deseas crear (tus anhelos)",
        recommended_book="El hombre en busca del sentido: Viktor Frankl (lo encuentras en la carpeta de Bonus)",
        audio_file=None,
        order_number=5,
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module 5 créé (ID: {module.id})")
    return module

def create_theme1_cards(db: Session, theme_id: int):
    """Cards du Thème 1: Claridad y sentido"""
    print("\n🎴 Création des cards du Thème 1...")
    
    cards = []
    order = 1
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 1",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Claridad y Sentido</h1>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin: 0; font-size: 1.1em; font-style: italic;">"Cuando no sabes hacia dónde vas, cualquier camino parece confuso. Pero cuando conectas con tu verdad interna, cada paso empieza a tener sentido."</p>
</div>

<p style="margin-bottom: 16px; font-size: 1.05em;">La claridad es la luz que guía el camino en medio del caos. En momentos de cambio, dolor o confusión, lo primero que suele apagarse es el sentido: ese hilo invisible que une tus decisiones, emociones y acciones hacia una dirección que resuena con quien eres de verdad.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Propósito de Este Módulo</h3>
<p style="margin-bottom: 0;">Este módulo no busca que tomes decisiones perfectas, sino ayudarte a recordar qué es importante para ti, qué anhelas realmente, y cómo dar los primeros pasos hacia allí.</p>
</div>

<p style="margin-bottom: 16px;">Porque cuando el sentido está presente, la acción fluye con más calma y propósito.</p>
</div>""",
        "card_type": "intro",
        "order_number": order
    })
    order += 1
    
    # SUBTEMA 1: Construcción de metas claras
    cards.extend([
        {
            "title": "Subtema 1: Construcción de Metas Claras - Introducción",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Construcción de Metas Claras</h1>

<p style="margin-bottom: 16px;">Cuando atravesamos procesos de cambio, dolor o incertidumbre, es común sentirnos perdidos. No porque no sepamos hacer cosas o porque no seamos capaces, sino porque perdemos de vista el <strong>para qué</strong>.</p>

<p style="margin-bottom: 16px;">Sentimos que estamos haciendo, pero no sabemos si lo que hacemos tiene dirección. O peor: creemos que deberíamos tener metas… pero no logramos conectar con ninguna.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Lo Importante</h3>
<p style="margin-bottom: 0;">Y es que la claridad no es solo una decisión mental. Es un estado emocional y profundo en el que lo que deseas, lo que valoras y lo que eliges se alinean en una misma dirección.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Construcción de Metas Claras - Qué Significa",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué significa tener una meta clara?</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">Una meta clara es mucho más que un objetivo escrito. Es una expresión de sentido, es un deseo consciente que nace desde adentro, no desde lo que el entorno espera de ti.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Muchas veces confundimos metas con mandatos:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin: 20px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">• "Debería ser más productiva@"</p>
<p style="margin-bottom: 12px;">• "Tengo que encontrar pareja"</p>
<p style="margin-bottom: 0;">• "Necesito tener éxito ya"</p>
</div>

<p style="margin-bottom: 16px;">Pero estos "deberías" suelen estar cargados de presión, comparación y miedo.</p>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin: 20px 0; border-radius: 5px;">
<p style="margin-bottom: 0;">Una meta clara en cambio, nace de la conexión contigo misma (o): es una traducción de tus valores, necesidades y anhelos reales, no de lo que aprendiste que "toca hacer".</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-size: 1.05em;">Tener una meta clara no se trata de apurarte, sino de honrar tu ritmo y elegir con conciencia hacia dónde quieres dirigir tu energía vital.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "Construcción de Metas Claras - Por Qué Cuesta",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Por qué cuesta tanto definir metas?</h2>

<p style="margin-bottom: 16px;">Porque para tener claridad, necesitas primero:</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• Silenciar el ruido de las expectativas externas</p>
<p style="margin-bottom: 12px;">• Reconectar con lo que realmente importa para ti</p>
<p style="margin-bottom: 12px;">• Permitir lo que sientes, incluso si es confuso</p>
<p style="margin-bottom: 0;">• Soltar la fantasía de tener todo claro antes de empezar</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">También es común que no nos permitamos tener metas porque sentimos que:</h3>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin: 20px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">• "No me lo merezco todavía"</p>
<p style="margin-bottom: 12px;">• "No sé por dónde empezar"</p>
<p style="margin-bottom: 12px;">• "Tengo miedo de fracasar o decepcionarme"</p>
<p style="margin-bottom: 0;">• "Tengo miedo al éxito"</p>
</div>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-weight: 600; color: {C_ACCENT};">Pero no tener metas claras no significa que no tengas deseos, significa que no te has dado el espacio, la guía o la compasión para escuchar y ordenar lo que hay dentro de ti.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "Construcción de Metas Claras - Diferencia",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué diferencia a una meta auténtica de una meta impuesta?</h2>

<div style="background: #fff5f5; border-left: 5px solid #d9534f; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<h3 style="color: #d9534f; margin-top: 0;">Meta Impuesta</h3>
<p style="margin-bottom: 0;">Una meta impuesta te hace sentir que tienes que cumplir con algo. A veces viene disfrazada de éxito, de validación, de la voz de alguien más que te dice qué deberías lograr.</p>
</div>

<div style="background: #f0fff0; border-left: 5px solid #5cb85c; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<h3 style="color: #5cb85c; margin-top: 0;">Meta Auténtica</h3>
<p style="margin-bottom: 0;">Una meta auténtica te moviliza desde adentro. No siempre es grandiosa o perfecta, pero te conecta con una emoción: propósito, paz, entusiasmo, amor, justicia, libertad.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 0; font-size: 1.1em; font-weight: 600;">La meta no es el fin, la meta es la expresión externa de una verdad interna.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 3
        },
        {
            "title": "Construcción de Metas Claras - Claves",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Claves para empezar a construir metas con sentido</h2>

<p style="margin-bottom: 16px;">Antes de entrar a ejercicios, es importante entender algunas claves que preparan el terreno:</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Tus metas deben hablar tu idioma emocional.</h4>
<p style="margin-bottom: 0;">Si una meta no te conmueve, no es tuya. No importa si suena bien. Lo importante es que te haga sentir que tiene sentido para ti.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. No todo deseo necesita tener un plan ahora.</h4>
<p style="margin-bottom: 0;">A veces, el primer paso no es ejecutar, sino reconocer: "Esto es importante para mí". Eso ya es claridad en acción.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. La meta no es lo que haces. Es lo que deseas vivir.</h4>
<p style="margin-bottom: 0;">Muchas personas dicen "quiero viajar", pero en realidad anhelan libertad, aventura o expansión. Comprender lo que hay detrás del deseo te acerca más a una meta con raíz.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Tus metas no tienen que ser productivas, tienen que ser verdaderas.</h4>
<p style="margin-bottom: 0;">Si tu meta es descansar, sanar, volver a confiar, está bien. De hecho, a veces eso es más valiente que perseguir logros vacíos.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 4
        },
        {
            "title": "Ejercicio: Construcción de Metas Claras",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Empieza a Crear tus Metas</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a crear tus metas.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Claridad y Sentido</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Objetivo y Ejercicio 1.1: Construcción de metas claras</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 5
        }
    ])
    order += 6
    
    # SUBTEMA 2: Objetivos alcanzables
    cards.extend([
        {
            "title": "Subtema 2: Objetivos Alcanzables",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Objetivos Alcanzables</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Muchas veces nos frustramos no porque no tengamos metas, sino porque nos exigimos estar en la cima sin haber construido el camino. Queremos cambios grandes, pero olvidamos que todo proceso profundo empieza con pasos pequeños, sostenibles y realistas.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¿Qué es un objetivo alcanzable?</h3>
<p style="margin-bottom: 0;">Un objetivo alcanzable es aquel que puedes cumplir desde el lugar emocional, físico y mental en el que estás hoy. No es resignarse. Es cuidarte mientras avanzas.</p>
</div>

<p style="margin-bottom: 16px;">Cuando defines objetivos que se adaptan a tu momento presente, entras en un estado de <strong>acción amable</strong>. Y desde ahí, la motivación no se basa en la presión, sino en el progreso.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin-bottom: 12px;">Como dice Marian Rojas: <em>"El cerebro necesita metas concretas para liberar dopamina, el neurotransmisor de la motivación."</em></p>
<p style="margin-bottom: 0;">Pero si esas metas son tan altas que parecen inalcanzables, en lugar de motivarte, te paralizan. Y entonces empiezas a creer que el problema eres tú… cuando en realidad lo que falló fue la estrategia.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Objetivos Alcanzables - Qué Puedes Hacer",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué puedes hacer para construir objetivos alcanzables?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Parte desde tu realidad actual, no desde la ideal</h4>
<p style="margin-bottom: 0;">Tal vez hoy no tienes la energía de hace seis meses. Tal vez estás sanando o reconstruyéndote. Está bien. Un objetivo alcanzable se adapta a tu presente sin castigarte por no estar "mejor".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Hazlo concreto y específico</h4>
<p style="margin-bottom: 0;">Tu mente necesita claridad. Cambia frases vagas como "quiero estar bien" por otras que puedas visualizar: "Voy a salir a caminar 20 minutos tres veces por semana" o "Esta semana me voy a dormir antes de las 11pm".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Divide el objetivo en pasos pequeños y posibles</h4>
<p style="margin-bottom: 0;">Si un objetivo te abruma, es señal de que necesita ser más simple. No empieces con "quiero escribir un libro", empieza con "voy a escribir 15 minutos al día". Eso también cuenta. Y mucho.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Suelta el ideal de hacerlo perfecto</h4>
<p style="margin-bottom: 0;">La perfección paraliza. El avance imperfecto construye. Lo importante no es cómo se ve, sino que lo hagas. Un paso real vale más que mil planes mentales. (como ya aprendimos 😉)</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Celebra cada pequeño avance, no solo los grandes logros</h4>
<p style="margin-bottom: 0;">Tu cerebro necesita reconocimiento para sostener el esfuerzo. Agradecerte, reconocerte y validar lo que sí hiciste refuerza tu motivación interna. Y te conecta con la confianza. (a seguir poniendo en práctica 😉)</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Ejercicio: Objetivos Alcanzables",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Define tus Objetivos</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a definir tus objetivos.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1: Claridad y Sentido</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.2: Objetivos alcanzables</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 2
        }
    ])
    order += 3
    
    # Conclusion du Thème 1
    cards.append({
        "title": "Conclusión del Tema 1",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 1</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Llegar a este punto significa que ya no estás dando pasos a ciegas. Has aprendido a escuchar lo que realmente importa para ti, a diferenciar entre lo que nace de tu verdad y lo que proviene de presiones externas, y a traducir esa claridad en metas y objetivos que puedes alcanzar.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Claridad como Brújula</h3>
<p style="margin-bottom: 0;">Aquí es donde la reflexión se convierte en dirección. La claridad no es un destino, es una brújula que te ayuda a tomar decisiones alineadas con quien eres hoy y con la vida que quieres crear.</p>
</div>

<p style="margin-bottom: 16px;">Y cuando tus metas son auténticas y alcanzables, cada paso que das deja de sentirse como una carga y se convierte en una elección consciente.</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px; font-weight: 600; color: {C_ACCENT};">A partir de ahora, ya no se trata de "seguir pensando qué hacer", sino de moverte con la certeza de que cada acción tiene sentido para ti.</p>
<p style="margin-bottom: 0;">Este es el inicio de tu etapa de <strong>libertad en acción</strong>: dejar de vivir en la duda y comenzar a avanzar con seguridad hacia tus anhelos.</p>
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
    print(f"✅ {len(cards)} cards créées pour le Thème 1")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU MODULE 5 + THÈME 1")
        print("=" * 70)
        
        # Créer le module
        module = create_module(db)
        
        # Créer le thème 1
        theme1 = Theme(
            title="Claridad y sentido",
            content="La claridad es la luz que guía el camino en medio del caos. Este módulo te ayuda a recordar qué es importante para ti, qué anhelas realmente, y cómo dar los primeros pasos hacia allí.",
            order_number=1,
            module_id=module.id
        )
        db.add(theme1)
        db.flush()
        print(f"✅ Thème 1 créé (ID: {theme1.id})")
        
        # Créer les cards du thème 1
        num_cards = create_theme1_cards(db, theme1.id)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 5 + THÈME 1 CRÉÉS!")
        print("=" * 70)
        print(f"📚 Module 5 ID: {module.id}")
        print(f"📚 Thème 1 ID: {theme1.id} ({num_cards} cards)")
        print(f"\n🎯 Prochains: Thèmes 2 et 3")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

