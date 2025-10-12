"""
Script pour créer TOUS les exercices du Module 3 (3 thèmes)
Le Module 3 a BEAUCOUP d'exercices (11 en total!)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_exercises_theme1(db: Session, theme_id: int):
    """Créer les exercices pour le Thème 1 du Module 3 - Espejos del alma"""
    print("\n📝 Création des exercices du Thème 1...")
    
    # EJERCICIO 1.1: De dónde vengo y a donde voy?
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: De dónde vengo y a donde voy?",
        parent_title="Ejercicio #1: Bases",
        instructions="""Este ejercicio tiene como objetivo invitarte a explorar tu historia relacional, identificar cómo las experiencias pasadas han moldeado tu forma de relacionarte y reflexionar sobre los patrones que sigues en tus relaciones. Además, te permitirá imaginar y proyectar un nuevo camino para construir vínculos más conscientes, saludables y auténticos.

**Espejos del alma**

En este espacio te invito a reflexionar sobre los eventos, relaciones y experiencias que han dejado una marca en ti. Todos venimos de un lugar emocional único, formado por aprendizajes, desafíos y momentos significativos. Este ejercicio no se trata de juzgar tu pasado, sino de comprenderlo para construir un presente y futuro más consciente.
Piensa en tu historia como un mapa: necesitas saber de dónde vienes para decidir hacia dónde quieres ir.
¡Este es un momento para conectar con las lecciones y los recursos internos que ya posees!

**Escribiendo tu historia relacional**

Antes de comenzar con el paso a paso, quiero que te tomes un momento para reflexionar profundamente sobre tu historia relacional. Escribe un párrafo largo y detallado sobre cómo han sido tus relaciones a lo largo de tu vida.

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Reflexión inicial: Tu historia relacional",
                "instructions": """Comienza con tus primeros vínculos:
• ¿Cómo fue tu relación con tus padres o cuidadores principales?
• ¿Qué experiencias recuerdas como significativas?
• ¿Cómo crees que esas experiencias marcaron tu forma de ver las relaciones?

Reflexiona sobre tus amistades:
• ¿Cómo fueron tus amistades más importantes durante tu infancia y adolescencia?
• ¿Te sentiste incluido/a, apoyado/a o visto/a?
• ¿Hubo algún patrón que se repitiera en esas relaciones?

Piensa en tus relaciones amorosas:
• ¿Cómo han sido tus relaciones románticas más significativas?
• ¿Qué emociones predominaban? ¿Qué buscabas en esas relaciones?
• ¿Notas que ciertas dinámicas o patrones se repiten en tus vínculos amorosos?

Ejemplo:
"Cuando pienso en mi relación con mis padres, recuerdo que mi madre era muy cariñosa pero también muy exigente. Siempre buscaba su aprobación, y eso me llevó a esforzarme mucho en todo, incluso en agradar a los demás. En la escuela, tenía amistades que me hacían sentir importante, pero siempre temía que me dejaran de lado. Con mis parejas, suelo sentir la necesidad de ser perfecta para evitar que me abandonen, pero a veces me doy cuenta de que eso me hace sentir agotada y no siempre puedo ser yo misma." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu historia relacional completa (padres, amistades, parejas)"
                    }
                ]
            },
            {
                "title": "Paso 1: Eventos significativos",
                "instructions": """Piensa en al menos tres eventos significativos en tus relaciones (con tu familia, amistades o parejas) que creas que dejaron una marca en ti. Para cada evento, responde:
• ¿Qué pasó en ese momento y cómo te sentiste?
• ¿Qué aprendiste sobre ti o sobre las relaciones a partir de esa experiencia?
• ¿Cómo crees que esa vivencia ha influido en tus relaciones actuales?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Evento 1: ¿Qué pasó y cómo te sentiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 1: ¿Qué aprendiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 1: ¿Cómo ha influido en tus relaciones actuales?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 2: ¿Qué pasó y cómo te sentiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 2: ¿Qué aprendiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 2: ¿Cómo ha influido en tus relaciones actuales?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 3: ¿Qué pasó y cómo te sentiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 3: ¿Qué aprendiste?"
                    },
                    {
                        "type": "text",
                        "question": "Evento 3: ¿Cómo ha influido en tus relaciones actuales?"
                    }
                ]
            },
            {
                "title": "Paso 2: Patrones actuales",
                "instructions": """Reflexiona sobre cómo las emociones y formas de relacionarte que desarrollaste en el pasado siguen presentes hoy.
Pregúntate:
• ¿Qué emociones predominan en tus relaciones actuales (seguridad, ansiedad, distancia)?
• ¿Qué haces o evitas hacer en tus relaciones qué crees que está influenciado por tu historia?
• ¿Qué buscas en los demás que tal vez podrías ofrecerte a ti mismo/a?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué emociones predominan en tus relaciones actuales?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué haces o evitas hacer influenciado por tu historia?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué buscas en los demás que podrías ofrecerte a ti mismo/a?"
                    }
                ]
            },
            {
                "title": "Paso 3: Proyectar tus relaciones futuras",
                "instructions": """Imagina cómo te gustaría que fueran tus relaciones en el futuro. Crea una guía para ti mismo/a con los principios y valores que quieres que definan tus vínculos. Piensa en cómo deseas actuar y sentirte en esas relaciones.

Preguntas para proyectar tus relaciones:
• ¿Qué tipo de vínculos quiero construir (amistades, relaciones familiares, amorosas)?
• ¿Qué valores son esenciales para mí en una relación (honestidad, respeto, apoyo mutuo)?
• ¿Qué puedo hacer yo para fomentar esas dinámicas en mis relaciones?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué tipo de vínculos quieres construir en el futuro?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué valores son esenciales para ti en una relación?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué puedes hacer para fomentar esas dinámicas?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_1)
    db.flush()
    print(f"✅ Ejercicio 1.1 creado (ID: {exercise_1_1.id})")
    
    # EJERCICIO 1.2: Mi estilo de apego
    exercise_1_2 = Exercise(
        title="Ejercicio 1.2: Mi estilo de apego",
        parent_title="Ejercicio #1: Bases",
        instructions="""Explora tu estilo de apego y cómo influye en tus relaciones.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Recorrido por tus relaciones",
                "instructions": """Haz un recorrido por tus relaciones significativas (familiares, amistades, parejas). Piensa en cómo te has sentido y comportado en cada una de ellas.

Pregúntate:
• ¿Te resulta fácil confiar en los demás o sueles tener dudas sobre sus intenciones?
• ¿Cómo manejas los conflictos? ¿Prefieres evitarlos, enfrentarlos de inmediato o buscar validación constante?
• ¿Tiendes a buscar mucha cercanía o valoras mantener cierta distancia emocional?
• ¿Te sientes cómodo/a siendo vulnerable o te cuesta abrirte?""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Te resulta fácil confiar en los demás?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo manejas los conflictos?"
                    },
                    {
                        "type": "text",
                        "question": "¿Buscas cercanía o mantienes distancia emocional?"
                    },
                    {
                        "type": "text",
                        "question": "¿Te sientes cómodo/a siendo vulnerable?"
                    }
                ]
            },
            {
                "title": "Paso 2: Comportamientos recurrentes",
                "instructions": """A partir de tus reflexiones, identifica comportamientos o emociones recurrentes que podrían estar relacionados con tu estilo de apego.

Pregúntate:
• ¿Qué emociones predominan en tus relaciones (ansiedad, distancia, seguridad, confusión)?
• ¿Cómo reaccionas cuando sientes que alguien importante se aleja o no está disponible?
• ¿Qué tipo de dinámicas tiendes a repetir con diferentes personas (buscar atención, evitar discusiones, desconfiar)?

Ejemplo práctico:
Me doy cuenta de que, cuando mi pareja está distante, inmediatamente siento ansiedad y pienso que algo está mal conmigo. Esto me lleva a buscar su atención de forma insistente.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué emociones predominan en tus relaciones?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo reaccionas cuando alguien se aleja?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué dinámicas tiendes a repetir?"
                    }
                ]
            },
            {
                "title": "Paso 3: Identifica tu estilo de apego",
                "instructions": """Con base en lo que identificaste, haz una conexión entre tu estilo de apego y cómo influye en tus relaciones. Usa la guía a continuación para identificar tu estilo:

• **Apego seguro**: Te sientes cómodo con la cercanía, confías en los demás y manejas los conflictos de manera equilibrada.
• **Apego ansioso**: Buscas mucha validación y temes ser abandonado/a, lo que puede generar ansiedad en tus vínculos.
• **Apego evitativo**: Prefieres mantener distancia emocional para evitar sentirte vulnerable o depender de alguien.
• **Apego desorganizado**: Te sientes atraído/a por la cercanía, pero también temes ser herido/a, lo que genera comportamientos contradictorios.

Pregúntate:
• ¿Qué estilo de apego sientes que refleja mejor tu manera de relacionarte?
• ¿Qué patrones de este estilo crees que afectan tus relaciones de manera negativa?
• ¿Qué aspectos te gustaría cambiar o fortalecer en tus relaciones?

Ejemplo práctico:
Creo que tengo un apego ansioso porque busco mucha validación y me preocupo constantemente por perder a las personas importantes. Me gustaría aprender a confiar más en mí y en mis vínculos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué estilo de apego refleja mejor tu manera de relacionarte?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué patrones afectan negativamente tus relaciones?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué te gustaría cambiar o fortalecer?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    print(f"✅ Ejercicio 1.2 creado (ID: {exercise_1_2.id})")
    
    # EJERCICIO 1.3: Soy el adulto que necesité
    exercise_1_3 = Exercise(
        title="Ejercicio 1.3: Soy el adulto que necesité",
        parent_title="Ejercicio #1: Bases",
        instructions="""Aprende a darte el apoyo emocional que necesitaste en el pasado.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce necesidades del pasado",
                "instructions": """Siéntate en un lugar tranquilo y cierra los ojos por unos momentos. Respira profundamente y permite que tu mente recuerde las experiencias significativas de tu infancia. Enfócate en lo que necesitabas emocionalmente en esos momentos, pero que quizás no recibiste de la manera que deseabas.

Pregúntate:
• ¿Qué necesitaba escuchar de los adultos a mi alrededor para sentirme amado/a y valorado/a?
• ¿Hubo momentos en los que no me sentí apoyado/a o validado/a? ¿Cómo me habría gustado que respondieran?
• ¿Qué emociones experimentaba con frecuencia (soledad, inseguridad, miedo, alegría) y cómo buscaba manejar esas emociones?

Escribe unas frases sobre lo que sentías y necesitabas en esos momentos. Sé honesto/a contigo mismo/a y evita juzgar tus recuerdos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué necesitabas escuchar para sentirte amado/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Hubo momentos sin apoyo? ¿Cómo te habría gustado que respondieran?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué emociones experimentabas y cómo las manejabas?"
                    }
                ]
            },
            {
                "title": "Paso 2: Patrones en relaciones actuales",
                "instructions": """Ahora, reflexiona sobre cómo esas carencias emocionales del pasado pueden estar presentes en tu vida hoy. Observa las maneras en que buscas satisfacer esas necesidades en tus relaciones actuales, ya sea con pareja, amigos o familiares.

Pregúntate:
• ¿Qué cosas busco en los demás que quizás podría ofrecerme a mí mismo/a?
• ¿Hay momentos en los que me siento emocionalmente dependiente de alguien o evito las relaciones? ¿Por qué?
• ¿Qué puedo hacer para cuidar de mis emociones antes de recurrir a los demás?

Escribe tus respuestas y nota si hay algún patrón o comportamiento que se repita.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué buscas en los demás que podrías ofrecerte a ti mismo/a?"
                    },
                    {
                        "type": "text",
                        "question": "¿Te sientes dependiente o evitas relaciones? ¿Por qué?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué puedes hacer para cuidar tus emociones por ti mismo/a?"
                    }
                ]
            },
            {
                "title": "Paso 3: Sé tu propio sostén",
                "instructions": """Piensa en cómo puedes empezar a atender esas necesidades emocionales desde tu propia capacidad como adulto. Imagina que estás hablando contigo mismo/a como lo harías con un niño que necesita consuelo, apoyo o guía.

Pregúntate:
• ¿Qué palabras puedo decirme hoy para darme seguridad y amor?
• ¿Qué acciones puedo tomar para cuidar de mis emociones y necesidades?
• ¿Cómo puedo recordarme que no necesito ser perfecto/a para ser valioso/a?

Ejemplo práctico:
• Si siento inseguridad, puedo recordarme: "Está bien sentir esto, estoy aprendiendo y creciendo. Soy suficiente tal como soy."
• Si noto que busco aprobación constante, puedo dedicarme un momento para escribir mis logros y recordarme que soy valioso/a por lo que ya soy, no por lo que hago.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué palabras puedes decirte para darte seguridad y amor?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué acciones tomarás para cuidar tus emociones?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te recordarás que eres valioso/a tal como eres?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; seguro ya te sientes más familiarizado con las meditaciones; de igual manera te recuerdo que es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación para SANAR las 5 HERIDAS del ALMA | SANA los DAÑOS de tu CORAZÓN
https://www.youtube.com/watch?v=A84ikOKrBrI

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (Bases) para saber que has completado esta parte y pases a agendar tu quinta sesión 1:1.

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
    """Créer les exercices pour le Thème 2 du Module 3 - BEAUCOUP d'exercices (5!)"""
    print("\n📝 Création des exercices du Thème 2 (5 exercices!)...")
    
    # Je vais créer les 5 exercices du thème 2, mais je vais les diviser en plusieurs parties pour ne pas dépasser la limite de tokens
    
    # EJERCICIO 2.1: Patrones que se repiten
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Patrones que se repiten",
        parent_title="Ejercicio #2: Fundamentos",
        instructions="""El propósito de este ejercicio es invitarte a reflexionar sobre cómo los fundamentos sólidos de conexión con uno mismo y con los demás pueden transformar tu manera de relacionarte.

**Creando conexiones**

En este espacio te invito a reflexionar sobre los pilares fundamentales de una conexión sana, tanto contigo mismo/a como con los demás. Reflexiona sobre cómo, en tus relaciones pasadas, la falta de consciencia o la dificultad para identificar patrones, gestionar el duelo, o negociar tus necesidades, te ha afectado.

¡Este es tu momento para construir relaciones sobre bases sólidas!

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Recuerda relaciones significativas",
                "instructions": """Siéntate en un lugar tranquilo, cierra los ojos y respira profundamente. Permítete recordar las relaciones pasadas que han sido significativas en tu vida. Enfócate en aquellas que se destacan por los mismos problemas o dinámicas que se repiten.

Pregúntate:
• ¿He elegido a personas con características similares? ¿Qué patrones de comportamiento o emociones se repiten?
• ¿Hay una constante sensación de insatisfacción o de no ser valorado en estas relaciones?
• ¿Cómo me comporté en estas relaciones? ¿Actué de manera similar en cada una de ellas? ¿Qué emociones surgieron en cada relación?
• ¿Hubo momentos en los que me sentí rechazado, ignorado o no comprendido? ¿Cómo reaccioné ante esos momentos?

Escribe lo que recuerdas y observa los patrones emocionales o comportamientos que se repiten.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Has elegido personas con características similares? ¿Qué patrones se repiten?"
                    },
                    {
                        "type": "text",
                        "question": "¿Hay insatisfacción o falta de valoración constante?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te comportaste en estas relaciones?"
                    },
                    {
                        "type": "text",
                        "question": "Describe momentos de rechazo o incomprensión y tu reacción"
                    }
                ]
            },
            {
                "title": "Paso 2: Patrones actuales",
                "instructions": """Ahora que tienes claridad sobre los patrones en tus relaciones pasadas, observa cómo estos pueden estar influyendo en tu vida actual.

Pregúntate:
• ¿Sigo eligiendo personas que repiten los mismos comportamientos de mis relaciones pasadas, aunque no me hagan bien?
• ¿Tiendes a recrear conflictos o situaciones similares a las que viviste en el pasado? Si es así, ¿cómo te comportas frente a ellos?
• ¿Cómo te sientes actualmente en tu relación con los demás? ¿Repites ciertos patrones de comportamiento que te han generado dolor o frustración en el pasado?

Escribe tus respuestas y observa si los patrones continúan de alguna manera en tus relaciones actuales.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Sigues eligiendo personas con comportamientos dañinos?"
                    },
                    {
                        "type": "text",
                        "question": "¿Recreas conflictos del pasado? ¿Cómo reaccionas?"
                    },
                    {
                        "type": "text",
                        "question": "¿Repites patrones que te han generado dolor?"
                    }
                ]
            },
            {
                "title": "Paso 3: Romper los patrones",
                "instructions": """Es el momento de pensar en cómo puedes empezar a romper esos patrones. Recuerda que estos patrones se mantienen por la familiaridad y no porque sean buenos para ti. Ahora, actúa desde tu rol de adulto y toma conciencia de cómo puedes transformar esos hábitos en nuevas oportunidades para crear relaciones más saludables.

Pregúntate:
• ¿Qué necesito cambiar en mis elecciones de pareja o en mi forma de relacionarme con los demás para no repetir lo mismo?
• ¿Cómo puedo poner límites saludables que me protejan de caer en relaciones o comportamientos que no me benefician?
• ¿Qué acciones puedo tomar para conocerme mejor y evitar seguir eligiendo lo que no me ayuda a crecer?

Escribe las respuestas con acciones concretas que puedas empezar a tomar hoy para cambiar el rumbo de tus relaciones.

Ejemplo práctico:
Si te das cuenta de que tiendes a elegir parejas que no te valoran, puedes recordarte: "Merezco ser tratado/a con respeto y amor. No voy a conformarme con menos de lo que merezco."
Si en el pasado has permitido que tus relaciones te generen inseguridades, puedes recordarte: "Soy suficiente tal y como soy, y mis necesidades emocionales son válidas." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué necesitas cambiar en tus elecciones o forma de relacionarte?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo puedes poner límites saludables?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué acciones concretas tomarás hoy?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_1)
    db.flush()
    print(f"✅ Ejercicio 2.1 creado (ID: {exercise_2_1.id})")
    
    # Les autres exercices du thème 2 seront créés dans la suite...
    # Pour ne pas dépasser la limite, je vais continuer avec les exercices restants
    
    db.commit()
    return 1  # Pour l'instant, retourne 1, sera mis à jour

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DE TOUS LES EXERCICES DU MODULE 3")
        print("=" * 70)
        
        # IDs des thèmes du Module 3
        THEME_1_ID = 10  # Thème 1: Espejos del alma
        THEME_2_ID = 11  # Thème 2: Construyendo vínculos sanos
        THEME_3_ID = 12  # Thème 3: Del amor propio al amor compartido
        
        # Créer les exercices du thème 1
        num_ex_t1 = create_exercises_theme1(db, THEME_1_ID)
        
        # Créer les exercices du thème 2
        num_ex_t2 = create_exercises_theme2(db, THEME_2_ID)
        
        print("\n" + "=" * 70)
        print("✅ EXERCICES DU MODULE 3 EN COURS DE CRÉATION...")
        print("=" * 70)
        print(f"📚 Thème 1 (Bases): {num_ex_t1} exercices créés")
        print(f"📚 Thème 2 (Fundamentos): {num_ex_t2} exercice créé (suite à venir)")
        print("\n⚠️  Le Module 3 a beaucoup d'exercices (11 en total)")
        print("⚠️  Le script sera complété en plusieurs parties")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

