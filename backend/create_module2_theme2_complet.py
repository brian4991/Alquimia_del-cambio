"""
Script pour créer le Thème 2 du Module 2 COMPLET - fidèle au texte original
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
        title="Transformando la autoexigencia y perfeccionismo",
        content="El perfeccionismo y la autoexigencia extrema a menudo surgen del deseo de ser validados, de evitar el error o de sentirnos dignos.",
        order_number=2,
        module_id=module_id
    )
    db.add(theme)
    db.flush()
    print(f"✅ Thème 2 créé (ID: {theme.id})")
    return theme

def create_theme2_cards(db: Session, theme_id: int):
    """Cards du thème 2 - CONTENU COMPLET"""
    print("\n🎴 Création des cards du Thème 2...")
    
    cards = [
        {
            "title": "Bienvenida al Tema 2",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Transformando la Autoexigencia y Perfeccionismo</h1>

<p style="margin-bottom: 16px;">El perfeccionismo y la autoexigencia extrema a menudo surgen del deseo de ser validados, de evitar el error o de sentirnos dignos. Sin embargo, en lugar de impulsarnos, estas tendencias suelen llevarnos a la insatisfacción constante, el agotamiento y la sensación de que nunca somos "suficientes".</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">Un Cambio de Mentalidad</h3>
<p style="margin-bottom: 0;">Hacer un cambio de mentalidad no significa renunciar al esfuerzo o a la búsqueda de la excelencia, sino cambiar nuestra relación con ellos. Es aprender a aceptar que el error es parte del crecimiento, que no necesitamos ser perfectos para ser valiosos, y que la compasión hacia nosotros mismos es clave para avanzar con confianza y bienestar.</p>
</div>

<p style="margin-bottom: 16px;">Este proceso implica desaprender hábitos rígidos y construir una nueva mentalidad más flexible, equilibrada y amable.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        
        {
            "title": "Subtema 1: Darme Cuenta de los Pensamientos Autocríticos - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 1: Darme Cuenta de los Pensamientos Autocríticos</h1>

<p style="margin-bottom: 16px;">La autocrítica es como un eco constante que nos habla en la mente. A veces, esta voz crítica es tan fuerte que creemos que es nuestra propia verdad, cuando en realidad es solo un patrón aprendido.</p>

<p style="margin-bottom: 16px;">Si te detienes a escucharla, podrías notar que esa voz no te impulsa a mejorar, sino que te frena, te hace sentir insuficiente y puede disminuir tu confianza.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Origen de la Autocrítica</h3>
<p style="margin-bottom: 0;">La autocrítica se forma a menudo en la infancia, cuando internalizamos las expectativas de figuras autoritarias, como padres o maestros. Esos mensajes, aunque bien intencionados, se convierten en un "guión" que seguimos de adultos, interpretando nuestras acciones con la misma dureza con la que lo hacían cuando éramos niños.</p>
</div>

<p style="margin-bottom: 16px;">Este patrón puede ser muy dañino, ya que el cerebro tiende a enfocarse más en lo negativo, una tendencia conocida como <strong>sesgo de negatividad</strong>. Por lo tanto, la crítica constante puede reforzar la idea de que nunca somos lo suficientemente buenos.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        
        {
            "title": "Tres Recomendaciones Clave - Parte 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Tres Recomendaciones Clave</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">1. Identifica la voz crítica</h3>
<p style="margin-bottom: 12px;"><strong>Imagina que cometiste un error en el trabajo y piensas: "Soy un desastre, nunca hago nada bien".</strong></p>
<p style="margin-bottom: 12px;"><strong>Cuestiónalo:</strong> ¿Es esto completamente cierto? ¿Realmente nunca haces nada bien? Tal vez hayas hecho muchas cosas correctamente antes, pero este error puntual activa tu voz crítica.</p>
<p style="margin-bottom: 0;"><strong>Replantea el pensamiento:</strong> "Cometí un error, pero eso no define todo mi desempeño. Aprenderé de esto y seguiré mejorando". Esto te ayuda a desafiar la negatividad y adoptar una perspectiva más equilibrada.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">2. Practica la autocompasión</h3>
<p style="margin-bottom: 0;">Habla contigo mismo/a como lo harías con un amigo cercano. Reconoce tus errores sin juzgarte severamente, y recuerda que todos cometemos fallos y eso no define tu valor.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">3. Reestructura tus pensamientos</h3>
<p style="margin-bottom: 12px;">Cuando te sientas crítico/a, cambia la perspectiva. En lugar de pensar en lo negativo, busca aprender de la situación.</p>
<p style="margin-bottom: 12px;"><strong>Por ejemplo, piensas:</strong> "Siempre me equivoco".</p>
<p style="margin-bottom: 0;"><strong>Replantea:</strong> "A veces me equivoco, pero eso no significa que no pueda hacerlo bien".</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 3
        },
        
        {
            "title": "Pensamientos Autocríticos - Parte 3: Conclusión",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Comprendiendo la Autocrítica</h2>

<p style="margin-bottom: 16px;">Desde la psicología, podemos aprender que la autocrítica no solo está vinculada a nuestra infancia y a las expectativas de figuras autoritarias, sino que también está profundamente relacionada con nuestra necesidad de pertenencia y el miedo al rechazo.</p>

<div style="background: {C_BG_GRAY}; padding: 20px; border-radius: 8px; margin: 24px 0;">
<p style="margin-bottom: 12px;">La crítica interna, al no ser gestionada adecuadamente, puede generar un ciclo de ansiedad, inseguridad y estrés, lo cual impacta negativamente en nuestra autoestima y bienestar emocional.</p>
<p style="margin-bottom: 0;">Además, al reconocer estos patrones, podemos desarrollar un diálogo interno más saludable, mejorando nuestra capacidad para gestionar el estrés y promover un crecimiento personal basado en la autocompasión, no en la autoexigencia.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 4
        },
        
        {
            "title": "Ejercicio: Darme Cuenta de los Pensamientos Autocríticos",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Reconoce tu Perfeccionismo</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu perfeccionismo.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Perfectamente imperfect@</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.1: Darme cuenta de los pensamientos autocríticos</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 5
        },
        
        {
            "title": "Subtema 2: El Perfeccionismo - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 2: El Perfeccionismo</h1>

<p style="margin-bottom: 16px;">El perfeccionismo puede ser una fuerza poderosa, pero también destructiva. A menudo se enmascara como un impulso hacia la excelencia, pero en realidad, puede ser una forma de miedo al fracaso y al rechazo.</p>

<p style="margin-bottom: 16px;">La psicología sugiere que el perfeccionismo se desarrolla a partir de la necesidad de aprobación externa o de sentir que debemos ser perfectos para merecer amor y aceptación. Sin embargo, la verdad es que esta búsqueda constante de la perfección puede dejarnos sintiéndonos insuficientes y estancados.</p>

<div style="background: {C_BG_GRAY}; border-left: 5px solid {C_TITLE}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">La Trampa del Perfeccionismo</h3>
<p style="margin-bottom: 0;">El perfeccionismo se asocia con altos niveles de ansiedad, estrés y autoexigencia. Es como si, a cada paso, te dijeras a ti mismo: "Nada de esto es suficiente". Las personas perfeccionistas suelen establecer estándares inalcanzables y, cuando no los alcanzan, experimentan una fuerte sensación de fracaso y desilusión.</p>
</div>

<p style="margin-bottom: 16px;">Este ciclo continuo puede llevarnos a procrastinar, ya que, en el fondo, tememos que el resultado nunca sea lo suficientemente bueno.</p>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        
        {
            "title": "El Perfeccionismo - Parte 2: Recomendaciones Prácticas",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Recomendaciones Prácticas para Mejorar el Perfeccionismo</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Establece estándares realistas</h3>
<p style="margin-bottom: 12px;">A menudo, el perfeccionista establece metas tan altas que se vuelven inalcanzables. Un paso clave es aprender a poner expectativas realistas y alcanzables. Esto no significa conformarse, sino permitirte ser humano y reconocer que la perfección no es necesaria para tener éxito.</p>
<p style="margin-bottom: 0;"><strong>Tip:</strong> Pregúntate: "¿Esto es realmente lo mejor que puedo hacer en este momento, dadas las circunstancias?" Establecer metas alcanzables te permitirá sentirte exitoso, incluso cuando las cosas no sean perfectas.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">Aprende a disfrutar del proceso, no solo del resultado</h3>
<p style="margin-bottom: 12px;">El perfeccionista está tan centrado en el resultado final que pierde de vista la importancia del proceso. Disfrutar del proceso, incluso cuando no es perfecto, puede ser una de las formas más efectivas de liberarte del perfeccionismo. Al enfocarte en el proceso, permites que cada paso, aunque pequeño, sea valioso.</p>
<p style="margin-bottom: 0;"><strong>Ejemplo práctico:</strong> Si estás trabajando en un proyecto creativo, en lugar de obsesionarte con que el producto final debe ser perfecto, disfruta de cada fase del proceso: la exploración de ideas, los errores, los ajustes. Cada uno de esos momentos tiene un valor único que te ayudará a crecer.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Haz pequeños actos de imperfección consciente</h3>
<p style="margin-bottom: 12px;">Un ejercicio poderoso es hacer algo intencionalmente imperfecto. Esto puede ser tan simple como dejar de lado una tarea que siempre tratas de perfeccionar, o realizar una actividad sin corregirla mil veces.</p>
<p style="margin-bottom: 0;"><strong>Tip:</strong> Al realizar estos pequeños actos de imperfección, permite que te sientas bien con lo que has hecho, sin necesidad de hacer ajustes adicionales. Esto te ayudará a reducir la ansiedad y a aceptar que lo suficiente está bien.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        
        {
            "title": "El Perfeccionismo - Parte 3: Conclusión",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Libérate del Perfeccionismo</h2>

<p style="margin-bottom: 16px;">El perfeccionismo, aunque inicialmente puede parecer un impulso positivo hacia la mejora, a menudo termina siendo una trampa emocional que nos impide avanzar.</p>

<p style="margin-bottom: 16px;">Al hacerle frente y aprender a ser más compasivos con nosotros mismos, podemos liberar esa carga y redirigir nuestra energía hacia metas realistas y alcanzables.</p>

<div style="background: {C_TITLE}; color: white; padding: 20px; border-radius: 10px; margin: 24px 0;">
<h3 style="margin-top: 0; color: white;">La Clave</h3>
<p style="margin-bottom: 0;">La clave es recordar que no tenemos que ser perfectos para ser valiosos; la imperfección es parte de lo que nos hace humanos.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 8
        },
        
        {
            "title": "Ejercicio: Carta al Perfeccionismo",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Reconoce tu Imperfección</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu imperfección.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Perfectamente imperfect@</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.2: Carta al perfeccionismo - Perdón y Reconocimiento</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 9
        },
        
        {
            "title": "Subtema 3: Desafío de la Imperfección - Parte 1",
            "content": f"""<div style="{css()}">
<h1 style="color: {C_TITLE}; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Subtema 3: Desafío de la Imperfección</h1>

<p style="margin-bottom: 16px;">El desafío de la imperfección es un paso esencial en el proceso de liberarnos de la tiranía del perfeccionismo.</p>

<p style="margin-bottom: 16px;">En la psicología, entendemos que la imperfección es una parte inevitable y valiosa de la experiencia humana. Sin embargo, nuestra cultura a menudo nos enseña a temerla, asociándola con el fracaso, la vergüenza o la incompetencia.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">Una Nueva Perspectiva</h3>
<p style="margin-bottom: 0;">Pero, si dejamos de ver la imperfección como algo negativo y la aceptamos como una oportunidad de crecimiento, podemos transformarla en una herramienta poderosa para avanzar en nuestra vida emocional.</p>
</div>

<p style="margin-bottom: 16px;">La perfección no solo es inalcanzable, sino que puede ser perjudicial. Entendemos que la imperfección no es sinónimo de fracaso, sino de proceso, aprendizaje y crecimiento.</p>

<p style="margin-bottom: 16px;">Nos permite experimentar, fallar, aprender y, lo más importante, humanizarnos. La perfección crea una falsa imagen de control, pero la imperfección nos conecta con nuestra vulnerabilidad y nuestra autenticidad.</p>
</div>""",
            "card_type": "theory",
            "order_number": 10
        },
        
        {
            "title": "Desafío de la Imperfección - Parte 2: Qué Puedes Hacer",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Qué Puedes Hacer para Aliviar el Perfeccionismo</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">1. Abraza el "suficientemente bueno"</h3>
<p style="margin-bottom: 12px;">En lugar de buscar siempre el "mejor resultado", pregúntate: "¿Esto es lo suficientemente bueno?" Practicar el concepto de "suficientemente bueno" ayuda a reducir la presión y te permite avanzar sin esperar que todo sea perfecto. Este enfoque no solo es más realista, sino también más saludable.</p>
<p style="margin-bottom: 0;"><strong>Ejemplo práctico:</strong> Imagina que estás trabajando en un proyecto en el que quieres que todo esté impecable. En lugar de corregir una y otra vez, decide que cuando hayas cumplido con los objetivos principales, es suficiente. Reconoce tus logros, sin sobrecargarte buscando la perfección.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">2. Reflexiona sobre lo que puedes aprender de tus errores</h3>
<p style="margin-bottom: 12px;">Cuando cometemos errores, nuestro cerebro tiene la oportunidad de aprender y adaptarse. Este es un principio clave de la neuroplasticidad: la capacidad del cerebro para formar nuevas conexiones. Los errores no son fracasos, sino momentos de crecimiento y aprendizaje.</p>
<p style="margin-bottom: 0;"><strong>Tip:</strong> Cuando te enfrentes a un error o fallo, pregúntate: "¿Qué puedo aprender de esto? ¿Cómo puedo mejorar la próxima vez?". Esta perspectiva te ayudará a ver la imperfección como parte natural de tu proceso de crecimiento.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 11
        },
        
        {
            "title": "Desafío de la Imperfección - Parte 3: Más Estrategias",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Más Estrategias para Abrazar la Imperfección</h2>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">3. Celebra los "fracasos"</h3>
<p style="margin-bottom: 12px;">Cambia tu narrativa en torno al fracaso. En lugar de verlo como algo negativo, empieza a verlo como un peldaño hacia el éxito. La gente exitosa aunque también puede tener miedo de fracasar; simplemente aprenden de los fracasos y siguen adelante.</p>
<p style="margin-bottom: 0;"><strong>Ejemplo práctico:</strong> Si no conseguiste un resultado esperado, celebra la valentía de haberte lanzado al intento. Di algo como: "Aunque no salió como esperaba, he aprendido X, y eso me acerca más a mi meta". Al hacerlo, transformas el fracaso en un paso hacia el éxito.</p>
</div>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_TITLE}; padding: 20px; margin-bottom: 16px; border-radius: 5px;">
<h3 style="color: {C_ACCENT}; margin-top: 0;">4. Acepta tu vulnerabilidad</h3>
<p style="margin-bottom: 12px;">La imperfección está intrínsecamente conectada con nuestra vulnerabilidad. Reconocer que no somos infalibles, que cometemos errores y que tenemos limitaciones, nos conecta con nuestra humanidad y nos permite desarrollar empatía hacia nosotros mismos y los demás.</p>
<p style="margin-bottom: 0;"><strong>Tip:</strong> En lugar de ocultar tus fallos o debilidades, compártelos de manera auténtica con las personas cercanas. Esto no solo ayuda a reducir la carga emocional, sino que también fomenta relaciones más profundas y genuinas.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 12
        },
        
        {
            "title": "Conclusión del Tema 2",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px; border-bottom: 3px solid {C_ACCENT}; padding-bottom: 12px;">Conclusión del Tema 2</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">El desafío de la imperfección es <strong>liberador</strong>.</p>

<p style="margin-bottom: 16px;">En lugar de luchar contra lo que somos, podemos aprender a aceptar y abrazar nuestras imperfecciones. Esta aceptación nos permite vivir de una manera más auténtica, compasiva y enfocada en el proceso.</p>

<p style="margin-bottom: 16px;">Al hacerlo, reducimos la presión interna y podemos disfrutar más plenamente del camino, en lugar de estar atrapados en la meta perfecta.</p>

<div style="background: {C_BG_LIGHT}; border-left: 5px solid {C_ACCENT}; padding: 20px; margin: 24px 0; border-radius: 5px;">
<h3 style="color: {C_TITLE}; margin-top: 0;">La Verdadera Riqueza</h3>
<p style="margin-bottom: 0;">La verdadera riqueza de la vida radica en lo imperfecto, lo inesperado y lo genuino.</p>
</div>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 32px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.4em;">Siguiente Paso</h3>
<p style="margin-bottom: 0; font-size: 1.1em;">Continúa al Tema 3: Celebrar y celebrarse</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 13
        },
        
        {
            "title": "Ejercicio: Desafío de la Imperfección",
            "content": f"""<div style="{css()}">
<h2 style="color: {C_TITLE}; font-size: 1.8em; margin-bottom: 20px;">Abraza tu Imperfección</h2>

<p style="margin-bottom: 20px; font-size: 1.1em;">A continuación vas a empezar a reconocer tu imperfección.</p>

<div style="background: {C_TITLE}; color: white; padding: 24px; border-radius: 10px; margin: 28px 0; text-align: center;">
<h3 style="margin-top: 0; color: white; font-size: 1.5em;">Ejercicio #2: Perfectamente imperfect@</h3>
<p style="font-size: 1.2em; margin-bottom: 0; font-weight: 600;">Ejercicio 2.3: Desafío de la imperfección</p>
</div>

<p style="margin-top: 24px; color: #5a5a5a; font-style: italic;">Ve a realizar el siguiente ejercicio.</p>
</div>""",
            "card_type": "exercise",
            "order_number": 14
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
    print(f"✅ {len(cards)} cards créées pour le Thème 2")
    return len(cards)

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DU THÈME 2 DU MODULE 2")
        print("=" * 70)
        
        MODULE_ID = 2
        
        # Créer le thème 2
        theme2 = create_theme2(db, MODULE_ID)
        num_cards2 = create_theme2_cards(db, theme2.id)
        
        print("\n" + "=" * 70)
        print("✅ THÈME 2 CRÉÉ")
        print("=" * 70)
        print(f"📚 Thème 2 ID: {theme2.id} ({num_cards2} cards)")
        print(f"\n🎯 Exécute maintenant le script pour le thème 3")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

