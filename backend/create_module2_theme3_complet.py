"""
Script pour créer le Thème 3 du Module 2 COMPLET - fidèle au texte original
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

def create_theme3(db: Session, module_id: int):
    """Thème 3"""
    print("\n📚 Création du Thème 3...")
    theme = Theme(
        title="Celebrar y celebrarse",
        content="Aprende a celebrar tus logros, grandes y pequeños, y construye amor propio auténtico.",
        order_number=3,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 3 créé (ID: {theme.id})")
    return theme

def create_theme3_cards(db: Session, theme_id: int):
    """Cards du thème 3 - CONTENU COMPLET"""
    print("\n🎴 Création des cards du Thème 3...")
    
    cards = [
        {
            "title": "Bienvenida al Tema 3",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Celebrar y Celebrarse</h1>

<p style="margin-bottom: 16px;">¿Cuándo fue la última vez que celebraste un logro, incluso si era pequeño?</p>

<p style="margin-bottom: 16px;">Muchas veces, estamos tan enfocados en lo que falta por hacer o en lo que creemos que no hicimos bien, que olvidamos reconocer lo lejos que hemos llegado.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Un Acto de Amor Propio</h3>
<p style="margin-bottom: 0;">Este tema trata de algo fundamental: aprender a detenerte, mirar tu esfuerzo y decir: 'Lo hice bien'. Celebrarte no es solo una cuestión de autoestima, es un acto de amor propio y una práctica que te ayuda a mantener la motivación y el equilibrio emocional.</p>
</div>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: Reconocer los Pequeños-Grandes Éxitos - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Reconocer los Pequeños-Grandes Éxitos</h1>

<p style="margin-bottom: 16px;">Muchas veces pensamos que los logros tienen que ser extraordinarios para merecer reconocimiento, pero eso no es verdad.</p>

<p style="margin-bottom: 16px;">En la vida diaria, los pequeños pasos que damos hacia adelante son los que realmente construyen el camino hacia nuestras metas. Reconocer estos pequeños-grandes éxitos no es solo un acto de gratitud hacia ti mismo, sino una manera de entrenar a tu mente para enfocarse en lo que haces bien, en lugar de en lo que falta.</p>

<p style="margin-bottom: 16px;">Este hábito refuerza la confianza y te motiva a seguir avanzando.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">El Sesgo de Negatividad</h3>
<p style="margin-bottom: 0;">La mente humana está predispuesta a la "negatividad" recordamos más los fracasos que los éxitos, porque nuestro cerebro está diseñado para detectar amenazas y prevenir errores. Sin embargo, esto puede generar una desconexión con nuestras propias capacidades, llevándonos a sentir que nunca es suficiente.</p>
</div>

<p style="margin-bottom: 16px;">Reconocer los pequeños logros combate esta tendencia negativa al activar el sistema de recompensa del cerebro, que libera dopamina y refuerza el comportamiento positivo, en este caso reconocer nuestros logros.</p>

<p style="margin-bottom: 16px;">Con el tiempo, este hábito te ayuda a construir una narrativa más equilibrada y saludable sobre quién eres y de lo que eres capaz.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "Pequeños-Grandes Éxitos - Parte 2: ¿Qué Podemos Aprender?",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Qué Podemos Aprender al Reconocer los Pequeños-Grandes Éxitos?</h2>

<p style="margin-bottom: 16px;">Nuestra percepción del éxito está influenciada por patrones mentales y sociales que priorizan los grandes logros visibles, como obtener un título, un ascenso o comprar una casa.</p>

<p style="margin-bottom: 16px;">Sin embargo, este enfoque puede desconectarnos de los avances cotidianos que son esenciales para nuestro bienestar y desarrollo personal.</p>

<p style="margin-bottom: 20px; font-weight: 600;">Al aprender a valorar los pequeños-grandes éxitos, obtenemos múltiples beneficios:</p>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        
        {
            "title": "Cinco Beneficios de Reconocer tus Logros - Parte 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Cinco Beneficios Clave</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">1. Refuerzo positivo</h3>
<p style="margin-bottom: 0;">Cuando reconocemos un logro, como terminar un proyecto o aprender algo nuevo, nuestro cerebro se siente bien y nos da una "recompensa", como cuando te sientes feliz por haber hecho algo bien. Esto sucede porque el cerebro libera dopamina, que nos motiva a seguir trabajando con el mismo esfuerzo. Es como cuando te das un pequeño premio a ti mismo por lograr algo, lo que te hace querer seguir intentándolo.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">2. Reestructuración cognitiva</h3>
<p style="margin-bottom: 0;">Las personas que suelen ser muy autocríticas a menudo se centran más en lo que hicieron mal que en lo que hicieron bien. Por ejemplo, si entregan un informe con un pequeño error, en lugar de ver todo el trabajo bien hecho, solo piensan en ese error. Al reconocer los logros, incluso los pequeños, cambiamos nuestra forma de ver las cosas. Es como si te dieras cuenta de que, además de ese error, hubo muchas cosas que hiciste bien, lo que te motiva a seguir mejorando sin ser tan duro contigo mismo.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">3. Aumento de la autoestima</h3>
<p style="margin-bottom: 0;">Reconocer nuestros logros, por pequeños que sean, fortalece nuestra autoestima al recordarnos que somos capaces de avanzar y superar retos. Este acto es especialmente valioso para personas que se sienten atrapadas en ciclos de inseguridad o síndrome del impostor, ya que les permite construir una imagen más realista y positiva de sí mismas.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        
        {
            "title": "Cinco Beneficios - Parte 4: Continuación",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Más Beneficios</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">4. Fomento de la resiliencia</h3>
<p style="margin-bottom: 0;">Celebrar los pequeños éxitos ayuda a construir resiliencia, porque nos enseña a encontrar esperanza y satisfacción incluso en las dificultades. Por ejemplo, en lugar de enfocarnos en cuánto falta para alcanzar una meta, aprendemos a valorar los pasos que ya hemos dado, lo que nos da fuerza para continuar.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">5. Conexión con el presente</h3>
<p style="margin-bottom: 0;">Reconocer los pequeños logros nos ancla al presente y fomenta la práctica de la gratitud. En un mundo donde muchas veces vivimos apresurados por lo que viene, detenernos a celebrar lo que ya hemos conseguido nos permite disfrutar más del proceso, lo cual es clave para un bienestar emocional duradero.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 5
        },
        
        {
            "title": "Ejercicio: Reconocer los Pequeños-Grandes Éxitos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Celebra tu Ser</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a celebrar tu ser.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Mi fiesta interior</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.1: Reconocer los pequeños-grandes éxitos</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 6
        },
        
        {
            "title": "Subtema 2: Enfoque en el Proceso y Esfuerzo - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: Enfoque en el Proceso y Esfuerzo</h1>

<p style="margin-bottom: 16px;">La tendencia a medir el valor de nuestras acciones únicamente por los resultados finales, como completar un proyecto, alcanzar una meta o recibir reconocimiento, es común, pero puede ser contraproducente.</p>

<p style="margin-bottom: 16px;">La psicología positiva y las teorías del mindset (mentalidad) nos indican que este enfoque puede limitarnos y generar frustración, especialmente cuando los objetivos son a largo plazo o implican un esfuerzo significativo. El enfocarse exclusivamente en los resultados incrementa el estrés y reduce la satisfacción personal.</p>

<div style="background: {C_BG_GRAY}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Mentalidad de Crecimiento</h3>
<p style="margin-bottom: 0;">En cambio, al centrar nuestra atención en el proceso y el esfuerzo, activamos el sistema de recompensa del cerebro de una manera más constante y positiva. Esta mentalidad de "crecimiento" fomenta una mayor motivación intrínseca, reduce la ansiedad y nos permite ver los errores y desafíos como oportunidades de aprendizaje.</p>
</div>

<p style="margin-bottom: 16px;">Cambiar el enfoque hacia el proceso no solo mejora nuestra resiliencia, sino que también fortalece nuestra capacidad para afrontar adversidades y nos acerca más a una sensación de bienestar general.</p>
</div>""",
            "card_type": "theory",
            "order_number": 7
        },
        
        {
            "title": "Enfoque en el Proceso - Parte 2: Recomendaciones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Recomendaciones para Enfocarte en el Proceso y el Esfuerzo</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Crea un ritual de autoevaluación positiva</h3>
<p style="margin-bottom: 0;">Al final de cada día o semana, pregúntate: ¿Qué hice hoy que me acercó a mis objetivos, aunque sea un pequeño paso? Esto puede incluir acciones como tomar una decisión difícil, enfrentar una conversación complicada, o simplemente mantenerte constante en tus hábitos. Por ejemplo, si estás trabajando en tu bienestar físico, puedes celebrar el hecho de haberte levantado temprano para hacer ejercicio, aunque no hayas corrido más rápido o levantado más peso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Visualiza tus esfuerzos como piezas de un rompecabezas</h3>
<p style="margin-bottom: 0;">Cada acción que tomas, por más pequeña que parezca, es una pieza que contribuye al cuadro más grande. Imagina que estás armando un rompecabezas complejo: no puedes ver la imagen completa hasta que todas las piezas estén en su lugar, pero cada pieza tiene un valor único. Este enfoque te ayuda a conectar el esfuerzo diario con el propósito más amplio de tu vida.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 8
        },
        
        {
            "title": "Enfoque en el Proceso - Parte 3: Más Recomendaciones",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Más Estrategias</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Cambia la narrativa interna</h3>
<p style="margin-bottom: 0;">En lugar de decirte: "Todavía no he llegado" o "No soy lo suficientemente bueno", intenta cambiar tu lenguaje interno. Por ejemplo, di: "Estoy construyendo algo importante, paso a paso" o "El simple hecho de intentarlo ya es un acto de valentía." La manera en que te hablas a ti mismo afecta directamente tu percepción del proceso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Aprecia los microéxitos del camino</h3>
<p style="margin-bottom: 0;">Piensa en alguien que está aprendiendo a tocar un instrumento musical. Si solo se enfoca en tocar una pieza compleja perfectamente, puede sentirse desanimado. Pero si celebra los momentos en los que sus dedos se mueven con más fluidez o aprende un nuevo acorde, comenzará a disfrutar más del proceso de aprendizaje y menos del destino final.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 9
        },
        
        {
            "title": "Ejercicio: Enfoque en el Proceso",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Celebra el Proceso</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a celebrar tu ser.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Mi fiesta interior</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.2: Enfoque en el proceso y esfuerzo</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 10
        },
        
        {
            "title": "Subtema 3: Construyendo un Puente hacia el Amor Propio - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Construyendo un Puente hacia el Amor Propio</h1>

<p style="margin-bottom: 16px;">Amarse no es una meta lejana ni una frase bonita. Es un camino profundo que se recorre todos los días, especialmente si has pasado años siendo dura o duro contigo mismo, intentando encajar, cumpliendo expectativas o dejando tus necesidades para después.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Un Puente que se Construye</h3>
<p style="margin-bottom: 0;">En Alquimia del Cambio, entendemos el amor propio como un puente que se construye paso a paso, con conciencia, compasión y acciones coherentes. No se trata de decirte "me amo" mientras te ignorás, te abandonás o te exigís ser otra persona. Se trata de recordarte quién sos y actuar desde ese lugar de respeto, humanidad y valor interno.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 11
        },
        
        {
            "title": "Amor Propio - Parte 2: ¿Cómo Empezar a Amarte?",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">¿Cómo Empezar a Amarte?</h2>

<p style="margin-bottom: 16px; font-weight: 600;">Aquí algunas formas cotidianas de construir ese puente:</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Cuida tu diálogo interno</h3>
<p style="margin-bottom: 12px;">Observá cómo te hablás en tu día a día: cuando te equivocás, cuando no podés con todo, cuando algo no sale como esperás.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> La próxima vez que estés lavando los platos o caminando al trabajo, repetí en voz baja una frase amable como: "Estoy haciendo lo mejor que puedo, y eso es suficiente".</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Reconocé tus esfuerzos, no solo los resultados</h3>
<p style="margin-bottom: 12px;">El amor propio también se fortalece cuando reconoces que levantarte a pesar del cansancio, cocinarte algo nutritivo o responder un mensaje difícil es un acto de amor hacia ti.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> Mientras te cepillas los dientes por la noche, nombra una cosa que hiciste hoy que te hace sentir orgullosa o orgulloso.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Poné límites con amor, no con culpa</h3>
<p style="margin-bottom: 12px;">Decir "hoy necesito descansar" o "esto no me hace bien" es una forma de honrarte.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> Antes de aceptar un compromiso, tomate 5 segundos y pregúntate: ¿Lo hago por compromiso o por verdadero deseo?</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 12
        },
        
        {
            "title": "Amor Propio - Parte 3: Más Formas de Construir el Puente",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Más Formas de Cultivar el Amor Propio</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Elegí momentos que te nutran emocionalmente</h3>
<p style="margin-bottom: 12px;">El amor propio también se cultiva con pequeños gestos de cuidado diario: tomar un té con calma, escuchar tu música favorita, caminar en silencio o cocinar algo que disfrutes.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> Agenda 15 minutos por día solo para ti aunque sea para respirar, leer o estar en silencio.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Acepta tu historia y dejá de castigarte por el pasado</h3>
<p style="margin-bottom: 12px;">Todos tenemos heridas y errores, no eres eso, eres quien ha decidido seguir sanando.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> Escribí una nota o mensaje breve a tu "yo" del pasado reconociendo todo lo que ha enfrentado con valentía.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Permítete descansar sin sentir culpa</h3>
<p style="margin-bottom: 12px;">El descanso no es un lujo, es una necesidad emocional y física.</p>
<p style="margin-bottom: 0;"><strong>Actividad cotidiana:</strong> Al llegar a casa, en lugar de ir directo a cumplir tareas, regálate 10 minutos de pausa: una ducha consciente, un estiramiento o simplemente sentarte con una bebida caliente.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 13
        },
        
        {
            "title": "Ejercicio: Construyendo un Puente hacia el Amor Propio",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Conecta con tu Amor Propio</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a conectar con tu amor propio.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #3: Mi fiesta interior</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 3.3: Construyendo un puente hacia el amor propio</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 14
        },
        
        {
            "title": "Conclusión del Tema 3",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 3</h2>

<p style="margin-bottom: 16px;">Recuerda que cada pequeño paso que das es un logro en sí mismo. No te limites a esperar el "gran éxito" para sentirte orgulloso de ti.</p>

<p style="margin-bottom: 16px;">Cada momento de esfuerzo, cada desafío superado, y cada lección aprendida a lo largo del camino, son pruebas de tu crecimiento y tu capacidad de seguir adelante.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<p style="margin-bottom: 12px;">La verdadera magia está en el proceso, no solo en el resultado final. Cuando te enfocas en lo que haces y en cómo lo haces, te permites evolucionar, aprender y, sobre todo, disfrutar del viaje.</p>
<p style="margin-bottom: 0;">Así que sigue celebrando esos pequeños-grandes avances, porque son los que realmente te están llevando a donde deseas estar.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">¡Confía en el Proceso y en Ti Mismo!</h3>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 15
        },
        
        {
            "title": "¡Felicidades por Completar el Módulo 2!",
            "content": f"""<div style="{css()}">
<div style="background: {C_TITLE}; color: white; padding: 40px; border-radius: 15px; text-align: center; margin: 40px 0;">
<h1 style="margin-top: 0; color: white; font-size: 2.5em;">¡Felicidades!</h1>
<h2 style="color: white; margin-bottom: 20px;">Has completado el Módulo 2: Celebra tu ser</h2>
<p style="font-size: 1.2em; margin-bottom: 0;">Has dado un paso enorme en tu amor propio y autoaceptación.</p>
</div>

<div style="background: {C_BG_GRAY}; padding: 30px; border-radius: 10px; margin: 30px 0;">
<h3 style="color: {C_TITLE}; margin-top: 0; text-align: center;">Lo que has logrado:</h3>
<p style="text-align: center; margin-bottom: 16px;">✓ Identificaste tus fortalezas internas</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Miraste al interior con compasión</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Transformaste la autocrítica y el perfeccionismo</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Aprendiste a celebrar tus logros</p>
<p style="text-align: center; margin-bottom: 16px;">✓ Te enfocaste en el proceso</p>
<p style="text-align: center; margin-bottom: 0;">✓ Construiste un puente hacia el amor propio</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 16
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
    print(f"✅ {len(cards)} cards créées pour le Thème 3")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 3 DU MODULE 2")
        print("=" * 70)
        
        MODULE_ID = 2
        
        # Créer le thème 3
        theme3 = create_theme3(db, MODULE_ID)
        num_cards3 = create_theme3_cards(db, theme3.id)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 3 CRÉÉ - MODULE 2 COMPLET!")
        print("=" * 70)
        print(f"📚 Thème 3 ID: {theme3.id} ({num_cards3} cards)")
        print(f"\n🎉 Le Module 2 complet est maintenant disponible!")
        print("\n📊 Récapitulatif:")
        print("   - Thème 1: 13 cards")
        print("   - Thème 2: 14 cards")
        print(f"   - Thème 3: {num_cards3} cards")
        print(f"   Total: {13 + 14 + num_cards3} cards")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

