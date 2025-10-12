"""
Script pour COMPLÉTER tous les exercices restants du Module 3
- Thème 2: 4 exercices restants (2.2 à 2.5)
- Thème 3: 3 exercices (3.1 à 3.3)
Total: 7 exercices
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_remaining_theme2_exercises(db: Session, theme_id: int):
    """Créer les 4 exercices restants du Thème 2"""
    print("\n📝 Création des exercices restants du Thème 2...")
    
    # EJERCICIO 2.2: Este duelo ya no me pertenece
    exercise_2_2 = Exercise(
        title="Ejercicio 2.2: Este duelo ya no me pertenece",
        parent_title="Ejercicio #2: Fundamentos",
        instructions="""Aprende a sanar y soltar los duelos relacionales del pasado.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce el duelo",
                "instructions": """Encuentra un lugar tranquilo donde te sientas cómodo/a. Cierra los ojos y haz algunas respiraciones profundas. A medida que respires, permítete recordar las relaciones pasadas que han dejado un impacto emocional importante. Pueden ser relaciones amorosas, pero también cualquier otro tipo de vínculo significativo. Piensa en el dolor o la tristeza que esas experiencias te causaron.

Pregúntate:
• ¿Qué perdí emocionalmente en esta relación?
• ¿Qué cosas aún me duelen de esa relación?
• ¿Qué tipo de huellas dejó en mí esta experiencia?

Escribe todo lo que surge de estas preguntas. No te apresures, permítete sentir lo que surge y ser honesto contigo mismo.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué perdiste emocionalmente en esta relación?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué cosas aún te duelen de esa relación?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué huellas dejó en ti esta experiencia?"
                    }
                ]
            },
            {
                "title": "Paso 2: Checklist de sanación",
                "instructions": """Ahora es el momento de evaluar si realmente has sanado o si el dolor de ese duelo aún está presente en tu vida. Haz un checklist para comprobarlo. Puedes marcar con un "sí" o "no" las siguientes afirmaciones:

• ¿Puedo recordar la relación sin sentir un dolor profundo?
• ¿Soy capaz de hablar de la relación sin revivir emociones negativas intensas?
• ¿Puedo ver lo positivo de la relación (lo que aprendí, lo que me enseñó)?
• ¿Me siento libre de esos recuerdos que me afectan emocionalmente?
• ¿Puedo ver a la otra persona como alguien que tiene su propia vida, sin necesidad de seguir enganchado a la mía?

Si la mayoría de las respuestas son "no", es probable que necesites trabajar un poco más en soltar ese duelo. Si las respuestas son "sí", entonces es una señal de que has logrado sanar y liberarte de ese dolor.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Responde el checklist: ¿Has sanado este duelo? (Explica tus respuestas)"
                    }
                ]
            },
            {
                "title": "Paso 3: Herramientas de cierre",
                "instructions": """El siguiente paso es tomar acción para hacer las paces con el dolor y sanar completamente. Aquí te doy algunas ideas:

• **Carta de despedida**: Escribe una carta a la persona o la relación, expresando todo lo que necesitas decir. No tienes que enviarla, simplemente dejar que las palabras fluyan. Al final de la carta, termina diciendo: "Este duelo ya no me pertenece. Lo suelto con amor y gratitud por lo aprendido."

• **Ritual de cierre**: Crea un pequeño ritual que te ayude a cerrar este capítulo. Puede ser prender una vela mientras visualizas cómo sueltas ese dolor, o comprar una rosa y ponerla en un cajón; a los días cuando esté marchita, será símbolo de que el dolor se ha ido y has cerrado este capítulo.

• **Reemplazar el dolor con gratitud**: Piensa en todo lo que esa relación te enseñó. Escribe tres cosas que aprendiste de esa experiencia y tres cosas que agradecerías por haber vivido esa relación.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué herramienta de cierre elegiste? Describe tu experiencia"
                    },
                    {
                        "type": "text",
                        "question": "Escribe 3 aprendizajes de esa relación"
                    },
                    {
                        "type": "text",
                        "question": "Escribe 3 cosas que agradeces de haber vivido esa experiencia"
                    }
                ]
            },
            {
                "title": "Paso 4: Mirar hacia el futuro",
                "instructions": """Una vez que sientas que has sanado y soltado el duelo, es importante mirar hacia el futuro y crear espacio para lo nuevo.

Pregúntate:
• ¿Qué nuevas oportunidades estoy abriendo para mí al soltar este duelo?
• ¿Qué tipo de relaciones quiero crear en el futuro, sabiendo lo que ahora sé sobre mí mismo?
• ¿Cómo puedo asegurarme de no repetir los mismos patrones que me trajeron dolor?

Recuerda: Sanar un duelo lleva tiempo, y no es un proceso lineal. Es completamente válido sentir que hay días buenos y días más difíciles. Lo importante es que te permitas sentir, reconocer lo aprendido, y soltar lo que ya no te pertenece para avanzar con paz en tu vida.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué nuevas oportunidades se abren al soltar este duelo?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué tipo de relaciones quieres crear en el futuro?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo evitarás repetir patrones dolorosos?"
                    }
                ]
            },
            {
                "title": "Paso 5: Rutina de bienestar (Continuidad)",
                "instructions": """*Paso de continuidad; ten esto listo para nuestra sesión 2 de este módulo

**Crear una rutina de bienestar y reinventar tu vida**

Una vez que hayas sanado y soltado el duelo, es el momento perfecto para reconstruir tu vida. Establece:

1. **Rutina de bienestar personal**: Ejercicio, alimentación consciente, meditación, buen sueño
2. **Círculo de apoyo positivo**: Rodéate de personas que te inspiran y elevan
3. **Reinventar tu vida**: Establece nuevas metas, retoma hobbies, visualiza tu futuro

Importante: Si no tenías saldos pendientes con los duelos, este paso es un chequeo y una guía para el futuro. No solo se trata de parejas amorosas, adáptalo a tu situación.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué rutina de bienestar vas a implementar?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    print(f"✅ Ejercicio 2.2 creado (ID: {exercise_2_2.id})")
    
    # EJERCICIO 2.3: Negociando necesidades
    exercise_2_3 = Exercise(
        title="Ejercicio 2.3: Negociando necesidades",
        parent_title="Ejercicio #2: Fundamentos",
        instructions="""Aprende a identificar y comunicar tus necesidades esenciales en las relaciones.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tus necesidades",
                "instructions": """Siéntate en un lugar tranquilo y respira profundamente. Haz un espacio para conectar contigo mismo y reflexiona sobre lo siguiente:

1. ¿Cuáles son las necesidades emocionales y físicas más importantes para ti en una relación?
Tómate tu tiempo para pensar en lo que realmente necesitas para sentirte valorado, respetado y cuidado.

2. ¿Cuáles son los aspectos que consideras imprescindibles en una relación?
Esto puede incluir cosas como honestidad, fidelidad, compromiso o respeto mutuo.

Escribe tus respuestas de manera libre, sin juzgarte. Este es tu espacio para ser sincero contigo mismo.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cuáles son tus necesidades emocionales y físicas más importantes?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aspectos son imprescindibles para ti en una relación?"
                    }
                ]
            },
            {
                "title": "Paso 2: Listas de negociables y NO negociables",
                "instructions": """Ahora que tienes una idea clara de lo que necesitas en tus relaciones, es hora de hacer dos listas:

• **Lista de lo NO negociable**: Aquí debes escribir todas las necesidades que son esenciales para tu bienestar y felicidad, aquellas que no estás dispuesto a comprometer bajo ninguna circunstancia. Ejemplos: Respeto mutuo, Fidelidad, Apoyo emocional

• **Lista de lo NEGOCIABLE**: En esta lista escribe las necesidades que son flexibles y con las que puedes ser más adaptable según las circunstancias de la relación. Ejemplos: Tiempo de calidad juntos, Frecuencia de contacto, Intereses compartidos""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla con tus necesidades:",
                        "table_config": {
                            "columns": [
                                {"title": "Negociables", "type": "text"},
                                {"title": "NO negociables", "type": "text"}
                            ],
                            "rows": 15
                        }
                    }
                ]
            },
            {
                "title": "Paso 3: Aplicación práctica",
                "instructions": """Ahora que has identificado tus no negociables y negociables, es momento de ponerlo en práctica.

1. Escoge una relación (puede ser con pareja, familia, o amigos) donde sientas que tus necesidades no están siendo completamente respetadas.

2. Haz una lista rápida de los no negociables que son relevantes en esa relación en particular. Pregúntate:
• ¿Hay algo que estoy tolerando que no debería?
• ¿Qué es lo que realmente necesito que cambie para sentirme respetado y valorado?

3. Comunica lo que necesitas de forma clara y directa. Por ejemplo:
• Si necesitas más respeto, di: "Es importante para mí que se respeten mis tiempos y decisiones."
• Si necesitas más apoyo emocional, di: "Me gustaría que me apoyaras cuando tengo un mal día, solo escuchando sin dar consejos."

4. Observa la respuesta de la otra persona. ¿Está dispuesto a negociar o comprometerse? Si no es así, reflexiona sobre cómo eso impacta tu bienestar.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿En qué relación aplicarás esto?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué estás tolerando que no deberías?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo comunicarás tus necesidades?"
                    }
                ]
            },
            {
                "title": "Paso 4: Compromiso contigo mismo/a",
                "instructions": """Ahora que has identificado tus no negociables, haz un compromiso contigo mismo de no estar cerca de personas que no respeten estos principios.

Reflexiona:
• ¿Estás dispuesto a mantener relaciones con personas que no respetan tus valores fundamentales?
• ¿Qué acciones concretas puedes tomar para distanciarte de relaciones que no son saludables?

Escribe un compromiso claro:
"Me comprometo a mantener relaciones con personas que respeten mis necesidades esenciales. Si alguien no respeta mis no negociables, tomaré la decisión de alejarme para cuidar mi bienestar emocional."

(Aclaro: no siempre hay que tirar las relaciones, esto es cuando ya no hay solución, pero es importante intentarlo, negociar con la persona y buscar fortalecer el vínculo antes de tener que alejarse definitivamente)""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu compromiso personal sobre tus necesidades no negociables"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_3)
    db.flush()
    print(f"✅ Ejercicio 2.3 creado (ID: {exercise_2_3.id})")
    
    # EJERCICIO 2.4: Mi Persona Equilibrio
    exercise_2_4 = Exercise(
        title="Ejercicio 2.4: Mi Persona Equilibrio",
        parent_title="Ejercicio #2: Fundamentos",
        instructions="""Define las características de una persona que te aporte equilibrio en tu vida.

Tiempo estimado: 30 minutos""",
        order_number=4,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Analiza tus atracciones pasadas",
                "instructions": """Busca un espacio tranquilo, respira profundamente y piensa en las personas con las que has tenido relaciones significativas. No te enfoques solo en parejas románticas, también considera amistades o vínculos cercanos.

Pregúntate:
• ¿Qué características me han atraído en el pasado?
• ¿Cuáles de esas características han sido saludables y cuáles han terminado generándome dolor o insatisfacción?
• ¿He priorizado rasgos superficiales (atractivo físico, estatus, popularidad) sobre cualidades que realmente sostienen una relación sana?
• ¿He ignorado señales de alerta porque algo en esa persona me resultaba muy atractivo?

Anota tus respuestas y observa si hay patrones en lo que has priorizado y en cómo esas elecciones han impactado tus relaciones.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué características te han atraído en el pasado?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cuáles han sido saludables y cuáles dolorosas?"
                    },
                    {
                        "type": "text",
                        "question": "¿Has priorizado rasgos superficiales sobre cualidades sustanciales?"
                    }
                ]
            },
            {
                "title": "Paso 2: Define lo que realmente necesitas",
                "instructions": """Ahora que tienes una mayor conciencia de lo que has priorizado en el pasado, es momento de definir qué es lo que realmente necesitas en una relación equilibrada.

Pregúntate:
• ¿Cuáles son las cualidades que realmente me hacen sentir en paz y en confianza con alguien?
• ¿Qué características admiro en una pareja a largo plazo?
• ¿Cuáles son los valores que quiero compartir con mi pareja? (Ejemplo: respeto, compromiso, generosidad, responsabilidad emocional)
• ¿Qué aspectos me generan estabilidad emocional y cuáles me desestabilizan?
• ¿Cómo puedo aprender a diferenciar una atracción superficial de una conexión profunda y equilibrada?

Anota estas respuestas en una lista y obsérvala como una guía para futuras elecciones.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué cualidades te hacen sentir en paz y confianza?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué valores quieres compartir con tu pareja?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué te genera estabilidad y qué te desestabiliza?"
                    }
                ]
            },
            {
                "title": "Paso 3: Crea tu Persona Equilibrio",
                "instructions": """Ahora, define el perfil de la persona que se alinea con lo que realmente necesitas. No se trata de idealizar a alguien perfecto, sino de reconocer qué tipo de persona es un buen complemento para ti, equilibrando lo que te atrae con lo que te hace bien.

Ejemplo práctico:
• Me gustan las personas extrovertidas, pero no quiero alguien que solo viva de fiesta y no tenga estabilidad.
• Me atraen las personas seguras de sí mismas, pero necesito que también sean empáticas y accesibles, no arrogantes.
• Me gusta la aventura y la espontaneidad, pero también valoro la estabilidad y la comunicación emocional.

**¿Por qué equilibrio?** Porque puede que algunas características de tus ex parejas no fueran negativas, pero había otras realmente dañinas. Aquí es donde logras identificar las cualidades que te atraen y combinarlas con aquellas que necesitas para formar un balance saludable en una relación.""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Analiza las características de tus ex parejas:",
                        "table_config": {
                            "columns": [
                                {"title": "Características de mis ex parejas", "type": "text"},
                                {"title": "Características NO negociables que afectan mi equilibrio", "type": "text"}
                            ],
                            "rows": 15
                        }
                    },
                    {
                        "type": "text",
                        "question": "✅ Ahora describe tu PERSONA EQUILIBRIO completa (combina lo que te atrae con lo que necesitas para tu bienestar)"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_4)
    db.flush()
    print(f"✅ Ejercicio 2.4 creado (ID: {exercise_2_4.id})")
    
    # EJERCICIO 2.5: Fundamentos de bienestar
    exercise_2_5 = Exercise(
        title="Ejercicio 2.5: Fundamentos de bienestar",
        parent_title="Ejercicio #2: Fundamentos",
        instructions="""Define los valores esenciales que necesitas en una relación.

Tiempo estimado: 30 minutos""",
        order_number=5,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reflexiona sobre valores pasados",
                "instructions": """Siéntate en un lugar tranquilo, respira profundamente y trae a tu mente relaciones significativas en tu vida (parejas, amistades, familia).

Pregúntate:
• ¿Qué valores estaban presentes en estas relaciones que me hicieron sentir seguro y valorado?
• ¿Cuándo me he sentido más respetado y comprendido en una relación?
• ¿Hubo momentos en los que me di cuenta de que faltaba un valor esencial (compromiso, respeto, admiración, confianza)? ¿Cómo me afectó eso?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué valores te hicieron sentir seguro/a y valorado/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cuándo te sentiste más respetado/a y comprendido/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué valores faltaron y cómo te afectó?"
                    }
                ]
            },
            {
                "title": "Paso 2: Define tus 5 valores esenciales",
                "instructions": """Ahora que has reflexionado sobre lo que te ha hecho bien y lo que ha faltado en tus relaciones, define los valores esenciales que necesitas en una relación.

Haz una lista de al menos 5 valores no negociables que consideres fundamentales para el bienestar en una relación de pareja.

Ejemplo:
1. Respeto – Quiero estar con alguien que valore mi opinión y mis límites.
2. Compromiso – Necesito una pareja que tenga disposición para construir una relación a largo plazo.
3. Admiración mutua – Deseo una relación donde ambos nos inspiremos y admiremos genuinamente.
4. Empatía – Es esencial que mi pareja sepa escucharme y ponerse en mi lugar.
5. Valores compartidos – Quiero que tengamos principios de vida similares para construir un futuro juntos.

Escribe los tuyos y reflexiona: ¿Los valores que he elegido están alineados con lo que realmente necesito para una relación sana?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus 5 valores no negociables (uno por línea con explicación)"
                    }
                ]
            },
            {
                "title": "Paso 3: Aplicación y compromiso",
                "instructions": """Ahora que tienes tu lista de valores esenciales, es momento de aplicarlos a la realidad.

Pregúntate:
• ¿Las personas con las que me relaciono actualmente reflejan estos valores?
• ¿En mis relaciones pasadas, estos valores estaban presentes o los sacrifiqué por otros aspectos?
• ¿Estoy dispuesto a mantenerme firme en estos valores sin ceder ante relaciones que no los respeten?

Escribe un compromiso contigo mismo para elegir relaciones que honren estos valores.

Ejemplo de afirmación:
"Elijo rodearme de personas que me respeten, me valoren y compartan mis principios de vida. No aceptaré menos de lo que merezco." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Las personas actuales en tu vida reflejan estos valores?"
                    },
                    {
                        "type": "text",
                        "question": "Escribe tu compromiso personal sobre estos valores"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación para LIBERARSE del APEGO EMOCIONAL que te LIMITA y ser LIBRE
https://www.youtube.com/watch?v=HaB-L6ZOco0

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (FUNDAMENTOS) para saber que has completado esta parte, pueda revisarte, darte retroalimentación y puedas avanzar al ejercicio número 3.

¡Te veo pronto!""",
                "questions": []
            }
        ])
    )
    db.add(exercise_2_5)
    db.flush()
    print(f"✅ Ejercicio 2.5 creado (ID: {exercise_2_5.id})")
    
    db.commit()
    return 4

def create_theme3_exercises(db: Session, theme_id: int):
    """Créer les 3 exercices du Thème 3 - Conexiones"""
    print("\n📝 Création des exercices du Thème 3...")
    
    # EJERCICIO 3.1: Comunicación Asertiva
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: Comunicación Asertiva en las Relaciones",
        parent_title="Ejercicio #3: Conexiones",
        instructions="""Las conexiones humanas son esenciales para nuestro bienestar. Relacionarnos desde el amor y el respeto no solo fortalece nuestros vínculos, sino que también tiene un impacto positivo en nuestra salud mental y física.

En este espacio te invito a reflexionar sobre las relaciones que has tenido a lo largo de tu vida, tanto las positivas como las desafiantes. De todas ellas, seguro que has aprendido valiosas lecciones. Ahora, con esa experiencia, te ofrezco herramientas que te permitirán relacionarte desde tu mejor versión, cultivando relaciones equilibradas y saludables.

*Nota: para estos ejercicios puedes usar el recurso: comunicación para tener información amplia sobre el tema y las relaciones, también te recomiendo el libro: Las 7 reglas de oro para vivir en pareja de John Gottman y Nan Silver, puedes encontrarlo en la sección de bonus

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce tu estilo de comunicación",
                "instructions": """Antes de mejorar tu comunicación, es importante reconocer cómo te comunicas actualmente en tus relaciones. Busca un lugar tranquilo, respira profundo y reflexiona sobre lo siguiente:

• Cuando tienes un conflicto, ¿cómo reaccionas? (¿Gritas, te callas, evades el tema, te defiendes rápidamente?)
• ¿Expresas tus necesidades de manera clara o esperas que el otro las adivine?
• ¿Sientes que los demás realmente te escuchan cuando hablas?
• ¿Tienes miedo de decir lo que piensas por temor a la reacción del otro?

Escribe tus respuestas para tomar conciencia de tus patrones de comunicación.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo reaccionas en los conflictos?"
                    },
                    {
                        "type": "text",
                        "question": "¿Expresas tus necesidades claramente?"
                    },
                    {
                        "type": "text",
                        "question": "¿Sientes que te escuchan?"
                    },
                    {
                        "type": "text",
                        "question": "¿Tienes miedo de expresarte?"
                    }
                ]
            },
            {
                "title": "Paso 2: Reescribe un mensaje de manera asertiva",
                "instructions": """Piensa en una conversación reciente en la que sentiste que no te expresaste de la mejor manera. Tal vez reaccionaste impulsivamente, no dijiste lo que realmente querías, o el mensaje no fue claro.

Describe la situación brevemente: ¿Con quién fue la conversación? ¿Sobre qué trataba? ¿Cómo te expresaste en ese momento?

Identifica qué faltó: ¿Tu mensaje fue agresivo, pasivo o poco claro?

Reescribe tu mensaje de manera asertiva utilizando estos principios:
1. Hablar desde el "yo" en lugar de culpar.
2. Expresar lo que sientes sin atacar.
3. Ser claro y directo sin ser hiriente.

Ejemplo práctico:
🛑 Mensaje original (no asertivo): "Siempre estás en el teléfono cuando estamos juntos, nunca me prestas atención."
✅ Mensaje asertivo: "Me gustaría que cuando estemos juntos podamos compartir sin distracciones, porque para mí es importante sentirme presente en nuestra relación."

Reescribe tu propia situación aplicando estos principios.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe la situación (quién, qué, cómo te expresaste)"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué faltó en tu mensaje original?"
                    },
                    {
                        "type": "text",
                        "question": "Reescribe el mensaje de forma asertiva"
                    }
                ]
            },
            {
                "title": "Paso 3: Practica la escucha activa",
                "instructions": """La comunicación asertiva no solo se trata de hablar bien, sino también de saber escuchar. Para este paso, busca a alguien con quien practicar (puede ser tu pareja, un amigo o un familiar).

Ejercicio de escucha activa:
1. Pídele que te cuente algo que le haya pasado recientemente.
2. Mientras habla, evita interrumpir y concéntrate en comprender su mensaje.
3. Una vez que termine, parafrasea lo que escuchaste para asegurarte de que entendiste bien.
   Ejemplo: "Si entiendo bien, te sentiste frustrado porque esperabas más apoyo en esa situación, ¿cierto?"
4. Pregunta si interpretaste correctamente su mensaje.

Después, reflexiona:
• ¿Cómo se sintió la otra persona al ser escuchada de esta forma?
• ¿Cómo fue tu experiencia al escuchar activamente?

Anota tus observaciones sobre cómo cambia la dinámica cuando realmente escuchamos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Con quién practicaste la escucha activa?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo se sintió la otra persona?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo fue tu experiencia?"
                    }
                ]
            },
            {
                "title": "Paso 4: Compromiso de mejora",
                "instructions": """Ahora que has identificado áreas de mejora en tu comunicación, elige una acción concreta para aplicar a partir de hoy.

Ejemplo:
• Cuando sienta que quiero reaccionar impulsivamente, tomaré una respiración profunda antes de hablar.
• Expresaré mis necesidades de manera clara en lugar de esperar que el otro las adivine.
• Haré preguntas para confirmar que he entendido bien lo que la otra persona me dice.

Escribe tu compromiso personal y ponlo en un lugar visible para recordarlo.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu compromiso personal para mejorar tu comunicación"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    print(f"✅ Ejercicio 3.1 creado (ID: {exercise_3_1.id})")
    
    # EJERCICIO 3.2: Resolución consciente de conflictos
    exercise_3_2 = Exercise(
        title="Ejercicio 3.2: Resolución consciente de conflictos",
        parent_title="Ejercicio #3: Conexiones",
        instructions="""Aprende a manejar los conflictos de manera consciente y constructiva.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Analiza un conflicto pasado",
                "instructions": """Piensa en una discusión o desacuerdo que hayas tenido con tu pareja, un amigo, un familiar o incluso un compañero de trabajo.

Escribe:
• ¿Qué ocurrió?
• ¿Cómo reaccionaste? (¿Fuiste impulsivo? ¿Te cerraste? ¿Evitaste la conversación?)
• ¿Cómo reaccionó la otra persona?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué ocurrió en el conflicto?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo reaccionaste?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo reaccionó la otra persona?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica tu patrón",
                "instructions": """Los conflictos suelen activar patrones automáticos. Reflexiona sobre cuál de estos se parece más a tu estilo de respuesta:

• **Evitación**: Prefiero ignorar el problema y esperar a que pase.
• **Explosión**: Reacciono con enojo o frustración sin pensar demasiado en mis palabras.
• **Defensiva**: Me enfoco en justificarme en lugar de escuchar a la otra persona.
• **Solución consciente**: Trato de calmarme y expresar mis pensamientos de manera respetuosa.

¿Cuál es el estilo que más usaste en este conflicto?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué patrón identificaste en tu respuesta al conflicto?"
                    }
                ]
            },
            {
                "title": "Paso 3: Reescribe el conflicto conscientemente",
                "instructions": """Ahora, piensa en cómo podrías haber manejado el conflicto de una manera más consciente. Usa estos tres pasos:

1. **Reconoce tu emoción sin culpar**
   Ejemplo: En lugar de "Siempre ignoras lo que digo", prueba "Me siento ignorado cuando hablo y no recibo respuesta. Me gustaría que podamos escucharnos mejor."

2. **Escucha antes de reaccionar**
   Pregúntate: "¿Estoy interpretando la situación desde mis miedos o heridas del pasado?"

3. **Busca una solución juntos**
   En lugar de pelear por quién tiene razón, piensa: "¿Qué podemos hacer diferente la próxima vez para resolver esto de manera más sana?"

Ahora, reescribe cómo podrías haber expresado tu punto de vista usando estos principios.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Reescribe cómo manejarías el conflicto conscientemente"
                    }
                ]
            },
            {
                "title": "Paso 4: Compromiso de acción",
                "instructions": """Piensa en una acción concreta que puedas aplicar la próxima vez que enfrentes un conflicto.

Ejemplo:
• Tomarme 5 minutos antes de responder en una discusión.
• Preguntar antes de asumir lo que el otro piensa.
• Hablar desde mis emociones en lugar de culpar.

¿Qué acción específica te comprometes a probar en tu próxima discusión?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué acción específica aplicarás en tu próximo conflicto?"
                    }
                ]
            },
            {
                "title": "Paso 5: Elegir tus batallas",
                "instructions": """No todos los conflictos merecen una pelea. A veces, entramos en discusiones que no nos llevan a ninguna parte. Recuerda: Tu pareja, amigo o familiar no es tu enemigo. No vas con él/ella al campo de batalla, sino que ambos están en el mismo equipo.

Reflexiona sobre estas preguntas antes de entrar en un conflicto:
• ¿Este conflicto es realmente importante o solo estoy reaccionando desde la emoción del momento?
• ¿Lo que quiero expresar ayudará a mejorar la relación o solo quiero "ganar" la discusión?
• ¿Podemos encontrar un punto medio en lugar de luchar por quién tiene la razón?
• ¿Cómo puedo abordar esto sin atacar ni sentir que debo defenderme?

Ejercicio práctico:
Piensa en una discusión reciente y evalúa:
• ¿Era un tema realmente importante para la relación o fue algo momentáneo?
• Si pudieras volver atrás, ¿lo manejarías de otra manera?
• ¿Qué puedes aprender para futuras conversaciones?

Recuerda: No todas las discusiones valen la pena. A veces, elegir la paz sobre el orgullo fortalece más la relación. El objetivo no es ganar la pelea, sino encontrar juntos una solución que los acerque.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Analiza una discusión reciente: ¿Era realmente importante?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué aprendiste para futuras conversaciones?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_2)
    db.flush()
    print(f"✅ Ejercicio 3.2 creado (ID: {exercise_3_2.id})")
    
    # EJERCICIO 3.3: Equilibrio entre individualidad y relación
    exercise_3_3 = Exercise(
        title="Ejercicio 3.3: Equilibrio entre individualidad y relación",
        parent_title="Ejercicio #3: Conexiones",
        instructions="""Aprende a mantener tu individualidad mientras construyes una relación sana.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tu tiempo individual",
                "instructions": """Antes de compartir con otro, es fundamental conocer qué te hace sentir bien contigo mismo.

Tómate unos minutos para reflexionar y escribir:

*Nota: si en este momento no tienes pareja, de igual manera te invito a realizar el ejercicio ya que esto te permite conocer lo que necesitas; y tener claridad cuando estés en una relación.

• ¿Cuáles son las actividades que disfrutas hacer solo? (Ejemplo: leer, hacer ejercicio, meditar, escribir, caminar).
• ¿Cuánto tiempo necesitas semanalmente para estas actividades sin sentir que descuidas tu relación?
• ¿Hay algo que has dejado de hacer por priorizar la relación? ¿Cómo puedes retomarlo sin afectar la conexión con tu pareja?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué actividades disfrutas hacer solo/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cuánto tiempo necesitas para ti semanalmente?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué has dejado de hacer por la relación?"
                    }
                ]
            },
            {
                "title": "Paso 2: Actividades compartidas",
                "instructions": """Ahora piensa en aquellas actividades que disfrutas con tu pareja y que fortalecen la conexión

• ¿Cuáles son las actividades que realmente los unen? (Ejemplo: cocinar juntos, ver películas, viajar, salir a cenar, practicar un deporte).
• ¿Hay actividades que hacen por costumbre, pero que en realidad no disfrutan tanto?
• ¿Qué les gustaría probar juntos para salir de la rutina?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué actividades los unen realmente?"
                    },
                    {
                        "type": "text",
                        "question": "¿Hacen algo por costumbre que no disfrutan?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué les gustaría probar juntos?"
                    }
                ]
            },
            {
                "title": "Paso 3: Diseña tu rutina de equilibrio",
                "instructions": """Con base en los pasos anteriores, diseña una rutina semanal donde puedas integrar ambas dimensiones: tu individualidad y la relación

Escribe un esquema con:
• **Tiempo para ti**: ¿Cuándo y cómo te dedicarás a tus actividades individuales?
• **Tiempo en pareja**: ¿Qué momentos compartirán sin distracciones?
• **Tiempo libre o flexible**: Espacios para improvisar o adaptarse a las necesidades del momento.

Ejemplo:
**Lunes a viernes:**
• 7:00 am – Tiempo personal: Meditación y ejercicio
• 8:00 pm – Actividad compartida: Cocinar y cenar juntos

**Fin de semana:**
• Sábado en la mañana – Tiempo individual: Salida con amigos
• Sábado en la tarde – Actividad compartida: Paseo o película
• Domingo – Tiempo flexible según lo que ambos necesiten""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu rutina semanal de equilibrio (detalla días, horarios y actividades)"
                    }
                ]
            },
            {
                "title": "Paso 4: Evaluación y ajuste",
                "instructions": """Después de una o dos semanas con esta rutina, reflexiona:

• ¿Sientes que tienes más equilibrio entre tu individualidad y la relación?
• ¿Notas que la relación se siente más conectada o más libre?
• ¿Es necesario ajustar algunos tiempos o actividades?

El equilibrio no es una fórmula fija, sino una práctica constante de ajuste y comunicación. Recuerda que una relación sana no significa perderte en el otro, sino encontrar un ritmo que les permita crecer juntos sin dejar de ser ustedes mismos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Después de implementar la rutina: ¿Sientes más equilibrio?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué ajustes necesitas hacer?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación ATRAER el AMOR VERDADERO | RITUAL para ELEVAR la ENERGÍA del AMOR
https://www.youtube.com/watch?v=fAPw72wCzJg

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (CONEXIONES) para saber que has completado esta parte y pases a agendar tu sexta sesión 1:1 y obtener acceso a la siguiente estación (módulo #4).

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
        print("🚀 COMPLÉTION DU MODULE 3 - EXERCICES RESTANTS")
        print("=" * 70)
        
        # IDs des thèmes du Module 3
        THEME_2_ID = 11  # Thème 2: Construyendo vínculos sanos
        THEME_3_ID = 12  # Thème 3: Del amor propio al amor compartido
        
        # Compléter les exercices du thème 2 (4 restants)
        num_ex_t2 = create_remaining_theme2_exercises(db, THEME_2_ID)
        
        # Créer les exercices du thème 3 (3 exercices)
        num_ex_t3 = create_theme3_exercises(db, THEME_3_ID)
        
        print("\n" + "=" * 70)
        print("✅ MODULE 3 COMPLÉTÉ!")
        print("=" * 70)
        print(f"📚 Thème 2 (Fundamentos): {num_ex_t2} exercices supplémentaires créés (Total: 5)")
        print(f"📚 Thème 3 (Conexiones): {num_ex_t3} exercices créés")
        print(f"\n✨ Total Module 3: 11 exercices complets!")
        print("\n🎉 Tous les exercices du Module 3 sont maintenant disponibles!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

