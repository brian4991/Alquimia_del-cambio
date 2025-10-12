"""
Script pour créer tous les exercices du Module 4: De la expectativa a la realidad
Version simplifiée sans problèmes d'encodage
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def create_all_exercises_module4(db: Session):
    """Créer tous les exercices du Module 4"""
    
    print("\n" + "=" * 70)
    print("🚀 CRÉATION DE TOUS LES EXERCICES DU MODULE 4")
    print("=" * 70)
    
    # IDs des thèmes du Module 4
    THEME_1_ID = 19  # Rompiendo barreras
    THEME_2_ID = 20  # Despertar auténtico
    THEME_3_ID = 21  # Mapa de acción hacia la autenticidad
    
    exercises_created = []
    
    # EJERCICIO 1.1
    print("\n📝 Création de l'Ejercicio 1.1...")
    exercise_1_1 = Exercise(
        title="Ejercicio 1.1: Mis acuerdos",
        parent_title="Ejercicio #1: Acuerdos",
        instructions="Este ejercicio tiene como propósito ayudarte a identificar los acuerdos internos que has hecho a lo largo de tu vida.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tus acuerdos",
                "instructions": "Encuentra un espacio tranquilo donde puedas reflexionar sin interrupciones. Respira profundamente y pregúntate: ¿Cuáles son las creencias sobre mí mismo/a que han estado presentes desde mi infancia? Escribe al menos 7 acuerdos que sientas que han marcado tu vida.",
                "questions": [
                    {"type": "text", "question": "Lista tus 7 acuerdos internos que han marcado tu vida"}
                ]
            },
            {
                "title": "Paso 2: Reflexiona sobre su impacto",
                "instructions": "Para cada acuerdo, reflexiona sobre: ¿De dónde viene? ¿Cómo influye en mi vida actual? ¿Cómo me hace sentir?",
                "questions": [
                    {"type": "text", "question": "Analiza el impacto de tus acuerdos en tu vida"}
                ]
            },
            {
                "title": "Paso 3: Transforma tus acuerdos",
                "instructions": "Transforma tus acuerdos limitantes en afirmaciones que te empoderen. Escribe nuevas versiones que reflejen tu verdadero valor.",
                "questions": [
                    {"type": "text", "question": "Escribe tus nuevos acuerdos transformados"}
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
        title="Ejercicio 1.2: La voz interior a la que sirvo",
        parent_title="Ejercicio #1: Acuerdos",
        instructions="Tiempo estimado: 30 minutos",
        order_number=2,
        theme_id=THEME_1_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica tu voz interior",
                "instructions": "Durante un día, pon atención a cómo te hablas a ti mismo. ¿Es una voz de apoyo o de juicio? ¿A quién sirve esa voz?",
                "questions": [
                    {"type": "text", "question": "¿Qué frases recurrentes te dices a ti mismo/a?"},
                    {"type": "text", "question": "¿A quién sirve esa voz? (papá, mamá, otra persona)"}
                ]
            },
            {
                "title": "Paso 2: Cuestiona su veracidad",
                "instructions": "Reflexiona sobre el origen de estas frases. ¿Son basadas en hechos o en el miedo?",
                "questions": [
                    {"type": "text", "question": "¿De dónde vienen estas creencias y reflejan la verdad sobre ti hoy?"}
                ]
            },
            {
                "title": "Paso 3: Transforma tu voz interna",
                "instructions": "Transforma las frases negativas en mensajes positivos y realistas. Haz una lista con al menos 7 frases transformadas.",
                "questions": [
                    {"type": "text", "question": "Lista tus 7 frases transformadas"}
                ]
            },
            {
                "title": "Paso 4: Crea afirmaciones diarias",
                "instructions": "Escribe afirmaciones que refuercen tu confianza y repítelas diariamente.",
                "questions": [
                    {"type": "text", "question": "Escribe tus afirmaciones diarias (al menos 5)"}
                ]
            },
            {
                "title": "Paso 5: Meditación y cierre",
                "instructions": "Meditación: Los 4 ACUERDOS TOLTECAS - https://www.youtube.com/watch?v=nn_VJ7ew2cc<br><br>☝ Instrucción: Envíame un mensaje con la palabra (ACUERDOS) para agendar tu séptima sesión 1:1.",
                "questions": []
            }
        ])
    )
    db.add(exercise_1_2)
    db.flush()
    print(f"  ✅ Ejercicio 1.2 créé (ID: {exercise_1_2.id})")
    
    # EJERCICIO 2.1
    print("\n📝 Création de l'Ejercicio 2.1...")
    exercise_2_1 = Exercise(
        title="Ejercicio 2.1: Mi ser",
        parent_title="Ejercicio #2: Ser",
        instructions="Este ejercicio te ayuda a reconocer las capas que te han alejado de tu verdadera esencia.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Identifica lo aprendido vs lo auténtico",
                "instructions": "Reflexiona sobre qué partes de ti provienen de tu esencia y cuáles de la influencia de otros.",
                "questions": [
                    {"type": "text", "question": "¿Qué partes de ti provienen de la influencia de otros?"}
                ]
            },
            {
                "title": "Paso 2: Reconoce tu verdadero ser",
                "instructions": "Identifica los rasgos que sí sientes como parte de tu verdadero ser.",
                "questions": [
                    {"type": "text", "question": "Describe tu verdadero ser sin las etiquetas que otros te han puesto"}
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
        title="Ejercicio 2.2: Cultivando la autoconciencia",
        parent_title="Ejercicio #2: Ser",
        instructions="Tiempo estimado: 30 minutos",
        order_number=2,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Observa tu autenticidad",
                "instructions": "¿Cuándo actúas desde tu autenticidad? ¿Cuándo te sientes desconectado/a?",
                "questions": [
                    {"type": "text", "question": "¿Cuándo actúas desde tu autenticidad y cuándo te sientes desconectado/a?"}
                ]
            },
            {
                "title": "Paso 2: Identifica patrones limitantes",
                "instructions": "Piensa en situaciones donde no actuaste desde tu verdadero ser.",
                "questions": [
                    {"type": "text", "question": "Describe situaciones donde no actuaste desde tu verdadero ser"}
                ]
            },
            {
                "title": "Paso 3: Diferencia lo que deseas de lo aprendido",
                "instructions": "¿Qué deseas realmente vs qué has aprendido a desear?",
                "questions": [
                    {"type": "text", "question": "Lista las cosas que realmente deseas, sin importar la opinión externa"}
                ]
            },
            {
                "title": "Paso 4: Compromiso con la autoconciencia",
                "instructions": "Crea una afirmación que refuerce tu compromiso con tu verdadero ser.",
                "questions": [
                    {"type": "text", "question": "Escribe tu afirmación de autenticidad"}
                ]
            }
        ])
    )
    db.add(exercise_2_2)
    db.flush()
    print(f"  ✅ Ejercicio 2.2 créé (ID: {exercise_2_2.id})")
    
    # EJERCICIO 2.3
    print("\n📝 Création de l'Ejercicio 2.3...")
    exercise_2_3 = Exercise(
        title="Ejercicio 2.3: Abrazando la vulnerabilidad",
        parent_title="Ejercicio #2: Ser",
        instructions="Tiempo estimado: 30 minutos",
        order_number=3,
        theme_id=THEME_2_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Reconoce cómo ocultas tu vulnerabilidad",
                "instructions": "¿Cómo te proteges para que los demás no vean tu vulnerabilidad?",
                "questions": [
                    {"type": "text", "question": "¿Cómo ocultas tu vulnerabilidad y cómo te ha afectado?"}
                ]
            },
            {
                "title": "Paso 2: Explora una situación vulnerable",
                "instructions": "Piensa en una situación reciente donde sentiste vulnerabilidad pero la ocultaste.",
                "questions": [
                    {"type": "text", "question": "Describe una situación vulnerable y qué te habría gustado expresar"},
                    {"type": "text", "question": "Escribe un mensaje de compasión para ti mismo/a"}
                ]
            },
            {
                "title": "Paso 3: Acción concreta",
                "instructions": "Elige una acción concreta para abrazar tu vulnerabilidad hoy.<br><br>Meditación: CONSTELACIÓN FAMILIAR - https://www.youtube.com/watch?v=ZuTyYBDl82k<br><br>☝ Envíame un mensaje con la palabra (SER) para continuar.",
                "questions": [
                    {"type": "text", "question": "Escribe tu compromiso para abrazar tu vulnerabilidad"}
                ]
            }
        ])
    )
    db.add(exercise_2_3)
    db.flush()
    print(f"  ✅ Ejercicio 2.3 créé (ID: {exercise_2_3.id})")
    
    # EJERCICIO 3.1
    print("\n📝 Création de l'Ejercicio 3.1...")
    exercise_3_1 = Exercise(
        title="Ejercicio 3.1: La vida que sí quiero",
        parent_title="Ejercicio #3: Realidad",
        instructions="Este ejercicio te ayuda a construir la vida que realmente deseas.<br><br>Tiempo estimado: 30 minutos",
        order_number=1,
        theme_id=THEME_3_ID,
        exercise_sections=json.dumps([
            {
                "title": "Paso 1: Observa tu vida actual",
                "instructions": "¿Qué disfrutas de tu vida actual y qué no refleja tu verdadero ser?",
                "questions": [
                    {"type": "text", "question": "¿Qué disfrutas de tu vida actual y qué no refleja tu verdadero ser?"}
                ]
            },
            {
                "title": "Paso 2: Define tu visión",
                "instructions": "Define tus valores esenciales, deseos verdaderos y emociones que quieres sentir.",
                "questions": [
                    {"type": "text", "question": "Define tus valores, deseos y las emociones que quieres sentir"}
                ]
            },
            {
                "title": "Paso 3: Identifica obstáculos",
                "instructions": "¿Qué creencias te frenan y cómo las transformarás?",
                "questions": [
                    {"type": "text", "question": "¿Qué creencias te frenan y cómo las transformarás?"}
                ]
            },
            {
                "title": "Paso 4: Define acciones concretas",
                "instructions": "Define 3 pequeñas acciones que puedas hacer esta semana.",
                "questions": [
                    {"type": "text", "question": "Lista tus 3 acciones concretas para esta semana"}
                ]
            },
            {
                "title": "Paso 5: Crea tu afirmación",
                "instructions": "Crea una afirmación que te motive a seguir avanzando.<br><br>Meditación: MANIFIESTA tu FUTURO DESEADO - https://www.youtube.com/watch?v=WB7zsan7WYs<br><br>☝ Envíame un mensaje con la palabra (REALIDAD) para agendar tu octava sesión 1:1.",
                "questions": [
                    {"type": "text", "question": "Escribe tu afirmación personal"}
                ]
            }
        ])
    )
    db.add(exercise_3_1)
    db.flush()
    print(f"  ✅ Ejercicio 3.1 créé (ID: {exercise_3_1.id})")
    
    db.commit()
    
    print("\n" + "=" * 70)
    print("✅ TOUS LES EXERCICES DU MODULE 4 CRÉÉS AVEC SUCCÈS!")
    print("=" * 70)
    print(f"📚 Thème 1 (Rompiendo barreras): 2 exercices")
    print(f"📚 Thème 2 (Despertar auténtico): 3 exercices")
    print(f"📚 Thème 3 (Mapa de acción): 1 exercice")
    print(f"\n✨ Total: 6 exercices créés!")
    print("\n🎉 Module 4 est maintenant COMPLET (21 cartes + 6 exercices)!")

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        create_all_exercises_module4(db)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

