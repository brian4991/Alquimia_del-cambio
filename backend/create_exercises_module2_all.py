"""
Script pour créer TOUS les exercices du Module 2 (3 thèmes)
Ejercicio #1 = Thème 1
Ejercicio #2 = Thème 2  
Ejercicio #3 = Thème 3
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_exercises_theme1(db: Session, theme_id: int):
    """Créer les exercices pour le Thème 1 du Module 2"""
    print("\n📝 Création des exercices du Thème 1...")
    
    # EJERCICIO 1.1: Identificación de fortalezas
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: Identificación de fortalezas",
        parent_title="Ejercicio #1: Mi valor",
        instructions="""Este ejercicio te ayudará a identificar tus fortalezas personales, aquellas cualidades que te permiten superar retos y avanzar en la vida, así como los patrones que pueden estar limitando tu capacidad de reconocerlas. A través de esta reflexión, aprenderás a valorar lo que ya eres y cómo esas fortalezas te apoyan cada día.

**Reconociendo mis fortalezas**

Recuerda cómo se han desarrollado tus fortalezas a lo largo de tu vida. Piensa en tu niñez: ¿Qué habilidades o cualidades empezaste a mostrar desde pequeño? ¿Qué situaciones o experiencias te ayudaron a fortalecerlas a medida que crecías? Reflexiona sobre cómo esas fortalezas te han acompañado en tu camino y cómo te han ayudado a superar obstáculos. Este ejercicio es una oportunidad para conectar con el poder que siempre ha estado dentro de ti, reconocerte y valorarte.

¡Este es tu momento para descubrir y celebrar cómo tus fortalezas han crecido contigo!

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tus fortalezas",
                "instructions": """Tómate un momento para pensar en tus fortalezas, aquellas cualidades o habilidades que consideras valiosas. Pregúntate:
• ¿En qué áreas de mi vida me siento competente y seguro/a?
• ¿Qué cualidades admiro de mí mismo/a cuando pienso en mis logros?
• ¿Qué habilidades y talentos me han ayudado a superar obstáculos o situaciones difíciles?

Anota al menos 10 fortalezas que creas que te definen, desde lo más obvio hasta lo más sutil. Ejemplos de fortalezas pueden ser: paciencia, empatía, creatividad, perseverancia, capacidad de liderazgo, etc.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus 10 fortalezas principales (una por línea)"
                    }
                ]
            },
            {
                "title": "Paso 2: Retroalimentación de personas cercanas",
                "instructions": """A menudo, tendemos a subestimar nuestras fortalezas o a no verlas con claridad. Para obtener una visión más completa de ti mismo/a, pide retroalimentación a 5 personas cercanas (pueden ser amigos, familiares o colegas) y hazles las siguientes preguntas:
• ¿Cuáles crees que son mis 5 principales fortalezas?
• ¿En qué situaciones me has visto usar esas fortalezas con éxito?

Anota sus respuestas y compáralas con las que escribiste en el Paso 1. ¿Coinciden algunas respuestas? ¿Te sorprendió algo que dijeron?""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla con las respuestas de 5 personas:",
                        "table_config": {
                            "columns": [
                                {"title": "Nombre de la persona", "type": "text"},
                                {"title": "Fortalezas que identificaron en ti", "type": "text"}
                            ],
                            "rows": 5
                        }
                    }
                ]
            },
            {
                "title": "Paso 3: Identifica creencias limitantes",
                "instructions": """A veces, incluso cuando somos conscientes de nuestras fortalezas, podemos tener creencias limitantes que nos impiden reconocerlas o utilizarlas plenamente. Reflexiona sobre los siguientes puntos:
• ¿Existen creencias o pensamientos que me hagan dudar de mis fortalezas? Por ejemplo: "No soy lo suficientemente bueno/a", "No soy capaz de liderar", "No soy creativo/a".
• ¿De dónde podrían haber venido estas creencias? ¿Están relacionadas con experiencias pasadas, críticas o expectativas ajenas?

Haz una lista de esas creencias limitantes y escribe cómo te afectan en tu vida cotidiana. (utiliza como apoyo el recurso "creencias" para que lo identifiques fácilmente)""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla de creencias limitantes:",
                        "table_config": {
                            "columns": [
                                {"title": "Mi creencia limitante", "type": "text"},
                                {"title": "Efecto en la vida cotidiana", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "Paso 4: Transforma las creencias limitantes",
                "instructions": """Para cada creencia limitante que hayas identificado, escribe una afirmación positiva que la desafíe. Aquí tienes un ejemplo:
• Creencia limitante: "No soy lo suficientemente bueno/a para asumir roles de liderazgo."
• Afirmación positiva: "Tengo la capacidad de liderar con confianza y aprender de mis experiencias."

Repite estas afirmaciones todos los días, especialmente en momentos en los que enfrentes desafíos. Este paso te ayudará a transformar las creencias limitantes en pensamientos más empoderadores.""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Transforma tus creencias limitantes en afirmaciones positivas:",
                        "table_config": {
                            "columns": [
                                {"title": "Creencia limitante", "type": "text"},
                                {"title": "Afirmación positiva", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "Paso 5: Reflexión sobre el uso de fortalezas",
                "instructions": """Para finalizar, reflexiona sobre situaciones recientes en las que hayas utilizado tus fortalezas. Piensa en:
• ¿Cuándo fue la última vez que utilicé alguna de mis fortalezas para resolver un problema o ayudar a alguien?
• ¿Cómo me sentí al hacerlo? ¿Cómo me afectó positivamente?

Escribe sobre una situación específica en la que pusiste en práctica alguna de tus fortalezas. Esto te ayudará a reforzar tu confianza en ellas y a ver su impacto real en tu vida.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe una situación reciente donde utilizaste tus fortalezas y cómo te sentiste"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_1)
    db.flush()
    print(f"✅ Ejercicio 1.1 creado (ID: {exercise_1_1.id})")
    
    # EJERCICIO 1.2: Una mirada al interior
    exercise_1_2 = Exercise(
        title="Ejercicio 1.2: Una mirada al interior",
        parent_title="Ejercicio #1: Mi valor",
        instructions="""Este ejercicio te ayudará a conectar con tu esencia y aceptarte tal como eres.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Conexión contigo mismo/a",
                "instructions": """Siéntate en un lugar tranquilo y respira profundamente. Cierra los ojos y permite que tu mente se calme. Mientras respiras, siente tu cuerpo y observa cómo te sientes en este momento. Conéctate con la idea de que ya eres suficiente tal y como eres.

Pregúntate:
• ¿Cómo me siento ahora mismo?
• ¿Qué cualidades internas me hacen ser quien soy?

Escribe de manera breve lo que surja sin juzgarte.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sientes ahora mismo?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué cualidades internas te hacen ser quien eres?"
                    }
                ]
            },
            {
                "title": "Paso 2: Momentos de autenticidad",
                "instructions": """Ahora, mira hacia adentro y piensa en momentos de tu vida donde te hayas sentido verdaderamente tú mismo/a, en tu forma más auténtica.

Pregúntate:
• ¿Cuándo me he sentido completamente en paz y fiel a quien soy?
• ¿Qué emociones o cualidades estaban presentes en esos momentos?

Escribe unos pocos pensamientos sobre cómo esas experiencias han reflejado tu esencia.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cuándo te has sentido completamente en paz y fiel a quien eres?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué emociones o cualidades estaban presentes en esos momentos?"
                    }
                ]
            },
            {
                "title": "Paso 3: Aceptación de imperfecciones",
                "instructions": """Parte de conocerte a ti mismo/a es aceptar que la perfección no existe y que las imperfecciones también forman parte de tu ser.

Pregúntate:
• ¿Cómo puedo aceptar mis imperfecciones y aprender de ellas?
• ¿Qué áreas de mi vida puedo abrazar con más compasión y menos juicio?

Escribe sobre lo que te gustaría aceptar de ti mismo/a y cómo podrías integrar más compasión en tu vida diaria.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo puedes aceptar tus imperfecciones y aprender de ellas?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué áreas de tu vida puedes abrazar con más compasión y menos juicio?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    print(f"✅ Ejercicio 1.2 creado (ID: {exercise_1_2.id})")
    
    # EJERCICIO 1.3: Aceptación y compasión
    exercise_1_3 = Exercise(
        title="Ejercicio 1.3: Aceptación y compasión",
        parent_title="Ejercicio #1: Mi valor",
        instructions="""Este ejercicio te guiará en el proceso de aceptarte con compasión.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identificar lo que cuesta aceptar",
                "instructions": """Siéntate en un lugar tranquilo, respira profundamente y cierra los ojos. Con cada inhalación, permite que tu cuerpo se relaje. Con cada exhalación, suelta cualquier tensión o juicio hacia ti mismo/a.

Pregúntate:
• ¿Qué parte de mí siento que me cuesta aceptar?
• ¿Cómo me trato a mí mismo/a cuando cometo errores o no estoy a la altura de mis expectativas?

Escribe brevemente sobre las partes de ti mismo/a que te resulta difícil aceptar. No te juzgues, solo observa.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué parte de ti te cuesta aceptar?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te tratas cuando cometes errores?"
                    }
                ]
            },
            {
                "title": "Paso 2: Practicar la compasión hacia ti mismo/a",
                "instructions": """La compasión comienza con el reconocimiento de que todos somos humanos, con nuestras fallas y vulnerabilidades. Ahora, reflexiona sobre cómo puedes ser más amable y compasivo/a contigo mismo/a.

Pregúntate:
• Si un amigo cercano estuviera pasando por lo mismo que yo, ¿cómo le mostraría compasión?
• ¿Qué palabras de aliento le diría a esa persona, y cómo puedo darme esas mismas palabras a mí mismo/a?

Escribe unas líneas con las palabras compasivas que le dirías a un ser querido, pero dirígelas hacia ti mismo/a. Esto es un ejercicio para empezar a ofrecerte el mismo apoyo y comprensión que brindarías a los demás.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo le mostrarías compasión a un amigo cercano en tu situación?"
                    },
                    {
                        "type": "text",
                        "question": "Escribe palabras compasivas dirigidas a ti mismo/a"
                    }
                ]
            },
            {
                "title": "Paso 3: Integrar la aceptación",
                "instructions": """La aceptación es un proceso continuo, y se trata de reconocer que, aunque tenemos áreas por mejorar, ya somos completos tal como somos. Reflexiona sobre cómo puedes integrar la aceptación en tu vida cotidiana.

Pregúntate:
• ¿Cómo puedo aceptar mis imperfecciones sin juzgarme?
• ¿Qué parte de mí puedo empezar a abrazar hoy con más compasión y menos crítica?

Escribe lo que te gustaría aceptar de ti mismo/a hoy, sin prisa por cambiar, solo con el propósito de hacer las paces con lo que eres en este momento.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo puedes aceptar tus imperfecciones sin juzgarte?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué parte de ti puedes empezar a abrazar hoy con más compasión?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación del AMOR PROPIO y la AUTOESTIMA para AGRADECER, SOLTAR, MERECER y PONER LÍMITES
https://www.youtube.com/watch?v=1P37pJGmISo&t=845s

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (VALOR) para saber que has completado esta parte y pases a agendar tu tercera sesión 1:1.

¡Te veo pronto!""",
                "questions": []
            }
        ])
    )
    db.add(exercise_1_3)
    db.flush()
    print(f"✅ Ejercicio 1.3 creado (ID: {exercise_1_3.id})")
    
    db.commit()
    return 3

def create_exercises_theme2(db: Session, theme_id: int):
    """Créer les exercices pour le Thème 2 du Module 2"""
    print("\n📝 Création des exercices du Thème 2...")
    
    # EJERCICIO 2.1: Darme cuenta de los pensamientos autocríticos
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Darme cuenta de los pensamientos autocríticos",
        parent_title="Ejercicio #2: Perfectamente imperfect@",
        instructions="""El propósito de este ejercicio es invitarte a explorar la belleza de la imperfección y desafiar las creencias que tienes sobre lo que significa ser perfecto. Al final de este ejercicio, te habrás conectado con la idea de que no necesitas ser perfecto para ser valioso, y que las imperfecciones son parte esencial de tu humanidad.

**Venciendo al perfeccionismo**

En este espacio, te invito a reflexionar sobre el poder transformador de la imperfección. Piensa en momentos de tu vida en los que el miedo a no ser perfecto te haya detenido o generado ansiedad. ¿Cómo ha afectado este miedo tu forma de actuar, de relacionarte o de tomar decisiones? Reflexiona sobre cómo el perfeccionismo te ha limitado y qué has aprendido de esos momentos. Este ejercicio te brinda la oportunidad de liberarte de esa presión y comenzar a ver la belleza en lo imperfecto. Al aceptar tus errores y defectos, descubrirás que no necesitas ser perfecto para ser valioso ni para avanzar.

¡Este es tu momento para abrazar tu humanidad y reconocer que, en la imperfección, también está la grandeza!

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tus creencias sobre la perfección",
                "instructions": """Comienza haciendo una lista de las creencias que tienes sobre lo que significa ser perfecto. Tómate tu tiempo y escribe lo que realmente piensas. Algunas preguntas que podrían ayudarte son:
• ¿Qué significa para mí la perfección?
• ¿Qué tipos de cosas me esfuerzo por hacer de manera perfecta?
• ¿Cómo me siento cuando no alcanzo la perfección?
• ¿Qué pasa si algo que hago no es perfecto?

Esta reflexión te ayudará a entender mejor la presión que te impones a ti mismo y de dónde vienen esas expectativas.""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla con tus creencias sobre la perfección y su versión positiva:",
                        "table_config": {
                            "columns": [
                                {"title": "Creencias sobre la perfección", "type": "text"},
                                {"title": "Versión positiva del pensamiento", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "Paso 2: Analiza situaciones con la técnica TREC",
                "instructions": """Piensa en situaciones recientes en las que hayas sentido que algo no salió "como esperabas" y cómo reaccionaste. Reflexiona sobre lo que sentiste en esos momentos:
• ¿Cómo te sentiste cuando algo no salió perfecto?
• ¿Cómo respondiste a ese momento? ¿Te sentiste avergonzado o frustrado?
• ¿Qué pensamientos pasaron por tu mente en ese momento? ¿Pensaste que eso significaba que habías fallado o que no eras lo suficientemente bueno?

Es importante ser honesto contigo mismo aquí, para que puedas empezar a desafiar esos pensamientos y patrones de pensamiento automáticos.

Nota: Lee el Recurso: TREC para comprender lo que debes realizar o envíame un mensaje si surgen dudas y tranquilo/a seguiremos trabajando esta herramienta en sesión.

TREC (Terapia Racional Emotiva Conductual):
- A = Activating Event (Evento activador)
- B = Beliefs (Creencias sobre el evento)
- C = Consequences (Consecuencias emocionales y conductuales)
- D = Disputing (Disputa de creencias irracionales)
- E = Effective new beliefs (Nuevas creencias efectivas)""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Analiza una situación usando el modelo TREC:",
                        "table_config": {
                            "columns": [
                                {"title": "A - Evento", "type": "text"},
                                {"title": "B - Creencias", "type": "text"},
                                {"title": "C - Consecuencias", "type": "text"},
                                {"title": "D - Disputa", "type": "text"},
                                {"title": "E - Nueva creencia", "type": "text"}
                            ],
                            "rows": 3
                        }
                    }
                ]
            },
            {
                "title": "Paso 3: Haz una tarea intencionalmente imperfecta",
                "instructions": """Ahora, escoge una tarea que normalmente intentarías hacer de manera perfecta, pero esta vez, hazla intencionalmente imperfecta. Puede ser algo sencillo, como escribir un correo electrónico, organizar tu espacio, o preparar una comida.

• El objetivo aquí es hacerlo de manera intencional y consciente, permitiéndote errores. No corrijas ni revises excesivamente; solo hazlo lo mejor que puedas, sabiendo que no es necesario que sea perfecto.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe la tarea que hiciste intencionalmente imperfecta (o adjunta evidencia)"
                    }
                ]
            },
            {
                "title": "Paso 4: Reflexión sobre la experiencia",
                "instructions": """Después de realizar la tarea imperfecta, reflexiona sobre la experiencia. Tómate un momento para escribir tus pensamientos y sentimientos sobre lo que hiciste. Algunas preguntas que pueden guiarte:
• ¿Cómo te sentiste al dejar de lado la perfección y aceptar la imperfección?
• ¿Qué pensamientos surgieron al ver que la tarea no fue perfecta?
• ¿Fue realmente tan malo como pensabas? ¿Qué aprendiste de hacerlo de manera imperfecta?
• ¿Qué impacto tuvo en tu bienestar el permitirte ser imperfecto?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sentiste al dejar de lado la perfección?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aprendiste de hacer algo de manera imperfecta?"
                    }
                ]
            },
            {
                "title": "Paso 5: Crea afirmaciones positivas",
                "instructions": """Finalmente, escribe una breve declaración que reemplace tus creencias pasadas sobre la perfección por una visión más flexible y compasiva. Por ejemplo:
• "La imperfección es humana y la acepto en mí mismo/a."
• "No necesito ser perfecto/a para ser valioso/a. Mi valor viene de mi autenticidad."
• "Mis errores son oportunidades de crecimiento, no de fracaso."

Esta afirmación te ayudará a reconocer que la perfección no es el estándar que defines para tu vida, sino la capacidad de aceptarte como eres, con tus virtudes y defectos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu afirmación positiva sobre la imperfección"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_1)
    db.flush()
    print(f"✅ Ejercicio 2.1 creado (ID: {exercise_2_1.id})")
    
    # EJERCICIO 2.2: Carta al perfeccionismo
    exercise_2_2 = Exercise(
        title="Ejercicio 2.2: Carta al perfeccionismo - Perdón y Reconocimiento",
        parent_title="Ejercicio #2: Perfectamente imperfect@",
        instructions="""Escribe una carta al perfeccionismo, reconociendo su papel en tu vida y despidiéndote de él con compasión.

Tiempo estimado: 20 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce la presencia del perfeccionismo",
                "instructions": """Escribe sobre cómo el perfeccionismo ha estado presente en tu vida. Reconoce los momentos en los que te exigiste demasiado.

Ejemplo del inicio:
"Querido perfeccionismo, durante mucho tiempo me has acompañado en mi vida, impulsándome a buscar lo mejor, pero también haciéndome sentir que nunca era suficiente..." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe el inicio de tu carta reconociendo al perfeccionismo"
                    }
                ]
            },
            {
                "title": "Paso 2: Pide perdón y reflexiona",
                "instructions": """Reflexiona sobre las veces que te juzgaste o ignoraste tus logros debido al perfeccionismo. Escríbele un perdón sincero a esas partes de ti.

Ejemplo de esta parte:
"Perfeccionismo, te pido perdón por las veces que me exigí más allá de lo saludable. Me duele recordar las ocasiones en que logré grandes cosas, pero no me permití celebrarlas porque sentía que no eran suficientes..." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe la parte de perdón y reflexión de tu carta"
                    }
                ]
            },
            {
                "title": "Paso 3: Cierre y compromiso",
                "instructions": """Cierra tu carta comprometiéndote a valorar tus logros y abrazar tus imperfecciones. Celebra tus fortalezas.

Ejemplo de cierre:
"Hoy decido cambiar esta relación contigo, perfeccionismo. Agradezco lo que intentaste hacer por mí, pero ahora elijo valorarme tal como soy. Me comprometo a reconocer mis logros, celebrar mis fortalezas y abrazar mis imperfecciones como parte de mi humanidad." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe el cierre de tu carta con tu compromiso"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    print(f"✅ Ejercicio 2.2 creado (ID: {exercise_2_2.id})")
    
    # EJERCICIO 2.3: Desafío de la imperfección
    exercise_2_3 = Exercise(
        title="Ejercicio 2.3: Desafío de la imperfección",
        parent_title="Ejercicio #2: Perfectamente imperfect@",
        instructions="""Diseña y completa un desafío personal que te permita practicar la aceptación de la imperfección.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica el área de desafío",
                "instructions": """Reflexiona sobre situaciones donde la imperfección te cause malestar o ansiedad.
• ¿Es en tu trabajo, tus relaciones, tu imagen personal o en tus metas?
• Anota un ejemplo concreto (cómo presentar algo "incompleto", pedir ayuda, o aceptar un error).""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿En qué área la imperfección te causa más malestar?"
                    },
                    {
                        "type": "text",
                        "question": "Describe un ejemplo concreto de esta situación"
                    }
                ]
            },
            {
                "title": "Paso 2: Diseña tu desafío",
                "instructions": """Selecciona un pequeño desafío que te permita practicar la aceptación de la imperfección en esa área. Puede ser algo como:
• Dejar que algo quede "suficientemente bueno" en lugar de "perfecto".
• Decir "no sé" cuando no tengas la respuesta.
• Compartir algo personal aunque no sea impecable.

Ejemplo:
Hoy, en lugar de revisar mi informe tres veces, lo entregaré tras una sola revisión. Me recordará que lo importante es avanzar, no alcanzar la perfección.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe tu desafío específico de imperfección"
                    }
                ]
            },
            {
                "title": "Paso 3: Reflexión post-desafío",
                "instructions": """Después de completar el desafío, responde:
• ¿Cómo te sentiste al permitirte ser imperfecto/a?
• ¿Qué aprendiste sobre ti al enfrentar esta situación?
• ¿Qué harías diferente la próxima vez para seguir practicando la aceptación?

Nota: Si prefieres, puedes diseñar tu propio desafío relacionado con la imperfección. La clave es elegir algo que sea significativo para ti y te permita avanzar con autocompasión.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sentiste al permitirte ser imperfecto/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aprendiste sobre ti?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué harías diferente la próxima vez?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación para MEJORAR tu AUTOESTIMA | CÓMO AUMENTAR el AMOR PROPIO
https://www.youtube.com/watch?v=WjDOhmd5p8g&t=897s

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (IMPERFECCIÓN) para saber que has completado esta parte, pueda revisarte, darte retroalimentación y puedas avanzar al ejercicio número 3.

¡Te veo pronto!""",
                "questions": []
            }
        ])
    )
    db.add(exercise_2_3)
    db.flush()
    print(f"✅ Ejercicio 2.3 creado (ID: {exercise_2_3.id})")
    
    db.commit()
    return 3

def create_exercises_theme3(db: Session, theme_id: int):
    """Créer les exercices pour le Thème 3 du Module 2"""
    print("\n📝 Création des exercices du Thème 3...")
    
    # EJERCICIO 3.1: Reconocer los pequeños-grandes éxitos
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: Reconocer los pequeños-grandes éxitos",
        parent_title="Ejercicio #3: Mi fiesta interior",
        instructions="""En este espacio, te invito a reflexionar sobre los momentos en los que has avanzado, independientemente del resultado final. Piensa en los pequeños pasos que te han llevado a estar donde estás hoy: decisiones que tomaste, desafíos que enfrentaste y el esfuerzo que dedicaste a mejorar. Tal vez no obtuviste el resultado perfecto, pero el hecho de haberte movido hacia adelante ya es digno de celebrarse.

**Honrando tus logros y esfuerzos**

En este espacio, te invito a reflexionar sobre todo lo que has recorrido, incluso cuando nadie más lo vio.
Sobre esas veces que elegiste seguir, aunque estabas cansada.
Sobre los pequeños avances que quizás no celebraste, pero que marcaron una gran diferencia en tu camino.
¿Cuántas veces te exigiste más, sin darte crédito por lo que ya habías logrado?
¿Qué logros de este año merecen ser reconocidos por ti, aunque no hayan sido perfectos?
¿Qué parte de ti te sostuvo cuando dudabas de todo?
A veces estamos tan enfocados en lo que falta, que olvidamos ver la fuerza que nos trajo hasta aquí.

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Lista de logros recientes",
                "instructions": """Piensa en los últimos días o semanas y escribe al menos tres cosas que hayas logrado, sin importar su tamaño. Estos pueden ser desde completar una tarea pendiente hasta haber manejado una situación difícil emocionalmente.
• ¿Qué hiciste para lograrlo?
• ¿Cómo te sentiste en el momento y cómo te sientes ahora al recordarlo?

Ejemplo:
Logro: Me levanté temprano y fui al gimnasio aunque no tenía ganas.
Reflexión: Me sentí orgulloso porque superé mi resistencia inicial y prioricé mi bienestar.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Logro 1: ¿Qué lograste?"
                    },
                    {
                        "type": "text",
                        "question": "Logro 1: ¿Cómo lo lograste y cómo te sientes al recordarlo?"
                    },
                    {
                        "type": "text",
                        "question": "Logro 2: ¿Qué lograste?"
                    },
                    {
                        "type": "text",
                        "question": "Logro 2: ¿Cómo lo lograste y cómo te sientes al recordarlo?"
                    },
                    {
                        "type": "text",
                        "question": "Logro 3: ¿Qué lograste?"
                    },
                    {
                        "type": "text",
                        "question": "Logro 3: ¿Cómo lo lograste y cómo te sientes al recordarlo?"
                    }
                ]
            },
            {
                "title": "Paso 2: Reflexión profunda sobre un logro",
                "instructions": """Elige uno de los logros que escribiste en el paso anterior. Ahora, reflexiona sobre su impacto:
• ¿Qué esfuerzo personal requirió?
• ¿Qué aprendizaje o crecimiento trajo a tu vida?
• ¿Cómo te acerca a la persona que quieres ser?

Ejemplo:
Logro: Terminé un proyecto difícil en el trabajo.
Reflexión: Este logro muestra mi capacidad de compromiso y perseverancia, incluso cuando las cosas no son fáciles. Aprendí a manejar mi tiempo mejor y eso me hace sentir más seguro en mis capacidades.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué esfuerzo personal requirió este logro?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aprendizaje o crecimiento trajo a tu vida?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te acerca a la persona que quieres ser?"
                    }
                ]
            },
            {
                "title": "Paso 3: Ritual de celebración",
                "instructions": """Elige un pequeño ritual para honrar tus logros recientes y conectarte con tu valor. Puede ser algo simbólico pero significativo para ti:
• Escribe una lista de afirmaciones positivas: Ejemplo: "Hoy reconozco que soy capaz y valioso por todo lo que hago."
• Tómate un momento de gratitud: Prepara una taza de tu bebida favorita, siéntate en calma y di en voz alta: "Estoy orgulloso de mí por..."
• Haz algo especial para ti: Regálate un pequeño gesto que simbolice tu éxito, como una pausa para disfrutar algo que te guste.

Ejemplo de reflexión final:
Hoy reconozco que cada paso, por pequeño que parezca, es un triunfo en mi camino. Mis logros, sean grandes o pequeños, son prueba de mi esfuerzo y merecen ser celebrados.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué ritual elegiste para celebrar tus logros?"
                    },
                    {
                        "type": "text",
                        "question": "Escribe tu reflexión final sobre tu celebración"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    print(f"✅ Ejercicio 3.1 creado (ID: {exercise_3_1.id})")
    
    # EJERCICIO 3.2: Enfoque en el proceso y esfuerzo
    exercise_3_2 = Exercise(
        title="Ejercicio 3.2: Enfoque en el proceso y esfuerzo",
        parent_title="Ejercicio #3: Mi fiesta interior",
        instructions="""Aprende a valorar el proceso y el esfuerzo, no solo los resultados.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reflexiona sobre el proceso",
                "instructions": """Piensa en algo importante que hayas hecho recientemente o estés haciendo: puede ser un proyecto, una meta personal o incluso superar un desafío.
• ¿Qué pasos has dado para avanzar?
• ¿Qué aprendizajes han surgido a lo largo del camino, incluso de los errores?
• ¿Cómo has cambiado o crecido durante este proceso?

Ejemplo:
Proceso: Estuve trabajando en mejorar mi salud física.
Reflexión: Cada día que decidí moverme, elegir comida más nutritiva o descansar fue una victoria en sí misma. Aprendí que el progreso no siempre es visible, pero el esfuerzo constante transforma mi forma de cuidarme.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿En qué proceso o meta estás trabajando?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué pasos has dado para avanzar?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aprendizajes han surgido del proceso?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo has cambiado o crecido?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica tus esfuerzos valiosos",
                "instructions": """Escribe tres cosas que hayas hecho en este proceso que te hayan requerido esfuerzo, compromiso o valentía, incluso si crees que no son "perfectas".
• ¿Cómo contribuyó cada una de estas acciones a tu avance?
• ¿Qué cualidades tuyas quedaron reflejadas en ese esfuerzo (ej. paciencia, resiliencia, creatividad)?

Ejemplo:
1. Me levanté temprano para caminar, aunque tenía sueño. Eso demostró mi disciplina.
2. Fui amable conmigo mismo al comer algo que me gustaba sin culparme. Eso mostró mi capacidad de autoaceptación.
3. Ajusté mi plan cuando algo no funcionó, y eso reflejó mi flexibilidad y capacidad de adaptarme.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Esfuerzo 1: ¿Qué hiciste? ¿Qué cualidad reflejó?"
                    },
                    {
                        "type": "text",
                        "question": "Esfuerzo 2: ¿Qué hiciste? ¿Qué cualidad reflejó?"
                    },
                    {
                        "type": "text",
                        "question": "Esfuerzo 3: ¿Qué hiciste? ¿Qué cualidad reflejó?"
                    }
                ]
            },
            {
                "title": "Paso 3: Honra el camino recorrido",
                "instructions": """Elige un pequeño gesto que honre no el resultado, sino el camino recorrido y todo lo que has aprendido y crecido en el proceso. Aquí tienes algunas ideas:
• Escribe una nota para ti mismo: Agradece el esfuerzo que has puesto y lo lejos que has llegado, sin importar si has alcanzado el resultado final.
• Crea un símbolo del proceso: Dibuja o escribe una línea que represente cada paso que has dado, recordándote que cada uno importa.
• Haz algo que te conecte con el presente: Tómate un momento para hacer una pausa, respirar y reconocer que estar en el camino ya es un logro.

Ejemplo de reflexión final:
Hoy me doy permiso para valorar el esfuerzo que he puesto en cada paso. Reconozco que cada pequeño avance, incluso los retrocesos, son parte de mi crecimiento. No necesito llegar a la meta para sentirme orgulloso de lo que estoy logrando día a día.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué gesto elegiste para honrar tu camino?"
                    },
                    {
                        "type": "text",
                        "question": "Escribe tu reflexión final sobre el proceso"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_2)
    db.flush()
    print(f"✅ Ejercicio 3.2 creado (ID: {exercise_3_2.id})")
    
    # EJERCICIO 3.3: Construyendo un puente hacia el amor propio
    exercise_3_3 = Exercise(
        title="Ejercicio 3.3: Construyendo un puente hacia el amor propio",
        parent_title="Ejercicio #3: Mi fiesta interior",
        instructions="""Este ejercicio reúne los temas trabajados en este módulo, ayudándote a integrar el reconocimiento de tu valor, transformar la autoexigencia y celebrar quién eres desde la compasión.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Recuerda un momento de superación",
                "instructions": """Cierra los ojos y recuerda un momento en tu vida donde superaste algo importante o aprendiste una lección valiosa.
• Escríbelo en una frase corta: ¿Qué sucedió?
• ¿Qué cualidad o fortaleza utilizaste para afrontarlo?

Ejemplo:
"Cuando perdí un examen importante, pero me levanté para prepararme mejor la próxima vez. Mostré resiliencia y determinación." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe el momento de superación en una frase"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué cualidad o fortaleza utilizaste?"
                    }
                ]
            },
            {
                "title": "Paso 2: Afirmaciones de autocompasión",
                "instructions": """Mírate al espejo o coloca tu mano sobre tu corazón y repite estas frases o adapta las tuyas:
• "Reconozco mis fortalezas y mis errores; ambos forman parte de mi historia."
• "Me perdono por las veces en las que fui demasiado duro conmigo mismo."

Ejemplo:
Al mirarte, puedes decir: "Hoy me permito ser humano y suficiente tal como soy." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué afirmaciones te dijiste frente al espejo?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te sentiste al decirte estas palabras?"
                    }
                ]
            },
            {
                "title": "Paso 3: Crea un símbolo de amor propio",
                "instructions": """Elige un objeto cercano (puede ser una piedra, una pluma, o incluso un dibujo rápido) y dale un significado especial.
• Mientras sostienes el objeto, repite: "Este es mi recordatorio de que el proceso y las imperfecciones hacen mi vida única y valiosa."

Ejemplo:
"Esta flor en mi escritorio me recordará todos los días que mi esfuerzo y mis pequeños logros son suficientes." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué objeto elegiste como símbolo?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué significado le diste a este objeto?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación ORACIÓN PODEROSA hacia TI | PURIFICAR y ELEVAR la ENERGÍA del AMOR PROPIO
https://www.youtube.com/watch?v=Zd9YlTlxjjw&t=902s

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (FIESTA) para saber que has completado esta parte y pases a agendar tu cuarta sesión 1:1 y obtener acceso a la siguiente estación (módulo #3).

¡Te veo pronto!""",
                "questions": []
            }
        ])
    )
    db.add(exercise_3_3)
    db.flush()
    print(f"✅ Ejercicio 3.3 creado (ID: {exercise_3_3.id})")
    
    db.commit()
    return 3

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DE TOUS LES EXERCICES DU MODULE 2")
        print("=" * 70)
        
        # IDs des thèmes du Module 2 (remplacer par les vrais IDs)
        THEME_1_ID = 7  # Thème 1: Reconociendo tu valor interno
        THEME_2_ID = 8  # Thème 2: Transformando la autoexigencia y perfeccionismo  
        THEME_3_ID = 9  # Thème 3: Celebrar y celebrarse
        
        # Créer tous les exercices
        num_ex_t1 = create_exercises_theme1(db, THEME_1_ID)
        num_ex_t2 = create_exercises_theme2(db, THEME_2_ID)
        num_ex_t3 = create_exercises_theme3(db, THEME_3_ID)
        
        print("\n" + "=" * 70)
        print("✅ TOUS LES EXERCICES DU MODULE 2 CRÉÉS!")
        print("=" * 70)
        print(f"📚 Thème 1 (Mi valor): {num_ex_t1} exercices créés")
        print(f"📚 Thème 2 (Perfectamente imperfect@): {num_ex_t2} exercices créés")
        print(f"📚 Thème 3 (Mi fiesta interior): {num_ex_t3} exercices créés")
        print(f"\n✨ Total: {num_ex_t1 + num_ex_t2 + num_ex_t3} exercices créés!")
        print("\n🎉 Les exercices sont maintenant disponibles dans l'application!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

