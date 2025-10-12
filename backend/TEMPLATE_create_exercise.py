"""
TEMPLATE pour créer des exercices à partir de fichiers .txt

INSTRUCTIONS:
1. Lire le fichier .txt de l'exercice
2. Copier ce template
3. Remplir les informations:
   - THEME_ID: l'ID du thème (ex: 13)
   - EXERCISE_NUMBER: le numéro (ex: "1.1", "2.1", etc.)
   - EXERCISE_TITLE: le titre sans le numéro
   - PARENT_TITLE: titre du GROUPE d'exercices (affiché en HAUT)
   - ORDER_NUMBER: l'ordre dans le thème (1, 2, 3...)
   - INSTRUCTIONS: les instructions générales
   - SECTIONS: copier-coller les sections du .txt

HIÉRARCHIE DES TITRES:
- PARENT_TITLE: Affiché EN HAUT de la page (ex: "Ejercicio #1: Historia")
  → Partagé par tous les sous-exercices du même groupe (1.1, 1.2, 1.3)
- TITLE: Affiché dans la sidebar (ex: "Ejercicio 1.1: Explorando mi historia...")
  → Format: "Ejercicio X.X: [EXERCISE_TITLE]"

RÈGLES IMPORTANTES:
- Questions multiples dans une section = les regrouper avec \\n\\n
- Rester FIDÈLE au texte original
- Ne PAS inventer ou modifier les questions
- Titre format: "Ejercicio X.X: Titre"
- Parent title format: "Ejercicio #X: Nom du groupe"
"""
import sys
import io
import json

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

# ==========================================
# CONFIGURATION - À MODIFIER
# ==========================================

THEME_ID = 13  # ID du thème
EXERCISE_NUMBER = "1.1"  # Numéro de l'exercice
EXERCISE_TITLE = "Explorando mi historia Emocional"  # Titre SANS le numéro
PARENT_TITLE = "Ejercicio #1: Historia"  # Titre du groupe d'exercices (affiché en haut)
ORDER_NUMBER = 1  # Ordre dans le thème

# Instructions générales de l'exercice
INSTRUCTIONS = """En este espacio te invito a escribir tu historia personal.

¿De dónde vienes? ¿Dónde naciste? ¿Cómo fue tu infancia? ¿Qué recuerdos te marcaron en tu adolescencia? ¿Cómo es tu vida actual? ¿Qué momentos importantes han dejado huella en tu camino?

Antes de sumergirnos en la identificación de tus emociones, quiero que te conectes profundamente con tu historia.

Tiempo estimado: 30 minutos"""

# Sections de l'exercice
# Format: liste de dictionnaires avec title, instructions, questions
SECTIONS = [
    {
        "title": "1. Reflexiona sobre tu familia",
        "instructions": "Dedica unos minutos a pensar en tu familia de origen (padres, abuelos, hermanos u otras figuras importantes de tu infancia). Responde las siguientes pregunta, no te limites a la hora de escribir, expresa todo lo que necesitas:",
        "questions": "¿Cómo manejaban las emociones en tu familia? ¿Se expresaban abiertamente, se reprimían, o se evitaban?\n\n¿Qué emociones eran \"aceptables\" de mostrar y cuáles no lo eran?\n\n¿Había algún miembro de la familia que evitará o exagerara ciertas emociones (como el enojo, tristeza, miedo o alegría)? ¿Cómo afectaba esto a la dinámica familiar?"
    },
    {
        "title": "2. Identifica patrones emocionales familiares",
        "instructions": "Ahora, trata de identificar si hubo patrones emocionales repetitivos en tu familia:",
        "questions": "¿Notabas alguna emoción que era común en la familia (por ejemplo, mucha tensión, enfado o silencio)?\n\n¿Recuerdas alguna situación específica en la que los miembros de tu familia reaccionaban de manera predecible?"
    },
    # Ajouter d'autres sections ici...
]

# ==========================================
# CODE - NE PAS MODIFIER EN DESSOUS
# ==========================================

def create_exercise(db: Session):
    """Créer l'exercice avec les données configurées ci-dessus"""
    
    full_title = f"Ejercicio {EXERCISE_NUMBER}: {EXERCISE_TITLE}"
    
    print(f"\n📝 Création de l'exercice:")
    print(f"   Titre (sous-exercice): {full_title}")
    print(f"   Parent Title (groupe): {PARENT_TITLE}")
    print(f"   Theme ID: {THEME_ID}")
    print(f"   Order: {ORDER_NUMBER}")
    print(f"   Sections: {len(SECTIONS)}")
    
    # Vérifier si existe déjà
    existing = db.query(Exercise).filter(
        Exercise.theme_id == THEME_ID,
        Exercise.title == full_title
    ).first()
    
    if existing:
        print(f"\n⚠️  L'exercice existe déjà (ID: {existing.id})")
        response = input("Voulez-vous le supprimer et recréer? (yes/no): ")
        if response.lower() != 'yes':
            print("❌ Annulation")
            return False
        db.delete(existing)
        db.commit()
        print("✅ Exercice supprimé")
    
    # Créer les sections au format JSON
    exercise_sections = []
    for i, section in enumerate(SECTIONS):
        exercise_sections.append({
            "title": section["title"],
            "instructions": section["instructions"],
            "questions": [
                {
                    "id": f"section_{i+1}",
                    "question": section["questions"],
                    "type": "textarea",
                    "required": True
                }
            ]
        })
    
    # Créer l'exercice
    exercise = Exercise(
        title=full_title,
        parent_title=PARENT_TITLE,
        instructions=INSTRUCTIONS,
        order_number=ORDER_NUMBER,
        theme_id=THEME_ID,
        exercise_sections=json.dumps(exercise_sections)
    )
    
    db.add(exercise)
    db.commit()
    
    print(f"\n✅ Exercice créé avec succès!")
    print(f"   ID: {exercise.id}")
    print(f"   Titre (sous-exercice): {exercise.title}")
    print(f"   Parent Title (groupe): {exercise.parent_title}")
    print(f"   Sections: {len(exercise_sections)}")
    
    return True

def main():
    """Fonction principale"""
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("📚 CRÉATION D'EXERCICE")
        print("=" * 70)
        
        success = create_exercise(db)
        
        if success:
            print("\n" + "=" * 70)
            print("✅ EXERCICE CRÉÉ AVEC SUCCÈS")
            print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()

