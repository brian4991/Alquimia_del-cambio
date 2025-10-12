"""
Script pour créer les exercices du Thème 1 du Module 1
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_exercises_theme1(db: Session, theme_id: int):
    """Créer les 3 exercices pour le Thème 1 (Historia Emocional)"""
    print("\n📝 Création des exercices du Thème 1...")
    
    # EJERCICIO 1.1: Explorando mi historia Emocional
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: Explorando mi historia Emocional",
        parent_title="Ejercicio #1: Historia",
        instructions="""El ejercicio principal para este tema se centrará en la exploración profunda de tu historia emocional y cómo tus experiencias pasadas, particularmente en tu familia y en la infancia, han moldeado tus patrones emocionales actuales. Recuerda que este proceso no debe ser abrumador, sino que te brindará claridad sobre la manera en que reaccionas y sientes en el presente. A través de estos ejercicios, comenzarás a observar con mayor consciencia los patrones y raíces emocionales que influyen en tu vida actual.

**Tu Historia**

En este espacio te invito a escribir tu historia personal. ¿De dónde vienes? ¿Dónde naciste? ¿Cómo fue tu infancia? ¿Qué recuerdos te marcaron en tu adolescencia? ¿Cómo es tu vida actual? ¿Qué momentos importantes han dejado huella en tu camino?

Antes de sumergirnos en la identificación de tus emociones, quiero que te conectes profundamente con tu historia. Permítete aventurarte en este maravilloso viaje a través del tiempo, explorando las etapas que han formado la persona que eres hoy. Tómate un momento para recordar, para revivir esos instantes que dejaron una impresión duradera en tu corazón y mente. Aquí es donde comienza la magia: en el reconocimiento de quién has sido y cómo cada experiencia ha contribuido a tu presente.

¡Este es tu momento para redescubrirte y abrazar tu historia con valentía y curiosidad!

Tiempo estimado: 30 minutos de reflexión""",
        order_number=1,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reflexiona sobre tu familia",
                "instructions": "Dedica unos minutos a pensar en tu familia de origen (padres, abuelos, hermanos u otras figuras importantes de tu infancia). Responde las siguientes preguntas, no te limites a la hora de escribir, expresa todo lo que necesitas:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo manejaban las emociones en tu familia? ¿Se expresaban abiertamente, se reprimían, o se evitaban?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué emociones eran \"aceptables\" de mostrar y cuáles no lo eran?"
                    },
                    {
                        "type": "text",
                        "question": "¿Había algún miembro de la familia que evitará o exagerara ciertas emociones (como el enojo, tristeza, miedo o alegría)? ¿Cómo afectaba esto a la dinámica familiar?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica patrones emocionales familiares",
                "instructions": "Ahora, trata de identificar si hubo patrones emocionales repetitivos en tu familia:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Notabas alguna emoción que era común en la familia (por ejemplo, mucha tensión, enfado o silencio)?"
                    },
                    {
                        "type": "text",
                        "question": "¿Recuerdas alguna situación específica en la que los miembros de tu familia reaccionaban de manera predecible (por ejemplo, cuando había conflictos, quién solía calmar la situación, quién evitaba hablar)?"
                    }
                ]
            },
            {
                "title": "Paso 3: Reflexiona sobre tu niñez y adolescencia",
                "instructions": "Pasa a explorar cómo estos patrones familiares influyeron en ti. Responde:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo manejabas las emociones cuando eras niño/a o adolescente? ¿Sentías que tenías permiso para expresar lo que sentías?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué emociones solías experimentar con más frecuencia? ¿Alguna vez las reprimías o no sabías cómo gestionarlas?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te relacionabas emocionalmente con los demás (familiares, amigos, compañeros)?"
                    }
                ]
            },
            {
                "title": "Paso 4: Comparación con el presente",
                "instructions": "Finalmente, compara tus emociones de la infancia/adolescencia con tu vida adulta. Piensa en los patrones emocionales que reconoces en tu vida actual y responde:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Existen similitudes entre cómo tu familia manejaba las emociones y cómo lo haces ahora?"
                    },
                    {
                        "type": "text",
                        "question": "¿Tiendes a repetir algunos de esos patrones familiares o has desarrollado nuevos?"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_1)
    db.flush()
    print(f"✅ Ejercicio 1.1 creado (ID: {exercise_1_1.id})")
    
    # EJERCICIO 1.2: Reconociendo Patrones Emocionales
    exercise_1_2 = Exercise(
        title="Ejercicio 1.2: Reconociendo Patrones Emocionales",
        parent_title="Ejercicio #1: Historia",
        instructions="""Este ejercicio te ayudará a reconocer los patrones emocionales que se repiten en tu vida actual y conectarlos con sus orígenes.

Tiempo estimado: 30 minutos""",
        order_number=2,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Haz un inventario emocional",
                "instructions": "Tómate un momento para reflexionar sobre las emociones que experimentas con más frecuencia en tu vida cotidiana. Escribe una lista de las emociones que sueles sentir en distintas áreas de tu vida (trabajo, relaciones, familia). Preguntas para guiarte:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué emociones suelen aparecer cuando tienes problemas en el trabajo?"
                    },
                    {
                        "type": "text",
                        "question": "¿Qué sientes más a menudo en tus relaciones personales?"
                    },
                    {
                        "type": "text",
                        "question": "¿Existen emociones recurrentes cuando te enfrentas a situaciones desafiantes?"
                    }
                ]
            },
            {
                "title": "Paso 2: Identifica el origen de los patrones",
                "instructions": "Una vez que tengas tu lista de emociones frecuentes, responde:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Recuerdas cuándo empezaste a sentir estas emociones con regularidad?"
                    },
                    {
                        "type": "text",
                        "question": "¿Podrías identificar situaciones o eventos en tu vida que hayan generado estos patrones emocionales?"
                    },
                    {
                        "type": "text",
                        "question": "Piensa si estas emociones tienen raíces en tu infancia o adolescencia. Por ejemplo, ¿solías sentir ansiedad en situaciones familiares tensas, y ahora la misma emoción aparece cuando tienes conflictos en el trabajo?"
                    }
                ]
            },
            {
                "title": "Paso 3: Reconoce las respuestas automáticas",
                "instructions": "Reflexiona sobre las situaciones actuales en las que sueles reaccionar de manera automática o predecible. Anota:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Hay algún comportamiento que repites cuando experimentas una emoción específica (por ejemplo, aislarte cuando te sientes triste o enojarte cuando te critican)?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cuáles son las respuestas emocionales que te gustaría cambiar porque ya no te sirven?"
                    }
                ]
            },
            {
                "title": "Paso 4: Conecta con tus emociones actuales",
                "instructions": "Piensa en una situación reciente que te haya generado una emoción intensa. ¿Cómo reaccionaste en ese momento? ¿Fue una respuesta automática o intencional? Este paso te permitirá observar cómo tus patrones emocionales influyen en tu presente.",
                "questions": [
                    {
                        "type": "text",
                        "question": "Describe una situación reciente que te generó una emoción intensa y cómo reaccionaste"
                    }
                ]
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    print(f"✅ Ejercicio 1.2 creado (ID: {exercise_1_2.id})")
    
    # EJERCICIO 1.3: Raíces Emocionales
    exercise_1_3 = Exercise(
        title="Ejercicio 1.3: Raíces Emocionales",
        parent_title="Ejercicio #1: Historia",
        instructions="""Este ejercicio te ayudará a explorar las raíces profundas de tus emociones actuales.

Tiempo estimado: 30 minutos""",
        order_number=3,
        theme_id=theme_id,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reflexiona sobre eventos clave en tu vida",
                "instructions": "Piensa en eventos importantes de tu infancia o adolescencia que consideres hayan tenido un impacto emocional en ti (por ejemplo, mudanzas, conflictos familiares, momentos de éxito o fracaso). Anota:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Cómo te sentiste en esos momentos?"
                    },
                    {
                        "type": "text",
                        "question": "¿Recuerdas alguna emoción específica que hayas experimentado con frecuencia en esa época?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo reaccionaste emocionalmente ante estos eventos?"
                    }
                ]
            },
            {
                "title": "Paso 2: Explora tus primeras experiencias emocionales",
                "instructions": "El siguiente paso es identificar las primeras veces que experimentaste ciertas emociones intensas (alegría, miedo, tristeza, enojo):",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Qué eventos o relaciones influyeron en esas emociones?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo te afectaron a largo plazo? Por ejemplo, si experimentaste rechazo o abandono en algún momento, ¿cómo influye esto en cómo te relacionas ahora con otras personas?"
                    }
                ]
            },
            {
                "title": "Paso 3: Conecta tus emociones con el presente",
                "instructions": "Finalmente, identifica si alguna de las emociones de estos eventos tempranos aún influye en cómo te sientes o reaccionas ahora:",
                "questions": [
                    {
                        "type": "text",
                        "question": "¿Hay emociones del pasado que sigues experimentando en situaciones similares?"
                    },
                    {
                        "type": "text",
                        "question": "¿Cómo se manifiestan esas emociones en tu vida actual (por ejemplo, ansiedad en relaciones cercanas, miedo al fracaso en tu trabajo)?"
                    }
                ]
            },
            {
                "title": "Meditación complementaria",
                "instructions": """Te invito a realizar esta meditación que complementa tu trabajo interno; no te preocupes si es la primera vez; no te preocupes si no es sencillo al principio; es una práctica que se mejora con el tiempo, como todo proceso, intenta escuchar con calma y seguir los pasos que Monica te indica, si tienes alguna duda escríbeme para guiarte (para una mejor experiencia utiliza audífonos; hazlo en un momento donde no te interrumpan, puedas estar en calma y finalmente trata de escribir en un diario todo lo que sentiste y aprendiste)

Meditación SANAR tus EMOCIONES | VIBRAR ALTO desde el AMOR
https://www.youtube.com/watch?v=oO_wnpgGDdg

☝Instrucción: Una vez que hayas completado el ejercicio envíame un mensaje de texto con la palabra (HISTORIA) para saber que has completado esta parte y pases a agendar tu primera sesión 1:1.

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

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("🚀 CRÉATION DES EXERCICES THÈME 1 - MODULE 1")
        print("=" * 70)
        
        # ID du thème 1
        THEME_1_ID = 1  # Thème 1: Explorando mi historia emocional
        
        # Créer les exercices du thème 1
        num_ex = create_exercises_theme1(db, THEME_1_ID)
        
        print("\n" + "=" * 70)
        print("✅ TOUS LES EXERCICES DU THÈME 1 CRÉÉS!")
        print("=" * 70)
        print(f"📚 Thème 1 (Historia Emocional): {num_ex} exercices créés")
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

