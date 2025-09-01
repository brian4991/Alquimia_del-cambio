from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
import os

from auth import get_current_admin_user
from database import get_db
from models import User, Module, Theme, ThemeCard, Exercise
from import_complete_data_railway import import_complete_data_to_railway

router = APIRouter(tags=["admin-import"])

@router.post("/admin/import-database")
def trigger_database_import(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Route admin pour déclencher l'import de la base de données complète"""
    
    try:
        # Vérifier que l'utilisateur est bien admin
        if current_admin.role != 'admin':
            raise HTTPException(status_code=403, detail="Admin access required")
        
        # Vérifier si des modules existent déjà (éviter les doublons)
        existing_modules = db.query(Module).count()
        
        if existing_modules > 1:  # Plus que le module par défaut
            return {
                "success": False,
                "message": f"Import annulé: {existing_modules} modules existent déjà. Supprimez d'abord les modules existants si vous voulez réimporter.",
                "existing_modules": existing_modules
            }
        
        # Déclencher l'import
        success = import_complete_data_to_railway()
        
        if success:
            # Compter les modules après import
            total_modules = db.query(Module).count()
            total_themes = db.query(Theme).count()
            total_cards = db.query(ThemeCard).count()
            total_exercises = db.query(Exercise).count()
            
            return {
                "success": True,
                "message": "Import terminé avec succès!",
                "imported_data": {
                    "modules": total_modules,
                    "themes": total_themes,
                    "cards": total_cards,
                    "exercises": total_exercises
                }
            }
        else:
            return {
                "success": False,
                "message": "Erreur lors de l'import. Vérifiez les logs.",
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'import: {str(e)}")

@router.get("/admin/database-status")
def get_database_status(current_admin: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    """Obtenir le statut actuel de la base de données"""
    
    try:
        modules = db.query(Module).all()
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
            "modules": modules_info,
            "database_initialized": len(modules) > 0
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")
