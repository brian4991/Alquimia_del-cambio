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
            "title": "🎯 Introducción al Tema",
            "content": """# Explorando mi Historia Emocional

**El propósito** de este tema es guiarte a través de la exploración consciente de tu historia emocional. 

A lo largo de nuestra vida, vamos acumulando experiencias que moldean la forma en que sentimos, reaccionamos y gestionamos nuestras emociones.

## ¿Por qué es importante?

Al reconocer los patrones emocionales y descubrir las raíces de estos, podrás comprender mejor cómo las experiencias pasadas siguen influyendo en tu presente. 

Este autoconocimiento es fundamental para aprender a gestionar las emociones de manera más consciente y efectiva.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "📚 Recursos y Subtemas",
            "content": """## En este tema exploraremos:

**📍 Subtemas:**
• **Reconocer patrones emocionales**
• **Raíces emocionales**

**📚 Recursos disponibles:**
- Mi carta de aceptación y compromiso
- Emocionario, técnicas de gestión emocional para el día a día
- ¿Qué necesito realmente cuando me siento así?

> **¡Importante!** No olvides tu carta de aceptación y compromiso: es lo primero antes de comenzar. Disfruta el viaje que te espera.

Empezamos con dos ejercicios muy valiosos que son el punto de partida para reconectar con tu historia.""",
            "card_type": "resources",
            "order_number": 2
        },
        {
            "title": "🧠 ¿Qué son los Patrones Emocionales?",
            "content": """# Reconocer Patrones Emocionales

Los patrones emocionales son **respuestas automáticas** que repetimos en situaciones similares a lo largo de nuestra vida. 

Estas respuestas se forman a partir de nuestras primeras experiencias emocionales y las conexiones que hacemos entre emociones y eventos específicos.

## 📖 Ejemplos:

**Ejemplo 1:**
Si en nuestra infancia asociamos la crítica con el miedo al rechazo, es probable que, en la vida adulta, respondamos a cualquier forma de crítica con ansiedad o inseguridad.

**Ejemplo 2:**
Si creciste en un ambiente donde la expresión emocional era reprimida, es probable que desarrolles un patrón de evitación emocional en tu vida adulta.""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "🔬 La Ciencia: Neuroplasticidad",
            "content": """## Base Científica

Desde el campo de la **psicología cognitiva**, se ha demostrado que nuestras emociones están en gran parte influenciadas por esquemas mentales, o "mapas" que desarrollamos a lo largo del tiempo.

### 🧠 Neuroplasticidad

La **neurociencia** nos muestra que el cerebro puede cambiar sus conexiones, lo que significa que podemos "reprogramar" cómo reaccionamos emocionalmente a través del autoconocimiento y la práctica consciente.

Este proceso se conoce como **neuroplasticidad**, y es lo que nos permite adoptar nuevas formas de gestionar nuestras emociones una vez que somos conscientes de los patrones emocionales que hemos desarrollado.

> **La buena noticia:** Identificar estos patrones es esencial para desactivarlos.""",
            "card_type": "theory",
            "order_number": 4
        },
        {
            "title": "🔍 Señales de Patrones Recurrentes",
            "content": """## Señales de Patrones Emocionales Recurrentes:

### 1. 💥 Reacciones exageradas a ciertas situaciones
A veces, cuando alguien nos critica o dice algo que no nos gusta, podemos sentirnos muy enojados o muy tristes, incluso si lo que dijeron no era tan grave. Esto pasa porque hemos aprendido a reaccionar así en el pasado.

### 2. 🔄 Sentir las mismas emociones en situaciones parecidas
Puede que te sientas frustrado o nervioso en ciertos lugares o con ciertas personas, como en el trabajo o en una reunión social. Esto ocurre porque esas situaciones te recuerdan a otras donde ya te sentiste así antes.

### 3. 🚫 Evitar ciertos temas o emociones
Si hay cosas que prefieres no hablar o sentir, como el miedo o la tristeza, podrías intentar ignorarlas. En lugar de enfrentarlas, quizás optes por aislarte o discutir con los demás para no sentirte vulnerable.

> Al identificar estos patrones, podemos empezar a comprender que nuestras emociones **no siempre reflejan la realidad del presente**, sino que están condicionadas por experiencias anteriores.""",
            "card_type": "practical",
            "order_number": 5
        },
        {
            "title": "🌱 ¿Qué son las Raíces Emocionales?",
            "content": """# Raíces Emocionales

Las raíces emocionales son las **experiencias pasadas**, a menudo en la infancia o adolescencia, que forman la base de nuestros patrones emocionales actuales.

Estas experiencias tempranas, tanto positivas como negativas, juegan un papel crucial en el desarrollo de nuestro sistema emocional.

## 🎓 Teoría del Apego - John Bowlby

En **psicología del desarrollo**, el modelo del apego propuesto por John Bowlby sostiene que nuestras primeras relaciones, particularmente con los cuidadores primarios, influyen en cómo formamos relaciones y regulamos nuestras emociones en el futuro.

### 📖 Ejemplo:
Si en nuestra infancia aprendimos que expresar tristeza no era aceptado o no recibía la validación necesaria, podríamos haber desarrollado una tendencia a reprimir esa emoción.""",
            "card_type": "theory",
            "order_number": 6
        },
        {
            "title": "💔 Impacto de las Raíces Emocionales",
            "content": """## Impacto de las Raíces Emocionales:

### 🔗 Apego inseguro
Puede generar dependencia emocional o dificultades para confiar en los demás.

### 😔 Experiencias de rechazo  
Pueden llevar a una sensibilidad exagerada ante la crítica o el conflicto.

### 🤐 Ambientes familiares poco expresivos emocionalmente
Pueden resultar en la incapacidad de expresar necesidades emocionales de manera asertiva.

### 💥 Momentos traumáticos
Pueden generar reacciones desproporcionadas ante situaciones de pérdida o estrés en la vida adulta.

---

### 🌟 El poder del autoconocimiento

Explorar estas raíces no solo es importante para comprender por qué reaccionamos de cierta manera, sino que también nos permite **tomar el control** sobre cómo queremos responder en el futuro.

El autoconocimiento de nuestras raíces emocionales nos da el poder de cambiar nuestras narrativas emocionales y romper patrones que ya no nos sirven.""",
            "card_type": "practical",
            "order_number": 7
        },
        {
            "title": "✨ Conclusión del Tema 1",
            "content": """## 🏗️ Construyendo tu Fundamento Emocional

Este tema es el **fundamento** para construir un mayor entendimiento de ti mismo a nivel emocional:

**🔍 Reconocer patrones emocionales** es el primer paso para observar cómo respondes a situaciones y relaciones.

**🌱 Explorar raíces emocionales** te permitirá entender por qué reaccionas de esa manera.

Con este conocimiento, comenzarás a tomar decisiones más conscientes sobre cómo gestionar tus emociones y evitarás caer en respuestas automáticas que no contribuyen a tu bienestar.

## 💡 Reflexión Final

Es crucial recordar que las emociones **no se generan en el vacío**; están profundamente conectadas a nuestra historia y a las experiencias que nos han moldeado.

Este proceso de autoexploración te brinda una visión más clara de esas conexiones, permitiéndote tomar las riendas de tu mundo emocional con **mayor comprensión y compasión**.

---

🎯 **Próximo paso**: En el Tema 2 profundizaremos en el autoconocimiento emocional para identificar tus emociones primarias y reconocer tus necesidades.""",
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
            "title": "🎯 Autoconocimiento Emocional Profundo",
            "content": """# Tema 2: Autoconocimiento Emocional Profundo

## 🎯 Objetivo del tema

En este tema, profundizaremos en la **identificación de tus emociones primarias** y en el **reconocimiento de las necesidades emocionales**.

## ¿Por qué es crucial?

Es crucial entender que nuestras emociones no solo son respuestas inmediatas a los eventos, sino que también son **señales** que nos indican nuestras necesidades internas no satisfechas.

Al desarrollar un mayor autoconocimiento emocional, podrás:
- ✅ Identificar estas señales
- ✅ Actuar de manera más consciente
- ✅ Evitar respuestas automáticas o reactivas

---

Este proceso te permitirá responder de manera más intencional y evitar perpetuar patrones no deseados.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🎭 Las 6 Emociones Primarias",
            "content": """# Identificar Emociones Primarias

## ¿Qué son las emociones primarias?

Las emociones primarias son las **respuestas emocionales más básicas e instintivas** que todos los seres humanos experimentan.

### 🎭 Las 6 emociones primarias universales:
1. **Miedo** 😰
2. **Tristeza** 😢  
3. **Alegría** 😊
4. **Enojo** 😠
5. **Sorpresa** 😮
6. **Asco** 🤢

## 🧬 Función evolutiva

Estas emociones tienen una **función evolutiva**: nos ayudan a responder a nuestro entorno de manera rápida para sobrevivir y adaptarnos.

Sin embargo, a menudo no estamos completamente conscientes de estas emociones, y es común que las disfrazamos o las racionalicemos en lugar de experimentarlas plenamente.

## 🎯 ¿Por qué identificarlas?

Es importante aprender a identificar estas emociones a medida que surgen, **sin juicio ni represión**, ya que cada una de ellas contiene información valiosa sobre lo que necesitamos en ese momento.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🌟 Beneficios de Identificar Emociones",
            "content": """## Beneficios de identificar las emociones primarias:

### ✅ Consciencia emocional
Al ser más conscientes de tus emociones primarias, puedes actuar de manera más alineada con tus valores y deseos, en lugar de reaccionar impulsivamente.

### ✅ Prevención de conflictos  
Al identificar las emociones en el momento en que surgen, puedes evitar que escalen en situaciones conflictivas o dañinas.

### ✅ Desarrollo de empatía
Cuando reconoces tus propias emociones, también te vuelves más empático hacia las emociones de los demás, lo que mejora las relaciones interpersonales.

## 🎓 Paul Ekman - Investigación

Según **Paul Ekman**, un reconocido psicólogo en el campo de las emociones, las emociones primarias son universales y están presentes en todas las culturas. 

Esto sugiere que, aunque las expresiones emocionales pueden variar entre diferentes sociedades, la experiencia interna de estas emociones es compartida por todos los seres humanos.

Ekman también señala que identificar y regular estas emociones es fundamental para el bienestar psicológico, ya que nos permiten procesar nuestras experiencias de manera efectiva.""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "🚨 Reconocer Necesidades Emocionales",
            "content": """# Reconocer Necesidades Emocionales

## El sistema de alerta emocional

Cada emoción primaria está conectada a una **necesidad emocional**. Las emociones actúan como un sistema de alerta que nos indica si nuestras necesidades están siendo satisfechas o no.

### 📖 Ejemplos de conexiones:

**🔸 El miedo** puede señalar una necesidad de seguridad

**🔸 La tristeza** puede revelar una necesidad de apoyo o consuelo

**🔸 El enojo** puede indicar que sentimos que se ha violado un límite importante

Al identificar estas necesidades, puedes empezar a tomar acciones más efectivas para satisfacerlas y evitar quedarte atrapado en ciclos emocionales insalubres.

## ⚠️ Riesgos de ignorar las necesidades

El reconocimiento de las necesidades emocionales es una habilidad esencial para el autoconocimiento. Sin este reconocimiento, corremos el riesgo de malinterpretar nuestras emociones y responder de manera incorrecta a ellas.

A menudo, cuando ignoramos nuestras necesidades, nos sentimos desbordados, desconectados de nosotros mismos y de los demás.""",
            "card_type": "theory",
            "order_number": 4
        },
        {
            "title": "💫 Beneficios de Reconocer Necesidades",
            "content": """## Beneficios de reconocer necesidades emocionales:

### ✅ Satisfacción personal
Ser consciente de tus necesidades emocionales te permite satisfacerlas de manera efectiva, lo que lleva a una mayor sensación de bienestar y satisfacción.

### ✅ Reducción del estrés
Al entender y abordar tus necesidades emocionales, puedes reducir la ansiedad y el estrés relacionados con la insatisfacción emocional.

### ✅ Mejora en las relaciones
Reconocer tus propias necesidades emocionales también te permite comunicarte mejor con los demás y establecer relaciones más saludables y auténticas.

## 🎓 Carl Rogers - Teoría Humanista

**Carl Rogers**, uno de los fundadores de la psicología humanista, destacó la importancia de las necesidades emocionales en su teoría de la "persona completa". 

Rogers sostuvo que cuando las personas son conscientes de sus necesidades y trabajan activamente para satisfacerlas, tienden a ser más equilibradas y felices. 

En cambio, cuando estas necesidades se ignoran o se niegan, surgen conflictos internos y disfunciones en las relaciones.

Investigaciones recientes en el campo de la **psicología positiva** sugieren que la identificación de las necesidades emocionales y la capacidad de satisfacerlas son claves para el desarrollo de resiliencia emocional.""",
            "card_type": "theory",
            "order_number": 5
        },
        {
            "title": "🎯 Conclusión del Tema 2",
            "content": """## Conexión Profunda Contigo Mismo/a

Este tema te llevará a un nivel más profundo de conexión contigo mismo/a. 

Identificar tus emociones primarias y las necesidades emocionales que subyacen a estas es un paso crucial para entender por qué reaccionas de ciertas maneras en situaciones cotidianas y cómo puedes tomar decisiones más alineadas con tu bienestar.

## 🛠️ Herramientas para la vida diaria

Al desarrollar este nivel de autoconocimiento emocional, estarás mejor equipado/a para responder de manera más intencional y saludable en tu vida diaria, creando un equilibrio emocional más sólido.

## 🔄 Proceso aplicable

En la próxima sección, te guiaré a través de ejercicios específicos que te ayudarán a poner en práctica esta identificación de emociones y el reconocimiento de tus necesidades emocionales, haciendo que el proceso de autoconocimiento sea claro y aplicable.

---

🎯 **Próximo paso**: En el Tema 3 aprenderemos técnicas concretas para gestionar y expresar nuestras emociones de manera saludable.""",
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
            "title": "🎯 Gestionando y Expresando Emociones",
            "content": """# Tema 3: Gestionando y Expresando Emociones

## 🎯 El paso final hacia el dominio emocional

En esta última parte del módulo, nos adentraremos en cómo **gestionar y expresar** nuestras emociones de manera saludable y efectiva.

Saber identificar nuestras emociones es un primer paso esencial, pero ser capaces de **regularlas y expresarlas de manera asertiva** es lo que realmente nos permite avanzar hacia una vida más equilibrada y consciente.

## 🛠️ Herramientas que desarrollarás:

### Subtema 1: Técnicas de regulación emocional
- Las 7 técnicas prácticas para gestionar emociones intensas
- Estrategias basadas en investigación científica
- Aplicación en tu vida diaria

### Subtema 2: Comunicación asertiva
- Cómo expresar lo que sientes sin ser agresivo o pasivo
- Técnicas para comunicar necesidades de manera efectiva
- Construcción de relaciones más saludables

### Subtema 3: Tu caja de herramientas emocionales
- Recopilación de todas las técnicas aprendidas
- Organización personal de recursos
- Plan de mantenimiento emocional

---

Este tema te proporcionará las herramientas necesarias para gestionar las emociones más difíciles y comunicar lo que sientes y necesitas de una manera clara, respetuosa y efectiva.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🧠 ¿Por qué Regular las Emociones?",
            "content": """# Técnicas de Regulación Emocional

## ¿Por qué es importante la regulación emocional?

Las emociones, especialmente las intensas, pueden ser abrumadoras si no sabemos cómo manejarlas. 

La **regulación emocional** es la capacidad de manejar y responder a una experiencia emocional de manera saludable.

## 🎓 Teoría de James Gross

La teoría de **James Gross** sobre la regulación emocional ha mostrado que quienes desarrollan esta habilidad son más capaces de:

- ✅ Mantener relaciones interpersonales satisfactorias
- ✅ Tener menos niveles de estrés
- ✅ Gozar de mayor bienestar general

## 🛠️ Estrategias principales:

### 🔄 Reevaluación del pensamiento
Reinterpretar una situación para cambiar su impacto emocional. En lugar de ver un evento como una amenaza, puedes aprender a verlo como un desafío o una oportunidad de crecimiento.

### 🧘 Mindfulness y atención plena
Nos ayuda a observar nuestras emociones sin juzgarlas, reduciendo su intensidad y permitiéndonos responder con mayor claridad.

### 🫁 Respiración y técnicas de relajación
El control de la respiración es muy efectivo para disminuir la activación fisiológica asociada con el estrés o la ira.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "✨ Técnica 1-2: Validación y Respiración",
            "content": """## 🛠️ Técnicas Prácticas para el Día a Día

### 1. ✅ Reconoce y valida tus emociones

Uno de los primeros pasos en la regulación emocional es ser consciente de lo que sientes. En lugar de ignorar tus emociones o juzgarte por sentirlas, tómate un momento para reconocerlas y aceptarlas.

**📖 Ejemplo:** Si estás frustrado después de un día difícil en el trabajo, en lugar de decir "No debería sentirme así", trata de decir "Es normal sentirme frustrado después de un día así". Esta validación te permitirá tomar decisiones más sabias sobre cómo manejar la emoción.

### 2. 🫁 Practica la respiración consciente

Cuando sientas que una emoción intensa, como la ansiedad o la ira, está aumentando, una técnica rápida y efectiva es la respiración profunda.

**💡 Técnica 4-4-4:**
- Inhala por la nariz durante **4 segundos**
- Sostén el aire por **4 segundos** 
- Exhala lentamente por la boca durante **4 segundos**
- Repite este ciclo **3 o 4 veces**

**📖 Ejemplo:** Estás en una discusión con alguien cercano y notas que te estás alterando. Antes de responder impulsivamente, respira profundamente y date unos segundos para calmarte.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "🏷️ Técnica 3-4: Etiquetado y Redirección",
            "content": """### 3. 🏷️ Etiqueta tus emociones

Identificar y ponerle nombre a lo que estás sintiendo es otra forma de regulación emocional. Al etiquetar la emoción, puedes distanciarte de ella y evitar que te controle.

**📖 Ejemplo:** En vez de decir "Estoy molesto", intenta ser más específico: "Estoy molesto porque siento que no me están escuchando". Esto te da claridad sobre lo que realmente está ocurriendo y te permite encontrar soluciones más prácticas.

### 4. ⚡ Redirige la energía de las emociones intensas

A veces, las emociones intensas necesitan ser canalizadas. En lugar de actuar impulsivamente, busca formas constructivas de liberar esa energía.

**💡 Actividades recomendadas:**
- Practicar ejercicio
- Escribir en un diario
- Hacer una actividad creativa

**📖 Ejemplo:** Después de una conversación tensa en el trabajo o con la familia, te sientes abrumado por la frustración. En lugar de discutir más, opta por salir a caminar durante 10 minutos.

> **Tip:** Si eliges escuchar música, evita entrar a redes sociales para realmente canalizar tu emoción y no evadirla.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "🧠 Técnica 5-7: Pensamientos, Límites y Autocuidado",
            "content": """### 5. 🧠 Cuida tus pensamientos

Nuestras emociones están fuertemente ligadas a nuestros pensamientos. Si alimentamos pensamientos negativos o catastróficos, nuestras emociones se intensificarán.

**💡 Reestructuración cognitiva:** Identifica pensamientos limitantes y reemplázalos por otros más realistas y equilibrados.

**📖 Ejemplo:** Si piensas "Nunca haré bien mi trabajo" después de un error, intenta cambiarlo a "Cometí un error, pero puedo aprender de él y mejorar".

### 6. 🚧 Establece límites emocionales

Aprender a decir "no" o a poner límites con los demás también es una forma de regular tus emociones.

**📖 Ejemplo:** Tu colega te pide que te quedes más horas en el trabajo, pero ya te sientes estresado. Puedes decir: "Hoy no puedo, necesito descansar para rendir mejor mañana".

### 7. 💆 Utiliza el autocuidado como herramienta de regulación

Cuando cuidas de ti mismo regularmente, creas una base sólida para enfrentar los desafíos emocionales.

**📖 Ejemplo:** Al final de una semana estresante, dedica tiempo a una actividad que disfrutes, como leer un libro, darte un baño relajante o ver una película.""",
            "card_type": "practical",
            "order_number": 5
        },
        {
            "title": "💬 Comunicación Asertiva",
            "content": """# Comunicación Asertiva de las Necesidades

## ¿Qué es la comunicación asertiva?

La comunicación asertiva es una habilidad interpersonal clave que permite expresar nuestras emociones y necesidades de manera honesta y directa, respetando al mismo tiempo los derechos y sentimientos de los demás.

## 🎓 Albert Ellis - Investigación

Según estudios del psicólogo **Albert Ellis**, la falta de asertividad puede llevar a la acumulación de frustración, resentimiento y conflictos interpersonales.

## 🔑 Características de la comunicación asertiva:

### ✨ Claridad
Expresar lo que sientes y necesitas de manera directa y sin ambigüedades. En lugar de evitar el conflicto, la asertividad se enfoca en resolverlo desde la comprensión mutua.

### 👤 Uso de "Yo" en lugar de "Tú"
Cuando expresamos nuestras emociones en primera persona, evitamos culpar a los demás y tomamos responsabilidad por lo que sentimos.

**📖 Ejemplo:** "Me siento ignorado cuando no respondes a mis mensajes" en lugar de "Nunca respondes a mis mensajes".

### ⚖️ Equilibrio entre expresión y escucha
Ser asertivo implica no solo expresar lo que necesitas, sino también estar dispuesto a escuchar y comprender las necesidades del otro.""",
            "card_type": "theory",
            "order_number": 6
        },
        {
            "title": "🌟 Beneficios de la Comunicación Asertiva",
            "content": """## Beneficios de la comunicación asertiva:

### ✅ Promueve relaciones más honestas y abiertas
La comunicación asertiva fomenta un entorno de confianza y sinceridad en las relaciones.

### ✅ Mejora la satisfacción personal y profesional
La asertividad está vinculada a una mayor satisfacción en las interacciones personales y en el ámbito laboral.

### ✅ Reduce el malestar emocional
Al expresar las necesidades de manera clara y respetuosa, las personas asertivas experimentan menos frustración y resentimiento.

### ✅ Ayuda a prevenir conflictos
La asertividad facilita una comunicación directa y constructiva, minimizando malentendidos y desacuerdos.

### ✅ Aumenta la autoconfianza y disminuye la ansiedad
Las personas que se comunican asertivamente tienden a sentirse más seguras de sí mismas, lo que reduce su nivel de ansiedad en situaciones sociales o profesionales.

---

## 📖 Ejemplo práctico:

**En lugar de decir:** "Nunca me escuchas"

**Di:** "Me siento ignorado/a cuando no respondes a lo que te digo. ¿Podemos encontrar un momento para hablar?"

Esta forma de comunicación abre el diálogo en lugar de cerrarlo.""",
            "card_type": "practical",
            "order_number": 7
        },
        {
            "title": "🧰 Tu Caja de Herramientas Emocionales",
            "content": """# Construcción de tu Caja de Herramientas Emocionales

## ¿Qué es una caja de herramientas emocionales?

Es una recopilación personal de técnicas, estrategias y recordatorios que puedes utilizar para gestionar tus emociones y navegar los desafíos emocionales de manera más efectiva.

## 🛠️ Ejemplos de lo que puedes incluir:

### 🫁 Técnicas de respiración
Que te ayuden a calmarte en momentos de estrés.

### 💬 Recordatorios de frases asertivas
Que te ayuden a comunicarte mejor con los demás.

### 📝 Un diario de emociones
Donde puedas escribir tus pensamientos y sentimientos en situaciones difíciles.

### 🌟 Visualizaciones
Imágenes mentales que te inspiren calma o fortaleza en momentos complicados.

## 🎯 Organización sugerida:

- **Técnicas rápidas** (para momentos de crisis)
- **Herramientas diarias** (para mantenimiento emocional)
- **Estrategias a largo plazo** (para crecimiento continuo)

## ¿Por qué es importante?

Al tener una colección clara de herramientas, sabes que siempre puedes recurrir a ellas cuando las emociones se vuelven abrumadoras. La investigación en psicología sugiere que las personas que tienen recursos concretos para gestionar el estrés son más resilientes.""",
            "card_type": "practical",
            "order_number": 8
        },
        {
            "title": "🎉 Reflexión Final del Módulo",
            "content": """## 🌟 El Verdadero Crecimiento Personal

A lo largo de este módulo, has aprendido que cada emoción tiene un propósito y un mensaje, y que no gestionarlas puede llevarnos a patrones destructivos o estancamiento emocional.

Por eso, aprender a regularlas y expresarlas asertivamente no solo nos permite conectar mejor con los demás, sino también con nosotros mismos.

## 🎯 El Equilibrio Emocional

El verdadero crecimiento personal radica en ser capaces de:
- ✅ Escuchar nuestras emociones
- ✅ Atender nuestras necesidades  
- ✅ Tener el coraje de expresarlas de manera honesta y respetuosa

Cuando logramos este equilibrio, no solo resolvemos conflictos o reducimos el estrés; creamos un espacio para vivir de manera más auténtica, plena y consciente.

## 🧭 Navegando con Sabiduría

Recuerda, gestionar tus emociones **no significa controlarlas o reprimirlas**, sino aprender a navegar por ellas con sabiduría y compasión.

La práctica continua de estas herramientas te permitirá enfrentar cualquier desafío emocional que la vida te presente, con mayor claridad y confianza.

---

## 🎊 ¡Felicidades por completar el Módulo 1!

Has construido una base sólida para gestionar tu mundo emocional con mayor consciencia y asertividad.""",
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