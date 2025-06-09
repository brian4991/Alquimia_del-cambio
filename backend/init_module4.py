from sqlalchemy.orm import Session
from models import Module, Theme, Exercise, ThemeCard
from database import get_db

def create_module4_cards(db: Session, themes: list):
    """Create cards for Module 4 themes based on module4.txt content"""
    
    # Get theme references
    theme1, theme2, theme3 = themes
    
    # ===============================
    # TEMA 1 CARDS: Rompiendo barreras
    # ===============================
    
    theme1_cards = [
        {
            "title": "🎯 Introducción al Tema",
            "content": """# Rompiendo Barreras

**El propósito** de este tema es identificar las barreras mentales que hemos construido, cuestionarlas y reemplazarlas por creencias que realmente nos ayuden a vivir desde nuestra autenticidad.

## 💭 La reflexión fundamental

*"Lo que nos detiene no es lo que somos, sino lo que creemos que somos."*

## ¿Por qué es importante?

A lo largo de nuestra vida, absorbemos creencias, normas y expectativas que moldean nuestra forma de ver el mundo. Muchas de estas ideas vienen de nuestra familia, escuela, cultura y sociedad.

Sin darnos cuenta, terminamos actuando bajo reglas que **ni siquiera hemos elegido conscientemente**.

## En este tema exploraremos:

**📍 Subtemas:**
• **Mis acuerdos** - Los contratos internos que hemos firmado
• **La voz interior a la que sirvo** - Identificando nuestra narrativa interna

## 🎯 Objetivo

El primer paso para cualquier cambio es reconocer las barreras que hemos construido, muchas veces sin darnos cuenta.

No somos conscientes de los acuerdos internos que hemos hecho con nosotros mismos ni de las voces internas que influyen en nuestras decisiones.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "📜 Mis acuerdos",
            "content": """# Mis acuerdos

## 🏠 La casa llena de contratos

Imagina que tu mente es como una casa llena de contratos firmados. Algunos acuerdos los hiciste de forma consciente, pero la mayoría los **heredaste sin cuestionarlos**.

### Algunos de esos acuerdos dicen:
✅ "Merezco amor y respeto."
❌ "Si me equivoco, soy un fracaso."
✅ "Puedo ser auténtico sin miedo."
❌ "Tengo que ser como los demás esperan."

## 🤔 La pregunta clave

Si un contrato ya no te sirve, ¿qué harías? Exacto, **lo rompes y escribes uno nuevo**.

## 🌟 Los Cuatro Acuerdos de Miguel Ruiz

### 1. 💬 Sé impecable con tus palabras
Las palabras tienen un poder enorme. Ser impecable significa hablarnos con amor y respeto, tanto a nosotros mismos como a los demás.

**Ejemplo:** En lugar de "Soy un desastre en las relaciones", cambia a "Estoy aprendiendo a relacionarme de una manera más sana".

### 2. 🚫 No te tomes nada personal
Lo que los demás dicen o hacen es un reflejo de su propia realidad, no de la nuestra.

**Ejemplo:** Si alguien critica tu trabajo, recuerda que esa opinión es de la otra persona y no define tu valor.

### 3. ❓ No hagas suposiciones
Muchas veces sufrimos porque asumimos lo que los demás piensan sin preguntar.

**Ejemplo:** Si un amigo no responde un mensaje, en lugar de asumir que está enojado, simplemente pregúntale si todo está bien.

### 4. 💪 Haz siempre lo mejor que puedas
Nuestro "mejor" cambia según el día y nuestro estado. Lo importante es dar lo mejor según nuestras posibilidades en cada momento.

## 🔓 Rompiendo las barreras

Al aplicar estos principios, comenzamos a ver nuestra vida desde una perspectiva más libre, eligiendo conscientemente cómo queremos pensar, hablar y actuar.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🗣️ La voz interior a la que sirvo",
            "content": """# La voz interior a la que sirvo

## 🎧 La narradora constante

Nuestra voz interior es la narradora constante de nuestra vida. Es esa conversación interna que nunca se detiene y que define la manera en que nos percibimos a nosotros mismos y al mundo.

### 🤔 La pregunta fundamental:
¿Alguna vez te has detenido a escucharla con atención?

## 🌱 ¿De dónde viene nuestra voz interior?

Desde pequeños, absorbemos las palabras de figuras de autoridad como nuestros padres, maestros y la sociedad en general.

### Si en la infancia escuchaste frases como:
- "No eres suficiente."
- "No puedes cometer errores."
- "No hagas el ridículo."

Es posible que hoy, como adulto, repitas estas ideas en tu mente sin cuestionarlas.

## ⚖️ El impacto en nuestras decisiones

La manera en que nos hablamos influye directamente en:
- 💪 Nuestra confianza
- 🎯 Nuestras acciones  
- 🚀 Nuestra capacidad de asumir riesgos

### Si nuestra voz interior está dominada por el miedo y la autocrítica, tenderemos a:
- Evitar desafíos por miedo al fracaso
- Dudar de nuestras capacidades
- Procrastinar proyectos importantes
- Sentirnos atrapados en patrones de autosabotaje

## 🔄 Transformando la voz crítica en aliada

### 1. 👁️ Identifica el tipo de voz
Durante un día, pon atención a cómo te hablas. ¿Es una voz de apoyo o de juicio?

### 2. ❓ Cuestiona su veracidad
- ¿De dónde viene esta creencia?
- ¿Es un pensamiento basado en hechos o en el miedo?
- ¿Le hablaría de la misma manera a un ser querido?

### 3. ✨ Redefine tu diálogo interno
- "No eres lo suficientemente bueno" → "Estoy aprendiendo y mejorando cada día"
- "Siempre fracaso" → "Cada error me acerca a una nueva oportunidad"

### 4. 💎 Crea afirmaciones positivas
Escribe frases que refuercen tu confianza y repítelas diariamente.

**Ejemplo:** "Confío en mi capacidad para tomar decisiones".""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "✨ Conclusión del Tema 1",
            "content": """## 🚧 Rompiendo las Barreras Mentales

Romper barreras implica darnos cuenta de que muchas de las creencias que nos limitan **no son nuestras**, sino que fueron aprendidas.

### 🔍 Lo que has aprendido:

**Mis acuerdos:** Has identificado los contratos internos que ya no te sirven y aprendido los principios para crear acuerdos más saludables.

**La voz interior:** Has comenzado a reconocer el tipo de narrativa interna que domina tu mente y cómo transformarla en una aliada.

## 🌱 El resultado

Al aplicar los Cuatro Acuerdos y transformar tu voz interior, comenzamos a ver nuestra vida desde una perspectiva más libre.

Elegir conscientemente cómo queremos pensar, hablar y actuar es el primer paso hacia la autenticidad.

## 💡 Reflexión Final

Este es un proceso que lleva tiempo, pero cada pequeño paso que damos nos acerca a una versión más auténtica y en paz con nosotros mismos.

**La libertad comienza cuando cuestionamos lo que hemos aceptado como verdad sin examinar.**

---

🎯 **Próximo paso**: En el Tema 2 despertaremos a nuestro verdadero ser auténtico.""",
            "card_type": "conclusion",
            "order_number": 4
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
    # TEMA 2 CARDS: Despertar auténtico
    # ===============================
    
    theme2_cards = [
        {
            "title": "🎯 Despertar auténtico",
            "content": """# Tema 2: Despertar auténtico

## 💭 La reflexión de Ralph Waldo Emerson

*"Ser tú mismo en un mundo que constantemente intenta hacerte otra persona es el mayor logro."*

## 🌱 ¿Qué es la autenticidad?

**La autenticidad no es algo que se encuentra, es algo que se cultiva.**

Despertar a nuestro verdadero ser significa cuestionar esas capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura.

## 🎯 El proceso de despertar

Es un proceso de exploración y desaprendizaje, que nos lleva a reconocer quiénes somos más allá de:
- Las etiquetas
- Las expectativas  
- Los miedos

## En este tema exploraremos:

**📍 Subtemas:**
• **Tu verdadero ser** - Diferenciando el "yo aprendido" del "yo auténtico"
• **Cultivando la autoconciencia** - El puente hacia la autenticidad
• **Abrazando la vulnerabilidad** - La fortaleza de mostrarse tal como somos

## 💡 El objetivo

Conectar con tu esencia más allá del condicionamiento social y cultural, para vivir desde un lugar de autenticidad y coherencia interna.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "👤 Tu verdadero ser",
            "content": """# Tu verdadero ser

## ❌ El error más común

Muchas personas pasan gran parte de su vida siendo quienes **"deberían ser"** en lugar de quienes **realmente son**.

Esto sucede porque desde la infancia absorbemos mensajes sobre lo que es aceptable o deseable.

## 🤔 La pregunta clave

**¿Estoy viviendo desde mi autenticidad o desde lo que me dijeron que debía ser?**

## ⚖️ La diferencia fundamental

### 🎭 El "yo aprendido"
La versión de nosotros mismos que hemos construido para adaptarnos:
- Me adapto para agradar a los demás
- Tomo decisiones basadas en lo que se espera de mí
- Busco aprobación constante
- Evito mostrar mis emociones o vulnerabilidad

### 🌟 El "yo auténtico"  
Aquella parte que existe sin esfuerzo, sin necesidad de validación externa:
- Expreso lo que realmente siento y pienso
- Tomo decisiones alineadas con lo que deseo
- Confío en mi propio criterio
- Me permito sentir y expresarme libremente

## 🚨 Señales de desconexión con el yo auténtico

✅ Sensación de que constantemente estamos actuando para complacer a otros
✅ Insatisfacción o vacío a pesar de lograr objetivos externos  
✅ Miedo de mostrar nuestras emociones reales
✅ Percepción de falta de dirección o sentirse "perdidos"

## 🌈 Señales de alineación con el yo auténtico

✅ Mayor claridad sobre lo que queremos y valoramos
✅ Relaciones más genuinas y significativas
✅ Sensación de paz interna al actuar desde nuestra verdad
✅ Flujo natural en nuestras decisiones y acciones

## 💎 La clave

Para entender quién eres realmente, primero necesitas diferenciar entre lo que has aprendido de los demás y lo que proviene de ti mismo/a.

Despertar a tu verdadero ser es comenzar a identificar qué partes de ti se originan en el deseo de encajar y cuáles provienen de tu autenticidad. ☺️""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🧘 Cultivando la autoconciencia",
            "content": """# Cultivando la autoconciencia

## 🌉 El puente hacia la autenticidad

Vivir de manera auténtica requiere una profunda comprensión de quiénes somos más allá de nuestras experiencias y roles.

La **autoconciencia es el puente** que nos permite regresar a nuestro ser genuino y vivir en coherencia con lo que realmente sentimos y valoramos.

## ⚠️ El problema: Desconexión con el verdadero ser

Cuando olvidamos quienes somos o no tenemos claridad de esto, se nos dificulta más conectarnos con nuestra esencia.

### Señales de desconexión:
✅ Sensación de vacío o insatisfacción, aunque todo parezca estar "bien"
✅ Miedo a decepcionar a los demás al expresar nuestras verdaderas opiniones  
✅ Decisiones basadas en lo que se espera de nosotros y no en lo que realmente queremos
✅ Búsqueda constante de validación externa para sentirnos valiosos

## 🌟 El reconocimiento de la esencia humana

Para despertar la autoconciencia, es fundamental recordar que **somos más que nuestros pensamientos, emociones y circunstancias**.

Somos seres espirituales teniendo una experiencia humana.

### Este reconocimiento nos permite:
- 🔓 **Liberarnos del apego a la identidad social**: Nuestro valor no depende de cómo nos perciben los demás
- 👁️ **Ver más allá de la mente reactiva**: Identificar cuánto viene del condicionamiento y no de nuestra verdadera naturaleza
- 🏠 **Reconectar con lo que siempre hemos sido**: Antes de que las expectativas del mundo nos moldearan

## 🛤️ El camino de regreso: despertar la autoconciencia

### 🔹 Observar sin juzgar
La autoconciencia comienza con notar nuestros pensamientos, emociones y comportamientos sin etiquetarlos como "buenos" o "malos".

**Pregúntate:** ¿De dónde vienen estas ideas sobre mí mismo/a? ¿Son realmente mías o las he aprendido de otros?

### 🔹 Reconocer patrones limitantes
Identificar en qué momentos nos alejamos de nuestra autenticidad y por qué.

**Pregúntate:** ¿En qué situaciones sientes que no puedes ser tú mismo/a? ¿Qué temes que pase si lo eres?

### 🔹 Diferenciar lo que deseas de lo que aprendiste a desear
Muchas veces perseguimos metas que no nos llenan porque nos enseñaron que "eso es lo correcto".

### 🔹 Aceptar todas las partes de ti
No se trata de ser perfectos, sino de aceptar todo lo que somos con compasión y sin rechazo.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "💝 Abrazando la vulnerabilidad",
            "content": """# Abrazando la vulnerabilidad

## 🤔 ¿Vulnerabilidad = Debilidad?

¿Cuántas veces has sentido que mostrarte vulnerable es sinónimo de debilidad? Que si dejas que los demás vean tus miedos, tus dudas o tu dolor, podrían usarlos en tu contra.

La sociedad nos ha enseñado que ser fuerte es "aguantarse todo", no llorar y siempre demostrar que tenemos el control.

## 💪 **¿Y si en realidad la vulnerabilidad fuera una fortaleza?**

La psicóloga **Brené Brown** dice que la vulnerabilidad es el pegumento que une a las personas. Es la capacidad de mostrarnos tal y como somos, sin máscaras.

### 🤝 ¿Qué nos conecta realmente?
Piensa en esto: ¿qué hace que te sientas cercano a alguien? 

Probablemente no sea que todo en su vida es perfecto, sino que ha compartido contigo sus luchas, sus emociones reales.

**Nos conectamos más con la autenticidad que con la perfección.**

## 🚫 ¿Qué pasa cuando evitamos ser vulnerables?

Caemos en mecanismos de defensa que nos alejan de los demás y de nosotros mismos:

### ❌ La armadura emocional
Actuamos como si nada nos afectara. "Estoy bien, todo bien", aunque por dentro sintamos lo contrario.

### ❌ El perfeccionismo  
Creemos que si somos lo suficientemente "buenos", no nos rechazarán. Nos exigimos más de la cuenta.

### ❌ El distanciamiento
Evitamos la cercanía con los demás. Nos volvemos fríos o independientes en exceso.

## 💔 El problema
Aunque estos mecanismos nos protejan del dolor, también nos impiden sentir amor, conexión y autenticidad.

## 🌟 ¿Cómo abrazar la vulnerabilidad?

### 1. 🔄 Cambia tu perspectiva
La vulnerabilidad no es un defecto, es una habilidad que nos hace más humanos.

**Pregúntate:** "¿Qué pasaría si en lugar de esconder mi vulnerabilidad, la acepto y la comparto con quienes confío?"

### 2. 💬 Practica expresar lo que sientes
En vez de decir "Nada, no pasa nada", prueba con "Me siento triste porque esperaba otra respuesta y no sé cómo manejarlo".

### 3. 👥 Rodéate de personas seguras
No todos merecen ver tu vulnerabilidad. Comparte con personas que te escuchen sin juzgar.

### 4. 🤲 Atrévete a pedir ayuda
Aceptar que necesitas apoyo no te hace débil, te hace humano.

### 5. 💎 Acepta tus imperfecciones
En lugar de castigarte por lo que no puedes controlar, date permiso de ser quien eres.

## 🌈 La recompensa

La vulnerabilidad es el camino hacia la conexión, el amor y la autenticidad. **No necesitas ser perfecto para ser amado, solo necesitas ser tú.**""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "✨ Conclusión del Tema 2",
            "content": """## 🌅 El Despertar Auténtico

Ser auténtico es uno de los mayores actos de valentía que podemos hacer en nuestra vida. No porque sea difícil en sí mismo, sino porque desde pequeños hemos aprendido a adaptarnos para ser aceptados.

### 🔍 Lo que has aprendido:

**Tu verdadero ser:** Has aprendido a diferenciar entre el "yo aprendido" y el "yo auténtico", reconociendo qué partes de ti vienen del condicionamiento y cuáles de tu esencia.

**Cultivando la autoconciencia:** Has desarrollado la capacidad de observarte sin juicio y reconectar con tu esencia más allá de las expectativas externas.

**Abrazando la vulnerabilidad:** Has descubierto que la vulnerabilidad no es debilidad, sino el coraje de mostrarte tal como eres para crear conexiones auténticas.

## 🌱 El resultado

Ahora tienes las herramientas para cuestionar esas capas de condicionamiento y conectar con tu esencia más pura. 

Has aprendido que la autenticidad se cultiva a través de la autoconciencia y el coraje de ser vulnerable.

## 💎 Reflexión Final

**Queremos ser fieles a nosotros mismos, pero también tememos ser rechazados o incomprendidos.**

El despertar auténtico no está en hacer cambios radicales de la noche a la mañana, sino en aprender a alinear tus acciones con tu esencia, paso a paso.

---

🎯 **Próximo paso**: En el Tema 3 crearemos el mapa de acción hacia una vida auténtica.""",
            "card_type": "conclusion",
            "order_number": 5
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
    
    # ===============================
    # TEMA 3 CARDS: Mapa de acción hacia la autenticidad
    # ===============================
    
    theme3_cards = [
        {
            "title": "🎯 Mapa de acción hacia la autenticidad",
            "content": """# Tema 3: Mapa de acción hacia la autenticidad

## 🦁 El mayor acto de valentía

Ser auténtico es uno de los mayores actos de valentía que podemos hacer en nuestra vida. No porque sea difícil en sí mismo, sino porque desde pequeños hemos aprendido a adaptarnos para ser aceptados.

## 📚 Lo que hemos aprendido

Nos enseñaron a:
- Encajar
- No hacer demasiado ruido  
- Seguir ciertas reglas sociales sin cuestionarlas

## ⚔️ El conflicto interno

¿Qué pasa cuando lo que la sociedad espera de ti no encaja con quién realmente eres?

Queremos ser fieles a nosotros mismos, pero también tememos ser:
- Rechazados
- Juzgados
- Incomprendidos

## 🗺️ La respuesta no está en cambios radicales

**¿Cómo se empieza a vivir con autenticidad?**

No está en hacer cambios radicales de la noche a la mañana, sino en **aprender a alinear tus acciones con tu esencia**.

## En este tema exploraremos:

**📍 Subtema:**
• **Construir la vida que sí quiero** - Un proceso intencional hacia la autenticidad

## 🎯 Objetivo final

Desarrollar un mapa de acción claro y práctico que te permita construir conscientemente una vida alineada con tu verdadero ser, paso a paso.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🏗️ Construir la vida que sí quiero",
            "content": """# Construir la vida que sí quiero

## 💭 Cambiando la perspectiva

Muchas veces pensamos que nuestra vida está determinada por:
- Las circunstancias
- Lo que nos pasó en el pasado
- La familia en la que nacimos
- Las oportunidades que tuvimos (o no tuvimos)

## 🎯 La verdad liberadora

**En realidad, nuestra vida se construye día a día, con cada decisión, con cada pequeño paso que tomamos.**

Construir la vida que sí queremos no es un acto de suerte ni algo que ocurre de repente. Es un **proceso intencional**, un camino que requiere:
- Claridad
- Compromiso  
- Acción

## ❓ ¿Por qué a veces no elegimos la vida que queremos?

Muchas veces vivimos en **"piloto automático"**, atrapados en una rutina que no elegimos del todo.

### 🧠 Creencias limitantes
Pensamos cosas como "no soy suficiente", "es demasiado tarde para cambiar" o "eso no es para mí".

### 😨 Miedo al cambio
Aunque no estemos felices con nuestra vida actual, al menos es familiar. A veces nos quedamos donde estamos porque nos da miedo lo desconocido.

### 👥 Expectativas externas  
La sociedad, la familia y los amigos opinan sobre lo que deberíamos hacer. Tomamos decisiones para complacerlos en lugar de pensar en lo que realmente queremos.

### 🌫️ Falta de claridad
Sentimos que algo no está bien en nuestra vida, pero no sabemos exactamente qué cambiar o hacia dónde ir.

## 🔄 Pequeñas acciones, grandes cambios

**Construir la vida que quieres no significa cambiarlo todo de golpe.**

No necesitas dejar tu trabajo, mudarte de país o tomar una decisión radical de un día para otro. Los cambios más importantes comienzan con pequeños pasos.

### 🌱 Ejemplos prácticos:

**Si quieres más tranquilidad:**
→ Empieza por crear momentos de calma en tu día

**Si quieres mejores relaciones:**  
→ Empieza a poner límites a quienes te desgastan

**Si quieres cambiar de trabajo:**
→ Investiga opciones, actualiza tu CV o toma un curso

## 💡 No necesitas tenerlo todo claro para empezar

Lo que realmente transforma la vida es la capacidad de dar un paso, luego otro, y otro más.

## 🌟 Ejemplo inspirador

Imagina a alguien que ha pasado años en un trabajo que no le gusta, pero que no se atreve a salir porque le da miedo no encontrar algo mejor.

**Un día decide hacer algo pequeño:**
- Se inscribe en un curso
- Actualiza su currículum  
- Habla con alguien que trabaja en un área que le interesa

**Ese paso le da confianza.** Poco a poco, empieza a ver nuevas oportunidades. Meses después, consigue un trabajo que le apasiona.

**No cambió todo en un día, pero comenzó a moverse en la dirección correcta.**

## 🎯 Paso de acción

💡 **La vida que sí quieres no es un sueño imposible. Es algo que se construye con cada decisión que tomas.**

No importa cuánto tiempo hayas pasado en un camino que no te hace feliz. **Siempre puedes elegir moverte hacia algo que realmente resuene contigo.**

**No esperes el momento perfecto. Empieza hoy. Un paso, una elección, un cambio a la vez.** 💙""",
            "card_type": "practical",
            "order_number": 2
        },
        {
            "title": "✨ Conclusión del Tema 3",
            "content": """## 🗺️ Tu Mapa Hacia la Autenticidad

Has completado el proceso de crear tu mapa de acción hacia una vida más auténtica y alineada con tu verdadero ser.

### 🔍 Lo que has aprendido:

**Construir la vida que sí quieres:** Has comprendido que la vida no está determinada por las circunstancias, sino que se construye día a día con cada decisión consciente que tomas.

Has identificado las barreras que te impedían elegir conscientemente (creencias limitantes, miedo al cambio, expectativas externas, falta de claridad) y has aprendido que los cambios más duraderos comienzan con pequeños pasos.

## 🌱 El resultado

Ahora tienes claridad sobre:
- Qué es lo que realmente quieres en tu vida
- Cómo comenzar a moverte hacia esa visión  
- La importancia de actuar paso a paso, sin esperar el momento perfecto

## 💎 Reflexión Final del Módulo

**Has aprendido a resignificar el "deber ser" por el "deseo ser".**

Ya no vives atrapado en las expectativas externas ni en el miedo al "qué dirán". Tienes el derecho y la capacidad de vivir según tus propios deseos y valores.

Cuando actúas desde tu autenticidad, atraes a las personas y oportunidades alineadas contigo. Confías en tu voz interna y en tu capacidad de elegir lo que realmente te hace feliz.

**La vida auténtica no es un destino, es una forma de caminar. Cada día puedes elegir dar un paso más hacia quien realmente eres.**

---

🎉 **¡Felicidades por completar el Módulo 4!**

Has transformado la creencia "Siempre me detengo a pensar en lo que los demás dirán" por "Tengo el derecho de vivir según mis propios deseos y valores".""",
            "card_type": "conclusion",
            "order_number": 3
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


def init_module4(db: Session):
    """Initialize Module 4: De la expectativa a la realidad"""
    
    # Check if Module 4 already exists
    existing_module = db.query(Module).filter(Module.order_number == 4).first()
    if existing_module:
        print("Module 4 already exists")
        return
    
    print("Creating Module 4: De la expectativa a la realidad...")
    
    # Create Module 4
    module4 = Module(
        title="De la expectativa a la realidad",
        description="Resignifica el 'deber ser' por el 'deseo ser', yendo más allá de las expectativas externas para enfocarte y elegir lo que realmente quieres o deseas.",
        objective="El propósito de este módulo es que resignifiques el 'deber ser' por el 'deseo ser', yendo más allá de las expectativas externas, para enfocarte y elegir lo que realmente quieres o deseas.",
        belief_to_transform="Siempre me detengo a pensar en lo que los demás dirán, aunque me suelo negar aceptarlo, y eso no me deja hacer lo que realmente quiero.",
        expected_results="Logras ir más allá de las expectativas externas y enfocarte en lo que realmente deseas (entender qué es eso). Te permites vivir una vida más alineada con lo que te entrega sentido y plenitud.",
        recommended_book="", # Can be added later
        audio_file="", # Can be added later
        order_number=4,
        is_active=True
    )
    db.add(module4)
    db.flush()  # Get the ID
    
    # Create themes for Module 4
    theme1 = Theme(
        title="Rompiendo barreras",
        content="Identificar las barreras mentales que hemos construido, cuestionarlas y reemplazarlas por creencias que realmente nos ayuden a vivir desde nuestra autenticidad.",
        order_number=1,
        module_id=module4.id
    )
    
    theme2 = Theme(
        title="Despertar auténtico", 
        content="Cuestionar las capas de condicionamiento, mirar hacia adentro y conectar con nuestra esencia más pura más allá de las etiquetas, expectativas y miedos.",
        order_number=2,
        module_id=module4.id
    )
    
    theme3 = Theme(
        title="Mapa de acción hacia la autenticidad",
        content="Desarrollar un proceso intencional para construir conscientemente una vida alineada con el verdadero ser, paso a paso.",
        order_number=3,
        module_id=module4.id
    )
    
    db.add_all([theme1, theme2, theme3])
    db.flush()  # Get the IDs
    
    # Create theme cards using the card creator
    create_module4_cards(db, [theme1, theme2, theme3])
    
    # Create exercises for Module 4
    exercises = [
        # Theme 1 exercises
        Exercise(
            title="Acuerdos",
            question="Identifica los 'acuerdos' o creencias que has heredado sin cuestionar. ¿Cuáles de estos acuerdos ya no te sirven? ¿Qué nuevos acuerdos quieres hacer contigo mismo/a basados en los Cuatro Acuerdos de Miguel Ruiz?",
            instructions="Haz una lista de creencias sobre ti mismo/a, el éxito, las relaciones, etc. que has aceptado sin cuestionar. Para cada una, identifica si viene de tu familia, sociedad o experiencias pasadas. Luego, reescribe esas creencias aplicando los principios: sé impecable con tus palabras, no te tomes nada personal, no hagas suposiciones, haz siempre lo mejor que puedas.",
            order_number=1,
            theme_id=theme1.id
        ),
        Exercise(
            title="Mi voz interior",
            question="Analiza tu voz interior durante una semana. ¿Qué tipo de narrativa predomina en tu mente? ¿Es una voz crítica, alentadora, temerosa o confiada? ¿De dónde crees que viene esta voz y cómo puedes transformarla?",
            instructions="Durante 7 días, anota las frases más recurrentes que te dices a ti mismo/a. Clasifícalas como constructivas o destructivas. Para las destructivas, identifica su origen y reformúlalas de manera compasiva. Crea 3 afirmaciones personales que refuercen tu confianza y practícalas diariamente.",
            order_number=2,
            theme_id=theme1.id
        ),
        
        # Theme 2 exercises
        Exercise(
            title="Ser",
            question="Diferencia entre tu 'yo aprendido' y tu 'yo auténtico'. ¿En qué situaciones actúas para complacer a otros versus cuándo actúas desde tu autenticidad? ¿Qué te impide ser más auténtico/a y qué necesitas para cultivar más autoconciencia?",
            instructions="Crea dos columnas: una describiendo comportamientos del 'yo aprendido' (adaptado para agradar) y otra del 'yo auténtico' (expresión genuina). Identifica patrones y situaciones específicas donde cada uno predomina. Desarrolla estrategias concretas para aumentar momentos de autenticidad en tu día a día.",
            order_number=1,
            theme_id=theme2.id
        ),
        Exercise(
            title="Vulnerabilidad auténtica",
            question="¿Cómo te relacionas con la vulnerabilidad? ¿La ves como debilidad o fortaleza? Describe una situación donde mostrarte vulnerable podría fortalecer una relación o ayudarte a crecer. ¿Qué te impide abrazarla?",
            instructions="Reflexiona sobre tus mecanismos de defensa (armadura emocional, perfeccionismo, distanciamiento). Identifica una relación importante donde podrías ser más vulnerable de manera segura. Practica expresar una emoción auténtica en lugar de esconderla detrás de frases como 'estoy bien'.",
            order_number=2,
            theme_id=theme2.id
        ),
        
        # Theme 3 exercises  
        Exercise(
            title="Realidad",
            question="Define la vida que SÍ quieres construir. ¿Qué aspectos de tu vida actual no están alineados con tu verdadero ser? ¿Cuáles son los primeros 3 pequeños pasos que puedes dar para moverte hacia tu visión auténtica?",
            instructions="Visualiza tu vida ideal viviendo desde la autenticidad. Compárala con tu realidad actual e identifica las brechas más importantes. Para cada área de desalineación (trabajo, relaciones, estilo de vida), define un paso pequeño y concreto que puedas tomar en los próximos 30 días. No busques cambios radicales, sino acciones consistentes.",
            order_number=1,
            theme_id=theme3.id
        )
    ]
    
    db.add_all(exercises)
    db.commit()
    
    print("✅ Module 4 created successfully!")
    print(f"   - 1 Module created: {module4.title}")
    print(f"   - 3 Themes created")
    print(f"   - {len(exercises)} Exercises created")
    
    # Count cards
    total_cards = db.query(ThemeCard).filter(
        ThemeCard.theme_id.in_([theme1.id, theme2.id, theme3.id])
    ).count()
    print(f"   - {total_cards} Theme cards created")
    

if __name__ == "__main__":
    # For testing purposes
    from database import SessionLocal
    
    db = SessionLocal()
    try:
        init_module4(db)
    finally:
        db.close() 