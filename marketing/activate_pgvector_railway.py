#!/usr/bin/env python3
"""
Script pour activer pgvector sur Railway via CLI Railway.

Usage:
    railway login
    railway link  # ou railway init si nouveau projet
    python marketing/activate_pgvector_railway.py
"""

import subprocess
import sys
import os
import webbrowser
import platform


def run_command(cmd: list, check: bool = True) -> tuple[bool, str]:
    """Exécute une commande et retourne (success, output)."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=check
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "Command not found"


def check_railway_cli() -> bool:
    """Vérifie que Railway CLI est installé."""
    success, _ = run_command(["railway", "--version"], check=False)
    if not success:
        print("❌ Railway CLI n'est pas installé.")
        print("💡 Installe-le avec: npm install -g @railway/cli")
        return False
    print("✅ Railway CLI détecté")
    return True


def open_chrome(url: str) -> bool:
    """Ouvre Chrome avec l'URL spécifiée."""
    system = platform.system()
    
    try:
        if system == "Windows":
            # Windows: utilise le chemin Chrome ou start chrome
            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                "chrome.exe",  # Si dans PATH
            ]
            
            for chrome_path in chrome_paths:
                try:
                    subprocess.Popen([chrome_path, url], shell=False)
                    return True
                except FileNotFoundError:
                    continue
            
            # Fallback: utilise start avec chrome
            subprocess.Popen(f'start chrome "{url}"', shell=True)
            return True
            
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Google Chrome", url])
            return True
            
        else:  # Linux
            subprocess.Popen(["google-chrome", url])
            return True
            
    except Exception as e:
        print(f"⚠️  Impossible d'ouvrir Chrome automatiquement: {e}")
        print(f"💡 Ouvre manuellement: {url}")
        return False


def check_railway_auth() -> bool:
    """Vérifie que l'utilisateur est connecté à Railway."""
    success, output = run_command(["railway", "whoami"], check=False)
    if not success:
        print("❌ Tu n'es pas connecté à Railway.")
        print()
        print("🔐 Connexion à Railway...")
        print("🌐 Ouverture de Chrome pour l'authentification...")
        
        # Lance railway login (qui va ouvrir un navigateur)
        # On utilise webbrowser pour forcer Chrome si possible
        print()
        print("📝 Exécution de: railway login")
        
        # Ouvre Chrome avec Railway login
        railway_login_url = "https://railway.app/login"
        chrome_opened = open_chrome(railway_login_url)
        
        if chrome_opened:
            print("✅ Chrome ouvert avec Railway login")
        
        # Lance railway login en parallèle
        print()
        print("⏳ En attente de la connexion...")
        print("💡 Complète l'authentification dans Chrome, puis appuie sur Entrée ici.")
        
        try:
            input("   Appuie sur Entrée une fois connecté... ")
        except KeyboardInterrupt:
            print("\n❌ Connexion annulée")
            return False
        
        # Vérifie à nouveau
        success, output = run_command(["railway", "whoami"], check=False)
        if success:
            print(f"✅ Connecté en tant que: {output.strip()}")
            return True
        else:
            print("❌ Connexion échouée. Réessaye avec: railway login")
            return False
    
    print(f"✅ Déjà connecté: {output.strip()}")
    return True


def activate_pgvector() -> bool:
    """Active l'extension pgvector sur Railway."""
    print("📦 Activation de l'extension pgvector...")
    
    success, output = run_command([
        "railway", "run", "psql", 
        "-c", "CREATE EXTENSION IF NOT EXISTS vector;"
    ])
    
    if success:
        print("✅ pgvector activé avec succès!")
        return True
    else:
        print(f"❌ Erreur: {output}")
        return False


def verify_pgvector() -> bool:
    """Vérifie que pgvector est bien activé."""
    print("\n💡 Vérification...")
    
    success, output = run_command([
        "railway", "run", "psql",
        "-c", "SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';"
    ])
    
    if success:
        print(output)
        if "vector" in output.lower():
            print("✅ pgvector est bien activé!")
            return True
        else:
            print("⚠️  pgvector ne semble pas être activé")
            return False
    else:
        print(f"⚠️  Impossible de vérifier: {output}")
        return False


def main():
    print("=" * 60)
    print("🚀 Activation de pgvector sur Railway")
    print("=" * 60)
    print()
    
    # Vérifications
    if not check_railway_cli():
        sys.exit(1)
    
    if not check_railway_auth():
        sys.exit(1)
    
    print()
    
    # Activation
    if not activate_pgvector():
        sys.exit(1)
    
    # Vérification
    verify_pgvector()
    
    print()
    print("=" * 60)
    print("✅ Terminé!")
    print("=" * 60)


if __name__ == "__main__":
    main()
