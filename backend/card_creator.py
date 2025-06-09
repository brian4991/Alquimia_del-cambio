from sqlalchemy.orm import Session
from models import ThemeCard

def create_theme_cards(db: Session, themes: list):
    """Create cards for each theme based on module1.txt content"""
    
    # Get theme references
    theme1, theme2, theme3 = themes
    
    # ===============================
    # TEMA 1 CARDS: Explorando mi historia emocional
    # ===============================
    
    theme1_cards = [
        {
            "title": "Introducción al Tema",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Explorando mi Historia Emocional</h1>

<p><strong>El propósito</strong> de este tema es guiarte a través de la exploración consciente de tu historia emocional.</p>

<p>A lo largo de nuestra vida, vamos acumulando experiencias que moldean la forma en que sentimos, reaccionamos y gestionamos nuestras emociones.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">¿Por qué es importante?</h2>

<p>Al reconocer los patrones emocionales y descubrir las raíces de estos, podrás comprender mejor cómo las experiencias pasadas siguen influyendo en tu presente.</p>

<p>Este autoconocimiento es fundamental para aprender a gestionar las emociones de manera más consciente y efectiva.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Recursos y Subtemas",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">En este tema exploraremos:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Subtemas:</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li><strong>Reconocer patrones emocionales</strong></li>
<li><strong>Raíces emocionales</strong></li>
</ul>
</div>

<div style="background: #e8f5e8; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Recursos disponibles:</h3>
<ul style="list-style-type: dash; margin-left: 20px;">
<li>Mi carta de aceptación y compromiso</li>
<li>Emocionario, técnicas de gestión emocional para el día a día</li>
<li>¿Qué necesito realmente cuando me siento así?</li>
</ul>
</div>

<div style="background: #fff3cd; padding: 15px; border: 1px solid #ffeaa7; border-radius: 5px; margin: 15px 0;">
<p><strong>¡Importante!</strong> No olvides tu carta de aceptación y compromiso: es lo primero antes de comenzar. Disfruta el viaje que te espera.</p>
</div>

<p>Empezamos con dos ejercicios muy valiosos que son el punto de partida para reconectar con tu historia.</p>
</div>""",
            "card_type": "resources",
            "order_number": 2
        },
        {
            "title": "¿Qué son los Patrones Emocionales?",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Reconocer Patrones Emocionales</h1>

<p>Los patrones emocionales son <strong>respuestas automáticas</strong> que repetimos en situaciones similares a lo largo de nuestra vida.</p>

<p>Estas respuestas se forman a partir de nuestras primeras experiencias emocionales y las conexiones que hacemos entre emociones y eventos específicos.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Ejemplos:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #e74c3c; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Ejemplo 1:</h3>
<p>Si en nuestra infancia asociamos la crítica con el miedo al rechazo, es probable que, en la vida adulta, respondamos a cualquier forma de crítica con ansiedad o inseguridad.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #e74c3c; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Ejemplo 2:</h3>
<p>Si creciste en un ambiente donde la expresión emocional era reprimida, es probable que desarrolles un patrón de evitación emocional en tu vida adulta.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "La Ciencia: Neuroplasticidad",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Base Científica</h2>

<p>Desde el campo de la <strong>psicología cognitiva</strong>, se ha demostrado que nuestras emociones están en gran parte influenciadas por esquemas mentales, o "mapas" que desarrollamos a lo largo del tiempo.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Neuroplasticidad</h3>

<p>La <strong>neurociencia</strong> nos muestra que el cerebro puede cambiar sus conexiones, lo que significa que podemos "reprogramar" cómo reaccionamos emocionalmente a través del autoconocimiento y la práctica consciente.</p>

<p>Este proceso se conoce como <strong>neuroplasticidad</strong>, y es lo que nos permite adoptar nuevas formas de gestionar nuestras emociones una vez que somos conscientes de los patrones emocionales que hemos desarrollado.</p>

<div style="background: #e8f5e8; padding: 15px; border: 1px solid #27ae60; border-radius: 5px; margin: 15px 0;">
<p><strong>La buena noticia:</strong> Identificar estos patrones es esencial para desactivarlos.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 4
        },
        {
            "title": "Señales de Patrones Recurrentes",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Señales de Patrones Emocionales Recurrentes:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #e74c3c; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">1. Reacciones exageradas a ciertas situaciones</h3>
<p>A veces, cuando alguien nos critica o dice algo que no nos gusta, podemos sentirnos muy enojados o muy tristes, incluso si lo que dijeron no era tan grave. Esto pasa porque hemos aprendido a reaccionar así en el pasado.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #f39c12; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">2. Sentir las mismas emociones en situaciones parecidas</h3>
<p>Puede que te sientas frustrado o nervioso en ciertos lugares o con ciertas personas, como en el trabajo o en una reunión social. Esto ocurre porque esas situaciones te recuerdan a otras donde ya te sentiste así antes.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #9b59b6; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">3. Evitar ciertos temas o emociones</h3>
<p>Si hay cosas que prefieres no hablar o sentir, como el miedo o la tristeza, podrías intentar ignorarlas. En lugar de enfrentarlas, quizás optes por aislarte o discutir con los demás para no sentirte vulnerable.</p>
</div>

<div style="background: #e8f5e8; padding: 15px; border: 1px solid #27ae60; border-radius: 5px; margin: 15px 0;">
<p>Al identificar estos patrones, podemos empezar a comprender que nuestras emociones <strong>no siempre reflejan la realidad del presente</strong>, sino que están condicionadas por experiencias anteriores.</p>
</div>
</div>""",
            "card_type": "practical",
            "order_number": 5
        },
        {
            "title": "¿Qué son las Raíces Emocionales?",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Raíces Emocionales</h1>

<p>Las raíces emocionales son las <strong>experiencias pasadas</strong>, a menudo en la infancia o adolescencia, que forman la base de nuestros patrones emocionales actuales.</p>

<p>Estas experiencias tempranas, tanto positivas como negativas, juegan un papel crucial en el desarrollo de nuestro sistema emocional.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Teoría del Apego - John Bowlby</h2>

<p>En <strong>psicología del desarrollo</strong>, el modelo del apego propuesto por John Bowlby sostiene que nuestras primeras relaciones, particularmente con los cuidadores primarios, influyen en cómo formamos relaciones y regulamos nuestras emociones en el futuro.</p>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Ejemplo:</h3>
<p>Si en nuestra infancia aprendimos que expresar tristeza no era aceptado o no recibía la validación necesaria, podríamos haber desarrollado una tendencia a reprimir esa emoción.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        {
            "title": "Impacto de las Raíces Emocionales",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Impacto de las Raíces Emocionales:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #e74c3c; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Apego inseguro</h3>
<p>Puede generar dependencia emocional o dificultades para confiar en los demás.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #f39c12; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Experiencias de rechazo</h3>
<p>Pueden llevar a una sensibilidad exagerada ante la crítica o el conflicto.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #9b59b6; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Ambientes familiares poco expresivos emocionalmente</h3>
<p>Pueden resultar en la incapacidad de expresar necesidades emocionales de manera asertiva.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #e67e22; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Momentos traumáticos</h3>
<p>Pueden generar reacciones desproporcionadas ante situaciones de pérdida o estrés en la vida adulta.</p>
</div>

<hr style="margin: 20px 0; border: 1px solid #bdc3c7;">

<h3 style="color: #2c3e50;">El poder del autoconocimiento</h3>

<p>Explorar estas raíces no solo es importante para comprender por qué reaccionamos de cierta manera, sino que también nos permite <strong>tomar el control</strong> sobre cómo queremos responder en el futuro.</p>

<p>El autoconocimiento de nuestras raíces emocionales nos da el poder de cambiar nuestras narrativas emocionales y romper patrones que ya no nos sirven.</p>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        {
            "title": "Conclusión del Tema 1",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Construyendo tu Fundamento Emocional</h2>

<p>Este tema es el <strong>fundamento</strong> para construir un mayor entendimiento de ti mismo a nivel emocional:</p>

<p><strong>Reconocer patrones emocionales</strong> es el primer paso para observar cómo respondes a situaciones y relaciones.</p>

<p><strong>Explorar raíces emocionales</strong> te permitirá entender por qué reaccionas de esa manera.</p>

<p>Con este conocimiento, comenzarás a tomar decisiones más conscientes sobre cómo gestionar tus emociones y evitarás caer en respuestas automáticas que no contribuyen a tu bienestar.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Reflexión Final</h2>

<p>Es crucial recordar que las emociones <strong>no se generan en el vacío</strong>; están profundamente conectadas a nuestra historia y a las experiencias que nos han moldeado.</p>

<p>Este proceso de autoexploración te brinda una visión más clara de esas conexiones, permitiéndote tomar las riendas de tu mundo emocional con <strong>mayor comprensión y compasión</strong>.</p>

<hr style="margin: 20px 0; border: 1px solid #bdc3c7;">

<div style="background: #e8f5e8; padding: 15px; border: 1px solid #27ae60; border-radius: 5px; margin: 15px 0;">
<p><strong>Próximo paso:</strong> En el Tema 2 profundizaremos en el autoconocimiento emocional para identificar tus emociones primarias y reconocer tus necesidades.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 8
        }
    ]
    
    # Create Theme 1 cards
    for card_data in theme1_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme1.id
        )
        db.add(card)
    
    # ===============================
    # TEMA 2 CARDS: Autoconocimiento emocional profundo
    # ===============================
    
    theme2_cards = [
        {
            "title": "Autoconocimiento Emocional Profundo",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Tema 2: Autoconocimiento Emocional Profundo</h1>

<h2 style="color: #2c3e50; margin-top: 25px;">Objetivo del tema</h2>

<p>En este tema, profundizaremos en la <strong>identificación de tus emociones primarias</strong> y en el <strong>reconocimiento de las necesidades emocionales</strong>.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">¿Por qué es crucial?</h2>

<p>Es crucial entender que nuestras emociones no solo son respuestas inmediatas a los eventos, sino que también son <strong>señales</strong> que nos indican nuestras necesidades internas no satisfechas.</p>

<p>Al desarrollar un mayor autoconocimiento emocional, podrás:</p>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Identificar estas señales</li>
<li>Actuar de manera más consciente</li>
</ul>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Las 6 Emociones Primarias",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">¿Qué son las emociones primarias?</h2>

<p>Las emociones primarias son las <strong>respuestas emocionales más básicas e instintivas</strong> que todos los seres humanos experimentan.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Las 6 emociones primarias universales:</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>**Miedo** 😰</li>
<li>**Tristeza** 😢</li>
<li>**Alegría** 😊</li>
<li>**Enojo** 😠</li>
<li>**Sorpresa** 😮</li>
<li>**Asco** 🤢</li>
</ul>

<h3 style="color: #2c3e50; margin-top: 25px;">Función evolutiva</h3>

<p>Estas emociones tienen una <strong>función evolutiva</strong>: nos ayudan a responder a nuestro entorno de manera rápida para sobrevivir y adaptarnos.</p>

<p>Sin embargo, a menudo no estamos completamente conscientes de estas emociones, y es común que las disfrazamos o las racionalicemos en lugar de experimentarlas plenamente.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">¿Por qué identificarlas?</h3>

<p>Es importante aprender a identificar estas emociones a medida que surgen, <strong>sin juicio ni represión</strong>, ya que cada una de ellas contiene información valiosa sobre lo que necesitamos en ese momento.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "Beneficios de Identificar Emociones",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Beneficios de identificar las emociones primarias:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Consciencia emocional</h3>
<p>Al ser más conscientes de tus emociones primarias, puedes actuar de manera más alineada con tus valores y deseos, en lugar de reaccionar impulsivamente.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Prevención de conflictos</h3>
<p>Al identificar las emociones en el momento en que surgen, puedes evitar que escalen en situaciones conflictivas o dañinas.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Desarrollo de empatía</h3>
<p>Cuando reconoces tus propias emociones, también te vuelves más empático hacia las emociones de los demás, lo que mejora las relaciones interpersonales.</p>
</div>

<h3 style="color: #2c3e50; margin-top: 25px;">Paul Ekman - Investigación</h3>

<p>Según <strong>Paul Ekman</strong>, un reconocido psicólogo en el campo de las emociones, las emociones primarias son universales y están presentes en todas las culturas.</p>

<p>Esto sugiere que, aunque las expresiones emocionales pueden variar entre diferentes sociedades, la experiencia interna de estas emociones es compartida por todos los seres humanos.</p>

<p>Ekman también señala que identificar y regular estas emociones es fundamental para el bienestar psicológico, ya que nos permiten procesar nuestras experiencias de manera efectiva.</p>
</div>""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "Reconocer Necesidades Emocionales",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">El sistema de alerta emocional</h2>

<p>Cada emoción primaria está conectada a una <strong>necesidad emocional</strong>. Las emociones actúan como un sistema de alerta que nos indica si nuestras necesidades están siendo satisfechas o no.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Ejemplos de conexiones:</h3>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🔸 El miedo</h4>
<p>Puede señalar una necesidad de seguridad</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🔸 La tristeza</h4>
<p>Puede revelar una necesidad de apoyo o consuelo</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🔸 El enojo</h4>
<p>Puede indicar que sentimos que se ha violado un límite importante</p>
</div>

<p>Al identificar estas necesidades, puedes empezar a tomar acciones más efectivas para satisfacerlas y evitar quedarte atrapado en ciclos emocionales insalubres.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">⚠️ Riesgos de ignorar las necesidades</h3>

<p>El reconocimiento de las necesidades emocionales es una habilidad esencial para el autoconocimiento. Sin este reconocimiento, corremos el riesgo de malinterpretar nuestras emociones y responder de manera incorrecta a ellas.</p>

<p>A menudo, cuando ignoramos nuestras necesidades, nos sentimos desbordados, desconectados de nosotros mismos y de los demás.</p>
</div>""",
            "card_type": "theory",
            "order_number": 4
        },
        {
            "title": "Beneficios de Reconocer Necesidades",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Beneficios de reconocer necesidades emocionales:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Satisfacción personal</h3>
<p>Ser consciente de tus necesidades emocionales te permite satisfacerlas de manera efectiva, lo que lleva a una mayor sensación de bienestar y satisfacción.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Reducción del estrés</h3>
<p>Al entender y abordar tus necesidades emocionales, puedes reducir la ansiedad y el estrés relacionados con la insatisfacción emocional.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Mejora en las relaciones</h3>
<p>Reconocer tus propias necesidades emocionales también te permite comunicarte mejor con los demás y establecer relaciones más saludables y auténticas.</p>
</div>

<h3 style="color: #2c3e50; margin-top: 25px;">Carl Rogers - Teoría Humanista</h3>

<p><strong>Carl Rogers</strong>, uno de los fundadores de la psicología humanista, destacó la importancia de las necesidades emocionales en su teoría de la "persona completa".</p>

<p>Rogers sostuvo que cuando las personas son conscientes de sus necesidades y trabajan activamente para satisfacerlas, tienden a ser más equilibradas y felices.</p>

<p>En cambio, cuando estas necesidades se ignoran o se niegan, surgen conflictos internos y disfunciones en las relaciones.</p>

<p>Investigaciones recientes en el campo de la <strong>psicología positiva</strong> sugieren que la identificación de las necesidades emocionales y la capacidad de satisfacerlas son claves para el desarrollo de resiliencia emocional.</p>
</div>""",
            "card_type": "theory",
            "order_number": 5
        },
        {
            "title": "Conclusión del Tema 2",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Conexión Profunda Contigo Mismo/a</h2>

<p>Este tema te llevará a un nivel más profundo de conexión contigo mismo/a.</p>

<p>Identificar tus emociones primarias y las necesidades emocionales que subyacen a estas es un paso crucial para entender por qué reaccionas de ciertas maneras en situaciones cotidianas y cómo puedes tomar decisiones más alineadas con tu bienestar.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Herramientas para la vida diaria</h2>

<p>Al desarrollar este nivel de autoconocimiento emocional, estarás mejor equipado/a para responder de manera más intencional y saludable en tu vida diaria, creando un equilibrio emocional más sólido.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Proceso aplicable</h2>

<p>En la próxima sección, te guiaré a través de ejercicios específicos que te ayudarán a poner en práctica esta identificación de emociones y el reconocimiento de tus necesidades emocionales, haciendo que el proceso de autoconocimiento sea claro y aplicable.</p>

<hr style="margin: 20px 0; border: 1px solid #bdc3c7;">

<div style="background: #e8f5e8; padding: 15px; border: 1px solid #27ae60; border-radius: 5px; margin: 15px 0;">
<p><strong>Próximo paso:</strong> En el Tema 3 aprenderemos técnicas concretas para gestionar y expresar nuestras emociones de manera saludable.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 6
        }
    ]
    
    # Create Theme 2 cards
    for card_data in theme2_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme2.id
        )
        db.add(card)
    
    # Continue with Theme 3 cards...
    _create_theme3_cards(db, theme3)

def _create_theme3_cards(db: Session, theme3):
    """Create cards for Theme 3"""
    
    theme3_cards = [
        {
            "title": "Gestionando y Expresando Emociones",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Tema 3: Gestionando y Expresando Emociones</h1>

<h2 style="color: #2c3e50; margin-top: 25px;">El paso final hacia el dominio emocional</h2>

<p>En esta última parte del módulo, nos adentraremos en cómo <strong>gestionar y expresar</strong> nuestras emociones de manera saludable y efectiva.</p>

<p>Saber identificar nuestras emociones es un primer paso esencial, pero ser capaces de <strong>regularlas y expresarlas de manera asertiva</strong> es lo que realmente nos permite avanzar hacia una vida más equilibrada y consciente.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Herramientas que desarrollarás:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Subtema 1: Técnicas de regulación emocional</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Las 7 técnicas prácticas para gestionar emociones intensas</li>
<li>Estrategias basadas en investigación científica</li>
<li>Aplicación en tu vida diaria</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Subtema 2: Comunicación asertiva</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Cómo expresar lo que sientes sin ser agresivo o pasivo</li>
<li>Técnicas para comunicar necesidades de manera efectiva</li>
<li>Construcción de relaciones más saludables</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Subtema 3: Tu caja de herramientas emocionales</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Recopilación de todas las técnicas aprendidas</li>
<li>Organización personal de recursos</li>
<li>Plan de mantenimiento emocional</li>
</ul>
</div>

<p>Este tema te proporcionará las herramientas necesarias para gestionar las emociones más difíciles y comunicar lo que sientes y necesitas de una manera clara, respetuosa y efectiva.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "¿Por qué Regular las Emociones?",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Técnicas de Regulación Emocional</h2>

<h3 style="color: #2c3e50; margin-top: 25px;">¿Por qué es importante la regulación emocional?</h3>

<p>Las emociones, especialmente las intensas, pueden ser abrumadoras si no sabemos cómo manejarlas.</p>

<p>La <strong>regulación emocional</strong> es la capacidad de manejar y responder a una experiencia emocional de manera saludable.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Teoría de James Gross</h3>

<p>La teoría de <strong>James Gross</strong> sobre la regulación emocional ha mostrado que quienes desarrollan esta habilidad son más capaces de:</p>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>✅ Mantener relaciones interpersonales satisfactorias</li>
<li>✅ Tener menos niveles de estrés</li>
<li>✅ Gozar de mayor bienestar general</li>
</ul>

<h3 style="color: #2c3e50; margin-top: 25px;">Estrategias principales:</h3>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🔄 Reevaluación del pensamiento</h4>
<p>Reinterpretar una situación para cambiar su impacto emocional. En lugar de ver un evento como una amenaza, puedes aprender a verlo como un desafío o una oportunidad de crecimiento.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🧘 Mindfulness y atención plena</h4>
<p>Nos ayuda a observar nuestras emociones sin juzgarlas, reduciendo su intensidad y permitiéndonos responder con mayor claridad.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🫁 Respiración y técnicas de relajación</h4>
<p>El control de la respiración es muy efectivo para disminuir la activación fisiológica asociada con el estrés o la ira.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "Técnica 1-2: Validación y Respiración",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">🛠️ Técnicas Prácticas para el Día a Día</h2>

<h3 style="color: #2c3e50; margin-top: 25px;">1. ✅ Reconoce y valida tus emociones</h3>

<p>Uno de los primeros pasos en la regulación emocional es ser consciente de lo que sientes. En lugar de ignorar tus emociones o juzgarte por sentirlas, tómate un momento para reconocerlas y aceptarlas.</p>

<p><strong>📖 Ejemplo:</strong> Si estás frustrado después de un día difícil en el trabajo, en lugar de decir "No debería sentirme así", trata de decir "Es normal sentirme frustrado después de un día así". Esta validación te permitirá tomar decisiones más sabias sobre cómo manejar la emoción.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">2. 🫁 Practica la respiración consciente</h3>

<p>Cuando sientas que una emoción intensa, como la ansiedad o la ira, está aumentando, una técnica rápida y efectiva es la respiración profunda.</p>

<p><strong>💡 Técnica 4-4-4:</strong></p>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Inhala por la nariz durante <strong>4 segundos</strong></li>
<li>Sostén el aire por <strong>4 segundos</strong></li>
<li>Exhala lentamente por la boca durante <strong>4 segundos</strong></li>
</ul>

<p><strong>📖 Ejemplo:</strong> Estás en una discusión con alguien cercano y notas que te estás alterando. Antes de responder impulsivamente, respira profundamente y date unos segundos para calmarte.</p>
</div>""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "Técnica 3-4: Etiquetado y Redirección",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h3 style="color: #2c3e50; margin-top: 0;">3. 🏷️ Etiqueta tus emociones</h3>

<p>Identificar y ponerle nombre a lo que estás sintiendo es otra forma de regulación emocional. Al etiquetar la emoción, puedes distanciarte de ella y evitar que te controle.</p>

<p><strong>📖 Ejemplo:</strong> En vez de decir "Estoy molesto", intenta ser más específico: "Estoy molesto porque siento que no me están escuchando". Esto te da claridad sobre lo que realmente está ocurriendo y te permite encontrar soluciones más prácticas.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">4. ⚡ Redirige la energía de las emociones intensas</h3>

<p>A veces, las emociones intensas necesitan ser canalizadas. En lugar de actuar impulsivamente, busca formas constructivas de liberar esa energía.</p>

<p><strong>💡 Actividades recomendadas:</strong></p>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>Practicar ejercicio</li>
<li>Escribir en un diario</li>
<li>Hacer una actividad creativa</li>
</ul>

<p><strong>📖 Ejemplo:</strong> Después de una conversación tensa en el trabajo o con la familia, te sientes abrumado por la frustración. En lugar de discutir más, opta por salir a caminar durante 10 minutos.</p>

<p><strong>Tip:</strong> Si eliges escuchar música, evita entrar a redes sociales para realmente canalizar tu emoción y no evadirla.</p>
</div>""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "Técnica 5-7: Pensamientos, Límites y Autocuidado",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h3 style="color: #2c3e50; margin-top: 0;">5. 🧠 Cuida tus pensamientos</h3>

<p>Nuestras emociones están fuertemente ligadas a nuestros pensamientos. Si alimentamos pensamientos negativos o catastróficos, nuestras emociones se intensificarán.</p>

<p><strong>💡 Reestructuración cognitiva:</strong> Identifica pensamientos limitantes y reemplázalos por otros más realistas y equilibrados.</p>

<p><strong>📖 Ejemplo:</strong> Si piensas "Nunca haré bien mi trabajo" después de un error, intenta cambiarlo a "Cometí un error, pero puedo aprender de él y mejorar".</p>

<h3 style="color: #2c3e50; margin-top: 25px;">6. 🚧 Establece límites emocionales</h3>

<p>Aprender a decir "no" o a poner límites con los demás también es una forma de regular tus emociones.</p>

<p><strong>📖 Ejemplo:</strong> Tu colega te pide que te quedes más horas en el trabajo, pero ya te sientes estresado. Puedes decir: "Hoy no puedo, necesito descansar para rendir mejor mañana".</p>

<h3 style="color: #2c3e50; margin-top: 25px;">7. 💆 Utiliza el autocuidado como herramienta de regulación</h3>

<p>Cuando cuidas de ti mismo regularmente, creas una base sólida para enfrentar los desafíos emocionales.</p>

<p><strong>📖 Ejemplo:</strong> Al final de una semana estresante, dedica tiempo a una actividad que disfrutes, como leer un libro, darte un baño relajante o ver una película.</p>
</div>""",
            "card_type": "practical",
            "order_number": 5
        },
        {
            "title": "Comunicación Asertiva",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Comunicación Asertiva de las Necesidades</h2>

<h3 style="color: #2c3e50; margin-top: 25px;">¿Qué es la comunicación asertiva?</h3>

<p>La comunicación asertiva es una habilidad interpersonal clave que permite expresar nuestras emociones y necesidades de manera honesta y directa, respetando al mismo tiempo los derechos y sentimientos de los demás.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Albert Ellis - Investigación</h3>

<p>Según estudios del psicólogo <strong>Albert Ellis</strong>, la falta de asertividad puede llevar a la acumulación de frustración, resentimiento y conflictos interpersonales.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Características de la comunicación asertiva:</h3>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">✨ Claridad</h4>
<p>Expresar lo que sientes y necesitas de manera directa y sin ambigüedades. En lugar de evitar el conflicto, la asertividad se enfoca en resolverlo desde la comprensión mutua.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">👤 Uso de "Yo" en lugar de "Tú"</h4>
<p>Cuando expresamos nuestras emociones en primera persona, evitamos culpar a los demás y tomamos responsabilidad por lo que sentimos.</p>
</div>

<p><strong>📖 Ejemplo:</strong> "Me siento ignorado cuando no respondes a mis mensajes" en lugar de "Nunca respondes a mis mensajes".</p>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">⚖️ Equilibrio entre expresión y escucha</h4>
<p>Ser asertivo implica no solo expresar lo que necesitas, sino también estar dispuesto a escuchar y comprender las necesidades del otro.</p>
</div>
</div>""",
            "card_type": "theory",
            "order_number": 6
        },
        {
            "title": "Beneficios de la Comunicación Asertiva",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Beneficios de la comunicación asertiva:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Promueve relaciones más honestas y abiertas</h3>
<p>La comunicación asertiva fomenta un entorno de confianza y sinceridad en las relaciones.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Mejora la satisfacción personal y profesional</h3>
<p>La asertividad está vinculada a una mayor satisfacción en las interacciones personales y en el ámbito laboral.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Reduce el malestar emocional</h3>
<p>Al expresar las necesidades de manera clara y respetuosa, las personas asertivas experimentan menos frustración y resentimiento.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Ayuda a prevenir conflictos</h3>
<p>La asertividad facilita una comunicación directa y constructiva, minimizando malentendidos y desacuerdos.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">✅ Aumenta la autoconfianza y disminuye la ansiedad</h3>
<p>Las personas que se comunican asertivamente tienden a sentirse más seguras de sí mismas, lo que reduce su nivel de ansiedad en situaciones sociales o profesionales.</p>
</div>

<h3 style="color: #2c3e50; margin-top: 25px;">📖 Ejemplo práctico:</h3>

<p>En lugar de decir:</p>
<p>"Nunca me escuchas"</p>

<p>Di:</p>
<p>"Me siento ignorado/a cuando no respondes a lo que te digo. ¿Podemos encontrar un momento para hablar?"</p>

<p>Esta forma de comunicación abre el diálogo en lugar de cerrarlo.</p>
</div>""",
            "card_type": "practical",
            "order_number": 7
        },
        {
            "title": "Tu Caja de Herramientas Emocionales",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Construcción de tu Caja de Herramientas Emocionales</h2>

<h3 style="color: #2c3e50; margin-top: 25px;">¿Qué es una caja de herramientas emocionales?</h3>

<p>Es una recopilación personal de técnicas, estrategias y recordatorios que puedes utilizar para gestionar tus emociones y navegar los desafíos emocionales de manera más efectiva.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">🛠️ Ejemplos de lo que puedes incluir:</h3>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">�� Técnicas de respiración</h4>
<p>Que te ayuden a calmarte en momentos de estrés.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">💬 Recordatorios de frases asertivas</h4>
<p>Que te ayuden a comunicarte mejor con los demás.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">📝 Un diario de emociones</h4>
<p>Donde puedas escribir tus pensamientos y sentimientos en situaciones difíciles.</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h4 style="color: #2c3e50; margin-top: 0;">🌟 Visualizaciones</h4>
<p>Imágenes mentales que te inspiren calma o fortaleza en momentos complicados.</p>
</div>

<h3 style="color: #2c3e50; margin-top: 25px;">🎯 Organización sugerida:</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>**Técnicas rápidas** (para momentos de crisis)</li>
<li>**Herramientas diarias** (para mantenimiento emocional)</li>
<li>**Estrategias a largo plazo** (para crecimiento continuo)</li>
</ul>

<h3 style="color: #2c3e50; margin-top: 25px;">¿Por qué es importante?</h3>

<p>Al tener una colección clara de herramientas, sabes que siempre puedes recurrir a ellas cuando las emociones se vuelven abrumadoras. La investigación en psicología sugiere que las personas que tienen recursos concretos para gestionar el estrés son más resilientes.</p>
</div>""",
            "card_type": "practical",
            "order_number": 8
        },
        {
            "title": "Reflexión Final del Módulo",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">El Verdadero Crecimiento Personal</h2>

<p>A lo largo de este módulo, has aprendido que cada emoción tiene un propósito y un mensaje, y que no gestionarlas puede llevarnos a patrones destructivos o estancamiento emocional.</p>

<p>Por eso, aprender a regularlas y expresarlas asertivamente no solo nos permite conectar mejor con los demás, sino también con nosotros mismos.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">El Equilibrio Emocional</h3>

<p>El verdadero crecimiento personal radica en ser capaces de:</p>
<ul style="list-style-type: disc; margin-left: 20px;">
<li>✅ Escuchar nuestras emociones</li>
<li>✅ Atender nuestras necesidades</li>
<li>✅ Tener el coraje de expresarlas de manera honesta y respetuosa</li>
</ul>

<p>Cuando logramos este equilibrio, no solo resolvemos conflictos o reducimos el estrés; creamos un espacio para vivir de manera más auténtica, plena y consciente.</p>

<h3 style="color: #2c3e50; margin-top: 25px;">Navegando con Sabiduría</h3>

<p>Recuerda, gestionar tus emociones <strong>no significa controlarlas o reprimirlas</strong>, sino aprender a navegar por ellas con sabiduría y compasión.</p>

<p>La práctica continua de estas herramientas te permitirá enfrentar cualquier desafío emocional que la vida te presente, con mayor claridad y confianza.</p>

<hr style="margin: 20px 0; border: 1px solid #bdc3c7;">

<div style="background: #e8f5e8; padding: 15px; border: 1px solid #27ae60; border-radius: 5px; margin: 15px 0;">
<p><strong>¡Felicidades por completar el Módulo 1!</strong></p>
<p>Has construido una base sólida para gestionar tu mundo emocional con mayor consciencia y asertividad.</p>
</div>
</div>""",
            "card_type": "conclusion",
            "order_number": 9
        }
    ]
    
    # Create Theme 3 cards
    for card_data in theme3_cards:
        card = ThemeCard(
            title=card_data["title"],
            content=card_data["content"],
            card_type=card_data["card_type"],
            order_number=card_data["order_number"],
            theme_id=theme3.id
        )
        db.add(card) 