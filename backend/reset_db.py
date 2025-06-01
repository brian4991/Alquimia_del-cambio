import os
import sqlite3

# Remove the database file if it exists
if os.path.exists("app.db"):
    os.remove("app.db")
    print("✅ Ancienne base de données supprimée")
else:
    print("ℹ️ Aucune base de données à supprimer")

print("🔄 La nouvelle base de données sera créée au prochain démarrage du serveur")
print("🚀 Relancez le serveur avec: uvicorn main:app --host 0.0.0.0 --port 8000") 