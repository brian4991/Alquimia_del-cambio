import sqlite3
import os

if os.path.exists("psychology_app.db"):
    conn = sqlite3.connect("psychology_app.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT title FROM program_steps ORDER BY order_number")
        modules = cursor.fetchall()
        
        print("📋 Modules actuels dans la base de données :")
        for i, module in enumerate(modules, 1):
            print(f"{i}. {module[0]}")
        
        print(f"\nTotal: {len(modules)} modules")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
    finally:
        conn.close()
else:
    print("❌ Base de données n'existe pas - elle sera créée au prochain démarrage du serveur") 