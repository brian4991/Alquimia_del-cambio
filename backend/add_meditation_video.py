"""Script pour ajouter la colonne meditation_video_url aux modules"""
import sqlite3

def add_meditation_video_column():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # Vérifier si la colonne existe déjà
    cursor.execute("PRAGMA table_info(modules)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'meditation_video_url' not in columns:
        print("Ajout de la colonne meditation_video_url...")
        cursor.execute("ALTER TABLE modules ADD COLUMN meditation_video_url TEXT")
        conn.commit()
        print("Colonne ajoutée avec succès!")
    else:
        print("La colonne meditation_video_url existe déjà.")
    
    conn.close()

if __name__ == "__main__":
    add_meditation_video_column()
