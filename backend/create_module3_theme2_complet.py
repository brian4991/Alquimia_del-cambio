"""
Script pour créer le Thème 2 du Module 3 COMPLET - fidèle au texte original
Thème 2: Cimientos de conexión (5 subtemas)
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

def create_theme2(db: Session, module_id: int):
    """Thème 2"""
    print("\n📚 Création du Thème 2...")
    theme = Theme(
        title="Cimientos de conexión",
        content="Las relaciones saludables no surgen por azar; se construyen sobre cimientos sólidos que nos permiten conectar de manera auténtica con nosotros mismos y con los demás.",
        order_number=2,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 2 créé (ID: {theme.id})")
    return theme

def create_theme2_cards(db: Session, theme_id: int):
    """Cards du thème 2 - CONTENU COMPLET (5 subtemas)"""
    print("\n🎴 Création des cards du Thème 2...")
    
    # Vu la longueur, je vais créer les cards par lot pour chaque subtema
    cards = []
    
    # Introduction
    cards.append({
        "title": "Bienvenida al Tema 2",
        "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Cimientos de Conexión</h1>

<p style="margin-bottom: 16px;">Las relaciones saludables no surgen por azar; se construyen sobre cimientos sólidos que nos permiten conectar de manera auténtica con nosotros mismos y con los demás.</p>

<p style="margin-bottom: 16px;">Estos cimientos son la base de una relación sana y duradera, y surgen del autoconocimiento, la autocomprensión y la capacidad de negociar nuestras necesidades de forma respetuosa.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">El Poder del Autoconocimiento</h3>
<p style="margin-bottom: 0;">Al entender nuestros patrones, aprender a soltar lo que nos limita y aprender a equilibrar nuestras emociones, somos capaces de crear conexiones más profundas y significativas con las personas que nos rodean.</p>
</div>
</div>""",
        "card_type": "intro",
        "order_number": 1
    })
    
    # Subtema 1: Patrones que se repiten (cards 2-9)
    cards.extend([
        {
            "title": "Subtema 1: Patrones que Se Repiten - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Patrones que Se Repiten</h1>

<p style="margin-bottom: 16px;">A lo largo de nuestra vida, todos pasamos por momentos que nos marcan profundamente, tanto los buenos como los dolorosos. Sin embargo, cuando hablamos de relaciones amorosas, estas experiencias pasadas pueden tener una influencia mucho mayor de lo que imaginamos.</p>

<p style="margin-bottom: 16px;">Los patrones que repetimos en nuestras relaciones amorosas no son algo que suceda por casualidad. A menudo, nos encontramos atrapados en ciclos sin entender por qué siempre terminamos eligiendo a las mismas personas, o por qué nuestros comportamientos y reacciones parecen ser los mismos en cada relación.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Primer Paso</h3>
<p style="margin-bottom: 0;">Lo primero que necesitamos comprender es que entender estos patrones es el primer paso para liberarnos de ellos y crear relaciones más saludables.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "Patrones que Se Repiten - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Los Patrones y la Infancia</h2>

<p style="margin-bottom: 16px;">Los patrones en nuestras relaciones amorosas suelen estar profundamente conectados con las experiencias de nuestra infancia, especialmente con la relación que tuvimos con nuestros cuidadores primarios.</p>

<p style="margin-bottom: 16px;">Desde que somos pequeños, empezamos a aprender cómo interactuar con los demás, y muchas veces lo hacemos de manera inconsciente. Si crecimos en un entorno en el que faltaba apoyo emocional constante, o donde el amor se veía condicionado por ciertos logros o comportamientos, es muy probable que repitamos estos mismos patrones en nuestra vida adulta, sin darnos cuenta de ello.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<p style="margin-bottom: 12px;">Por ejemplo, muchas veces las personas que crecieron en un ambiente donde la seguridad emocional no era estable tienden a buscar parejas que les generen la misma sensación de incertidumbre.</p>
<p style="margin-bottom: 0;">A pesar de que esta situación les causa dolor, la inseguridad se convierte en lo "familiar", y aunque no sea lo más sano, lo buscan sin entender completamente por qué.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "Patrones que Se Repiten - Parte 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Tipos de Patrones Comunes</h2>

<p style="margin-bottom: 16px;">También está el patrón de elegir parejas inapropiadas. Aquellas personas que no han aprendido a reconocer su propio valor o que no han sanado su autoestima, muchas veces se sienten atraídas por quienes no pueden ofrecerles lo que realmente necesitan.</p>

<p style="margin-bottom: 16px;">Se enganchan en relaciones con personas que no valoran o respetan sus emociones. En muchos casos, este patrón está relacionado con un deseo inconsciente de corregir algo del pasado, de buscar una solución a lo que no se pudo vivir de manera sana en la infancia.</p>

<p style="margin-bottom: 16px;">Y no solo se trata de lo que elegimos en una pareja, sino también de cómo nos comportamos dentro de la relación. Es común que repitamos patrones de comportamiento dañinos, como ser excesivamente complacientes con las necesidades del otro a costa de las nuestras, o sentir la necesidad de ser controladores para no sentirnos vulnerables o abandonados.</p>

<p style="margin-bottom: 16px;">A menudo, estas conductas surgen como un intento de protegernos, pero en lugar de sanarnos, nos mantienen atrapados en relaciones que no nos permiten crecer.</p>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "Patrones que Se Repiten - Parte 4",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Por Qué Repetimos Estos Patrones?</h2>

<p style="margin-bottom: 16px;">Lo cierto es que la razón principal por la que seguimos repitiendo patrones es que nos sentimos atraídos por lo familiar. Aunque las experiencias no sean las mejores, lo conocido parece más seguro para nuestro cerebro.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Ciclo de lo Familiar</h3>
<p style="margin-bottom: 0;">Las emociones que experimentamos en la infancia, aunque sean dolorosas, nos parecen conocidas y, de alguna manera, buscamos recrearlas en nuestras relaciones. Esto se debe a que nuestro cerebro, en su afán de resolver lo no resuelto, nos lleva a repetir situaciones que, aunque no sean saludables, parecen ser lo único que conocemos.</p>
</div>

<p style="margin-bottom: 16px;">Por supuesto, estos patrones se refuerzan con el tiempo. Cuanto más nos enfrentamos a situaciones similares, más se graba en nuestro cerebro la idea de que eso es lo normal o lo que nos corresponde. Aunque podamos tener la intuición de que estamos repitiendo algo que no queremos, nos cuesta muchísimo romper ese ciclo.</p>
</div>""",
            "card_type": "theory",
            "order_number": 5
        },
        {
            "title": "Patrones que Se Repiten - Parte 5",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo Podemos Empezar a Cambiar Estos Patrones?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Reconocerlos</h4>
<p style="margin-bottom: 0;">El primer paso, y el más importante, es darnos cuenta de que estamos repitiendo un patrón. Esto requiere mirarnos a nosotros mismos con honestidad y preguntarnos: ¿qué se repite en mis relaciones pasadas? ¿Por qué siempre elijo a la misma persona o me comporto de la misma forma? Al identificar este patrón, ya estamos dando el primer paso para transformarlo.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Actuar diferente</h4>
<p style="margin-bottom: 0;">Una vez que somos conscientes de estos patrones, el siguiente paso es actuar de manera diferente. Cambiar nuestras elecciones, nuestras reacciones y nuestro comportamiento en las relaciones. Claro, esto no es algo que suceda de la noche a la mañana, pero con práctica y conciencia, podemos ir poco a poco reemplazando viejos hábitos con nuevos comportamientos más saludables.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Aceptar nuestra vulnerabilidad</h4>
<p style="margin-bottom: 0;">Romper los patrones requiere también un acto de aceptación. Aceptar que no todo tiene que ser perfecto, y que la vulnerabilidad no es una debilidad, sino una oportunidad para conectar de forma genuina. Cuando dejamos de lado el miedo al rechazo y la necesidad de control, podemos empezar a establecer relaciones más reales y significativas.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 6
        },
        {
            "title": "Ejercicio: Patrones que Se Repiten",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Identifica los Patrones en tus Relaciones</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a identificar los patrones en tus relaciones.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Fundamentos</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.1: Patrones que se repiten</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 7
        }
    ])
    
    # Subtema 2: Este duelo ya no me pertenece (cards 8-11)
    cards.extend([
        {
            "title": "Subtema 2: Este Duelo Ya No Me Pertenece - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Este Duelo Ya No Me Pertenece</h1>

<p style="margin-bottom: 16px;">El duelo es una experiencia profundamente humana que todos atravesamos en algún momento de nuestras vidas. Se produce cuando perdemos algo o a alguien que era importante para nosotros, ya sea por la muerte de un ser querido, el fin de una relación amorosa, o cualquier otro tipo de pérdida significativa (como amigos, un país, mascotas).</p>

<p style="margin-bottom: 16px;">Sin embargo, a veces nos aferramos a un duelo de manera que no nos permite avanzar. Esto puede suceder cuando no hemos cerrado bien una etapa, o cuando nos quedamos atrapados en emociones y recuerdos que no hemos procesado completamente.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Un Mensaje Importante</h3>
<p style="margin-bottom: 0;">Si estás atravesando un duelo, o si sientes que duelos del pasado aún te persiguen, es importante reconocer que ese dolor ya no tiene que ser parte de tu presente.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 8
        },
        {
            "title": "Este Duelo Ya No Me Pertenece - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El Proceso del Duelo</h2>

<p style="margin-bottom: 16px;">En primer lugar, es esencial comprender que el duelo no tiene un solo ritmo o forma. Algunas personas atraviesan la pérdida rápidamente, mientras que otras pueden necesitar más tiempo. Lo importante aquí es que cada persona tiene su propio proceso y eso está bien.</p>

<p style="margin-bottom: 16px;">No hay una manera correcta o incorrecta de vivir un duelo, pero sí hay formas en las que podemos ayudar a que este proceso sea saludable y sanador.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">La Resistencia al Dolor</h3>
<p style="margin-bottom: 0;">A veces, la resistencia al dolor es lo que nos mantiene atrapados en un ciclo de sufrimiento. Pensamos que debemos aferrarnos a ese dolor como una forma de honrar lo que hemos perdido, pero en realidad, este dolor no nos ayuda a avanzar. En lugar de permitirnos soltar, continuamos aferrándonos a ese sufrimiento, que termina afectando nuestra salud emocional y física.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 9
        },
        {
            "title": "Este Duelo Ya No Me Pertenece - Parte 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">El Proceso de Soltar el Duelo</h2>

<ul style="padding-left: 24px; margin-bottom: 16px;">
<li style="margin-bottom: 12px;">El primer paso para sanar es reconocer que ese duelo ya no te pertenece. Puede ser difícil aceptar que el dolor que sientes, por más legítimo que sea, ya no es algo que debas cargar. Aceptar el duelo no significa olvidar o negar lo que ocurrió, sino dejarlo ir de manera que puedas seguir adelante con tu vida.</li>
<li style="margin-bottom: 12px;">Cuando no hemos cerrado bien un duelo, puede que lo arrastremos con nosotros en cada relación o situación futura, y esto puede manifestarse en miedos, inseguridades o incluso patrones destructivos. Si has tenido duelos no resueltos, es probable que estos sigan impactando las decisiones que tomas, las personas que eliges en tu vida, o cómo manejas las emociones difíciles. Soltar ese duelo implica reconocer su huella, pero también permitirle ir para poder continuar tu camino.</li>
</ul>
</div>""",
            "card_type": "practical",
            "order_number": 10
        },
        {
            "title": "Este Duelo Ya No Me Pertenece - Parte 4",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo Soltar el Duelo?</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">1. Aceptar lo sucedido</h4>
<p style="margin-bottom: 0;">El primer paso para sanar es aceptar lo que ocurrió. No se trata de justificar lo que sucedió ni de minimizar el dolor, sino de permitir que la realidad sea parte de tu proceso de sanación. Reconocer que esa relación, esa persona o esa situación ya no forman parte de tu vida es crucial para soltar el dolor.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">2. Honrar lo vivido</h4>
<p style="margin-bottom: 0;">A veces, nuestro miedo a olvidar a alguien o algo nos mantiene aferrados al sufrimiento. Sin embargo, honrar lo vivido no significa seguir atados al dolor. Puedes recordar lo que fue importante para ti, los aprendizajes que obtuviste, pero sin seguir anclado en el sufrimiento.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">3. Dejar ir lo que no puedes controlar</h4>
<p style="margin-bottom: 0;">En muchos casos, el duelo está asociado a situaciones que no podemos cambiar, como la muerte o el final de una relación. Lidiar con lo que no podemos controlar es fundamental para soltar. No podemos cambiar el pasado, pero sí podemos decidir cómo vivir el presente y qué camino tomar en el futuro.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_ACCENT}; margin-top: 0;">4. Permitir el tiempo para sanar</h4>
<p style="margin-bottom: 0;">El duelo requiere tiempo, y es importante ser paciente contigo mismo. No hay un tiempo exacto para sanar, y cada persona se toma el tiempo que necesita. No apresures tu proceso de sanación ni te compares con otros. Lo importante es respetar tus tiempos y darte permiso para sanar.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h4 style="color: {C_TITLE}; margin-top: 0;">5. Cuidar de ti mismo</h4>
<p style="margin-bottom: 0;">Durante el proceso de duelo, puede ser fácil olvidarnos de nuestras propias necesidades. Es vital reconectar contigo mismo a través de actividades que te brinden paz y bienestar. Hacer ejercicio, meditar, conectar con la naturaleza o hablar con alguien de confianza son formas en las que puedes cuidar de ti mismo mientras te permites sanar.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 11
        },
        {
            "title": "Este Duelo Ya No Me Pertenece - Parte 5",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Liberar el Peso del Duelo No Resuelto</h2>

<p style="margin-bottom: 16px;">Cuando un duelo no se resuelve, puede dejar huellas invisibles que afectan otras áreas de tu vida. El miedo a la soledad, la ansiedad en nuevas relaciones o la dificultad para confiar pueden ser el resultado de no haber cerrado completamente un capítulo emocional.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Clave</h3>
<p style="margin-bottom: 0;">Al liberarte de esos duelos no resueltos, puedes empezar a construir nuevas bases emocionales más saludables y abiertas. La clave está en darle un espacio a la sanación y permitirte vivir sin el peso del pasado.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 12
        },
        {
            "title": "Ejercicio: Este Duelo Ya No Me Pertenece",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Revisar y Soltar ese Duelo</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a revisar y/o soltar ese duelo.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Fundamentos</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.2: Este duelo ya no me pertenece</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 13
        }
    ])
    
    # Je continue avec les 3 derniers subtemas dans le message suivant car c'est trop long
    
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
    print(f"✅ {len(cards)} cards créées pour le Thème 2 (Partie 1/2)")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 2 DU MODULE 3 (PARTIE 1)")
        print("=" * 70)
        
        MODULE_ID = 3
        
        # Créer le thème 2
        theme2 = create_theme2(db, MODULE_ID)
        num_cards = create_theme2_cards(db, theme2.id)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 2 PARTIE 1 CRÉÉE")
        print("=" * 70)
        print(f"📚 Thème 2 ID: {theme2.id} ({num_cards} cards)")
        print(f"\n⚠️  Il manque encore 3 subtemas (Negociando necesidades, Mi persona equilibrio, Fundamentos de bienestar)")
        print("🎯 Lance create_module3_theme2_part2_complet.py ensuite")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

