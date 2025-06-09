from database import SessionLocal
from models import Module, Theme, Exercise, ThemeCard

def check_all_modules():
    db = SessionLocal()
    try:
        # Get all modules
        modules = db.query(Module).order_by(Module.order_number).all()
        
        print("🎯 SISTEMA DE MÓDULOS - ALQUIMIA DEL CAMBIO")
        print("=" * 60)
        
        if not modules:
            print("❌ No modules found in database")
            return
            
        total_themes = 0
        total_cards = 0
        total_exercises = 0
        
        for module in modules:
            print(f"\n📚 MÓDULO {module.order_number}: {module.title}")
            print("-" * 50)
            print(f"   📝 Descripción: {module.description[:80]}...")
            print(f"   🎯 Creencia a transformar: {module.belief_to_transform[:80]}...")
            
            # Get themes for this module
            themes = db.query(Theme).filter(Theme.module_id == module.id).order_by(Theme.order_number).all()
            module_cards = 0
            module_exercises = 0
            
            print(f"\n   🎯 Temas ({len(themes)}):")
            for theme in themes:
                cards_count = db.query(ThemeCard).filter(ThemeCard.theme_id == theme.id).count()
                exercises_count = db.query(Exercise).filter(Exercise.theme_id == theme.id).count()
                
                print(f"      {theme.order_number}. {theme.title}")
                print(f"         └─ Cards: {cards_count}, Exercises: {exercises_count}")
                
                module_cards += cards_count
                module_exercises += exercises_count
            
            print(f"\n   📊 Totales del módulo:")
            print(f"      • Temas: {len(themes)}")
            print(f"      • Cards: {module_cards}")
            print(f"      • Exercises: {module_exercises}")
            
            total_themes += len(themes)
            total_cards += module_cards
            total_exercises += module_exercises
        
        print("\n" + "=" * 60)
        print("📈 RESUMEN GENERAL:")
        print(f"   • Total Módulos: {len(modules)}")
        print(f"   • Total Temas: {total_themes}")
        print(f"   • Total Cards: {total_cards}")
        print(f"   • Total Exercises: {total_exercises}")
        print("=" * 60)
        
        # Check system status
        expected_modules = 4
        if len(modules) == expected_modules:
            print("✅ Sistema completo: Todos los módulos están creados")
        else:
            print(f"⚠️  Sistema incompleto: {len(modules)}/{expected_modules} módulos creados")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_all_modules() 