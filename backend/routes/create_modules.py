from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any

from auth import get_current_admin_user
from database import get_db
from models import User, Module, Theme, ThemeCard, Exercise

router = APIRouter(tags=["create-modules"])

@router.post("/admin/create-missing-modules")
def create_missing_modules(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)) -> Dict[str, Any]:
    """Route admin pour créer les modules manquants (2, 3, 4, 5)"""
    
    try:
        # Vérifier que l'utilisateur est bien admin
        if current_admin.role != 'admin':
            raise HTTPException(status_code=403, detail="Admin access required")
        
        # Données des modules à créer
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
        themes_created = 0
        cards_created = 0
        exercises_created = 0
        
        for module_data in modules_data:
            # Vérifier si le module existe déjà
            existing_module = db.query(Module).filter(
                Module.order_number == module_data['order_number']
            ).first()
            
            if existing_module:
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
            
            # Créer des thèmes par défaut pour chaque module
            for i in range(1, 4):  # 3 thèmes par module
                theme = Theme(
                    title=f"Tema {i}: {module_data['title']}",
                    content=f"Contenido del tema {i} para el módulo {module_data['title']}. Este tema te ayudará a profundizar en los conceptos clave del módulo.",
                    order_number=i,
                    module_id=new_module.id
                )
                db.add(theme)
                db.flush()
                themes_created += 1
                
                # Créer des cartes par défaut pour chaque thème
                card_contents = [
                    {"title": "Introducción", "content": f"Bienvenido al tema {i} del módulo {module_data['title']}. En este tema exploraremos conceptos fundamentales.", "type": "content"},
                    {"title": "Conceptos Clave", "content": f"Los conceptos principales que aprenderás en este tema incluyen elementos esenciales para tu crecimiento personal.", "type": "theory"},
                    {"title": "Ejemplo Práctico", "content": f"Aquí tienes un ejemplo práctico de cómo aplicar lo que estás aprendiendo en tu vida diaria.", "type": "example"},
                    {"title": "Reflexión", "content": f"Tómate un momento para reflexionar sobre cómo estos conceptos se relacionan con tu experiencia personal.", "type": "content"},
                    {"title": "Preparación para Ejercicios", "content": f"Ahora que has explorado los conceptos, estás listo para poner en práctica lo aprendido.", "type": "exercise_intro"}
                ]
                
                for j, card_content in enumerate(card_contents, 1):
                    card = ThemeCard(
                        title=card_content["title"],
                        content=card_content["content"],
                        card_type=card_content["type"],
                        order_number=j,
                        theme_id=theme.id,
                        is_editable=True
                    )
                    db.add(card)
                    cards_created += 1
                
                # Créer des exercices par défaut pour chaque thème
                exercise_templates = [
                    {
                        "title": f"Reflexión Personal - Tema {i}",
                        "instructions": f"Reflexiona sobre los conceptos del tema {i}. ¿Cómo se relacionan con tu experiencia personal? Escribe tus pensamientos y observaciones."
                    },
                    {
                        "title": f"Aplicación Práctica - Tema {i}",
                        "instructions": f"Describe una situación específica donde puedes aplicar lo aprendido en el tema {i}. ¿Qué pasos concretos tomarías?"
                    },
                    {
                        "title": f"Integración - Tema {i}",
                        "instructions": f"¿Cómo integrarás los aprendizajes del tema {i} en tu vida diaria? Crea un plan de acción personal."
                    }
                ]
                
                for k, exercise_template in enumerate(exercise_templates, 1):
                    exercise = Exercise(
                        title=exercise_template["title"],
                        instructions=exercise_template["instructions"],
                        sub_questions="[]",
                        order_number=k,
                        theme_id=theme.id
                    )
                    db.add(exercise)
                    exercises_created += 1
        
        # Commit toutes les créations
        db.commit()
        
        # Obtenir le statut final
        total_modules = db.query(Module).count()
        
        return {
            "success": True,
            "message": f"Modules créés avec succès!",
            "created": {
                "modules": modules_created,
                "themes": themes_created,
                "cards": cards_created,
                "exercises": exercises_created
            },
            "total_modules_now": total_modules
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur lors de la création des modules: {str(e)}")

@router.get("/admin/modules-status")
def get_modules_status(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Obtenir le statut actuel des modules"""
    
    try:
        modules = db.query(Module).order_by(Module.order_number).all()
        modules_info = []
        
        for module in modules:
            theme_count = db.query(Theme).filter(Theme.module_id == module.id).count()
            card_count = db.query(ThemeCard).join(Theme).filter(Theme.module_id == module.id).count()
            exercise_count = db.query(Exercise).join(Theme).filter(Theme.module_id == module.id).count()
            
            modules_info.append({
                "id": module.id,
                "title": module.title,
                "order_number": module.order_number,
                "themes": theme_count,
                "cards": card_count,
                "exercises": exercise_count,
                "is_active": module.is_active
            })
        
        return {
            "total_modules": len(modules),
            "modules": modules_info
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")
