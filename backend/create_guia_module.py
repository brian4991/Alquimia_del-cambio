"""
Script pour créer un module basé sur la Guía avec système de cards
"""
import sys
import io

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Module, Theme, ThemeCard

def create_test_module(db: Session):
    """Créer un module de test basé sur la Guía"""
    
    # Vérifier si le module existe déjà
    existing = db.query(Module).filter(Module.title == "TEST - El Mapa de tus Emociones").first()
    if existing:
        print("⚠️  Module de test existe déjà (ID:", existing.id, ")")
        response = input("Voulez-vous le supprimer et recréer? (yes/no): ")
        if response.lower() == 'yes':
            db.delete(existing)
            db.commit()
            print("✅ Module supprimé")
        else:
            print("❌ Annulation")
            return None
    
    # Créer le module
    print("\n📦 Création du module...")
    module = Module(
        title="TEST - El Mapa de tus Emociones",
        description="Aprende a gestionar tu mundo emocional y expresar lo que sientes y necesitas.",
        objective="El propósito de este módulo es que aprendas a gestionar tu mundo emocional y expresar lo que sientes y necesitas, con una mayor consciencia y asertividad.",
        belief_to_transform="Expresar lo que siento me hace débil y vulnerable",
        expected_results="Logras gestionar y regular tu sentir y tus emociones. Logras escuchar tus necesidades y expresarlas con seguridad y asertividad.",
        recommended_book="Inteligencia emocional de Daniel Goleman (lo encuentras en la carpeta de Bonus)",
        audio_file=None,
        order_number=999,  # Pour être à la fin
        is_active=True
    )
    db.add(module)
    db.flush()
    print(f"✅ Module créé (ID: {module.id})")
    
    return module

def create_theme1(db: Session, module_id: int):
    """Créer le premier thème: Explorando mi historia emocional"""
    
    print("\n📚 Création du Thème 1...")
    theme = Theme(
        title="Explorando mi historia emocional",
        content="El propósito de este tema es guiarte a través de la exploración consciente de tu historia emocional.",
        order_number=1,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 1 créé (ID: {theme.id})")
    
    return theme

def create_theme1_cards(db: Session, theme_id: int):
    """Créer les cards du thème 1 basées sur la Guía"""
    
    print("\n🎴 Création des cards du Thème 1...")
    
    cards = [
        # Card 1: Introduction
        {
            "title": "Bienvenida al Tema 1",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Explorando mi Historia Emocional</h1>

<p style="font-size: 1.1em; margin-bottom: 16px;">El propósito de este tema es guiarte a través de la <strong>exploración consciente</strong> de tu historia emocional.</p>

<p style="margin-bottom: 16px;">A lo largo de nuestra vida, vamos acumulando experiencias que moldean la forma en que sentimos, reaccionamos y gestionamos nuestras emociones.</p>

<div style="background: #6b745a; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¿Por qué es importante?</h3>
<p style="margin-bottom: 0;">Al reconocer los patrones emocionales y descubrir las raíces de estos, podrás comprender mejor cómo las experiencias pasadas siguen influyendo en tu presente.</p>
</div>

<p style="margin-bottom: 16px;">Este autoconocimiento es fundamental para aprender a gestionar las emociones de manera más consciente y efectiva.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        # Card 2: Avant de commencer
        {
            "title": "Antes de Empezar",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">Preparándote para el Viaje</h2>

<p style="margin-bottom: 16px;">Antes de profundizar en los temas y después de haber completado <strong>"La carta de aceptación y compromiso"</strong>, quiero que empecemos por dos ejercicios muy valiosos.</p>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Punto de Partida</h3>
<p style="margin-bottom: 0;">Estos ejercicios son el punto de partida para reconectar con tu historia, que es la que hoy te ha permitido llegar hasta aquí, pero que sin duda podremos contar desde otra perspectiva.</p>
</div>

<h3 style="color: #6b745a; margin-top: 24px;">Empecemos</h3>
<p style="margin-bottom: 16px;">Ve al <strong>Ejercicio #1: Historia</strong> y <strong>Ejercicio 1.1: Explorando mi historia Emocional</strong> y escribe todo lo que puedas con detalles.</p>

<p style="font-style: italic; color: #5a5a5a;">Esto será suficiente para el día 1 pero muy renovador.</p>

<div style="background: #cbcbcc; border: 2px solid #6b745a; padding: 16px; margin: 20px 0; border-radius: 8px;">
<p style="margin: 0; font-weight: bold; color: #6b745a;">No olvides tu carta de aceptación y compromiso: es lo primero antes de comenzar. Disfruta el viaje que te espera.</p>
</div>
</div>""",
            "card_type": "content",
            "order_number": 2
        },
        
        # Card 3: Subtema 1 - Introduction
        {
            "title": "Reconocer Patrones Emocionales",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Subtema 1: Reconocer Patrones Emocionales</h1>

<p style="margin-bottom: 16px;">Los patrones emocionales son <strong>respuestas automáticas</strong> que repetimos en situaciones similares a lo largo de nuestra vida.</p>

<p style="margin-bottom: 16px;">Estas respuestas se forman a partir de nuestras primeras experiencias emocionales y las conexiones que hacemos entre emociones y eventos específicos.</p>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Ejemplo 1</h3>
<p style="margin-bottom: 0;">Si en nuestra infancia asociamos la crítica con el miedo al rechazo, es probable que, en la vida adulta, respondamos a cualquier forma de crítica con ansiedad o inseguridad.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #6b745a; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #a28d72; margin-top: 0;">Ejemplo 2</h3>
<p style="margin-bottom: 0;">Si creciste en un ambiente donde la expresión emocional era reprimida, es probable que desarrolles un patrón de evitación emocional en tu vida adulta, donde tiendes a ignorar o minimizar tus propias emociones.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        
        # Card 4: Base científica
        {
            "title": "Base Científica: Neuroplasticidad",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">La Ciencia Detrás de los Patrones</h2>

<p style="margin-bottom: 16px;">Desde el campo de la <strong>psicología cognitiva</strong>, se ha demostrado que nuestras emociones están en gran parte influenciadas por esquemas mentales, o "mapas" que desarrollamos a lo largo del tiempo.</p>

<p style="margin-bottom: 16px;">Estos esquemas emocionales son patrones de pensamientos y emociones que guían nuestras reacciones.</p>

<div style="background: #6b745a; color: white; padding: 24px; border-radius: 10px; margin: 28px 0;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Neuroplasticidad: La Clave del Cambio</h3>
<p style="margin-bottom: 12px;">La <strong>neurociencia</strong> nos muestra que el cerebro puede cambiar sus conexiones, lo que significa que podemos "reprogramar" cómo reaccionamos emocionalmente a través del autoconocimiento y la práctica consciente.</p>
<p style="margin-bottom: 0;">Este proceso se conoce como <strong>neuroplasticidad</strong>, y es lo que nos permite adoptar nuevas formas de gestionar nuestras emociones una vez que somos conscientes de los patrones emocionales que hemos desarrollado.</p>
</div>

<div style="background: #cbcbcc; border: 2px solid #6b745a; padding: 20px; margin: 24px 0; border-radius: 8px;">
<h3 style="color: #6b745a; margin-top: 0;">La Buena Noticia</h3>
<p style="margin-bottom: 0; color: #2d2d2d;">Identificar estos patrones es esencial para desactivarlos. El cerebro puede aprender nuevas formas de responder.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 4
        },
        
        # Card 5: Señales de patrones
        {
            "title": "Señales de Patrones Emocionales Recurrentes",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">Señales de Patrones Emocionales Recurrentes</h2>

<p style="margin-bottom: 24px;">Identifica estas señales en tu vida cotidiana:</p>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">1. Reacciones exageradas a ciertas situaciones</h3>
<p style="margin-bottom: 0;">A veces, cuando alguien nos critica o dice algo que no nos gusta, podemos sentirnos muy enojados o muy tristes, incluso si lo que dijeron no era tan grave. Esto pasa porque hemos aprendido a reaccionar así en el pasado.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #6b745a; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<h3 style="color: #a28d72; margin-top: 0;">2. Sentir las mismas emociones en situaciones parecidas</h3>
<p style="margin-bottom: 0;">Puede que te sientas frustrado o nervioso en ciertos lugares o con ciertas personas, como en el trabajo o en una reunión social. Esto ocurre porque esas situaciones te recuerdan a otras donde ya te sentiste así antes.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin-bottom: 20px; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">3. Evitar ciertos temas o emociones</h3>
<p style="margin-bottom: 0;">Si hay cosas que prefieres no hablar o sentir, como el miedo o la tristeza, podrías intentar ignorarlas. En lugar de enfrentarlas, quizás optes por aislarte o discutir con los demás para no sentirte vulnerable.</p>
</div>

<div style="background: #cbcbcc; padding: 20px; border-radius: 8px; margin-top: 24px;">
<p style="margin: 0; font-size: 1.05em;"><strong>Conclusión:</strong> Al identificar estos patrones, podemos empezar a comprender que nuestras emociones no siempre reflejan la realidad del presente, sino que están condicionadas por experiencias anteriores.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 5
        },
        
        # Card 6: Ejercicio patrones
        {
            "title": "Ejercicio: Reconociendo mis Patrones",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">A Continuación: Tu Mapa Emocional</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a armar tu <strong>mapa emocional interno</strong>.</p>

<div style="background: #6b745a; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1 Historia</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.2: Reconociendo Patrones Emocionales</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 6
        },
        
        # Card 7: Subtema 2 - Raíces
        {
            "title": "Raíces Emocionales",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h1 style="color: #6b745a; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Subtema 2: Raíces Emocionales</h1>

<p style="margin-bottom: 16px;">Las raíces emocionales son las <strong>experiencias pasadas</strong>, a menudo en la infancia o adolescencia, que forman la base de nuestros patrones emocionales actuales.</p>

<p style="margin-bottom: 16px;">Estas experiencias tempranas, tanto positivas como negativas, juegan un papel crucial en el desarrollo de nuestro sistema emocional.</p>

<div style="background: #cbcbcc; border-left: 5px solid #6b745a; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Teoría del Apego - John Bowlby</h3>
<p style="margin-bottom: 12px;">En <strong>psicología del desarrollo</strong>, el modelo del apego propuesto por John Bowlby sostiene que nuestras primeras relaciones, particularmente con los cuidadores primarios, influyen en cómo formamos relaciones y regulamos nuestras emociones en el futuro.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Ejemplo</h3>
<p style="margin-bottom: 0;">Si en nuestra infancia aprendimos que expresar tristeza no era aceptado o no recibía la validación necesaria, podríamos haber desarrollado una tendencia a reprimir esa emoción.</p>
</div>

<p style="margin-bottom: 16px;">Este patrón de represión emocional puede perdurar en la vida adulta, resultando en una incapacidad para expresar o incluso identificar correctamente sentimientos de tristeza.</p>
</div>""",
            "card_type": "theory",
            "order_number": 7
        },
        
        # Card 8: Impacto de las raíces
        {
            "title": "Impacto de las Raíces Emocionales",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">Impacto de las Raíces Emocionales</h2>

<p style="margin-bottom: 24px;">Las experiencias tempranas pueden tener diferentes impactos en nuestra vida adulta:</p>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Apego inseguro</h3>
<p style="margin-bottom: 0;">Puede generar dependencia emocional o dificultades para confiar en los demás.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #6b745a; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: #a28d72; margin-top: 0;">Experiencias de rechazo</h3>
<p style="margin-bottom: 0;">Pueden llevar a una sensibilidad exagerada ante la crítica o el conflicto.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Ambientes familiares poco expresivos emocionalmente</h3>
<p style="margin-bottom: 0;">Pueden resultar en la incapacidad de expresar necesidades emocionales de manera asertiva.</p>
</div>

<div style="background: #f5f5f0; border-left: 5px solid #6b745a; padding: 20px; margin-bottom: 24px; border-radius: 5px;">
<h3 style="color: #a28d72; margin-top: 0;">Momentos traumáticos</h3>
<p style="margin-bottom: 0;">Pueden generar reacciones desproporcionadas ante situaciones de pérdida o estrés en la vida adulta.</p>
</div>

<hr style="margin: 28px 0; border: 1px solid #cbcbcc;">

<div style="background: #6b745a; color: white; padding: 24px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Poder del Autoconocimiento</h3>
<p style="margin-bottom: 12px;">Explorar estas raíces no solo es importante para comprender por qué reaccionamos de cierta manera, sino que también nos permite <strong>tomar el control</strong> sobre cómo queremos responder en el futuro.</p>
<p style="margin-bottom: 0;">El autoconocimiento de nuestras raíces emocionales nos da el poder de cambiar nuestras narrativas emocionales y romper patrones que ya no nos sirven.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 8
        },
        
        # Card 9: Ejercicio raíces
        {
            "title": "Ejercicio: Explorando mis Raíces",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px;">Comprendiendo la Raíz de tus Emociones</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a comprender la raíz de tus emociones.</p>

<div style="background: #6b745a; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #1 Historia</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 1.3: Raíces Emocionales</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Dirígete a la sección de ejercicios para completar esta actividad.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 9
        },
        
        # Card 10: Conclusion
        {
            "title": "Conclusión del Tema 1",
            "content": """<div style="color: #2d2d2d; font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif; line-height: 1.8; max-width: 800px;">
<h2 style="color: #6b745a; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid #a28d72; padding-bottom: 12px;">Construyendo tu Fundamento Emocional</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">Este tema es el <strong>fundamento</strong> para construir un mayor entendimiento de ti mismo a nivel emocional.</p>

<div style="background: #cbcbcc; padding: 20px; border-radius: 8px; margin: 24px 0;">
<h3 style="color: #6b745a; margin-top: 0;">Lo que has aprendido:</h3>
<p style="margin-bottom: 12px;"><strong>Reconocer patrones emocionales</strong> es el primer paso para observar cómo respondes a situaciones y relaciones.</p>
<p style="margin-bottom: 0;"><strong>Explorar las raíces emocionales</strong> te permitirá entender por qué reaccionas de esa manera.</p>
</div>

<p style="margin-bottom: 16px;">Con este conocimiento, comenzarás a tomar decisiones más conscientes sobre cómo gestionar tus emociones y evitarás caer en respuestas automáticas que no contribuyen a tu bienestar.</p>

<div style="background: #f5f5f0; border-left: 5px solid #a28d72; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: #6b745a; margin-top: 0;">Recuerda</h3>
<p style="margin-bottom: 0;">Las emociones no se generan en el vacío; están profundamente conectadas a nuestra historia y a las experiencias que nos han moldeado. Este proceso de autoexploración te brinda una visión más clara de esas conexiones, permitiéndote tomar las riendas de tu mundo emocional con mayor comprensión y compasión.</p>
</div>

<div style="background: #6b745a; color: white; padding: 24px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Siguiente Paso</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Continúa al Tema 2: Autoconocimiento Emocional Profundo</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 10
        }
    ]
    
    # Créer toutes les cards
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
    print(f"✅ {len(cards)} cards créées")
    
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 60)
        print("🚀 CRÉATION DU MODULE GUÍA")
        print("=" * 60)
        
        # 1. Créer le module
        module = create_test_module(db)
        if not module:
            return
        
        # 2. Créer le thème 1
        theme = create_theme1(db, module.id)
        
        # 3. Créer les cards du thème 1
        num_cards = create_theme1_cards(db, theme.id)
        
        print("\n" + "=" * 60)
        print("✅ CRÉATION TERMINÉE AVEC SUCCÈS")
        print("=" * 60)
        print(f"📦 Module ID: {module.id}")
        print(f"📚 Thème ID: {theme.id}")
        print(f"🎴 Nombre de cards: {num_cards}")
        print("\n🎯 Le module de test est prêt à être consulté!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()

