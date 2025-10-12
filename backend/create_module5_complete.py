"""
Script pour créer le Module 5: Libertad en Acción
Avec ses 3 thèmes et toutes les cartes (version simplifiée)
Font: Source Sans Pro
Couleurs: #a28d72, #cbcbcc, #6b745a
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Module, Theme, ThemeCard

def create_module5(db: Session):
    """Créer le Module 5 complet"""
    
    print("\n" + "=" * 70)
    print("🚀 CRÉATION DU MODULE 5: Libertad en Acción")
    print("=" * 70)
    
    # Créer le module
    module = Module(
        title="Libertad en Acción",
        description="Fortalece tu confianza interna y obtén claridad sobre tus próximos pasos para avanzar con seguridad.",
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
    
    # THÈME 1: Claridad y sentido
    print("\n📚 Création du Thème 1: Claridad y sentido...")
    theme1 = Theme(
        title="Claridad y sentido",
        content="Conecta con tu verdad interna para que cada paso empiece a tener sentido.",
        order_number=1,
        module_id=module.id
    )
    db.add(theme1)
    db.flush()
    print(f"  ✅ Thème 1 créé (ID: {theme1.id})")
    
    # Cartes du Thème 1 - Version résumée pour éviter les problèmes d'encodage
    theme1_cards = []
    
    # Card 1
    theme1_cards.append(ThemeCard(
        title="Bienvenida al Tema 1",
        content="<h1 style='color: #6b745a;'>Claridad y Sentido</h1><p>Cuando no sabes hacia donde vas, cualquier camino parece confuso. Pero cuando conectas con tu verdad interna, cada paso empieza a tener sentido.</p><p>La claridad es la luz que guia el camino en medio del caos.</p>",
        card_type="intro",
        order_number=1,
        theme_id=theme1.id
    ))
    
    # Card 2
    theme1_cards.append(ThemeCard(
        title="Construcción de metas claras",
        content="<h2 style='color: #6b745a;'>Construcción de Metas Claras</h2><p>Una meta clara es mucho mas que un objetivo escrito. Es una expresión de sentido, es un deseo consciente que nace desde adentro.</p><p>Muchas veces confundimos metas con mandatos. Pero una meta clara nace de la conexión contigo mismo/a.</p>",
        card_type="content",
        order_number=2,
        theme_id=theme1.id
    ))
    
    # Card 3
    theme1_cards.append(ThemeCard(
        title="Claves para metas con sentido",
        content="<h2 style='color: #6b745a;'>Claves para Construir Metas</h2><p><strong>1. Tus metas deben hablar tu idioma emocional</strong><br>Si una meta no te conmueve, no es tuya.</p><p><strong>2. No todo deseo necesita un plan ahora</strong><br>A veces, el primer paso es reconocer: 'Esto es importante para mi'.</p><p><strong>3. La meta es lo que deseas vivir</strong><br>No es lo que haces, sino lo que anhelas experimentar.</p>",
        card_type="content",
        order_number=3,
        theme_id=theme1.id
    ))
    
    # Card 4
    theme1_cards.append(ThemeCard(
        title="Objetivos alcanzables",
        content="<h2 style='color: #6b745a;'>Objetivos Alcanzables</h2><p>Un objetivo alcanzable es aquel que puedes cumplir desde el lugar emocional, físico y mental en el que estas hoy.</p><p>No es resignarse. Es cuidarte mientras avanzas.</p><p>Como dice Marian Rojas: 'El cerebro necesita metas concretas para liberar dopamina, el neurotransmisor de la motivación.'</p>",
        card_type="content",
        order_number=4,
        theme_id=theme1.id
    ))
    
    # Card 5
    theme1_cards.append(ThemeCard(
        title="Construir objetivos alcanzables",
        content="<h2 style='color: #6b745a;'>Como Construir Objetivos</h2><p><strong>1. Parte desde tu realidad actual</strong><br>No desde la ideal.</p><p><strong>2. Hazlo concreto y específico</strong><br>Tu mente necesita claridad.</p><p><strong>3. Divide en pasos pequeños</strong><br>Si te abruma, hazlo mas simple.</p><p><strong>4. Suelta el ideal de perfección</strong><br>El avance imperfecto construye.</p>",
        card_type="content",
        order_number=5,
        theme_id=theme1.id
    ))
    
    # Card 6
    theme1_cards.append(ThemeCard(
        title="Conclusión Tema 1",
        content="<h2 style='color: #6b745a;'>Conclusión</h2><p>Llegar a este punto significa que ya no estas dando pasos a ciegas. Has aprendido a escuchar lo que realmente importa para ti.</p><p>La claridad no es un destino, es una brújula que te ayuda a tomar decisiones alineadas con quien eres hoy.</p><p>A partir de ahora, cada acción tiene sentido para ti. Este es el inicio de tu etapa de libertad en acción.</p>",
        card_type="content",
        order_number=6,
        theme_id=theme1.id
    ))
    
    for card in theme1_cards:
        db.add(card)
    db.flush()
    print(f"  ✅ {len(theme1_cards)} cartes créées pour le Thème 1")
    
    # THÈME 2: Esto ya no me pertenece
    print("\n📚 Création du Thème 2: Esto ya no me pertenece...")
    theme2 = Theme(
        title="Esto ya no me pertenece",
        content="Reconoce lo que ya no tiene lugar en tu vida y suelta aquello que dejó de nutrirte.",
        order_number=2,
        module_id=module.id
    )
    db.add(theme2)
    db.flush()
    print(f"  ✅ Thème 2 créé (ID: {theme2.id})")
    
    # Cartes du Thème 2
    theme2_cards = []
    
    # Card 1
    theme2_cards.append(ThemeCard(
        title="Bienvenida al Tema 2",
        content="<h1 style='color: #6b745a;'>Esto Ya No Me Pertenece</h1><p>Para avanzar con libertad, no basta con saber lo que quieres; también necesitas reconocer lo que ya no tiene lugar en tu vida.</p><p>Decir 'esto ya no me pertenece' no es huir ni negar lo vivido. Es un acto consciente de soltar aquello que dejó de nutrirte.</p>",
        card_type="intro",
        order_number=1,
        theme_id=theme2.id
    ))
    
    # Card 2
    theme2_cards.append(ThemeCard(
        title="Identificando creencias limitantes",
        content="<h2 style='color: #6b745a;'>Identificando Creencias Limitantes</h2><p>Las creencias limitantes son como filtros invisibles que distorsionan lo que creemos posible.</p><p>Una creencia no es una verdad absoluta, sino una interpretación repetida tantas veces que terminó pareciendo real.</p>",
        card_type="content",
        order_number=2,
        theme_id=theme2.id
    ))
    
    # Card 3
    theme2_cards.append(ThemeCard(
        title="Claves para identificarlas",
        content="<h2 style='color: #6b745a;'>Claves para Identificar Creencias</h2><p><strong>1. Escucha tus frases automáticas</strong><br>Observa que te dices sin filtrar.</p><p><strong>2. Ubica la emoción</strong><br>Las creencias limitantes viven en tu cuerpo.</p><p><strong>3. Detecta de dónde viene</strong><br>¿Es tuya o heredada?</p><p><strong>4. Identifica el patrón</strong><br>Si siempre aparece, es un freno interno.</p>",
        card_type="content",
        order_number=3,
        theme_id=theme2.id
    ))
    
    # Card 4
    theme2_cards.append(ThemeCard(
        title="Mi nuevo mindset",
        content="<h2 style='color: #6b745a;'>Mi Nuevo Mindset</h2><p>Un nuevo mindset no es simplemente 'pensar positivo', sino crear un sistema de creencias, pensamientos y hábitos que respalden tus objetivos.</p><p>El mindset actúa como el software que dirige tus decisiones.</p>",
        card_type="content",
        order_number=4,
        theme_id=theme2.id
    ))
    
    # Card 5
    theme2_cards.append(ThemeCard(
        title="Construir tu nuevo mindset",
        content="<h2 style='color: #6b745a;'>Claves para Tu Nuevo Mindset</h2><p><strong>1. Haz que tu mente trabaje a tu favor</strong><br>Enfócate en lo que puedes controlar.</p><p><strong>2. Progreso constante, no todo o nada</strong><br>Avanzar imperfecto sigue siendo avanzar.</p><p><strong>3. Creencias expansivas y realistas</strong><br>'Puedo aprender lo que me falta'.</p>",
        card_type="content",
        order_number=5,
        theme_id=theme2.id
    ))
    
    # Card 6
    theme2_cards.append(ThemeCard(
        title="Conclusión Tema 2",
        content="<h2 style='color: #6b745a;'>Conclusión</h2><p>Has hecho algo que muchas personas evitan: mirar de frente aquello que te ha limitado.</p><p>Tu nuevo mindset no es una promesa vacía: es una herramienta que has creado tu, desde tu verdad, para sostenerte en cada paso.</p><p>Lo que ayer te frenaba, hoy ya no te pertenece.</p>",
        card_type="content",
        order_number=6,
        theme_id=theme2.id
    ))
    
    for card in theme2_cards:
        db.add(card)
    db.flush()
    print(f"  ✅ {len(theme2_cards)} cartes créées pour le Thème 2")
    
    # THÈME 3: Energía en movimiento
    print("\n📚 Création du Thème 3: Energía en movimiento...")
    theme3 = Theme(
        title="Energía en movimiento",
        content="Transforma tu claridad y nuevas creencias en acción con sentido.",
        order_number=3,
        module_id=module.id
    )
    db.add(theme3)
    db.flush()
    print(f"  ✅ Thème 3 créé (ID: {theme3.id})")
    
    # Cartes du Thème 3
    theme3_cards = []
    
    # Card 1
    theme3_cards.append(ThemeCard(
        title="Bienvenida al Tema 3",
        content="<h1 style='color: #6b745a;'>Energía en Movimiento</h1><p>La verdadera transformación ocurre cuando toda esa claridad, tus nuevas creencias y tu propósito se convierten en movimiento.</p><p>La energía en movimiento es acción con sentido.</p><p>La libertad no llega esperando el momento perfecto, sino moviéndote desde donde estas, con lo que tienes, hacia lo que sueñas.</p>",
        card_type="intro",
        order_number=1,
        theme_id=theme3.id
    ))
    
    # Card 2
    theme3_cards.append(ThemeCard(
        title="Plan de acción",
        content="<h2 style='color: #6b745a;'>Plan de Acción</h2><p>Un plan de acción es la hoja de ruta que convierte tus ideas y objetivos en pasos concretos.</p><p>No es una lista infinita de tareas, sino un mapa claro que te dice que hacer, cuando y como.</p><p>El error mas común es intentar abarcar demasiado o plantear pasos poco realistas.</p>",
        card_type="content",
        order_number=2,
        theme_id=theme3.id
    ))
    
    # Card 3
    theme3_cards.append(ThemeCard(
        title="Construir tu plan",
        content="<h2 style='color: #6b745a;'>Como Construir Tu Plan</h2><p><strong>1. Empieza por el objetivo final</strong><br>Define con claridad que quieres lograr.</p><p><strong>2. Divide en etapas</strong><br>No saltes del punto A al Z.</p><p><strong>3. Acciones concretas</strong><br>Cada acción debe ser clara y medible.</p><p><strong>4. Pon fechas</strong><br>El tiempo crea compromiso.</p>",
        card_type="content",
        order_number=3,
        theme_id=theme3.id
    ))
    
    # Card 4
    theme3_cards.append(ThemeCard(
        title="Diseño de productividad",
        content="<h2 style='color: #6b745a;'>Diseño de Productividad</h2><p>La productividad real no se trata de hacer mas cosas, sino de hacer lo que realmente importa de manera consciente.</p><p>Un buen diseño de productividad puede implicar trabajar menos horas, pero con mas intención.</p><p>Tres principios: Organización clara, Trabajo profundo, Recuperación y descanso.</p>",
        card_type="content",
        order_number=4,
        theme_id=theme3.id
    ))
    
    # Card 5
    theme3_cards.append(ThemeCard(
        title="Trabajo profundo y descanso",
        content="<h2 style='color: #6b745a;'>Trabajo Profundo</h2><p>El trabajo profundo es la capacidad de concentrarte sin distracciones en una tarea importante.</p><p>Dedica al menos 1 o 2 bloques de tiempo al día a trabajo profundo, apagando notificaciones.</p><p><strong>El descanso no es un premio</strong><br>Es una herramienta de alto rendimiento. Sin descanso, la concentración baja y la creatividad se bloquea.</p>",
        card_type="content",
        order_number=5,
        theme_id=theme3.id
    ))
    
    # Card 6
    theme3_cards.append(ThemeCard(
        title="El maestro del equilibrio",
        content="<h2 style='color: #6b745a;'>El Maestro del Equilibrio</h2><p>Ser maestro del equilibrio es una habilidad consciente que se entrena con el tiempo.</p><p>No se trata de vivir una vida perfecta, sino de desarrollar la capacidad de observar, ajustar y priorizar.</p><p>Los 5 pilares: Salud física, Salud emocional, Relaciones, Propósito y trabajo, Tiempo personal.</p>",
        card_type="content",
        order_number=6,
        theme_id=theme3.id
    ))
    
    # Card 7
    theme3_cards.append(ThemeCard(
        title="Estrategias para el equilibrio",
        content="<h2 style='color: #6b745a;'>Estrategias de Equilibrio</h2><p><strong>1. Planifica desde el bienestar</strong><br>No desde la urgencia.</p><p><strong>2. Regla del 80/20</strong><br>El 20% de tus acciones genera el 80% de tus resultados.</p><p><strong>3. Revisión mensual</strong><br>Evalúa cada pilar del 1 al 10.</p><p><strong>4. Aprende a decir no</strong><br>Protege tu equilibrio poniendo límites.</p>",
        card_type="content",
        order_number=7,
        theme_id=theme3.id
    ))
    
    # Card 8
    theme3_cards.append(ThemeCard(
        title="Conclusión Tema 3",
        content="<h2 style='color: #6b745a;'>Conclusión</h2><p>Has aprendido a convertir tu visión en un plan de acción concreto, a trabajar con enfoque y sin desgaste.</p><p>La energía en movimiento no es hacer sin parar; es dirigir tu esfuerzo hacia lo que realmente importa.</p><p>Este es el momento en el que tus metas dejan de ser una intención para convertirse en parte de tu día a día.</p>",
        card_type="content",
        order_number=8,
        theme_id=theme3.id
    ))
    
    # Card 9 - Félicitations
    theme3_cards.append(ThemeCard(
        title="Felicidades",
        content="<h1 style='color: #6b745a; text-align: center;'>¡Felicidades por Completar el Módulo 5!</h1><p style='text-align: center; font-size: 1.2em;'>¡La verdadera libertad no esta en llegar mas rapido, sino en avanzar con la certeza de que cada paso que das te acerca a la vida que mereces vivir!</p><p style='text-align: center;'>🎉 Has completado tu transformación 🎉</p>",
        card_type="content",
        order_number=9,
        theme_id=theme3.id
    ))
    
    for card in theme3_cards:
        db.add(card)
    db.flush()
    print(f"  ✅ {len(theme3_cards)} cartes créées pour le Thème 3")
    
    db.commit()
    
    print("\n" + "=" * 70)
    print("✅ MODULE 5 CRÉÉ AVEC SUCCÈS!")
    print("=" * 70)
    print(f"📚 Thème 1 (Claridad y sentido): {len(theme1_cards)} cartes")
    print(f"📚 Thème 2 (Esto ya no me pertenece): {len(theme2_cards)} cartes")
    print(f"📚 Thème 3 (Energía en movimiento): {len(theme3_cards)} cartes")
    print(f"\n✨ Total: {len(theme1_cards) + len(theme2_cards) + len(theme3_cards)} cartes créées!")
    print("\n🎯 Prochaine étape: Créer les exercices du Module 5")

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        create_module5(db)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

