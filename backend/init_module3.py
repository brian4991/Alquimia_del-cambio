from sqlalchemy.orm import Session
from models import Module, Theme, Exercise, ThemeCard
from database import get_db

def create_module3_cards(db: Session, themes: list):
    """Create cards for Module 3 themes based on module3.txt content"""
    
    # Get theme references
    theme1, theme2, theme3 = themes
    
    # ===============================
    # TEMA 1 CARDS: Espejos del alma
    # ===============================
    
    theme1_cards = [
        {
            "title": "🎯 Introducción al Tema",
            "content": """# Espejos del Alma

**El propósito** de este tema es invitarte a reflexionar sobre cómo tus experiencias pasadas, tus patrones de apego y tus necesidades no satisfechas influyen en tus relaciones actuales.

## ¿Por qué es importante?

Comprender estas dinámicas no solo te ayuda a construir relaciones más sanas, sino que también te permite sanar partes de ti mismo que aún buscan equilibrio y conexión.

## En este tema exploraremos:

**📍 Subtemas:**
• **¿De dónde vengo y a dónde voy?**
• **Mi estilo de apego**
• **Soy el adulto que necesité**

Las relaciones personales, especialmente las más cercanas, son como espejos que reflejan quiénes somos y las experiencias que hemos acumulado a lo largo de la vida.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🔍 ¿De dónde vengo y a dónde voy?",
            "content": """# ¿De dónde vengo y a dónde voy?

## 🌱 ¿De dónde vengo?

Todo comienza en la **infancia**. Es en este período donde aprendemos nuestras primeras lecciones sobre el amor y las relaciones.

Estas lecciones no siempre se transmiten con palabras; muchas veces, las aprendemos observando cómo nuestros cuidadores se relacionan entre sí y con nosotros.

### 🤔 Preguntas reflexivas:
- ¿Había seguridad y calidez en esas interacciones?
- ¿O había distancia y conflicto?

Estas experiencias iniciales moldean nuestras expectativas sobre las relaciones futuras.

## 🚀 ¿A dónde voy?

Entender cómo nuestras experiencias pasadas nos han moldeado **no significa que estemos condenados a repetirlas**.

La psicología nos enseña que tenemos la capacidad de:
- ✅ Elegir
- ✅ Cambiar  
- ✅ Sanar

## 💡 El poder de la conciencia

Reconocer de dónde vienes no se trata de culpar a nadie, sino de **comprender**. Al explorar tu historia, puedes identificar patrones que ya no te sirven y que puedes cambiar.

Tu historia no define tu destino, pero sí te ofrece valiosas pistas sobre lo que necesitas para sanar y crecer.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "💝 Mi estilo de apego",
            "content": """# Mi estilo de apego

## ¿Qué es el estilo de apego?

El estilo de apego es como una **"huella emocional"** que determina cómo percibimos el amor, la confianza y la seguridad en nuestras relaciones.

## 🔐 Apego seguro
Si recibiste cuidado constante y amor incondicional, permites confiar en los demás, sentirte cómodo con la cercanía emocional y manejar conflictos sin miedo a perder la relación.

## 😰 Apego ansioso  
Si experimentaste respuestas impredecibles de tus cuidadores, puedes sentir miedo al abandono y tender a ser muy sensible a señales de rechazo.

## 🛡️ Apego evitativo
Si tus cuidadores fueron emocionalmente distantes, podrías haber aprendido a valerte por ti mismo y evitar la cercanía como protección del dolor.

## 🌪️ Apego desorganizado
Surge de experiencias tempranas de trauma o abandono. Es una mezcla de deseo de cercanía y miedo a ella.

## 💡 ¿Por qué es importante conocerlo?

Tu estilo de apego no es un destino fijo, pero sí es un punto de partida. Entender cómo te relacionas emocionalmente te da claridad sobre patrones que podrías estar repitiendo.""",
            "card_type": "theory",
            "order_number": 3
        },
        {
            "title": "🌟 Soy el adulto que necesité",
            "content": """# Soy el adulto que necesité

## 🎯 ¿Qué significa esto?

Ser "el adulto que necesitaste" significa tomar conciencia de lo que faltó en tu infancia y aprender a ofrecerte ahora aquello que siempre buscaste en los demás.

Es un acto de **amor propio** y **responsabilidad emocional**.

## 🔍 Reconociendo las necesidades no satisfechas

Cuando éramos niños, dependíamos completamente de los adultos para recibir amor, validación y protección. Si esas necesidades no se cubrieron de manera consistente, es posible que hayamos crecido con ciertas carencias emocionales.

## 🛠️ Recomendaciones para empezar:

### 1. 💚 Valida tus emociones
Cuando sientas tristeza, enojo o miedo, reconoce lo que estás experimentando. Dite: "Es válido sentir esto. Estoy aquí para mí."

### 2. 🏠 Crea un espacio seguro interno
Piensa en lo que un adulto cariñoso te habría dicho cuando eras niño/a para consolarte. Ahora, sé tú quien te hable con esas palabras.

### 3. 🚧 Establece límites saludables
Aprender a decir "no" y proteger tu espacio emocional es un acto de autocuidado.

## 🌈 Transformando tu relación contigo mismo/a

Cuando comienzas a atender tus propias necesidades, algo cambia. Dejas de buscar en los demás lo que puedes darte a ti mismo/a y te relacionas desde un lugar de abundancia, no de carencia.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "✨ Conclusión del Tema 1",
            "content": """## 🪞 Los Espejos del Alma

Entender cómo nos relacionamos con los demás comienza con mirar hacia dentro y reflexionar sobre nuestras experiencias pasadas.

### 🔍 Lo que has aprendido:

**De dónde vengo y a dónde voy:** Has explorado cómo tus experiencias infantiles moldearon tu forma de amar y relacionarte.

**Mi estilo de apego:** Has identificado tu patrón de apego y cómo influye en tus relaciones actuales.

**Soy el adulto que necesité:** Has aprendido a ser tu propio sostén emocional y a atender tus necesidades.

## 🌱 El resultado

Al reconocer esas raíces, puedes entender por qué actúas de cierta manera en tus relaciones y empezar a cambiar los patrones que ya no te sirven.

## 💡 Reflexión Final

Cuando conectamos con nuestro pasado y nos damos permiso de crecer desde ahí, empezamos a construir relaciones más conscientes, equilibradas y auténticas, basadas en la seguridad y el respeto mutuo.

---

🎯 **Próximo paso**: En el Tema 2 construiremos los cimientos de conexión para relaciones más sólidas.""",
            "card_type": "conclusion",
            "order_number": 5
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
    # TEMA 2 CARDS: Cimientos de conexión
    # ===============================
    
    theme2_cards = [
        {
            "title": "🎯 Cimientos de Conexión",
            "content": """# Tema 2: Cimientos de Conexión

## 🏗️ Construyendo bases sólidas

Las relaciones saludables no surgen por azar; se construyen sobre cimientos sólidos que nos permiten conectar de manera auténtica con nosotros mismos y con los demás.

## En este tema exploraremos:

**📍 Subtemas:**
• **Patrones que se repiten**
• **Este duelo ya no me pertenece**
• **Negociando necesidades**
• **Fundamentos de bienestar**
• **Mi persona equilibrio**

## 🎯 Objetivo

Estos cimientos surgen del autoconocimiento, la autocomprensión y la capacidad de negociar nuestras necesidades de forma respetuosa.

Al entender nuestros patrones, aprender a soltar lo que nos limita y equilibrar nuestras emociones, somos capaces de crear conexiones más profundas y significativas.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "🔄 Patrones que se repiten",
            "content": """# Patrones que se repiten

## 🌊 ¿Por qué repetimos patrones?

Los patrones que repetimos en nuestras relaciones amorosas no son casualidad. A menudo, nos encontramos atrapados en ciclos sin entender por qué siempre terminamos eligiendo a las mismas personas.

## 🧠 ¿De dónde vienen?

Los patrones en nuestras relaciones suelen estar profundamente conectados con las experiencias de nuestra infancia, especialmente con la relación que tuvimos con nuestros cuidadores primarios.

### 💫 Lo familiar vs. lo saludable

Muchas veces las personas que crecieron en un ambiente donde la seguridad emocional no era estable tienden a buscar parejas que les generen la misma sensación de incertidumbre.

A pesar de que esta situación les causa dolor, **la inseguridad se convierte en lo "familiar"**.

## 🔍 ¿Cómo podemos cambiar estos patrones?

### 1. 👁️ Reconocerlos
El primer paso es darnos cuenta de que estamos repitiendo un patrón. Pregúntate: ¿qué se repite en mis relaciones pasadas?

### 2. 🎯 Actuar diferente
Una vez conscientes, el siguiente paso es actuar de manera diferente. Cambiar nuestras elecciones, reacciones y comportamiento.

### 3. 💖 Aceptar nuestra vulnerabilidad
Romper los patrones requiere aceptar que no todo tiene que ser perfecto, y que la vulnerabilidad es una oportunidad para conectar genuinamente.""",
            "card_type": "theory",
            "order_number": 2
        },
        {
            "title": "🕊️ Este duelo ya no me pertenece",
            "content": """# Este duelo ya no me pertenece

## 💔 Comprendiendo el duelo

El duelo es una experiencia profundamente humana que todos atravesamos. Se produce cuando perdemos algo o a alguien importante para nosotros.

Sin embargo, a veces nos aferramos a un duelo de manera que no nos permite avanzar.

## 🔓 El proceso de soltar el duelo

El primer paso para sanar es reconocer que **ese duelo ya no te pertenece**. Puede ser difícil aceptar que el dolor que sientes, por más legítimo que sea, ya no es algo que debas cargar.

### 🌟 ¿Cómo soltar el duelo?

**1. ✅ Aceptar lo sucedido**
No se trata de justificar ni minimizar el dolor, sino de permitir que la realidad sea parte de tu proceso de sanación.

**2. 🙏 Honrar lo vivido**
Honrar lo vivido no significa seguir atados al dolor. Puedes recordar lo importante sin seguir anclado en el sufrimiento.

**3. 🤲 Dejar ir lo que no puedes controlar**
No podemos cambiar el pasado, pero sí podemos decidir cómo vivir el presente y qué camino tomar en el futuro.

**4. ⏰ Permitir el tiempo para sanar**
El duelo requiere tiempo. No hay un tiempo exacto para sanar, y cada persona se toma el tiempo que necesita.

## 🌈 Liberar el peso del duelo no resuelto

Al liberarte de esos duelos no resueltos, puedes empezar a construir nuevas bases emocionales más saludables y abiertas.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "⚖️ Negociando necesidades",
            "content": """# Negociando necesidades

## 🎯 ¿Qué significa negociar necesidades?

Negociar no significa ceder en todo, ni hacer que nuestras necesidades sean menos importantes. Se trata de aprender a comunicarlas efectivamente y encontrar puntos de acuerdo.

## 🔍 Identificando nuestras necesidades

Las necesidades pueden ser emocionales, físicas, psicológicas y sociales. Antes de negociar, necesitas conocerte: ¿Qué es lo que realmente necesito de una relación?

## 📝 Negociables vs. No negociables

### 🚫 Necesidades NO negociables
Son fundamentales para el bienestar emocional y psicológico:
- Respeto mutuo
- Honestidad
- Fidelidad  
- Comunicación abierta
- Seguridad emocional

### 🔄 Necesidades negociables
Son aquellas que no comprometen tu salud emocional pero pueden ser más flexibles.

## 💬 La importancia de la comunicación efectiva

Para que nuestras necesidades sean escuchadas y respetadas, necesitamos expresarlas de manera clara, honesta y sin miedo.

### 🛠️ Recomendaciones:

**1. 👂 Escucha activa**
Antes de expresar tus necesidades, escucha las del otro.

**2. 😌 Mantén la calma**
Evita gritos o acusaciones, usa un tono sereno y respetuoso.

**3. 🤝 Sé flexible pero firme**
Reconoce cuándo una necesidad puede ser negociable, pero mantente firme en lo fundamental.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "🏛️ Fundamentos de bienestar",
            "content": """# Fundamentos de bienestar

## 🎯 Los pilares de una relación sana

Lo que realmente define la calidad y estabilidad de una relación son los valores compartidos y el compromiso mutuo con el bienestar de la pareja.

## 🤝 1. Compromiso: La decisión diaria

El compromiso no es solo una promesa verbal, sino una **elección diaria** de estar presente en la relación.

### ✅ ¿Cómo se ve?
- La persona está disponible emocionalmente
- Sus palabras y acciones son coherentes
- Ambos hacen esfuerzos para mantener la conexión

## 🙏 2. Respeto: La base innegociable

Sin respeto, no hay relación sana. Amar a alguien no significa perderse en él ni tolerar faltas que dañen la dignidad propia.

### ✅ ¿Cómo se ve?
- Se comunican sin humillar ni invalidar
- Se sienten seguros expresando pensamientos
- No hay manipulación ni control

## ⭐ 3. Admiración: Ver lo mejor del otro

Más allá del amor y la atracción, la admiración mutua es clave en las relaciones duraderas.

### ✅ ¿Cómo se ve?
- Te inspira y motiva a crecer
- Valoras sus logros y apoyas sus sueños
- Disfrutas aprender de la otra persona

## 🧭 4. Valores compartidos: La brújula

Para que una relación funcione a largo plazo, es fundamental compartir valores esenciales sobre familia, fidelidad, crecimiento personal.""",
            "card_type": "theory",
            "order_number": 5
        },
        {
            "title": "⚖️ Mi persona equilibrio",
            "content": """# Mi persona equilibrio

## 🎯 Elegir conscientemente

Es momento de aplicar todo tu conocimiento para elegir conscientemente a una pareja que te guste, pero que también te haga bien.

## 🔄 Superando el falso dilema

No se trata de elegir entre:
- ❌ Lo que me gusta aunque me haga daño
- ❌ Lo saludable aunque no me emocione

### ✅ La verdadera opción:
Aprender a elegir lo que te gusta **en una versión equilibrada**.

## 📝 ¿Cómo definir mi persona equilibrio?

Necesitas claridad sobre dos cosas:

### 💕 Las características que te atraen
Ejemplo: carismático, independiente, con sentido del humor

### 🌱 Las características que necesitas para una relación sana
Ejemplo: comprometido, emocionalmente disponible, respetuoso

## 🔍 Señales de equilibrio vs. alerta

### ✅ Señales de equilibrio:
- La persona tiene lo que te gusta sin comprometer la estabilidad
- Hay emoción pero también tranquilidad y confianza
- No tienes que esforzarte para que funcione, fluye naturalmente

### 🚩 Señales de alerta:
- Tiene lo que te atrae pero ignora tus necesidades emocionales
- Te sientes en constante incertidumbre
- Tienes que justificar conductas que antes te hicieron daño

## 💡 Tu elección consciente

Amar no es un acto de sacrificio ni de renuncia. Es un acto de **sabiduría**.""",
            "card_type": "practical",
            "order_number": 6
        },
        {
            "title": "✨ Conclusión del Tema 2",
            "content": """## 🏗️ Construyendo Cimientos Sólidos

A lo largo de este tema, has explorado los cimientos que sostienen las relaciones saludables.

### 🔍 Lo que has aprendido:

**Patrones que se repiten:** Has identificado ciclos que puedes romper para elegir conscientemente.

**Soltar duelos:** Has aprendido a liberar el peso del pasado que ya no te pertenece.

**Negociar necesidades:** Has desarrollado herramientas para comunicar y equilibrar lo que necesitas.

**Fundamentos de bienestar:** Has identificado los pilares no negociables de una relación sana.

**Mi persona equilibrio:** Has aprendido a elegir desde la sabiduría, no desde la herida.

## 🌱 El resultado

Ya no eliges desde la herida o la repetición inconsciente, sino desde la claridad y el amor propio. Ahora tienes las herramientas para construir vínculos sanos, alineados con tu bienestar.

## 💎 Reflexión Final

Las relaciones no determinan tu valor, pero sí reflejan cuánto te valoras a ti mismo.

---

🎯 **Próximo paso**: En el Tema 3 aprenderemos a pasar del amor propio al amor compartido.""",
            "card_type": "conclusion",
            "order_number": 7
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
    # TEMA 3 CARDS: Del amor propio al amor compartido
    # ===============================
    
    theme3_cards = [
        {
            "title": "🎯 Del amor propio al amor compartido",
            "content": """# Tema 3: Del amor propio al amor compartido

## 💖 El amor propio como cimiento

El amor propio es el cimiento sobre el cual construimos nuestras relaciones. Si no nos conocemos, valoramos y respetamos a nosotros mismos, es difícil establecer vínculos sanos con los demás.

## ⚖️ El equilibrio esencial

El amor propio no significa aislamiento o autosuficiencia extrema; es el punto de partida para compartir nuestra vida sin perder nuestra esencia.

## 🎯 El desafío

Aprender a mantener el equilibrio: amar al otro sin dejar de amarnos a nosotros mismos.

## En este tema exploraremos:

**📍 Subtemas:**
• **Comunicación consciente**
• **Resolución de conflictos**  
• **Equilibrio: ¿cómo ser con otro?**

## 🔑 Habilidades clave

Para lograrlo, es fundamental desarrollar:
- Comunicación consciente
- Resolución de conflictos
- Capacidad de compartir sin perdernos

El amor no se trata de dos mitades que se complementan, sino de dos personas completas que deciden caminar juntas.""",
            "card_type": "intro",
            "order_number": 1
        },
        {
            "title": "💬 Comunicación consciente",
            "content": """# Comunicación consciente

## 🌉 El puente que conecta

La comunicación es el puente que conecta a dos personas. No basta con hablar; es necesario aprender a expresarnos de manera clara, respetuosa y efectiva.

## ⚠️ Problemas comunes en la comunicación:

- 🔸 Reacciones impulsivas en lugar de respuestas reflexionadas
- 🔸 Suposiciones en lugar de aclaraciones  
- 🔸 Expectativas no expresadas en lugar de peticiones claras

## 💡 1. Hablar desde la vulnerabilidad, no desde la acusación

### ❌ Evita:
"Nunca me prestas atención cuando hablo."

### ✅ Prueba:
"Me siento ignorado/a cuando no me miras mientras hablo, y eso me hace sentir desconectado/a de ti."

## 👂 2. Escucha para comprender, no para responder

### ✅ La escucha activa implica:
- Hacer contacto visual y asentir
- No interrumpir ni apresurarse a dar consejos
- Repetir o parafrasear: "Si entiendo bien, lo que te molesta es..."

## 🗣️ 3. Expresar necesidades en lugar de esperar que adivinen

### ❌ Evita:
"Últimamente siento que no te importo."

### ✅ Prueba:
"Me gustaría que planificáramos más tiempo juntos porque eso me hace sentir valorado/a."

## 💧 Ejemplo práctico: 'El vaso de agua'

Si tienes sed, en lugar de esperar que tu pareja adivine, simplemente di: "Me encantaría un vaso de agua, ¿me lo podrías traer?"

Expresar necesidades claramente evita malentendidos y genera vínculos más sólidos.""",
            "card_type": "practical",
            "order_number": 2
        },
        {
            "title": "🛠️ Resolución de conflictos",
            "content": """# Resolución de conflictos

## 🌱 El conflicto como oportunidad

El conflicto en una relación no es una señal de fracaso, sino una **oportunidad de crecimiento**. La diferencia entre una relación saludable y una destructiva está en cómo enfrentamos esos conflictos.

## 1. 🎯 El problema no es el conflicto, sino cómo lo manejamos

### ❌ Enfoque destructivo:
- Culpar al otro: "Nunca me prestas atención"
- Evitar el problema: "No quiero hablar de esto"
- Actuar con resentimiento: Distanciarse sin resolver

### ✅ Enfoque constructivo:
- Expresar sentimientos sin culpar
- Escuchar con empatía
- Buscar una solución juntos

## 2. 🧘 Regulación emocional antes de resolver

Cuando una discusión se intensifica, el cerebro entra en modo de lucha o huida.

### 🔑 Regla de oro:
**No intentes resolver un conflicto cuando las emociones están fuera de control.**

### 📍 Si la discusión escala:
- Pausa: "Necesito un momento para calmarme"
- Regula tu emoción: respira, camina, escribe
- Vuelve al diálogo con apertura

## 3. 💬 Comunicar sin atacar

### 🛑 Errores comunes:
- Generalizar: "Tú siempre... Nunca..."
- Atacar: "Eres egoísta"
- Victimizarse: "Siempre soy yo quien cede"

### ✅ Estrategias conscientes:
- Usa frases en primera persona
- Pregunta antes de asumir
- Evita lenguaje absolutista

## 4. 🎯 Enfócate en la solución, no en ganar

Pregúntate: **¿Prefieres tener razón o fortalecer la relación?**

Las relaciones más fuertes no son aquellas sin problemas, sino aquellas donde ambas personas enfrentan los conflictos con consciencia y respeto.""",
            "card_type": "practical",
            "order_number": 3
        },
        {
            "title": "⚖️ Equilibrio: ¿cómo ser con otro?",
            "content": """# Equilibrio: ¿cómo ser con otro?

## 🤔 La pregunta esencial

¿Cómo llevamos el amor propio a una relación sin perder nuestra identidad ni caer en el egoísmo?

## ⚖️ Los desequilibrios comunes

### 1. 🔄 Fusión excesiva
Uno se pierde en el otro, dejando de lado sus propias necesidades. La relación se vuelve dependencia emocional.

### 2. ❄️ Distancia excesiva  
Cada persona protege tanto su individualidad que no hay espacio para la conexión real. Relaciones frías sin cercanía.

## 💃 El baile de pareja

Piensa en una pareja bailando. Si uno se mueve sin tomar en cuenta al otro, el baile se desordena. Pero si ambos se sincronizan, sin perder su propia expresión, el baile fluye con armonía.

## 🔑 Claves para encontrar el equilibrio:

### ✅ Espacio propio y compartido
Es saludable compartir tiempo juntos, pero también que cada uno tenga sus propios momentos, hobbies y amigos.

### ✅ Autoconocimiento
Saber qué necesitas y qué te hace feliz antes de esperar que la relación lo haga por ti.

### ✅ Comunicación clara y honesta
Expresar lo que sientes sin miedo a perder al otro.

### ✅ Flexibilidad y adaptabilidad
No se trata de imponer tu forma de ser ni de ceder completamente, sino de encontrar un punto medio.

## 💎 El verdadero equilibrio

El amor no se trata de dos mitades que se complementan, sino de **dos personas completas que deciden caminar juntas**.

El verdadero equilibrio surge cuando puedes estar con alguien sin dejar de ser tú.""",
            "card_type": "practical",
            "order_number": 4
        },
        {
            "title": "✨ Conclusión del Tema 3",
            "content": """## 💖 Del Amor Propio al Amor Compartido

Construir una relación sana no significa perderse en el otro ni cerrarse en una independencia extrema, sino encontrar un equilibrio donde el amor propio y el amor compartido coexistan.

### 🔍 Lo que has aprendido:

**Comunicación consciente:** Has desarrollado habilidades para expresarte con claridad y escuchar con empatía, construyendo puentes en lugar de muros.

**Resolución de conflictos:** Has aprendido que los desacuerdos son oportunidades de crecimiento cuando se manejan con madurez y respeto.

**Equilibrio en la relación:** Has descubierto cómo ser parte de un "nosotros" sin dejar de ser "yo", integrando tu individualidad en un espacio de amor mutuo.

## 🌱 El resultado

Para lograrlo, es fundamental una comunicación donde podamos expresar nuestras emociones sin atacar ni reprimirnos. Aprender a gestionar desacuerdos desde la calma fortalece la conexión.

## 💎 Reflexión Final

**El amor sano no se trata de llenar vacíos, sino de compartir abundancia.**

Las relaciones más sólidas no nacen de la dependencia ni de la distancia, sino de la integración de dos personas que eligen crecer juntas, respetando su individualidad y creando un espacio de amor mutuo.

---

🎉 **¡Felicidades por completar el Módulo 3!**

Has aprendido el arte de amar: desde conocerte profundamente hasta elegir conscientemente y relacionarte de manera equilibrada y auténtica.""",
            "card_type": "conclusion",
            "order_number": 5
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


def init_module3(db: Session):
    """Initialize Module 3: El Arte de Amar"""
    
    # Check if Module 3 already exists
    existing_module = db.query(Module).filter(Module.order_number == 3).first()
    if existing_module:
        print("Module 3 already exists")
        return
    
    print("Creating Module 3: El Arte de Amar...")
    
    # Create Module 3
    module3 = Module(
        title="El Arte de Amar",
        description="Aprende a sostener relaciones personales asertivas y equilibrar tu individualidad para generar mayor estabilidad en tus vínculos.",
        objective="El propósito de este módulo es que aprendas a sostener relaciones personales asertivas, y equilibrar tu individualidad, de tal manera que logres generar una mayor estabilidad en tus vínculos.",
        belief_to_transform="Siempre elijo a las personas equivocadas, parece que estoy destinado a relaciones que no funcionan.",
        expected_results="Logras generar un equilibrio y estabilidad entre la experiencia individual (El Yo) y la experiencia relacional (El Nosotr@s). Aprendes a relacionarte de manera asertiva con tus vínculos, y ser más selectiv@ con las personas que atraes a tu vida.",
        recommended_book="", # Can be added later
        audio_file="", # Can be added later
        order_number=3,
        is_active=True
    )
    db.add(module3)
    db.flush()  # Get the ID
    
    # Create themes for Module 3
    theme1 = Theme(
        title="Espejos del alma",
        content="Reflexionar sobre cómo tus experiencias pasadas, patrones de apego y necesidades no satisfechas influyen en tus relaciones actuales.",
        order_number=1,
        module_id=module3.id
    )
    
    theme2 = Theme(
        title="Cimientos de conexión", 
        content="Construir bases sólidas para relaciones saludables a través del autoconocimiento, comprensión de patrones y negociación de necesidades.",
        order_number=2,
        module_id=module3.id
    )
    
    theme3 = Theme(
        title="Del amor propio al amor compartido",
        content="Desarrollar habilidades de comunicación consciente, resolución de conflictos y equilibrio para compartir la vida sin perder la esencia propia.",
        order_number=3,
        module_id=module3.id
    )
    
    db.add_all([theme1, theme2, theme3])
    db.flush()  # Get the IDs
    
    # Create theme cards using the card creator
    create_module3_cards(db, [theme1, theme2, theme3])
    
    # Create exercises for Module 3
    exercises = [
        # Theme 1 exercises
        Exercise(
            title="Bases",
            question="Reflexiona sobre tu historia emocional en las relaciones. ¿Qué patrones de comportamiento o elección de pareja se repiten en tu vida? ¿Cómo crees que tus experiencias de infancia han influido en tu forma de amar?",
            instructions="Haz un recorrido por tus relaciones significativas (románticas, familiares, amistades). Identifica patrones comunes: tipos de personas que eliges, formas de reaccionar ante conflictos, miedos recurrentes. Conecta estos patrones con experiencias tempranas que puedan haberlos originado.",
            order_number=1,
            theme_id=theme1.id
        ),
        Exercise(
            title="Mi estilo de apego",
            question="Identifica tu estilo de apego predominante (seguro, ansioso, evitativo, desorganizado). ¿Cómo se manifiesta este estilo en tus relaciones actuales? Proporciona ejemplos específicos.",
            instructions="Revisa las descripciones de cada estilo de apego y determina cuál resuena más contigo. Analiza situaciones recientes donde este estilo se haya manifestado. Reflexiona sobre cómo este patrón afecta tu forma de conectar con otros y qué puedes hacer para desarrollar un apego más seguro.",
            order_number=2,
            theme_id=theme1.id
        ),
        Exercise(
            title="Soy el adulto que necesité",
            question="¿Qué necesidades emocionales no fueron satisfechas en tu infancia? ¿Cómo puedes ser ahora el adulto que necesitabas entonces? Describe 3 formas específicas en las que puedes cuidar de ti mismo/a.",
            instructions="Identifica las carencias emocionales de tu infancia (validación, seguridad, amor incondicional, etc.). Para cada necesidad no satisfecha, desarrolla estrategias concretas de autocuidado que puedes implementar ahora. Escribe un compromiso contigo mismo/a sobre cómo vas a atender estas necesidades.",
            order_number=3,
            theme_id=theme1.id
        ),
        
        # Theme 2 exercises
        Exercise(
            title="Fundamentos",
            question="Define tus necesidades no negociables en una relación y tus aspectos negociables. ¿Cuáles son los fundamentos de bienestar que consideras esenciales (compromiso, respeto, admiración, valores compartidos)?",
            instructions="Crea dos listas claras: una con aspectos que no puedes comprometer para tu bienestar emocional, y otra con aspectos donde puedes ser flexible. Para cada fundamento de bienestar, define qué significa específicamente para ti y cómo se vería en una relación sana.",
            order_number=1,
            theme_id=theme2.id
        ),
        Exercise(
            title="Patrones relacionales",
            question="Analiza un patrón específico que se repite en tus relaciones. ¿Cuándo comenzó este patrón? ¿Qué función cumplía originalmente? ¿Cómo puedes cambiarlo conscientemente?",
            instructions="Elige un patrón concreto (por ejemplo: atraerte personas emocionalmente no disponibles, evitar conflictos, ser excesivamente complaciente). Rastrea su origen, comprende su propósito inicial de protección, y desarrolla estrategias específicas para actuar diferente la próxima vez que surja la situación.",
            order_number=2,
            theme_id=theme2.id
        ),
        Exercise(
            title="Mi persona equilibrio",
            question="Describe tu 'persona equilibrio': alguien que tenga las características que te atraen pero también las que necesitas para una relación sana. ¿Cómo reconocerías a esta persona? ¿Qué señales indicarían que es equilibrada?",
            instructions="Crea un perfil detallado que integre lo que te gusta con lo que necesitas. Define señales específicas de equilibrio versus señales de alerta. Reflexiona sobre cómo tus elecciones pasadas se alejaron de este equilibrio y qué harás diferente en el futuro.",
            order_number=3,
            theme_id=theme2.id
        ),
        Exercise(
            title="Duelos pendientes",
            question="¿Hay algún duelo (pérdida, relación pasada, decepción) que aún cargas y que puede estar afectando tus relaciones presentes? ¿Cómo puedes honrar esta experiencia y al mismo tiempo soltarla?",
            instructions="Identifica duelos no resueltos que puedan estar influyendo en tu presente. Para cada uno, escribe una carta de despedida donde reconozcas lo vivido, extraigas los aprendizajes y te permitas soltar conscientemente. Define rituales de cierre que te ayuden a liberar este peso emocional.",
            order_number=4,
            theme_id=theme2.id
        ),
        
        # Theme 3 exercises  
        Exercise(
            title="Conexiones",
            question="Practica la comunicación consciente: describe una situación reciente de conflicto o malentendido. ¿Cómo podrías haber comunicado tus necesidades de manera más efectiva usando las herramientas aprendidas?",
            instructions="Toma una situación real donde hubo dificultad comunicativa. Reescribe el diálogo usando: 1) Lenguaje en primera persona, 2) Expresión clara de necesidades, 3) Escucha activa. Practica estas nuevas formas de comunicación en tu día a día y documenta los resultados.",
            order_number=1,
            theme_id=theme3.id
        ),
        Exercise(
            title="Resolución de conflictos",
            question="Diseña tu estrategia personal para manejar conflictos futuros. ¿Cuáles son tus señales de alarma emocional? ¿Qué herramientas usarás para regularte? ¿Cómo enfocarás la resolución hacia soluciones constructivas?",
            instructions="Crea un 'plan de manejo de conflictos' personalizado que incluya: técnicas de autorregulación emocional, estrategias de comunicación no violenta, y métodos para mantener el foco en soluciones. Practica estos pasos en situaciones de menor intensidad para desarrollar el hábito.",
            order_number=2,
            theme_id=theme3.id
        ),
        Exercise(
            title="Mi balance relacional",
            question="¿Cómo defines el equilibrio entre ser tú mismo/a y estar en relación con otros? Describe tu visión de una relación donde ambas personas mantienen su individualidad mientras construyen algo juntos.",
            instructions="Define tu concepto personal de equilibrio relacional. Identifica áreas donde tiendes a fusionarte demasiado o a distanciarte excesivamente. Establece límites saludables que te permitan ser auténtico/a mientras nutres la conexión. Crea un compromiso personal sobre cómo vas a mantener este equilibrio.",
            order_number=3,
            theme_id=theme3.id
        )
    ]
    
    db.add_all(exercises)
    db.commit()
    
    print("✅ Module 3 created successfully!")
    print(f"   - 1 Module created: {module3.title}")
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
        init_module3(db)
    finally:
        db.close() 