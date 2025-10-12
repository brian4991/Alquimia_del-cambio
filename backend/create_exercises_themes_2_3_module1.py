"""
Script pour créer les exercices des Thèmes 2 et 3 du Module 1
Avec tableaux correctement structurés
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_exercises_theme2(db: Session, theme_id: int):
    """Créer les exercices pour le Thème 2 (Emociones)"""
    print("\n📝 Création des exercices du Thème 2...")
    
    # EJERCICIO 2.1: Identificar emociones
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Identificar emociones",
        parent_title="Ejercicio #2: Emociones",
        instructions="""Con este ejercicio, identificarás las emociones básicas y secundarias que experimentas durante el día, explorando cómo se relacionan entre sí. Esto te permitirá conocerte mejor y entender el origen de tus reacciones emocionales.

Tiempo estimado: 30 minutos""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identificar tus emociones",
                "instructions": """Elige un día reciente o un momento particular en el que hayas experimentado varias emociones intensas. Puede ser una situación de trabajo, una conversación importante, o incluso un evento cotidiano que te haya generado alguna emoción destacada.

Escribe en las columnas, repite el proceso con todas las emociones necesarias:
• Columna 1: "Emoción Básica". Aquí anota la emoción primaria que sentiste en ese momento (miedo, tristeza, alegría, enojo, sorpresa o asco).
• Columna 2: "Emoción Secundaria". Aquí escribe si detrás de esa emoción básica sentiste una emoción secundaria más compleja (como frustración, culpa, ansiedad, alivio, etc.).

(Apóyate del recurso "emocionario" para realizar con mayor detalle el ejercicio)""",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la siguiente tabla con tus emociones:",
                        "table_config": {
                            "columns": [
                                {"title": "Emoción Básica", "type": "text"},
                                {"title": "Emoción Secundaria", "type": "text"}
                            ],
                            "rows": 10
                        }
                    }
                ]
            },
            {
                "title": "Paso 2: Reflexión sobre la relación",
                "instructions": "Pregúntate: \"¿Cómo esta emoción básica me llevó a la secundaria?\" Reflexiona sobre la relación entre las dos emociones y anótalo. Por ejemplo, si primero sentiste miedo y luego ansiedad, explora por qué el miedo se transformó en esa ansiedad.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo tus emociones básicas te llevaron a las emociones secundarias?"
                    }
                ]
            },
            {
                "title": "Paso 3: Conclusión",
                "instructions": "Concluye el ejercicio haciendo una breve reflexión sobre lo que descubriste.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué emociones secundarias experimentas más seguido?"
                    },
                    {
                        "type": "text",
                        "question": "¿Te resultó fácil o difícil identificar la emoción secundaria después de la básica?"
                    }
                ]
            },
            {
                "title": "Reflexión Final",
                "instructions": "Al finalizar, escribe una conclusión de cómo te relacionas con tus emociones y cómo influyen en tus reacciones diarias.",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu reflexión final sobre cómo te relacionas con tus emociones"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_1)
    db.flush()
    print(f"✅ Ejercicio 2.1 creado (ID: {exercise_2_1.id})")
    
    # EJERCICIO 2.2: Reconocer necesidades emocionales
    exercise_2_2 = Exercise(
        title="Ejercicio 2.2: Reconocer necesidades emocionales",
        parent_title="Ejercicio #2: Emociones",
        instructions="""Identifica las necesidades detrás de tus emociones más significativas.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Selecciona tus emociones",
                "instructions": "Revisa la lista de emociones que realizaste en el Ejercicio 1. Elige tres emociones (básicas o secundarias) que fueron las más significativas o que se repitieron con más frecuencia.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cuáles son las tres emociones más significativas que identificaste?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica las necesidades",
                "instructions": """Para cada emoción, pregúntate: ¿Qué necesidad estaba tratando de expresarme esta emoción?

A continuación, una guía de ejemplos comunes:
• Miedo: Necesidad de seguridad, protección.
• Tristeza: Necesidad de consuelo, conexión o apoyo.
• Alegría: Necesidad de reconocimiento, gratitud o celebración.
• Enojo: Necesidad de respeto, límites o justicia.

(Apóyate del recurso "¿qué NECESITO realmente cuando me siento así?" para realizar con mayor detalle el ejercicio)""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Emoción 1: ¿Qué necesidad estaba tratando de expresarte esta emoción?"
                    },
                    {
                        "type": "text",
                        "question": "Emoción 2: ¿Qué necesidad estaba tratando de expresarte esta emoción?"
                    },
                    {
                        "type": "text",
                        "question": "Emoción 3: ¿Qué necesidad estaba tratando de expresarte esta emoción?"
                    }
                ]
            },
            {
                "title": "Paso 3: Anota con detalle",
                "instructions": "Anota tus respuestas en tu diario. Sé lo más específico posible con cada emoción y su necesidad asociada. Por ejemplo, si sentiste enojo en el trabajo, podrías descubrir que la necesidad detrás de esa emoción era sentirte valorado o escuchado.",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe con detalle la relación entre cada emoción y su necesidad asociada"
                    }
                ]
            },
            {
                "title": "Paso 4: Plan de acción",
                "instructions": "Reflexiona sobre cómo puedes satisfacer esas necesidades de manera más efectiva en el futuro. Pregúntate: ¿Qué puedo hacer de manera concreta para atender esta necesidad? Anota tus ideas y posibles acciones.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué acciones concretas puedes tomar para satisfacer estas necesidades?"
                    }
                ]
            },
            {
                "title": "Reflexión Final",
                "instructions": "Al terminar, escribe un breve resumen de lo que has aprendido sobre tus emociones y necesidades. ¿Te sientes más consciente de lo que realmente necesitas? ¿Cómo podrías aplicar este conocimiento en tu vida diaria?",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu reflexión final sobre lo que has aprendido"
                    }
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    print(f"✅ Ejercicio 2.2 creado (ID: {exercise_2_2.id})")
    
    # EJERCICIO 2.3: Creando un Plan para satisfacer mis necesidades
    exercise_2_3 = Exercise(
        title="Ejercicio 2.3: Creando un Plan para satisfacer mis necesidades",
        parent_title="Ejercicio #2: Emociones",
        instructions="""Crea un plan concreto para satisfacer tus necesidades emocionales.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Lista de necesidades",
                "instructions": "Revisa las necesidades que identificaste en el Ejercicio 2. Haz una lista de las necesidades más importantes que reconociste (por ejemplo, seguridad, conexión, respeto, etc.).",
                "questions": [
                    {
                        "type": "text",
                        "question": "Lista tus necesidades más importantes"
                    }
                ]
            },
            {
                "title": "Paso 2: Acciones concretas",
                "instructions": """Para cada necesidad, escribe una acción concreta que puedas realizar para satisfacerla. Por ejemplo:
• Si tu necesidad es seguridad, podrías establecer límites más claros en tus relaciones personales o laborales.
• Si tu necesidad es conexión, podrías reservar tiempo en tu agenda para compartir más momentos con amigos o seres queridos.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Para cada necesidad, ¿qué acción concreta puedes realizar?"
                    }
                ]
            },
            {
                "title": "Paso 3: Plan de Necesidades",
                "instructions": """Organiza tu "Plan de Necesidades" en forma de un plan. Escribe un plan de acción diario o semanal, donde incluyas al menos una acción pequeña y concreta que puedas hacer para atender tus necesidades emocionales.

(Imprime este plan y mantenlo contigo en el escritorio o un lugar visible donde puedas ponerlo en práctica)
(Apóyate del recurso "¿qué NECESITO realmente cuando me siento así?" para realizar con mayor detalle el ejercicio, el documento: "Plan de Necesidades" lo encuentras en tu folder)""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu plan de acción diario/semanal para atender tus necesidades"
                    }
                ]
            },
            {
                "title": "Reflexión Final",
                "instructions": "Escribe cómo te sientes al tener este plan y qué impacto crees que puede tener en tu vida. Este es un plan flexible, así que ajústalo conforme avanzas en tu proceso de autoconocimiento.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sientes al tener este plan y qué impacto crees que tendrá en tu vida?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; no te preocupes si no es sencillo al principio; es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación BIODESCODIFICACIÓN EMOCIONAL | SANACIÓN de HERIDAS PENDIENTES
https://www.youtube.com/watch?v=vq1fjlF9hKE

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (EMOCIONES) para saber que has completado esta parte, pueda revisarte, darte retroalimentación y puedas avanzar al ejercicio número 3""",
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
    """Créer les exercices pour le Thème 3 (Gestión Emocional)"""
    print("\n📝 Création des exercices du Thème 3...")
    
    # EJERCICIO 3.1: Técnicas de Regulación Emocional
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: Técnicas de Regulación Emocional",
        parent_title="Ejercicio #3: Gestión Emocional",
        instructions="""Con este ejercicio, aprenderás a identificar y gestionar las emociones que surgen en situaciones cotidianas, explorando cómo impactan tus pensamientos y acciones.

Realiza este ejercicio como mínimo con las 5 emociones básicas o tus emociones más recurrentes.

(Nota: utiliza el recurso: Técnicas de gestión emocional para el día a día para tener más apoyo)

Tiempo estimado: 30 minutos de reflexión""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "1. Reconoce la emoción",
                "instructions": """Antes de gestionar una emoción, necesitas identificarla claramente. Tómate unos minutos para centrarte y preguntarte: ¿Qué estoy sintiendo exactamente? ¿Es enojo, ansiedad, tristeza, frustración? Anótalo.

Ejemplo:
• Situación: Tengo una reunión importante y me siento ansioso. (usa la situación que desees)
• Emoción: Ansiedad""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe la situación"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué emoción identificaste?"
                    }
                ]
            },
            {
                "title": "2. Selecciona una técnica de regulación",
                "instructions": """Elige una según la emoción que identifiques y lo que más te funcione personalmente, si ya utilizas algunas herramientas que te han venido funcionando úsalas, pero también atrévete a experimentar otras:

• Respiración profunda y consciente: Inhala por la nariz durante 4 segundos, sostén la respiración durante 4 segundos y exhala lentamente por la boca durante otros 4. Hazlo 5 veces. Esta técnica te ayudará a reducir la activación fisiológica causada por la emoción.

• Reestructuración cognitiva (cambio de pensamiento): Identifica pensamientos automáticos que acompañan la emoción y cámbialos por pensamientos más realistas o constructivos. Pregúntate: "¿Estoy exagerando esta situación? ¿Cómo puedo ver esto desde una perspectiva más equilibrada?"

• Mindfulness: Centra tu atención en el momento presente, sin juzgar la emoción que sientes. Observa cómo se manifiesta en tu cuerpo, qué pensamientos surgen y permite que fluya sin reaccionar de inmediato.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué técnica elegiste?"
                    }
                ]
            },
            {
                "title": "3. Aplica la técnica",
                "instructions": """Después de haber elegido una técnica, ponla en práctica. Si elegiste respiración profunda, siéntate en un lugar cómodo, cierra los ojos y concéntrate en tu respiración. Si elegiste reestructuración cognitiva, analiza tus pensamientos irracionales y replantea el escenario.

Ejemplo:
• "En lugar de pensar 'Voy a fracasar en la reunión', lo cambio por 'He preparado bien la reunión y estoy listo para dar lo mejor de mí'." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe cómo aplicaste la técnica"
                    }
                ]
            },
            {
                "title": "4. Reflexiona",
                "instructions": "Después de practicar la técnica, escribe una reflexión breve sobre cómo te sientes y cómo ha cambiado tu estado emocional.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sientes después de aplicar la técnica? ¿Cómo cambió tu estado emocional?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    print(f"✅ Ejercicio 3.1 creado (ID: {exercise_3_1.id})")
    
    # EJERCICIO 3.2: Comunicación asertiva de las necesidades
    exercise_3_2 = Exercise(
        title="Ejercicio 3.2: Comunicación asertiva de las necesidades",
        parent_title="Ejercicio #3: Gestión Emocional",
        instructions="""Aprende a comunicar tus necesidades de manera clara y asertiva.

Tiempo estimado: 30 minutos de reflexión""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "1. Identifica tu necesidad",
                "instructions": """Piensa en una situación reciente en la que no comunicaste tus emociones o necesidades de manera clara. Reflexiona sobre cuál fue tu necesidad no satisfecha. Anótala.

Ejemplo:
• Situación: Me sentí frustrado cuando mi jefe no reconoció mi trabajo.
• Necesidad: Necesito reconocimiento por mi esfuerzo y contribución.""",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe la situación"
                    },
                    {
                        "type": "text",
                        "question": "¿Cuál fue tu necesidad no satisfecha?"
                    }
                ]
            },
            {
                "title": "2. Prepara tu comunicación asertiva",
                "instructions": """Utiliza el siguiente esquema para preparar una comunicación clara y asertiva:
"Yo siento (emoción) cuando (descripción objetiva de la situación) porque (razón personal). Me gustaría (una solicitud específica)."

Ejemplo:
"Yo siento frustración cuando mi esfuerzo no es reconocido porque valoro mucho recibir feedback sobre mi desempeño. Me gustaría que en el futuro pudiéramos agendar una reunión para revisar mi progreso y recibir tus comentarios." """,
                "questions": [
                    {
                        "type": "text",
                        "question": "Escribe tu comunicación asertiva usando el esquema"
                    }
                ]
            },
            {
                "title": "3. Simula tu comunicación",
                "instructions": "Antes de comunicarte con la persona implicada, practica en voz alta lo que vas a decir. Esto te permitirá sentirte más seguro/a y reducir la posibilidad de reaccionar emocionalmente de manera impulsiva.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Practicaste tu comunicación? ¿Cómo te sentiste al practicarla?"
                    }
                ]
            },
            {
                "title": "4. Pasa a la acción",
                "instructions": "Aplica esta técnica en la vida real, ya sea en una conversación personal o profesional. Recuerda mantener un tono calmado y escuchar la respuesta de la otra persona.",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe cómo fue la conversación real"
                    }
                ]
            },
            {
                "title": "5. Evaluación Final",
                "instructions": "Después de la conversación, reflexiona sobre los resultados. ¿Te sentiste entendido? ¿Cómo se desarrolló la comunicación? Escribe tus impresiones y ajusta tu enfoque para la próxima vez.",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Te sentiste entendido/a? ¿Qué ajustarías para la próxima vez?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_3_2)
    db.flush()
    print(f"✅ Ejercicio 3.2 creado (ID: {exercise_3_2.id})")
    
    # EJERCICIO 3.3: Construcción de mi caja de herramientas emocionales (LE PLUS LONG AVEC PLUSIEURS TABLEAUX!)
    exercise_3_3 = Exercise(
        title="Ejercicio 3.3: Construcción de mi caja de herramientas emocionales",
        parent_title="Ejercicio #3: Gestión Emocional",
        instructions="""Crea tu caja de herramientas personal para gestionar tus emociones de manera efectiva.

Tiempo estimado: 30 minutos de reflexión""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "1. Identifica tus recursos internos",
                "instructions": "Haz una lista de tus recursos internos (habilidades, fortalezas personales) que te ayudan a gestionar tus emociones. (Nota: agrega espacios en la tabla si es necesario)",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla de recursos internos:",
                        "table_config": {
                            "columns": [
                                {"title": "Recurso interno", "type": "text"},
                                {"title": "¿Lo reconozco en mí? (✔️ / ❌)", "type": "text"},
                                {"title": "¿Cómo me ayuda cuando me siento mal?", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "1b. Identifica tus recursos externos",
                "instructions": "Haz una lista de tus recursos externos (apoyo de amigos, técnicas que te funcionan) que te ayudan a gestionar tus emociones.",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla de recursos externos:",
                        "table_config": {
                            "columns": [
                                {"title": "Recurso Externo", "type": "text"},
                                {"title": "¿Lo tengo disponible? (✔️ / ❌)", "type": "text"},
                                {"title": "¿Cómo me ayuda en momentos de dificultad?", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "2. Crea tu caja de herramientas",
                "instructions": "Basándote en lo que has aprendido hasta ahora, selecciona tres técnicas o estrategias que más te hayan ayudado a gestionar tus emociones. Estos serán los primeros elementos de tu \"Caja de Herramientas Emocionales\".",
                "questions": [
                    {
                        "type": "table",
                        "question": "Completa la tabla con tus técnicas principales:",
                        "table_config": {
                            "columns": [
                                {"title": "Técnica", "type": "text"},
                                {"title": "¿Cuándo la uso?", "type": "text"},
                                {"title": "¿Cómo me hace sentir?", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "3. Organiza tu caja de herramientas",
                "instructions": "Divide tu caja en secciones. Una sección puede estar dedicada a técnicas para calmarte cuando estás en situaciones de alta tensión, otra sección puede ser para mejorar tu autoconfianza, y otra para expresar emociones.",
                "questions": [
                    {
                        "type": "table",
                        "question": "Organiza tus herramientas por categoría:",
                        "table_config": {
                            "columns": [
                                {"title": "Para calmarme", "type": "text"},
                                {"title": "Para aumentar mi confianza", "type": "text"},
                                {"title": "Para expresar mis emociones", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "4. Revisión regular",
                "instructions": "Una vez que tengas tu \"Caja de Herramientas Emocionales\" preparada, comprométete a revisarla y ajustarla de manera periódica. ¿Qué herramientas te han funcionado más? ¿Hay alguna técnica nueva que te gustaría probar? Anota tus ideas y sigue adaptando tu caja a tus necesidades.",
                "questions": [
                    {
                        "type": "table",
                        "question": "Evalúa y ajusta tus herramientas:",
                        "table_config": {
                            "columns": [
                                {"title": "Lo que me ha funcionado", "type": "text"},
                                {"title": "Lo que quiero probar", "type": "text"},
                                {"title": "Lo que quiero ajustar o dejar", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "5. Aplicación Diaria",
                "instructions": "Elige una herramienta de tu caja y ponla en práctica en tu vida diaria durante una semana. Toma nota de cómo te ayudó en situaciones concretas y cómo puedes seguir utilizándola para mejorar tu gestión emocional.",
                "questions": [
                    {
                        "type": "table",
                        "question": "Registro de aplicación semanal:",
                        "table_config": {
                            "columns": [
                                {"title": "Herramienta elegida", "type": "text"},
                                {"title": "Situaciones donde la usé", "type": "text"},
                                {"title": "¿Cómo me ayudó?", "type": "text"},
                                {"title": "¿La seguiré usando? (Sí/No)", "type": "text"}
                            ],
                            "rows": 8
                        }
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; no te preocupes si no es sencillo al principio; es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación LIBERAR tus EMOCIONES | ELEVA la VIBRACIÓN para ser FELIZ
https://www.youtube.com/watch?v=E8i7zopGw0c

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (GESTIÓN) para saber que has completado esta parte y pases a agendar tu segunda sesión 1:1, y obtener acceso a la siguiente estación (módulo #2)""",
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
        print("🚀 CRÉATION DES EXERCICES THÈMES 2 ET 3 - MODULE 1")
        print("=" * 70)
        
        # IDs des thèmes
        THEME_2_ID = 2  # Thème 2: Reconociendo tus emociones
        THEME_3_ID = 3  # Thème 3: Gestionando tus emociones de forma consciente
        
        # Créer les exercices du thème 2
        num_ex_t2 = create_exercises_theme2(db, THEME_2_ID)
        
        # Créer les exercices du thème 3
        num_ex_t3 = create_exercises_theme3(db, THEME_3_ID)
        
        print("\n" + "=" * 70)
        print("✅ TOUS LES EXERCICES CRÉÉS!")
        print("=" * 70)
        print(f"📚 Thème 2 (Emociones): {num_ex_t2} exercices créés")
        print(f"📚 Thème 3 (Gestión Emocional): {num_ex_t3} exercices créés")
        print(f"\n✨ Total: {num_ex_t2 + num_ex_t3} exercices créés avec tableaux!")
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

