"""
Script pour créer tous les exercices du Module 5: Libertad en Acción
3 exercices avec 7 sous-exercices au total (version simplifiée)
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_all_exercises_module5(db: Session):
    """Créer tous les exercices du Module 5"""
    
    print("\n" + "=" * 70)
    print("🚀 CRÉATION DE TOUS LES EXERCICES DU MODULE 5")
    print("=" * 70)
    
    # IDs des thèmes du Module 5
    THEME_1_ID = 22  # Claridad y sentido
    THEME_2_ID = 23  # Esto ya no me pertenece
    THEME_3_ID = 24  # Energía en movimiento
    
    exercises_created = []
    
    # EJERCICIO 1.1
    print("\n📝 Création de l'Ejercicio 1.1...")
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: Construcción de metas claras",
        parent_title="Ejercicio #1: Objetivos",
        instructions="Este ejercicio te ayudará a tener una visión clara y honesta de lo que realmente quieres para tu vida.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Mapa de tu presente",
                "instructions": "A continuación rellena las tres columnas: Lo que quiero conservar, Lo que quiero soltar, Lo que quiero crear. Dedica 5 minutos a cada columna.",
                "questions": [
                    {"type": "table", "question": "Completa tu mapa del presente:", "table_config": {"columns": [{"title": "Lo que quiero conservar", "type": "text"}, {"title": "Lo que quiero soltar", "type": "text"}, {"title": "Lo que quiero crear", "type": "text"}], "rows": 15}}
                ]
            },
            {
                "title": "Paso 2: Proyección al futuro",
                "instructions": "Cierra los ojos e imagina que han pasado 12 meses. Visualiza donde estas, que haces, quienes te rodean, como te sientes.",
                "questions": [
                    {"type": "text", "question": "Escribe todo lo que visualizaste sobre tu futuro ideal"}
                ]
            },
            {
                "title": "Paso 3: El filtro de la verdad",
                "instructions": "Revisa lo que escribiste y preguntate: ¿Esto lo deseo porque me representa o porque alguien mas espera que lo haga?",
                "questions": [
                    {"type": "text", "question": "¿Que deseos son genuinamente tuyos?"}
                ]
            },
            {
                "title": "Paso 4: El siguiente paso no negociable",
                "instructions": "De tu lista de deseos genuinos, elige solo uno que sea prioritario ahora. Define una acción específica para los próximos 7 días.",
                "questions": [
                    {"type": "text", "question": "¿Cual es tu deseo prioritario y tu acción para los próximos 7 días?"}
                ]
            },
            {
                "title": "Paso 5: Declaración de claridad",
                "instructions": "Escribe una frase en presente que resuma tu nuevo rumbo: 'A partir de hoy, me comprometo a construir una vida donde ______, tomando decisiones alineadas con ______.'",
                "questions": [
                    {"type": "text", "question": "Escribe tu declaración de claridad"}
                ]
            }
        ])
    )
    db.add(exercise_1_1)
    db.flush()
    print(f"  ✅ Ejercicio 1.1 créé (ID: {exercise_1_1.id})")
    
    # EJERCICIO 1.2
    print("\n📝 Création de l'Ejercicio 1.2...")
    exercise_1_2 = Exercise(
        title="Ejercicio 1.2: Objetivos alcanzables",
        parent_title="Ejercicio #1: Objetivos",
        instructions="Define un objetivo que puedas alcanzar desde tu realidad actual.<br><br>Tiempo estimado: 30 minutos",
        order_number=2,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Define tu dirección",
                "instructions": "Piensa en el area de tu vida que mas necesita avanzar ahora.",
                "questions": [
                    {"type": "text", "question": "Quiero avanzar en el area de ______"}
                ]
            },
            {
                "title": "Paso 2: Elige un objetivo prioritario",
                "instructions": "De todo lo que podrías hacer, elige una sola meta que realmente te impulse.",
                "questions": [
                    {"type": "text", "question": "Mi objetivo prioritario es"}
                ]
            },
            {
                "title": "Paso 3: Valida que sea alcanzable",
                "instructions": "¿Es realista? ¿Depende de mi? ¿Puedo medir mi avance?",
                "questions": [
                    {"type": "text", "question": "Valida tu objetivo respondiendo las 3 preguntas"}
                ]
            },
            {
                "title": "Paso 4: Tradúcelo en microacciones",
                "instructions": "Divide tu objetivo en acciones pequeñas.",
                "questions": [
                    {"type": "text", "question": "Lista tus microacciones (al menos 3)"}
                ]
            },
            {
                "title": "Paso 5: Ponle fecha",
                "instructions": "Decide cuando vas a hacer cada microacción. Meditaciones: IDENTIFICA tu PROPÓSITO - https://www.youtube.com/watch?v=J3mmwcpZ0EQ o PIDE al UNIVERSO tu REALIDAD DESEADA - https://www.youtube.com/watch?v=PoS_qOHiHVs<br><br>☝ Envíame un mensaje con la palabra (OBJETIVOS) para continuar.",
                "questions": [
                    {"type": "text", "question": "Escribe tu compromiso completo con fechas"}
                ]
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    print(f"  ✅ Ejercicio 1.2 créé (ID: {exercise_1_2.id})")
    
    # EJERCICIO 2.1
    print("\n📝 Création de l'Ejercicio 2.1...")
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Identificando mis creencias limitantes",
        parent_title="Ejercicio #2: Creencias",
        instructions="Descubre las raíces de tus frenos internos.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Define el objetivo",
                "instructions": "Escribe con claridad una meta o sueño específico que quieres lograr.",
                "questions": [
                    {"type": "text", "question": "Mi meta o sueño específico es"}
                ]
            },
            {
                "title": "Paso 2: Detecta pensamientos automáticos",
                "instructions": "Imagina que ya estas a punto de dar el primer paso. ¿Que frases, dudas o juicios aparecen?",
                "questions": [
                    {"type": "table", "question": "Completa la tabla:", "table_config": {"columns": [{"title": "Frases", "type": "text"}, {"title": "Dudas", "type": "text"}, {"title": "Juicios automáticos", "type": "text"}], "rows": 8}}
                ]
            },
            {
                "title": "Paso 3: Identifica la creencia central",
                "instructions": "Detrás de cada pensamiento hay una creencia mas profunda.",
                "questions": [
                    {"type": "table", "question": "Relaciona pensamiento con creencia central:", "table_config": {"columns": [{"title": "Pensamiento", "type": "text"}, {"title": "Creencia Central", "type": "text"}], "rows": 6}}
                ]
            },
            {
                "title": "Paso 4: Localiza emoción e impacto",
                "instructions": "Para cada creencia: emoción principal y efecto en tu acción.",
                "questions": [
                    {"type": "text", "question": "Describe la emoción y el efecto de cada creencia"}
                ]
            },
            {
                "title": "Paso 5: Cuestiona y reformula",
                "instructions": "¿Que evidencias tengo? ¿Ejemplos de lo contrario? ¿Nueva creencia mas útil?",
                "questions": [
                    {"type": "table", "question": "Transforma tus creencias:", "table_config": {"columns": [{"title": "Creencia limitante", "type": "text"}, {"title": "Nueva creencia", "type": "text"}], "rows": 10}}
                ]
            },
            {
                "title": "Paso 6: Conecta con la acción",
                "instructions": "Elige una acción concreta para esta semana alineada con tu nueva creencia.",
                "questions": [
                    {"type": "table", "question": "Acción por creencia:", "table_config": {"columns": [{"title": "Nueva creencia", "type": "text"}, {"title": "Acción", "type": "text"}], "rows": 6}}
                ]
            }
        ])
    )
    db.add(exercise_2_1)
    db.flush()
    print(f"  ✅ Ejercicio 2.1 créé (ID: {exercise_2_1.id})")
    
    # EJERCICIO 2.2
    print("\n📝 Création de l'Ejercicio 2.2...")
    exercise_2_2 = Exercise(
        title="Ejercicio 2.2: Mi nuevo mindset",
        parent_title="Ejercicio #2: Creencias",
        instructions="Define y ancla una nueva forma de pensar y actuar.<br><br>Tiempo estimado: 30 minutos",
        order_number=2,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Elige la creencia que mas te frenaba",
                "instructions": "Revisa el trabajo previo y selecciona la creencia con mas impacto.",
                "questions": [
                    {"type": "text", "question": "La creencia que mas me frenaba es"}
                ]
            },
            {
                "title": "Paso 2: Reformula con base realista",
                "instructions": "Transforma esa creencia en una afirmación motivadora y creíble. Usa: 'Aunque antes pensaba que ______, ahora elijo creer que ______, porque ______.'",
                "questions": [
                    {"type": "text", "question": "Escribe tu nueva afirmación"}
                ]
            },
            {
                "title": "Paso 3: Crea tu puente de pensamientos",
                "instructions": "Escribe 3-5 pensamientos intermedios que te ayuden a transitar.",
                "questions": [
                    {"type": "text", "question": "Lista tus pensamientos puente"}
                ]
            },
            {
                "title": "Paso 4: Ancla en acción",
                "instructions": "Acción específica coherente con tu nueva creencia para los próximos 3 días.",
                "questions": [
                    {"type": "table", "question": "Relaciona creencia con acción:", "table_config": {"columns": [{"title": "Nueva creencia", "type": "text"}, {"title": "Acción", "type": "text"}], "rows": 6}}
                ]
            },
            {
                "title": "Paso 5: Refuerzo diario",
                "instructions": "Durante 21 días, repite tu nueva creencia cada mañana. Usa Canva para crear tu imagen: https://www.canva.com/design/DAGu3fIXXXYQ<br><br>Meditación: CONOCER tus CREENCIAS PROFUNDAS - https://www.youtube.com/watch?v=JksRKP0aYxg<br><br>☝ Envíame un mensaje con la palabra (CREENCIAS) para continuar.",
                "questions": [
                    {"type": "text", "question": "Escribe tu compromiso de 21 días"}
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    print(f"  ✅ Ejercicio 2.2 créé (ID: {exercise_2_2.id})")
    
    # EJERCICIO 3.1
    print("\n📝 Création de l'Ejercicio 3.1...")
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: Plan de acción",
        parent_title="Ejercicio #3: Momento de accionar",
        instructions="Crea un plan de acción real y sostenible.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_3_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Define tu meta principal",
                "instructions": "Escribe tu objetivo final para los próximos 3 a 6 meses. Debe ser claro, específico y motivador.",
                "questions": [
                    {"type": "text", "question": "Mi objetivo final es"}
                ]
            },
            {
                "title": "Paso 2: Conecta con el para que",
                "instructions": "¿Por que es importante para ti? ¿Que cambiará? ¿Como te sentirás?",
                "questions": [
                    {"type": "text", "question": "Mi 'para que' es"}
                ]
            },
            {
                "title": "Paso 3: Divide en etapas",
                "instructions": "Descompón tu objetivo en 3 a 5 hitos intermedios.",
                "questions": [
                    {"type": "text", "question": "Lista tus hitos intermedios"}
                ]
            },
            {
                "title": "Paso 4: Crea acciones concretas",
                "instructions": "Para cada hito, escribe de 2 a 4 acciones específicas.",
                "questions": [
                    {"type": "table", "question": "Acciones por hito:", "table_config": {"columns": [{"title": "Hito", "type": "text"}, {"title": "Acción", "type": "text"}], "rows": 15}}
                ]
            },
            {
                "title": "Paso 5: Asigna fechas",
                "instructions": "Pon una fecha limite a cada acción. Revisa el recurso: Objetivos SMART.",
                "questions": [
                    {"type": "table", "question": "Completa tu plan SMART:", "table_config": {"columns": [{"title": "S", "type": "text"}, {"title": "M", "type": "text"}, {"title": "A", "type": "text"}, {"title": "R", "type": "text"}, {"title": "T", "type": "text"}], "rows": 5}}
                ]
            },
            {
                "title": "Paso 6: Evalúa y ajusta",
                "instructions": "Reserva un momento semanal para revisar tu plan.",
                "questions": [
                    {"type": "text", "question": "¿Cuando revisaras tu plan semanalmente?"}
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    print(f"  ✅ Ejercicio 3.1 créé (ID: {exercise_3_1.id})")
    
    # EJERCICIO 3.2
    print("\n📝 Création de l'Ejercicio 3.2...")
    exercise_3_2 = Exercise(
        title="Ejercicio 3.2: Diseño de productividad",
        parent_title="Ejercicio #3: Momento de accionar",
        instructions="Diseña una estructura semanal que maximice tu tiempo y energía.<br><br>Tiempo estimado: 30 minutos",
        order_number=2,
        theme_id=THEME_3_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Define tiempo disponible",
                "instructions": "Cuantas horas reales puedes dedicar a tus objetivos cada semana?",
                "questions": [
                    {"type": "text", "question": "Horas totales disponibles esta semana"}
                ]
            },
            {
                "title": "Paso 2: Identifica 3 prioridades clave",
                "instructions": "Las tres acciones o areas con mas impacto en tus objetivos.",
                "questions": [
                    {"type": "text", "question": "Mis 3 prioridades clave son"}
                ]
            },
            {
                "title": "Paso 3: Crea bloques de trabajo profundo",
                "instructions": "Al menos 1 o 2 bloques de 60-90 minutos al día sin interrupciones.",
                "questions": [
                    {"type": "text", "question": "Mis bloques de trabajo profundo son"}
                ]
            },
            {
                "title": "Paso 4: Integra pausas estratégicas",
                "instructions": "Microdescansos de 5-10 minutos y un bloque de descanso activo diario.",
                "questions": [
                    {"type": "text", "question": "Mis pausas y descansos son"}
                ]
            },
            {
                "title": "Paso 5: Diseña tu semana",
                "instructions": "Bloquea tus tiempos: prioridades, trabajo profundo, pausas, flexibilidad.",
                "questions": [
                    {"type": "text", "question": "Describe tu semana organizada (Lunes a Domingo)"}
                ]
            }
        ])
    )
    db.add(exercise_3_2)
    db.flush()
    print(f"  ✅ Ejercicio 3.2 créé (ID: {exercise_3_2.id})")
    
    # EJERCICIO 3.3
    print("\n📝 Création de l'Ejercicio 3.3...")
    exercise_3_3 = Exercise(
        title="Ejercicio 3.3: El maestro del equilibrio",
        parent_title="Ejercicio #3: Momento de accionar",
        instructions="Evalúa y diseña tu equilibrio de vida.<br><br>Tiempo estimado: 30 minutos",
        order_number=3,
        theme_id=THEME_3_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Rueda de la vida",
                "instructions": "Califica del 1 al 10: Salud física, Salud emocional, Tiempo personal, Relaciones, Propósito, Trabajo.",
                "questions": [
                    {"type": "text", "question": "Calificaciones de cada area"}
                ]
            },
            {
                "title": "Paso 2: Diagnóstico de impacto",
                "instructions": "Para areas con menos de 7: ¿Como afectan a las demás? ¿Consecuencias a mediano plazo?",
                "questions": [
                    {"type": "text", "question": "Analisis de impacto cruzado"}
                ]
            },
            {
                "title": "Paso 3: Prioridad estratégica",
                "instructions": "Elige una area para mejorar y una para mantener estable en las próximas 4 semanas.",
                "questions": [
                    {"type": "text", "question": "Area a mejorar"},
                    {"type": "text", "question": "Area a mantener"}
                ]
            },
            {
                "title": "Paso 4: Microacciones sostenibles",
                "instructions": "Acción principal de mejora (1-2 horas/semana) y acción de mantenimiento (1 vez/semana).",
                "questions": [
                    {"type": "text", "question": "Mis microacciones para cada area"}
                ]
            },
            {
                "title": "Paso 5: Integración en agenda",
                "instructions": "Bloquea en tu calendario las acciones como citas importantes.",
                "questions": [
                    {"type": "text", "question": "¿Como integraras esto en tu agenda?"}
                ]
            },
            {
                "title": "Paso 6: Seguimiento",
                "instructions": "Cada semana: ¿Cumpli? ¿Como esta mi energía? ¿Mejoró la calificación?<br><br>Meditación: MANIFESTACIÓN CONSCIENTE - https://www.youtube.com/watch?v=H-Ts8PcvvbE<br><br>☝ Envíame un mensaje con la palabra (ACCIONAR) para agendar tu novena y ultima sesión 1:1.",
                "questions": [
                    {"type": "text", "question": "Mi compromiso de seguimiento semanal"}
                ]
            }
        ])
    )
    db.add(exercise_3_3)
    db.flush()
    print(f"  ✅ Ejercicio 3.3 créé (ID: {exercise_3_3.id})")
    
    db.commit()
    
    print("\n" + "=" * 70)
    print("✅ TOUS LES EXERCICES DU MODULE 5 CRÉÉS AVEC SUCCÈS!")
    print("=" * 70)
    print(f"📚 Thème 1 (Claridad y sentido): 2 exercices")
    print(f"📚 Thème 2 (Esto ya no me pertenece): 2 exercices")
    print(f"📚 Thème 3 (Energía en movimiento): 3 exercices")
    print(f"\n✨ Total: 7 exercices créés avec de nombreux tableaux!")
    print("\n🎉 Module 5 est maintenant COMPLET (21 cartes + 7 exercices)!")

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        create_all_exercises_module5(db)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

