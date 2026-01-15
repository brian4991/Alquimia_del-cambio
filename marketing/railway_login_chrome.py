#!/usr/bin/env python3
"""
Script pour se connecter à Railway en ouvrant Chrome automatiquement.

Usage:
    python marketing/railway_login_chrome.py
"""

import subprocess
import sys
import platform


def open_chrome(url: str) -> bool:
    """Ouvre Chrome avec l'URL spécifiée."""
    system = platform.system()
    
    try:
        if system == "Windows":
            # Windows: essaie plusieurs chemins Chrome
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            ]
            
            for chrome_path in chrome_paths:
                try:
                    subprocess.Popen([chrome_path, url], shell=False)
                    return True
                except FileNotFoundError:
                    continue
            
            # Fallback: utilise start chrome
            subprocess.Popen(f'start chrome "{url}"', shell=True)
            return True
            
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Google Chrome", url])
            return True
            
        else:  # Linux
            subprocess.Popen(["google-chrome", url])
            return True
            
    except Exception as e:
        print(f"⚠️  Impossible d'ouvrir Chrome: {e}")
        return False


def main():
    print("=" * 60)
    print("🚂 Connexion à Railway avec Chrome")
    print("=" * 60)
    print()
    
    # Vérifie si déjà connecté
    try:
        result = subprocess.run(
            ["railway", "whoami"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0:
            print(f"✅ Déjà connecté: {result.stdout.strip()}")
            print("💡 Pour te déconnecter: railway logout")
            return
    except FileNotFoundError:
        print("❌ Railway CLI n'est pas installé.")
        print("💡 Installe-le avec: npm install -g @railway/cli")
        sys.exit(1)
    
    print("🔐 Connexion à Railway...")
    print("🌐 Ouverture de Chrome...")
    print()
    
    # Ouvre Chrome avec Railway login
    railway_url = "https://railway.app/login"
    if open_chrome(railway_url):
        print("✅ Chrome ouvert avec Railway login")
    else:
        print("⚠️  Chrome n'a pas pu être ouvert automatiquement")
        print(f"💡 Ouvre manuellement: {railway_url}")
    
    print()
    print("📝 Lancement de: railway login")
    print("⏳ Complète l'authentification dans Chrome...")
    print()
    
    # Lance railway login (qui va aussi ouvrir un navigateur)
    # Mais on a déjà ouvert Chrome, donc ça devrait utiliser Chrome
    try:
        subprocess.run(["railway", "login"], check=True)
        print()
        print("✅ Connexion réussie!")
        
        # Vérifie qui est connecté
        result = subprocess.run(
            ["railway", "whoami"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"👤 Connecté en tant que: {result.stdout.strip()}")
        
    except subprocess.CalledProcessError:
        print()
        print("❌ Erreur lors de la connexion")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print("❌ Connexion annulée")
        sys.exit(1)


if __name__ == "__main__":
    main()
