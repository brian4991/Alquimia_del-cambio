from sqlalchemy.orm import Session
from models import Module, Theme, Exercise, ThemeCard
from database import get_db

def create_module2_cards(db: Session, themes: list):
    """Create cards for Module 2 themes based on module2.txt content"""
    
    # Get theme references
    theme1, theme2, theme3 = themes
    
    # ===============================
    # TEMA 1 CARDS: Reconociendo tu valor interno
    # ===============================
    
    theme1_cards = [
        {
            "title": "Introducción al Tema",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Reconociendo tu Valor Interno</h1>

<p><strong>El propósito</strong> de este tema es guiarte hacia una comprensión más profunda de quién eres y por qué eres valioso, independientemente de tus logros o resultados.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">¿Por qué es importante?</h2>

<p>Muchas veces, la sociedad nos enseña a medir nuestro valor por lo que hacemos, pero aquí aprenderás a enfocarte en lo que eres y a cultivar una relación más compasiva contigo mismo.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">En este tema exploraremos:</h2>

<div style="background: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">Subtemas:</h3>
<ul style="list-style-type: disc; margin-left: 20px;">
<li><strong>Identificación de fortalezas</strong></li>
<li><strong>Una mirada al interior</strong></li>
<li><strong>Aceptación y compasión</strong></li>
</ul>
</div>

<p>El valor personal no depende de cumplir expectativas externas; surge de reconocer tus cualidades, fortalezas y singularidad como ser humano.</p>
</div>""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "Identificación de Fortalezas",
            "content": """<div style="color: black; font-family: Arial, sans-serif; line-height: 1.6;">
<h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">Identificación de Fortalezas</h1>

<h2 style="color: #2c3e50; margin-top: 25px;">¿Qué es el valor interno?</h2>

<p>Cuando hablamos de <strong>valor interno</strong>, nos referimos a esa parte de ti que no cambia con los errores, los éxitos o las opiniones de los demás. Es el núcleo de tu identidad, el lugar donde residen tus capacidades, tus intenciones y tu potencial.</p>

<h2 style="color: #2c3e50; margin-top: 25px;">Las fortalezas personales</h2>

<p>Las fortalezas personales son esas cualidades intrínsecas que te permiten superar obstáculos, crear relaciones significativas y aportar al mundo de manera única.</p>

<div style="background: #f8d7da; padding: 15px; border-left: 4px solid #e74c3c; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">El problema</h3>
<p>Muchas veces, pasamos tanto tiempo enfocándonos en nuestras debilidades o errores que dejamos de ver las cualidades que ya poseemos.</p>
</div>

<div style="background: #e8f5e8; padding: 15px; border-left: 4px solid #27ae60; margin: 15px 0;">
<h3 style="color: #2c3e50; margin-top: 0;">El cambio de perspectiva</h3>
<p>Reconocer tus fortalezas implica salir de un enfoque de "déficit" (donde buscas lo que falta) y entrar en un enfoque de "reconocimiento" (donde valoras lo que ya está).</p>
</div>

<p>Este cambio es poderoso porque activa en el cerebro un estado de gratitud y confianza, lo que fortalece nuestra capacidad de enfrentar desafíos.</p>
</div>""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🚫 Tres Limitaciones Comunes",
            "content": """# Tres acciones que limitan nuestras fortalezas:

## 1. 🧠 Creencias limitantes
Las creencias internas negativas, como "no soy lo suficientemente bueno" o "no merezco el éxito". Estas creencias nos hacen dudar de nuestra capacidad y nos impiden aprovechar todo nuestro potencial.

## 2. 🎯 Perfeccionismo
El deseo de hacer las cosas "perfectas" puede ser un obstáculo. Nos centramos tanto en evitar fallos que terminamos bloqueándonos o procrastinando.

## 3. 👥 Comparación constante con los demás
Compararse continuamente con los demás puede desvalorizarnos. Al centrarnos en lo que otros tienen o hacen, perdemos de vista nuestras propias fortalezas y nos sentimos incapaces de destacar.

---

## 💡 Reflexión importante

A veces, las limitaciones que sentimos no provienen de una falta de capacidad, sino de cómo hemos aprendido a vernos a nosotros mismos a lo largo del tiempo.

Al reconocer estas creencias limitantes, podemos empezar a liberar todo nuestro potencial y actuar con confianza en nuestras verdaderas fortalezas.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "🔍 Una Mirada al Interior",
            "content": """# Una Mirada al Interior

## La metáfora de las capas

Imagina que cada experiencia que has vivido es como una capa sobre tu ser interior. Con el tiempo, esas capas se acumulan, formando una especie de "coraza" que a veces nos impide ver quiénes somos realmente en el fondo.

### ✅ Estas capas no son malas
Son parte de lo que nos ha formado, pero muchas veces nos desconectan de nuestra esencia y nos dificultan reconocer nuestras verdaderas fortalezas.

## 🚪 El primer paso: mirar hacia adentro

Es empezar a mirar hacia adentro con honestidad, sin juzgar lo que encontramos. Es como cuando revisamos el interior de un armario desordenado.

Al principio, puede ser incómodo ver todo lo que hemos guardado allí: miedos, inseguridades, creencias limitantes. Pero solo cuando decidimos abrir esa puerta y mirar, podemos empezar a entender qué hay dentro y cómo eso influye en nuestra forma de vernos a nosotros mismos.

## 🎯 ¿Cómo hacerlo?

**Observa sin juzgar:** Tómate un momento para ser consciente de lo que sientes y piensas, sin intentar cambiarlo inmediatamente.

**Diferencia entre lo que eres y lo que sientes que eres:** Un concepto clave en psicología es entender que nuestras emociones no siempre reflejan la realidad. Lo que sentimos cuando nos criticamos, no siempre es lo que realmente somos.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "💝 Aceptación y Compasión",
            "content": """# Aceptación y Compasión

## ¿Por qué la aceptación y compasión son clave?

**Aceptar** no significa rendirse ante nuestras limitaciones, sino más bien reconocer nuestras áreas de crecimiento y tener la disposición de trabajarlas.

Es como mirar un mapa: sabemos dónde estamos, qué caminos podemos tomar y qué nos falta por recorrer, pero sin juzgar nuestra posición actual.

## 🤗 La compasión

La **compasión** es el ingrediente que nos permite acercarnos a nosotros mismos con amabilidad, sobre todo cuando cometemos errores. Nos ayuda a recordar que ser humano implica equivocarse, y no por ello dejamos de ser valiosos o capaces.

## ¿Cómo practicar la aceptación y la compasión?

### 1. 💬 Diálogo interno saludable
Cuando te enfrentes a un reto o una dificultad, observa tu voz interna. ¿Es amable o crítica? Si es negativa, intenta transformarla en algo más comprensivo.

*En lugar de*: "No soy capaz de hacer esto"
*Piensa*: "Estoy aprendiendo y puedo intentar de nuevo"

### 2. ✍️ La importancia de la autocompasión
Un ejercicio muy útil es practicar la autocompasión a través de la meditación o la escritura. Cuando sientas frustración o miedo por no estar a la altura, toma unos minutos para escribir una carta a ti mismo/a, como si fueras tu propio mejor amigo.

### 3. 🌟 Haz las paces con la imperfección
Aceptar y practicar la compasión también implica abrazar la imperfección. Todos tenemos áreas en las que podemos mejorar, pero esto no significa que no seamos valiosos ahora mismo.""",
            "card_type": "practical",
            "order_number": 5
        },
        {
            "title": "✨ Conclusión del Tema 1",
            "content": """## 🏗️ Construyendo una Conexión Profunda Contigo

Este tema es la **base** para desarrollar una conexión más profunda contigo mismo.

### 🔍 Lo que has aprendido:

**Identificar tus fortalezas:** Comienzas a reconocer tus capacidades innatas y lo que te hace único.

**Mirar al interior:** Te permite comprender las influencias pasadas que han formado tu forma de pensar y sentir.

**Aceptación y compasión:** Son esenciales para aceptar tanto tus logros como tus imperfecciones sin juicio.

## 🌱 El resultado

Este proceso de autoconocimiento te brinda la oportunidad de abrazar tu valor interno, facilitando decisiones más conscientes y un crecimiento personal más auténtico y empoderado.

Al aprender a mirar al interior de manera objetiva y compasiva, puedes comenzar a ver tus fortalezas de una manera más clara y libre de las influencias del pasado.

## 💡 Reflexión Final

Cuando empiezas a reconocerte sin las capas de juicio, puedes ver que esas fortalezas siempre han estado allí, solo que a veces estaban cubiertas por la crítica y el perfeccionismo.

---

🎯 **Próximo paso**: En el Tema 2 aprenderemos a transformar la autoexigencia y el perfeccionismo.""",
            "card_type": "conclusion",
            "order_number": 6
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
    # TEMA 2 CARDS: Transformando la autoexigencia y perfeccionismo
    # ===============================
    
    theme2_cards = [
        {
            "title": "🎯 Transformando la Autoexigencia y Perfeccionismo",
            "content": """# Tema 2: Transformando la Autoexigencia y Perfeccionismo

## 🎯 Objetivo del tema

El perfeccionismo y la autoexigencia extrema a menudo surgen del deseo de ser validados, de evitar el error o de sentirnos dignos. Sin embargo, en lugar de impulsarnos, estas tendencias suelen llevarnos a la insatisfacción constante, el agotamiento y la sensación de que nunca somos "suficientes".

## 🔄 El cambio de mentalidad

Hacer un cambio de mentalidad **no significa** renunciar al esfuerzo o a la búsqueda de la excelencia, sino cambiar nuestra relación con ellos.

Es aprender a:
- ✅ Aceptar que el error es parte del crecimiento
- ✅ Reconocer que no necesitamos ser perfectos para ser valiosos
- ✅ Entender que la compasión hacia nosotros mismos es clave para avanzar con confianza y bienestar

## En este tema exploraremos:

**📍 Subtemas:**
• **Darme cuenta de los pensamientos autocríticos**
• **El perfeccionismo**
• **Desafío de la imperfección**

Este proceso implica desaprender hábitos rígidos y construir una nueva mentalidad más flexible, equilibrada y amable.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🧠 Pensamientos Autocríticos",
            "content": """# Darme cuenta de los Pensamientos Autocríticos

## 🔊 La voz crítica interna

La autocrítica es como un eco constante que nos habla en la mente. A veces, esta voz crítica es tan fuerte que creemos que es nuestra propia verdad, cuando en realidad es solo un patrón aprendido.

Si te detienes a escucharla, podrías notar que esa voz no te impulsa a mejorar, sino que te frena, te hace sentir insuficiente y puede disminuir tu confianza.

## 👶 ¿De dónde viene?

La autocrítica se forma a menudo en la infancia, cuando internalizamos las expectativas de figuras autoritarias, como padres o maestros. Esos mensajes, aunque bien intencionados, se convierten en un "guión" que seguimos de adultos.

## 🧠 El sesgo de negatividad

El cerebro tiende a enfocarse más en lo negativo, una tendencia conocida como **sesgo de negatividad**. Por lo tanto, la crítica constante puede reforzar la idea de que nunca somos lo suficientemente buenos.

## 🔍 Tres recomendaciones clave:

### 1. Identifica la voz crítica
*Ejemplo*: Imagina que cometiste un error en el trabajo y piensas: "Soy un desastre, nunca hago nada bien".

### 2. Cuestiónalo
¿Es esto completamente cierto? ¿Realmente nunca haces nada bien? Tal vez hayas hecho muchas cosas correctamente antes, pero este error puntual activa tu voz crítica.

*Replantea*: "Cometí un error, pero eso no define todo mi desempeño. Aprenderé de esto y seguiré mejorando".

### 3. Practica la autocompasión
Habla contigo mismo/a como lo harías con un amigo cercano. Reconoce tus errores sin juzgarte severamente.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🎯 El Perfeccionismo",
            "content": """# El Perfeccionismo

## ⚠️ Una fuerza destructiva

El perfeccionismo puede ser una fuerza poderosa, pero también destructiva. A menudo se enmascara como un impulso hacia la excelencia, pero en realidad, puede ser una forma de miedo al fracaso y al rechazo.

## 🧠 Base psicológica

La psicología sugiere que el perfeccionismo se desarrolla a partir de la necesidad de aprobación externa o de sentir que debemos ser perfectos para merecer amor y aceptación.

### El problema
Esta búsqueda constante de la perfección puede dejarnos sintiéndonos insuficientes y estancados.

## 😰 Efectos del perfeccionismo

Se asocia con:
- Altos niveles de ansiedad
- Estrés
- Autoexigencia extrema

Es como si, a cada paso, te dijeras a ti mismo: "Nada de esto es suficiente".

## 🔄 El ciclo destructivo

Las personas perfeccionistas suelen:
1. Establecer estándares inalcanzables
2. No alcanzar esos estándares
3. Experimentar una fuerte sensación de fracaso y desilusión
4. Procrastinar por temor a que el resultado nunca sea lo suficientemente bueno

## 💡 Recomendaciones prácticas:

### 1. 🎯 Establece estándares realistas
Pregúntate: "¿Esto es realmente lo mejor que puedo hacer en este momento, dadas las circunstancias?"

### 2. 🛤️ Aprende a disfrutar del proceso
Enfócate en el camino, no solo en el destino.

### 3. 🌟 Haz pequeños actos de imperfección consciente
Realiza algo intencionalmente imperfecto para reducir la ansiedad y aceptar que lo suficiente está bien.""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "🌟 Desafío de la Imperfección",
            "content": """# Desafío de la Imperfección

## 🌈 Un paso esencial

El desafío de la imperfección es un paso esencial en el proceso de liberarnos de la tiranía del perfeccionismo.

En la psicología, entendemos que **la imperfección es una parte inevitable y valiosa** de la experiencia humana.

## ⚔️ El conflicto cultural

Nuestra cultura a menudo nos enseña a temerla, asociándola con el fracaso, la vergüenza o la incompetencia.

### 🔄 El cambio de perspectiva
Si dejamos de ver la imperfección como algo negativo y la aceptamos como una oportunidad de crecimiento, podemos transformarla en una herramienta poderosa para avanzar en nuestra vida emocional.

## 🧠 La verdad psicológica

**La perfección no solo es inalcanzable, sino que puede ser perjudicial.**

La imperfección no es sinónimo de fracaso, sino de:
- ✅ Proceso
- ✅ Aprendizaje  
- ✅ Crecimiento

Nos permite experimentar, fallar, aprender y, lo más importante, humanizarnos.

## 🛠️ Qué puedes hacer para aliviar el perfeccionismo:

### 1. 🎯 Abraza el "suficientemente bueno"
En lugar de buscar siempre el "mejor resultado", pregúntate: "¿Esto es lo suficientemente bueno?"

### 2. 📚 Reflexiona sobre lo que puedes aprender
Los errores no son fracasos, sino momentos de crecimiento y aprendizaje. Pregúntate: "¿Qué puedo aprender de esto?"

### 3. 🎉 Celebra los "fracasos"
Cambia tu narrativa: "Aunque no salió como esperaba, he aprendido X, y eso me acerca más a mi meta".

### 4. 💖 Acepta tu vulnerabilidad
La imperfección está conectada con nuestra vulnerabilidad. Reconocer que no somos infalibles nos conecta con nuestra humanidad.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "✨ Conclusión del Tema 2",
            "content": """## 🔓 El Desafío de la Imperfección es Liberador

En lugar de luchar contra lo que somos, podemos aprender a aceptar y abrazar nuestras imperfecciones.

### 🌱 Lo que has aprendido:

**Reconocer pensamientos autocríticos:** Has aprendido a identificar y cuestionar esa voz interna que te limita.

**Comprender el perfeccionismo:** Entiendes ahora que no es un impulso hacia la excelencia, sino un miedo disfrazado que puede paralizarte.

**Abrazar la imperfección:** Has descubierto que la imperfección es parte natural del crecimiento humano.

## 🎁 Los beneficios

Esta aceptación nos permite:
- ✅ Vivir de una manera más auténtica
- ✅ Ser más compasivos con nosotros mismos
- ✅ Enfocarnos en el proceso en lugar de estar atrapados en la meta perfecta
- ✅ Reducir la presión interna
- ✅ Disfrutar más plenamente del camino

## 💎 Reflexión Final

**La verdadera riqueza de la vida radica en lo imperfecto, lo inesperado y lo genuino.**

La perfección crea una falsa imagen de control, pero la imperfección nos conecta con nuestra vulnerabilidad y nuestra autenticidad.

---

🎯 **Próximo paso**: En el Tema 3 aprenderemos a celebrar y celebrarnos, reconociendo nuestros logros y enfocándonos en el proceso.""",
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
    # TEMA 3 CARDS: Celebrar y celebrarse
    # ===============================
    
    theme3_cards = [
        {
            "title": "🎯 Celebrar y Celebrarse",
            "content": """# Tema 3: Celebrar y Celebrarse

## 🤔 Una pregunta importante

¿Cuándo fue la última vez que celebraste un logro, incluso si era pequeño?

Muchas veces, estamos tan enfocados en lo que falta por hacer o en lo que creemos que no hicimos bien, que olvidamos reconocer lo lejos que hemos llegado.

## 🎯 De qué trata este tema

Este tema trata de algo fundamental: aprender a detenerte, mirar tu esfuerzo y decir: **'Lo hice bien'**.

### ¿Por qué es importante?

Celebrarte no es solo una cuestión de autoestima, es:
- ✅ Un acto de amor propio
- ✅ Una práctica que te ayuda a mantener la motivación
- ✅ Una herramienta para el equilibrio emocional

## En este tema exploraremos:

**📍 Subtemas:**
• **Reconocer los pequeños-grandes éxitos**
• **Enfoque en el proceso y esfuerzo**

### 🧠 Base científica

Reconocer los pequeños logros combate la tendencia negativa del cerebro al activar el sistema de recompensa, que libera dopamina y refuerza el comportamiento positivo.

Con el tiempo, este hábito te ayuda a construir una narrativa más equilibrada y saludable sobre quién eres y de lo que eres capaz.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🌟 Reconocer los Pequeños-Grandes Éxitos",
            "content": """# Reconocer los Pequeños-Grandes Éxitos

## 💭 Un cambio de perspectiva

Muchas veces pensamos que los logros tienen que ser extraordinarios para merecer reconocimiento, pero eso no es verdad.

En la vida diaria, los **pequeños pasos** que damos hacia adelante son los que realmente construyen el camino hacia nuestras metas.

## 🎯 ¿Por qué es importante?

Reconocer estos pequeños-grandes éxitos no es solo un acto de gratitud hacia ti mismo, sino una manera de entrenar a tu mente para enfocarse en lo que haces bien, en lugar de en lo que falta.

**Este hábito refuerza la confianza y te motiva a seguir avanzando.**

## 🧠 El sesgo de negatividad

La mente humana está predispuesta a la "negatividad": recordamos más los fracasos que los éxitos, porque nuestro cerebro está diseñado para detectar amenazas y prevenir errores.

### El problema
Esto puede generar una desconexión con nuestras propias capacidades, llevándonos a sentir que nunca es suficiente.

## 🎁 Múltiples beneficios:

### 1. 🧠 Refuerzo positivo
Cuando reconocemos un logro, nuestro cerebro libera dopamina, que nos motiva a seguir trabajando con el mismo esfuerzo.

### 2. 🔄 Reestructuración cognitiva
Las personas autocríticas suelen centrarse más en lo que hicieron mal. Al reconocer los logros, cambiamos nuestra forma de ver las cosas.

### 3. 💪 Aumento de la autoestima
Reconocer nuestros logros fortalece nuestra autoestima al recordarnos que somos capaces de avanzar y superar retos.

### 4. 🌱 Fomento de la resiliencia
Celebrar los pequeños éxitos ayuda a construir resiliencia, porque nos enseña a encontrar esperanza y satisfacción incluso en las dificultades.

### 5. 🎯 Conexión con el presente
Nos ancla al presente y fomenta la práctica de la gratitud. Detenernos a celebrar lo que ya hemos conseguido nos permite disfrutar más del proceso.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🛤️ Enfoque en el Proceso y Esfuerzo",
            "content": """# Enfoque en el Proceso y Esfuerzo

## ⚖️ El conflicto común

La tendencia a medir el valor de nuestras acciones únicamente por los resultados finales es común, pero puede ser contraproducente.

La psicología positiva nos indica que este enfoque puede limitarnos y generar frustración, especialmente cuando los objetivos son a largo plazo.

## 🧠 Lo que dice la ciencia

Según investigaciones, el enfocarse exclusivamente en los resultados:
- ❌ Incrementa el estrés
- ❌ Reduce la satisfacción personal

### 🔄 El cambio beneficioso

Al centrar nuestra atención en el proceso y el esfuerzo:
- ✅ Activamos el sistema de recompensa del cerebro de manera más constante
- ✅ Fomentamos una mayor motivación intrínseca
- ✅ Reducimos la ansiedad
- ✅ Vemos los errores como oportunidades de aprendizaje

## 🛠️ Recomendaciones prácticas:

### 1. 🔍 Crea un ritual de autoevaluación positiva
Al final de cada día o semana, pregúntate: "¿Qué hice hoy que me acercó a mis objetivos, aunque sea un pequeño paso?"

*Ejemplo*: Si estás trabajando en tu bienestar físico, puedes celebrar el hecho de haberte levantado temprano para hacer ejercicio, aunque no hayas corrido más rápido.

### 2. 🧩 Visualiza tus esfuerzos como piezas de un rompecabezas
Cada acción que tomas es una pieza que contribuye al cuadro más grande. No puedes ver la imagen completa hasta que todas las piezas estén en su lugar, pero cada pieza tiene un valor único.

### 3. 💬 Cambia la narrativa interna
*En lugar de*: "Todavía no he llegado" o "No soy lo suficientemente bueno"
*Di*: "Estoy construyendo algo importante, paso a paso" o "El simple hecho de intentarlo ya es un acto de valentía"

### 4. 🎵 Aprecia los microéxitos del camino
Como alguien que aprende un instrumento: si solo se enfoca en tocar una pieza compleja perfectamente, puede desanimarse. Pero si celebra cuando sus dedos se mueven con más fluidez, comenzará a disfrutar más del proceso.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "✨ Conclusión del Tema 3",
            "content": """## 🎉 La Magia del Proceso

Recuerda que **cada pequeño paso que das es un logro en sí mismo**.

No te limites a esperar el "gran éxito" para sentirte orgulloso de ti.

### 🌟 Lo que has aprendido:

**Reconocer pequeños-grandes éxitos:** Has aprendido que los pequeños avances diarios son los que realmente construyen el camino hacia tus metas.

**Enfocarte en el proceso:** Entiendes ahora que la verdadera riqueza está en el camino, no solo en el destino.

**Celebrar tu esfuerzo:** Has descubierto la importancia de reconocer y valorar tu trabajo constante.

## 🎁 Los beneficios de celebrarte:

- ✅ Mayor motivación intrínseca
- ✅ Mejor autoestima
- ✅ Más resiliencia ante los desafíos
- ✅ Conexión con el presente
- ✅ Narrativa interna más positiva

## 💎 Reflexión Final

**Cada momento de esfuerzo, cada desafío superado, y cada lección aprendida a lo largo del camino, son pruebas de tu crecimiento y tu capacidad de seguir adelante.**

La verdadera magia está en el proceso, no solo en el resultado final.

Cuando te enfocas en lo que haces y en cómo lo haces, te permites:
- 🌱 Evolucionar
- 📚 Aprender
- 🎯 Disfrutar del viaje

## 🌈 Mensaje final

**¡Confía en el proceso y en ti mismo!**

Sigue celebrando esos pequeños-grandes avances, porque son los que realmente te están llevando a donde deseas estar.

---

🎉 **¡Felicidades por completar el Módulo 2!**

Has dado un paso importante en tu transformación personal al aprender a valorarte más allá de tus logros y a abrazar tu imperfección como parte de tu humanidad.""",
            "card_type": "conclusion",
            "order_number": 4
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


def init_module2(db: Session):
    """Initialize Module 2: Celebra tu ser"""
    
    # Check if Module 2 already exists
    existing_module = db.query(Module).filter(Module.order_number == 2).first()
    if existing_module:
        print("Module 2 already exists")
        return
    
    print("Creating Module 2: Celebra tu ser...")
    
    # Create Module 2
    module2 = Module(
        title="Celebra tu ser",
        description="Aprende a valorarte más allá de la autoexigencia y reconocer el valor detrás de tus experiencias de logro y aprendizaje.",
        objective="El propósito de este módulo es que logres ir más allá de la autoexigencia para valorar de manera profunda todo lo que eres, y reconocer el valor detrás de tus experiencias de logro y aprendizaje.",
        belief_to_transform="Solo valgo por lo que hago o logro; mis imperfecciones me restan valor.",
        expected_results="Te liberas del exceso de autoexigencia y crítica personal. Aprendes a valorarte y amarte sin codependencias, reconociendo todo lo que ya eres y has logrado.",
        recommended_book="", # Can be added later
        audio_file="", # Can be added later
        order_number=2,
        is_active=True
    )
    db.add(module2)
    db.flush()  # Get the ID
    
    # Create themes for Module 2
    theme1 = Theme(
        title="Reconociendo tu valor interno",
        content="Guiarte hacia una comprensión más profunda de quién eres y por qué eres valioso, independientemente de tus logros o resultados.",
        order_number=1,
        module_id=module2.id
    )
    
    theme2 = Theme(
        title="Transformando la autoexigencia y perfeccionismo", 
        content="Cambiar tu relación con el perfeccionismo y la autoexigencia extrema para desarrollar una mentalidad más flexible, equilibrada y amable.",
        order_number=2,
        module_id=module2.id
    )
    
    theme3 = Theme(
        title="Celebrar y celebrarse",
        content="Aprender a reconocer tus logros, enfocarte en el proceso y desarrollar el hábito de celebrar tus avances.",
        order_number=3,
        module_id=module2.id
    )
    
    db.add_all([theme1, theme2, theme3])
    db.flush()  # Get the IDs
    
    # Create theme cards using the card creator
    create_module2_cards(db, [theme1, theme2, theme3])
    
    # Create exercises for Module 2
    exercises = [
        # Theme 1 exercises
        Exercise(
            title="Mi valor",
            question="¿Cuáles son tus principales fortalezas personales? Identifica al menos 5 cualidades que te permiten superar obstáculos y crear relaciones significativas.",
            instructions="Reflexiona profundamente sobre tus capacidades innatas, tus intenciones y tu potencial. Recuerda que el valor personal no depende de cumplir expectativas externas, sino de reconocer tus cualidades únicas como ser humano. Escribe con detalle sobre cada fortaleza y cómo la has demostrado en tu vida.",
            order_number=1,
            theme_id=theme1.id
        ),
        Exercise(
            title="Identificación de fortalezas",
            question="¿Cuáles de las tres limitaciones comunes (creencias limitantes, perfeccionismo, comparación con otros) reconoces más en ti? Describe cómo te han afectado.",
            instructions="Analiza honestamente cómo estas limitaciones han impactado tu capacidad de reconocer tus fortalezas. Para cada limitación que identifiques, escribe ejemplos específicos de situaciones donde la has experimentado y cómo te ha afectado.",
            order_number=2,
            theme_id=theme1.id
        ),
        Exercise(
            title="Una mirada al interior",
            question="Imagina que puedes quitar las 'capas' de experiencias que han cubierto tu ser interior. ¿Qué encuentras debajo? ¿Cuál es tu esencia verdadera?",
            instructions="Este ejercicio requiere introspección profunda. Tómate tiempo para mirar hacia adentro sin juzgar lo que encuentras. Diferencia entre lo que sientes que eres y lo que realmente eres. Describe tu núcleo auténtico, libre de las influencias externas y autocríticas.",
            order_number=3,
            theme_id=theme1.id
        ),
        Exercise(
            title="Aceptación y compasión",
            question="Escribe una carta a ti mismo/a como si fueras tu mejor amigo. ¿Qué le dirías para mostrar aceptación y compasión por sus imperfecciones?",
            instructions="Practica la autocompasión escribiendo esta carta con amabilidad genuina. Reconoce tus esfuerzos, valida tus sentimientos y recuerda que está bien no ser perfecto. Incluye palabras de aliento y comprensión que normalmente darías a alguien que amas incondicionalmente.",
            order_number=4,
            theme_id=theme1.id
        ),
        
        # Theme 2 exercises
        Exercise(
            title="Perfectamente imperfect@",
            question="Describe una situación reciente donde tu perfeccionismo te causó estrés o te impidió avanzar. ¿Cómo podrías haber manejado esa situación abrazando la imperfección?",
            instructions="Reflexiona sobre los costos emocionales del perfeccionismo en tu vida. Analiza cómo el miedo al fracaso o la necesidad de aprobación externa pueden haberte limitado. Reescribe la situación aplicando el concepto de 'suficientemente bueno' y enfocándote en el aprendizaje en lugar de la perfección.",
            order_number=1,
            theme_id=theme2.id
        ),
        Exercise(
            title="Darme cuenta de los pensamiento autocríticos",
            question="Identifica 3 pensamientos autocríticos recurrentes que tienes. Para cada uno, cuestiona su veracidad y reescríbelo de manera más compasiva.",
            instructions="Presta atención a tu diálogo interno durante una semana. Anota los pensamientos autocríticos más frecuentes. Para cada pensamiento, pregúntate: '¿Es esto completamente cierto? ¿Le diría esto a un amigo?' Luego reescribe cada pensamiento con compasión y realismo.",
            order_number=2,
            theme_id=theme2.id
        ),
        Exercise(
            title="Carta al perfeccionismo - Perdón y Reconocimiento",
            question="Escribe una carta a tu perfeccionismo. Reconoce cómo ha intentado protegerte, pero también perdónalo y despídete de sus aspectos destructivos.",
            instructions="Trata tu perfeccionismo como una parte de ti que ha tenido buenas intenciones pero métodos dañinos. Agradécele por tratar de mantenerte 'seguro' del rechazo o fracaso, pero explícale por qué ya no necesitas esa protección tan rígida. Despídete con comprensión y establece nuevas formas más saludables de buscar la excelencia.",
            order_number=3,
            theme_id=theme2.id
        ),
        Exercise(
            title="Desafío de la imperfección",
            question="Comprométete a hacer algo intencionalmente 'imperfecto' esta semana. Describe qué harás y cómo te sientes al respecto. Después, reflexiona sobre la experiencia.",
            instructions="Elige una actividad donde normalmente buscarías la perfección y hazla intencionalmente 'suficientemente buena'. Puede ser enviar un email sin revisarlo 10 veces, cocinar sin seguir la receta exactamente, o compartir una opinión sin estar 100% seguro. Documenta tus sentimientos antes, durante y después de la experiencia.",
            order_number=4,
            theme_id=theme2.id
        ),
        
        # Theme 3 exercises  
        Exercise(
            title="Mi fiesta interior",
            question="Haz una lista de 10 pequeños-grandes éxitos que has tenido en el último mes. Pueden ser cosas tan simples como levantarte temprano, tener una conversación difícil, o aprender algo nuevo.",
            instructions="Entrena tu mente para reconocer los logros diarios que normalmente pasas por alto. No importa qué tan pequeños parezcan estos éxitos - cada uno representa progreso y esfuerzo. Para cada éxito, escribe por qué es importante y cómo contribuye a tu crecimiento personal.",
            order_number=1,
            theme_id=theme3.id
        ),
        Exercise(
            title="Enfoque en el proceso y esfuerzo",
            question="Piensa en una meta importante que tienes. En lugar de enfocarte solo en el resultado final, identifica y celebra 3 aspectos del proceso que ya estás disfrutando o valorando.",
            instructions="Cambia tu perspectiva de orientada a resultados a orientada al proceso. Para tu meta elegida, identifica: 1) Qué estás aprendiendo en el camino, 2) Qué habilidades estás desarrollando, 3) Cómo cada pequeño paso te está transformando. Celebra estos aspectos del proceso independientemente del resultado final.",
            order_number=2,
            theme_id=theme3.id
        )
    ]
    
    db.add_all(exercises)
    db.commit()
    
    print("✅ Module 2 created successfully!")
    print(f"   - 1 Module created: {module2.title}")
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
        init_module2(db)
    finally:
        db.close() 