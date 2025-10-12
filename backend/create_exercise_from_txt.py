"""
Script générique pour créer des exercices à partir de fichiers .txt

Usage:
    python create_exercise_from_txt.py <theme_id> <exercise_number> <order_number> <txt_file_path>
    
Exemple:
    python create_exercise_from_txt.py 13 "1.1" 1 "../assets/Ejercicio #1 _Historia_.txt"
"""
import sys
import io
import json
import re

# Fix encoding for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Exercise

def parse_exercise_from_txt(txt_content, exercise_number):
    """
    Parse le contenu du fichier .txt et extrait les sections
    
    Format attendu:
    - Titre: "Ejercicio X.X: [Titre]"
    - Instructions générales (après Paso a Paso:)
    - Sections numérotées (1., 2., 3., etc.)
    - Questions regroupées dans chaque section
    """
    
    lines = txt_content.strip().split('\n')
    
    # Trouver le titre de l'exercice
    title = None
    instructions = ""
    sections = []
    current_section = None
    current_questions = []
    in_instructions = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Chercher le titre (ligne qui contient "Ejercicio")
        if f"Ejercicio {exercise_number}:" in line and not title:
            # Extraire juste le titre après "Ejercicio X.X: "
            match = re.search(rf"Ejercicio {re.escape(exercise_number)}:\s*(.+)", line)
            if match:
                title = match.group(1).strip()
        
        # Chercher "Paso a Paso:" pour commencer les instructions
        elif "Paso a Paso:" in line:
            in_instructions = True
            # Lire les instructions jusqu'à la première section numérotée
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                # Arrêter si on trouve une section numérotée
                if re.match(r'^\d+\.\s+', next_line):
                    i -= 1  # Revenir en arrière
                    break
                # Arrêter si ligne vide suivie d'une section
                if not next_line and i + 1 < len(lines) and re.match(r'^\d+\.\s+', lines[i+1].strip()):
                    i -= 1
                    break
                if next_line and next_line != "Paso a Paso:":
                    instructions += next_line + "\n\n"
                i += 1
            in_instructions = False
        
        # Chercher les sections numérotées (1., 2., 3., etc.)
        elif re.match(r'^\d+\.\s+', line):
            # Sauvegarder la section précédente si elle existe
            if current_section:
                sections.append({
                    "title": current_section["title"],
                    "instructions": current_section["instructions"],
                    "questions": "\n\n".join(current_questions)
                })
                current_questions = []
            
            # Nouvelle section
            section_match = re.match(r'^\d+\.\s+(.+):', line)
            if section_match:
                section_title = section_match.group(1).strip()
                current_section = {
                    "title": line,
                    "instructions": "",
                    "questions": []
                }
                
                # Lire les instructions de la section (jusqu'aux questions)
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    # Arrêter si on trouve une question (commence par ¿)
                    if next_line.startswith('¿'):
                        i -= 1
                        break
                    # Arrêter si nouvelle section
                    if re.match(r'^\d+\.\s+', next_line):
                        i -= 1
                        break
                    # Arrêter si "Tiempo estimado"
                    if "Tiempo estimado:" in next_line:
                        i -= 1
                        break
                    if next_line:
                        current_section["instructions"] += next_line + " "
                    i += 1
                current_section["instructions"] = current_section["instructions"].strip()
        
        # Chercher les questions (commencent par ¿)
        elif line.startswith('¿') and current_section:
            current_questions.append(line)
        
        # Chercher "Tiempo estimado:" pour les instructions globales
        elif "Tiempo estimado:" in line and not in_instructions:
            instructions += line + "\n"
        
        i += 1
    
    # Sauvegarder la dernière section
    if current_section and current_questions:
        sections.append({
            "title": current_section["title"],
            "instructions": current_section["instructions"],
            "questions": "\n\n".join(current_questions)
        })
    
    return {
        "title": title if title else f"Ejercicio {exercise_number}",
        "instructions": instructions.strip(),
        "sections": sections
    }

def create_exercise(db: Session, theme_id, exercise_number, order_number, txt_file_path):
    """Créer un exercice à partir d'un fichier .txt"""
    
    print(f"\n📖 Lecture du fichier: {txt_file_path}")
    
    # Lire le fichier
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier: {e}")
        return False
    
    # Parser le contenu
    print(f"📝 Parsing du contenu pour Ejercicio {exercise_number}...")
    parsed = parse_exercise_from_txt(content, exercise_number)
    
    if not parsed["sections"]:
        print("⚠️  Aucune section trouvée dans le fichier")
        return False
    
    print(f"✅ Titre: {parsed['title']}")
    print(f"✅ {len(parsed['sections'])} sections trouvées")
    
    # Vérifier si l'exercice existe déjà
    existing = db.query(Exercise).filter(
        Exercise.theme_id == theme_id,
        Exercise.title == f"Ejercicio {exercise_number}: {parsed['title']}"
    ).first()
    
    if existing:
        print(f"⚠️  L'exercice existe déjà (ID: {existing.id})")
        response = input("Voulez-vous le supprimer et recréer? (yes/no): ")
        if response.lower() == 'yes':
            db.delete(existing)
            db.commit()
            print("✅ Exercice supprimé")
        else:
            print("❌ Annulation")
            return False
    
    # Créer les sections au format JSON
    exercise_sections = []
    for section in parsed["sections"]:
        exercise_sections.append({
            "title": section["title"],
            "instructions": section["instructions"],
            "questions": [
                {
                    "id": f"q_{len(exercise_sections) + 1}",
                    "question": section["questions"],
                    "type": "textarea",
                    "required": True
                }
            ]
        })
    
    # Créer l'exercice
    exercise = Exercise(
        title=f"Ejercicio {exercise_number}: {parsed['title']}",
        instructions=parsed["instructions"],
        order_number=order_number,
        theme_id=theme_id,
        exercise_sections=json.dumps(exercise_sections)
    )
    
    db.add(exercise)
    db.commit()
    
    print(f"\n✅ Exercice créé avec succès!")
    print(f"   ID: {exercise.id}")
    print(f"   Titre: {exercise.title}")
    print(f"   Sections: {len(exercise_sections)}")
    
    return True

def main():
    """Fonction principale"""
    
    if len(sys.argv) < 5:
        print("❌ Usage: python create_exercise_from_txt.py <theme_id> <exercise_number> <order_number> <txt_file_path>")
        print("\nExemple:")
        print('   python create_exercise_from_txt.py 13 "1.1" 1 "../assets/Ejercicio #1 _Historia_.txt"')
        sys.exit(1)
    
    theme_id = int(sys.argv[1])
    exercise_number = sys.argv[2]
    order_number = int(sys.argv[3])
    txt_file_path = sys.argv[4]
    
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print(f"📚 CRÉATION D'EXERCICE À PARTIR DE FICHIER TXT")
        print("=" * 70)
        print(f"Theme ID: {theme_id}")
        print(f"Exercise Number: {exercise_number}")
        print(f"Order: {order_number}")
        print(f"File: {txt_file_path}")
        
        success = create_exercise(db, theme_id, exercise_number, order_number, txt_file_path)
        
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

