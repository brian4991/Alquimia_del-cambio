"""
Script pour ajouter les 2 DERNIERS subtemas du Thème 3 Module 5
Subtemas 2-3: Diseño de productividad + El maestro del equilibrio
FIDÉLITÉ 100% + CONCLUSION DU MODULE
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
    """Ajouter les 2 derniers subtemas + conclusion"""
    print("\n🎴 Ajout des 2 derniers subtemas + conclusion...")
    
    cards = []
    order = 6  # Continue après les 5 cartes existantes
    
    # SUBTEMA 2: Diseño de productividad
    cards.extend([
        {
            "title": "Subtema 2: Diseño de Productividad",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Diseño de Productividad</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">La productividad real no se trata de hacer más cosas, sino de hacer lo que realmente importa de manera consciente, en el menor tiempo posible, y con energía suficiente para disfrutar de tu vida fuera del trabajo.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<p style="margin-bottom: 0;">Vivimos en una cultura que glorifica estar ocupado, como si llenar la agenda fuera sinónimo de éxito. Sin embargo, la verdadera productividad es un equilibrio entre <strong>acción enfocada</strong> y <strong>descanso estratégico</strong>.</p>
</div>

<p style="margin-bottom: 16px;">De hecho, un buen diseño de productividad puede implicar trabajar menos horas, pero con más intención, eliminando distracciones y dedicando tiempo a actividades que realmente generan impacto.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Un diseño de productividad efectivo parte de tres principios:</h3>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;"><strong>1. Organización clara:</strong> saber qué hacer y cuándo hacerlo, evitando el desgaste mental de decidir sobre la marcha.</p>
<p style="margin-bottom: 12px;"><strong>2. Trabajo profundo:</strong> dedicar bloques de tiempo a tareas clave sin interrupciones.</p>
<p style="margin-bottom: 0;"><strong>3. Recuperación y descanso:</strong> integrar pausas y momentos de desconexión para mantener la creatividad y la energía.</p>
</div>

<p style="margin-bottom: 16px;">Cuando organizas tu productividad de esta manera, no solo avanzas más rápido hacia tus objetivos, sino que reduces la sensación de estar siempre corriendo detrás del tiempo.</p>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "Diseño de Productividad - Cómo Funciona",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cómo funciona un diseño de productividad efectivo</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<p style="margin-bottom: 12px;">• <strong>Enfoca tu energía en lo esencial:</strong> no todo lo que tienes pendiente tiene el mismo valor. Prioriza lo que más impacto tiene en tus objetivos.</p>
<p style="margin-bottom: 12px;">• <strong>Crea rutinas que automaticen decisiones:</strong> tener una estructura predefinida evita el desgaste de decidir constantemente qué hacer.</p>
<p style="margin-bottom: 12px;">• <strong>Integra el descanso como parte de la estrategia:</strong> el cerebro necesita pausas para procesar información y encontrar soluciones creativas.</p>
<p style="margin-bottom: 0;">• <strong>Planifica con flexibilidad:</strong> un buen sistema se adapta a imprevistos sin hacerte perder el foco.</p>
</div>

<h2 style="color: {C_ACCENT}; font-size: 1.6em; margin-top: 28px; margin-bottom: 16px;">Trabajo profundo: menos dispersión, más impacto</h2>

<p style="margin-bottom: 16px;">El trabajo profundo es la capacidad de concentrarte sin distracciones en una tarea importante durante un periodo prolongado. Aquí no hay multitarea, solo enfoque absoluto.</p>

<h3 style="color: {C_TITLE}; margin-top: 24px; margin-bottom: 16px;">Cuando trabajas profundamente:</h3>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• Avanzas más en menos tiempo.</p>
<p style="margin-bottom: 12px;">• Entregas resultados de mayor calidad.</p>
<p style="margin-bottom: 0;">• Sientes mayor satisfacción por el progreso real.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0;"><strong>Clave:</strong> Dedica al menos 1 o 2 bloques de tiempo al día a trabajo profundo, apagando notificaciones y evitando interrupciones.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 1
        },
        {
            "title": "Diseño de Productividad - El Descanso",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El descanso como parte de la productividad</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">El descanso no es un premio después de trabajar, es una herramienta de alto rendimiento. Sin descanso suficiente, la concentración baja, la creatividad se bloquea y la toma de decisiones se vuelve más lenta.</p>

<h3 style="color: {C_ACCENT}; margin-top: 24px; margin-bottom: 16px;">Tipos de descanso productivo:</h3>

<div style="background: {C_BG_LIGHT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• <strong>Microdescansos:</strong> 5-10 minutos entre bloques de trabajo para estirarte o moverte.</p>
<p style="margin-bottom: 12px;">• <strong>Descanso activo:</strong> actividades físicas o creativas que te desconectan mentalmente.</p>
<p style="margin-bottom: 0;">• <strong>Sueño reparador:</strong> la base para una mente clara y enfocada.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white;">Mentalidad clave:</h3>
<p style="margin-bottom: 0; font-size: 1.05em;">El descanso no te aleja de tus objetivos, te da la energía para alcanzarlos más rápido y de forma sostenible.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 2
        },
        {
            "title": "Ejercicio: Diseño de Productividad",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Diseña un Plan Productivo Real</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a diseñar un plan productivo real.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Energía en Movimiento</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.2: Diseño de productividad</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": order + 3
        }
    ])
    order += 4
    
    # SUBTEMA 3: El maestro del equilibrio
    cards.extend([
        {
            "title": "Subtema 3: El Maestro del Equilibrio",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: El Maestro del Equilibrio</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Ser maestro del equilibrio es una habilidad consciente que se entrena con el tiempo. No se trata de vivir una vida perfecta en la que todas las áreas estén en armonía constante, sino de desarrollar la capacidad de observar, ajustar y priorizar para que ninguna parte esencial de tu vida se quede vacía por demasiado tiempo.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Error Más Común</h3>
<p style="margin-bottom: 0;">El error más común es creer que para tener equilibrio hay que "hacerlo todo" o repartir las horas de forma idéntica entre trabajo, familia, descanso, ocio y desarrollo personal. En realidad, el equilibrio es dinámico: hay momentos donde ciertas áreas requieren más atención y otras menos, y el secreto está en adaptarse sin perder la visión global de lo que es importante para ti.</p>
</div>

<p style="margin-bottom: 16px;">El verdadero equilibrio se construye cuando tus objetivos y sueños no te llevan al agotamiento, cuando avanzas en tu vida sin sacrificar tu salud, tus relaciones ni tu paz interior.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0; font-size: 1.05em;">Aquí es donde conectamos todos los elementos que has trabajado en este módulo: claridad, creencias, mindset, plan de acción y productividad.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": order
        },
        {
            "title": "El Maestro del Equilibrio - Los Pilares",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Los pilares del equilibrio</h2>

<p style="margin-bottom: 16px;">El equilibrio se apoya en pilares que, al estar en buen estado, sostienen tu bienestar y tu capacidad de actuar. Estos pilares son:</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Salud física</h4>
<p style="margin-bottom: 0;">No puedes sostener tus metas si tu cuerpo está agotado o descuidado. Esto incluye descanso, alimentación, hidratación y movimiento. No se trata de cumplir rutinas estrictas, sino de mantener hábitos que te den energía para tu día.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Salud emocional</h4>
<p style="margin-bottom: 0;">La gestión de tus emociones, tu diálogo interno y tu conexión contigo misma(o) determinan tu capacidad para enfrentar desafíos. Un pilar emocional fuerte te ayuda a mantener el enfoque incluso en momentos difíciles.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Relaciones</h4>
<p style="margin-bottom: 0;">El apoyo y la conexión con otras personas son esenciales para el bienestar. Las relaciones sanas aportan energía; las relaciones cargadas de conflicto o desconexión, la consumen.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Propósito y trabajo</h4>
<p style="margin-bottom: 0;">Tener un sentido claro de para qué haces lo que haces te da dirección y motivación. Aquí entra no solo tu empleo o negocio, sino cualquier proyecto que sientas que aporta valor a tu vida.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Tiempo personal</h4>
<p style="margin-bottom: 0;">El espacio para hobbies, creatividad, descanso mental y disfrute sin productividad aparente es lo que recarga tu energía y previene el agotamiento.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<p style="margin: 0;"><strong>Clave:</strong> El equilibrio no se logra intentando estar al 100% en todos estos pilares a la vez, sino revisando de forma constante cuál necesita más atención y haciendo pequeños ajustes.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 1
        },
        {
            "title": "El Maestro del Equilibrio - La Balanza Dinámica",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">La balanza dinámica</h2>

<p style="margin-bottom: 16px; font-size: 1.05em;">El equilibrio es un baile, no una foto estática. Habrá momentos en los que un área demande más energía que las demás, y eso no significa que estés "desequilibrado" si eres consciente y lo gestionas.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
<p style="margin-bottom: 12px;">• Si atraviesas una etapa laboral intensa, quizá tu pilar de descanso y salud física deba reforzarse más que tus salidas sociales.</p>
<p style="margin-bottom: 0;">• Si estás atravesando un momento personal importante (un duelo, una mudanza, un inicio de proyecto), puede que tu ritmo de trabajo baje temporalmente para cuidar tu energía emocional.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white;">Mentalidad clave:</h3>
<p style="margin-bottom: 0; font-size: 1.05em;">No todo requiere tu máximo esfuerzo al mismo tiempo. La flexibilidad es parte esencial del equilibrio.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 2
        },
        {
            "title": "El Maestro del Equilibrio - Estrategias",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Estrategias para mantener el equilibrio a largo plazo</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Planifica desde el bienestar, no desde la urgencia</h4>
<p style="margin-bottom: 0;">Antes de llenar tu agenda de tareas, asegúrate de que hay espacios para el descanso, la alimentación y las actividades que recargan tu energía.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Aplica la regla del 80/20</h4>
<p style="margin-bottom: 0;">El 20% de tus acciones genera el 80% de tus resultados. Identifica cuáles son esas acciones clave y dales prioridad, reduciendo las tareas que ocupan tiempo pero no aportan valor real.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Revisión mensual de áreas</h4>
<p style="margin-bottom: 0;">Una vez al mes, evalúa cómo está cada pilar de tu vida del 1 al 10. Si alguno está bajo, define una acción específica para mejorarlo en las próximas semanas.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Rituales de pausa</h4>
<p style="margin-bottom: 0;">Incorpora momentos breves pero intencionales para reconectarte: meditar, caminar, escribir, escuchar música o simplemente estar en silencio.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Aprender a decir no</h4>
<p style="margin-bottom: 0;">El equilibrio se protege poniendo límites. Decir no a lo que no está alineado con tus prioridades es decir sí a lo que realmente importa.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": order + 3
        },
        {
            "title": "El Maestro del Equilibrio - Mensaje Clave",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_ACCENT}; font-size: 1.7em; margin-bottom: 20px;">Mensaje clave:</h2>

<div style="background: {C_TITLE}; color: white; padding: 28px; border-radius: 10px; margin: 28px 0; text-align: center;">
<p style="margin-bottom: 0; font-size: 1.05em; line-height: 1.8;">Ser maestro del equilibrio no significa vivir sin tensiones ni retos, sino aprender a mover tu energía de forma consciente para que cada paso que des hacia tus metas esté sostenido por una base estable. Es elegir una vida en la que tu éxito no se mida sólo por lo que logras, sino por la calidad de vida que disfrutas mientras lo haces.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": order + 4
        }
    ])
    order += 5
    
    # Conclusion du Thème 3
    cards.append({
        "title": "Conclusión del Tema 3",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 3</h1>

<p style="margin-bottom: 16px; font-size: 1.05em;">Llegar a este punto significa que ya no solo tienes claridad sobre lo que quieres, sino que cuentas con las herramientas para avanzar hacia ello de forma organizada, realista y sostenible.</p>

<p style="margin-bottom: 16px;">Has aprendido a convertir tu visión en un plan de acción concreto, a trabajar con enfoque y sin desgaste, y a mantener el equilibrio en todas las áreas de tu vida para que tus resultados no dependan de la fuerza de voluntad momentánea, sino de una estructura que te sostenga.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Energía en Movimiento</h3>
<p style="margin-bottom: 0;">La energía en movimiento no es hacer sin parar; es dirigir tu esfuerzo hacia lo que realmente importa, evitando la dispersión y protegiendo tu bienestar en el proceso. Es la capacidad de decidir qué merece tu atención, cómo vas a organizar tu tiempo y de qué manera vas a mantener tu vida en balance mientras avanzas.</p>
</div>

<p style="margin-bottom: 16px;">Este es el momento en el que tus metas dejan de ser una intención para convertirse en parte de tu día a día. Y cuando la acción se alinea con tu propósito y se sostiene en el tiempo, los resultados dejan de ser un sueño lejano y se convierten en una realidad alcanzable.</p>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px; font-weight: 600; color: {C_ACCENT};">A partir de aquí, no se trata de hacer más, sino de hacer mejor. No de correr hacia la meta, sino de caminar con firmeza, con la certeza de que cada paso que das está construyendo la vida que has decidido crear.</p>
<p style="margin-bottom: 0; font-size: 1.1em;">¡La verdadera libertad no está en llegar más rápido, sino en avanzar con la certeza de que cada paso que das te acerca a la vida que mereces vivir!</p>
</div>
</div>""",
        "card_type": "conclusion",
        "order_number": order
    })
    order += 1
    
    # Félicitations finales
    cards.append({
        "title": "¡Felicidades por completar el Módulo 5!",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2.2em; margin-bottom: 20px; text-align: center;">¡Felicidades por completar el Módulo 5!</h1>

<div style="background: linear-gradient(135deg, {C_TITLE} 0%, {C_ACCENT} 100%); color: white; padding: 32px; border-radius: 15px; margin: 32px 0; text-align: center;">
<h2 style="margin-top: 0; color: white; font-size: 1.8em;">🎉 ¡Un Logro Increíble!</h2>
<p style="font-size: 1.15em; margin-bottom: 0; line-height: 1.7;">Has completado un viaje profundo de transformación hacia la libertad en acción, pasando de la duda a la claridad, de las creencias limitantes a un nuevo mindset, y de la planificación a la acción real y sostenible.</p>
</div>

<h3 style="color: {C_TITLE}; margin-top: 32px; margin-bottom: 16px; font-size: 1.5em;">Lo Que Has Logrado:</h3>

<div style="background: {C_BG_LIGHT}; padding: 24px; border-radius: 10px; margin: 24px 0;">
<p style="margin-bottom: 16px;">✅ <strong>Obtuviste claridad y sentido</strong> al construir metas auténticas y objetivos alcanzables</p>
<p style="margin-bottom: 16px;">✅ <strong>Soltaste lo que ya no te pertenecía</strong> al identificar creencias limitantes y crear un nuevo mindset</p>
<p style="margin-bottom: 0;">✅ <strong>Pusiste tu energía en movimiento</strong> con un plan de acción, diseño de productividad y estrategias de equilibrio sostenible</p>
</div>

<div style="background: {C_ACCENT}; color: white; padding: 28px; border-radius: 10px; margin: 32px 0;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Recuerda</h3>
<p style="margin-bottom: 0; font-size: 1.05em; line-height: 1.8;">La libertad no está en esperar el momento perfecto, sino en moverte desde donde estás, con lo que tienes, hacia lo que sueñas. Cada paso que das desde tu claridad, con tu nuevo mindset y tu plan de acción, te acerca más a la vida que mereces vivir. ¡Ya no estás en la duda, estás en movimiento!</p>
</div>

<p style="text-align: center; font-size: 1.2em; color: {C_TITLE}; margin-top: 32px; font-weight: 600;">🌟 ¡Sigue avanzando con la certeza de que mereces lo que sueñas! 🌟</p>
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
    print(f"✅ {len(cards)} cards ajoutées (Subtemas 2-3 + conclusions)")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 AJOUT FINAL - SUBTEMAS 2-3 + CONCLUSIONS - MODULE 5")
        print("=" * 70)
        
        THEME_ID = 18  # Thème 3 Module 5
        
        num_cards = add_final_subtemas(db, THEME_ID)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 5 COMPLÈTEMENT TERMINÉ!")
        print("=" * 70)
        print(f"📚 {num_cards} cards ajoutées")
        print(f"\n🎉 RÉCAPITULATIF MODULE 5:")
        print(f"   • Thème 1: Claridad y sentido (11 cards)")
        print(f"   • Thème 2: Esto ya no me pertenece (10 cards)")
        print(f"   • Thème 3: Energía en movimiento (5 + {num_cards} cards)")
        print(f"\n✨ Total: ~{11 + 10 + 5 + num_cards} cards pour le Module 5!")
        print(f"\n🏆 TOUS LES 5 MODULES SONT MAINTENANT 100% COMPLETS!")
        print(f"\n🎊 L'APPLICATION EST MAINTENANT ENTIÈREMENT COMPLÈTE!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

