#!/usr/bin/env python3
"""
Script simplifié pour importer seulement les modules, thèmes, cartes et exercices
(sans les utilisateurs et leurs données)
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Module, Theme, ThemeCard, Exercise

def import_modules_only():
    """Importer seulement les modules et leur contenu vers Railway PostgreSQL"""
    
    # Vérifier si on a la DATABASE_URL (Railway)
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print("❌ DATABASE_URL non trouvée. Assurez-vous d'être connecté à Railway.")
        return False
    
    try:
        # Se connecter à Railway PostgreSQL
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        print("🔄 Création des modules manquants...")
        
        # Données hardcodées des modules 2-5 (basées sur votre structure)
        modules_data = [
            {
                "title": "Celebra tu ser",
                "description": "Aprende a valorarte y celebrar tu esencia única.",
                "objective": "El propósito de este módulo es que aprendas a valorarte, celebrar tu esencia única y desarrollar una autoestima saludable.",
                "belief_to_transform": "No soy suficiente tal como soy",
                "expected_results": "Desarrollas una autoestima sólida y aprendes a valorar tus cualidades únicas.",
                "recommended_book": "Los cuatro acuerdos de Miguel Ruiz",
                "audio_file": "modulo-2-intro.mp3",
                "order_number": 2
            },
            {
                "title": "El Arte de Amar",
                "description": "Descubre cómo amar de manera consciente y saludable.",
                "objective": "El propósito de este módulo es que aprendas a amar de manera consciente, saludable y auténtica.",
                "belief_to_transform": "El amor verdadero requiere sacrificio personal",
                "expected_results": "Desarrollas relaciones amorosas más conscientes y satisfactorias.",
                "recommended_book": "El Arte de Amar de Erich Fromm",
                "audio_file": "modulo-3-intro.mp3",
                "order_number": 3
            },
            {
                "title": "De la expectativa a la realidad",
                "description": "Aprende a gestionar expectativas y vivir en el presente.",
                "objective": "El propósito de este módulo es que aprendas a gestionar tus expectativas y vivir más plenamente en el presente.",
                "belief_to_transform": "Las cosas deben ser como yo espero que sean",
                "expected_results": "Desarrollas mayor flexibilidad mental y capacidad de adaptación.",
                "recommended_book": "El Poder del Ahora de Eckhart Tolle",
                "audio_file": "modulo-4-intro.mp3",
                "order_number": 4
            },
            {
                "title": "Libertad en Acción",
                "description": "Integra todo lo aprendido y vive con mayor libertad emocional.",
                "objective": "El propósito de este módulo es que integres todo lo aprendido y vivas con mayor libertad emocional.",
                "belief_to_transform": "Estoy limitado por mis circunstancias",
                "expected_results": "Vives con mayor libertad, autenticidad y propósito en tu vida diaria.",
                "recommended_book": "Man's Search for Meaning de Viktor Frankl",
                "audio_file": "modulo-5-intro.mp3",
                "order_number": 5
            }
        ]
        
        modules_created = 0
        
        try:
            for module_data in modules_data:
                # Vérifier si le module existe déjà
                existing_module = db.query(Module).filter(
                    Module.order_number == module_data['order_number']
                ).first()
                
                if existing_module:
                    print(f"⚠️  Module {module_data['order_number']} '{module_data['title']}' existe déjà")
                    continue
                
                # Créer le nouveau module
                new_module = Module(
                    title=module_data['title'],
                    description=module_data['description'],
                    objective=module_data['objective'],
                    belief_to_transform=module_data['belief_to_transform'],
                    expected_results=module_data['expected_results'],
                    recommended_book=module_data['recommended_book'],
                    audio_file=module_data['audio_file'],
                    order_number=module_data['order_number'],
                    is_active=True
                )
                
                db.add(new_module)
                db.flush()  # Pour obtenir l'ID
                modules_created += 1
                
                print(f"✅ Module {module_data['order_number']} '{module_data['title']}' créé (ID: {new_module.id})")
                
                # Créer des thèmes par défaut pour chaque module
                for i in range(1, 4):  # 3 thèmes par module
                    theme = Theme(
                        title=f"Thème {i} - {module_data['title']}",
                        content=f"Contenu du thème {i} pour le module {module_data['title']}",
                        order_number=i,
                        module_id=new_module.id
                    )
                    db.add(theme)
                    db.flush()
                    
                    # Créer des cartes par défaut pour chaque thème
                    for j in range(1, 6):  # 5 cartes par thème
                        card = ThemeCard(
                            title=f"Carte {j} - Thème {i}",
                            content=f"Contenu de la carte {j} pour le thème {i} du module {module_data['title']}",
                            card_type="content",
                            order_number=j,
                            theme_id=theme.id,
                            is_editable=True
                        )
                        db.add(card)
                    
                    # Créer des exercices par défaut pour chaque thème
                    for k in range(1, 4):  # 3 exercices par thème
                        exercise = Exercise(
                            title=f"Exercice {k} - Thème {i}",
                            instructions=f"Instructions pour l'exercice {k} du thème {i} - {module_data['title']}",
                            sub_questions="[]",
                            order_number=k,
                            theme_id=theme.id
                        )
                        db.add(exercise)
            
            # Commit toutes les créations
            db.commit()
            
            print(f"\n🎉 Import terminé avec succès!")
            print(f"📚 {modules_created} nouveaux modules créés")
            
            # Vérifier le résultat final
            print(f"\n📚 Modules maintenant dans Railway:")
            all_modules = db.query(Module).order_by(Module.order_number).all()
            for module in all_modules:
                theme_count = db.query(Theme).filter(Theme.module_id == module.id).count()
                card_count = db.query(ThemeCard).join(Theme).filter(Theme.module_id == module.id).count()
                exercise_count = db.query(Exercise).join(Theme).filter(Theme.module_id == module.id).count()
                print(f"   {module.order_number}. {module.title}")
                print(f"      📋 {theme_count} thèmes, 🃏 {card_count} cartes, ✏️ {exercise_count} exercices")
            
            return True
            
        except Exception as e:
            db.rollback()
            print(f"❌ Erreur lors de l'import: {e}")
            return False
        finally:
            db.close()
            
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

if __name__ == "__main__":
    import_modules_only()
