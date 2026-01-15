#!/usr/bin/env python3
"""
Script pour contourner l'erreur SSL Railway CLI sur Windows.

Le problème "invalid peer certificate: UnknownIssuer" est souvent causé par:
- Certificats d'entreprise/proxy
- Configuration SSL Windows
- Certificats manquants

Solutions:
1. Désactiver temporairement la vérification SSL (développement uniquement)
2. Configurer les certificats système
"""

import subprocess
import sys
import os
import platform


def set_ssl_env_vars():
    """Configure les variables d'environnement pour contourner SSL."""
    # Variables pour désactiver la vérification SSL (DEV UNIQUEMENT)
    os.environ["SSL_CERT_FILE"] = ""
    os.environ["SSL_CERT_DIR"] = ""
    os.environ["REQUESTS_CA_BUNDLE"] = ""
    os.environ["CURL_CA_BUNDLE"] = ""
    
    # Pour Rust/reqwest (utilisé par Railway CLI)
    os.environ["RUSTLS_NO_VERIFY"] = "1"  # Ne pas utiliser en production!
    
    print("⚠️  Mode SSL non vérifié activé (développement uniquement)")
    print()


def check_railway_cli():
    """Vérifie que Railway CLI est installé."""
    try:
        result = subprocess.run(
            ["railway", "--version"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0:
            print(f"✅ Railway CLI: {result.stdout.strip()}")
            return True
        else:
            print("❌ Railway CLI n'est pas installé.")
            print("💡 Installe-le avec: npm install -g @railway/cli")
            return False
    except FileNotFoundError:
        print("❌ Railway CLI n'est pas installé.")
        print("💡 Installe-le avec: npm install -g @railway/cli")
        return False


def try_railway_login():
    """Essaie de se connecter à Railway."""
    print("🔐 Tentative de connexion à Railway...")
    print()
    
    # Méthode 1: Avec variables SSL désactivées
    print("📝 Méthode 1: Connexion avec SSL non vérifié...")
    set_ssl_env_vars()
    
    try:
        # Lance railway login dans un nouveau processus avec les env vars
        env = os.environ.copy()
        env["RUSTLS_NO_VERIFY"] = "1"
        
        result = subprocess.run(
            ["railway", "login"],
            env=env,
            check=False
        )
        
        if result.returncode == 0:
            print("✅ Connexion réussie!")
            return True
        else:
            print("❌ Échec avec méthode 1")
            print()
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        print()
    
    # Méthode 2: Utiliser railway login avec --browser
    print("📝 Méthode 2: Connexion manuelle via navigateur...")
    print("💡 Ouvre Chrome manuellement et va sur: https://railway.app/login")
    print("💡 Puis copie ton token Railway depuis: https://railway.app/account/tokens")
    print()
    
    return False


def manual_token_setup():
    """Guide pour configuration manuelle du token."""
    print("=" * 60)
    print("🔑 Configuration manuelle du token Railway")
    print("=" * 60)
    print()
    print("1. Va sur: https://railway.app/account/tokens")
    print("2. Crée un nouveau token (ou utilise un existant)")
    print("3. Copie le token")
    print()
    
    token = input("Colle ton token Railway ici: ").strip()
    
    if not token:
        print("❌ Token vide")
        return False
    
    # Configure le token via variable d'environnement
    os.environ["RAILWAY_TOKEN"] = token
    
    print()
    print("✅ Token configuré!")
    print("💡 Pour le rendre permanent, ajoute dans ton .env:")
    print(f"   RAILWAY_TOKEN={token}")
    print()
    
    # Teste la connexion
    try:
        result = subprocess.run(
            ["railway", "whoami"],
            env=os.environ.copy(),
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"✅ Connecté: {result.stdout.strip()}")
            return True
        else:
            print("❌ Token invalide")
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


def main():
    print("=" * 60)
    print("🔧 Fix SSL Railway CLI - Windows")
    print("=" * 60)
    print()
    
    if not check_railway_cli():
        sys.exit(1)
    
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
            print("💡 Pas besoin de se reconnecter!")
            return
    except:
        pass
    
    print("⚠️  Erreur SSL détectée - Solutions:")
    print()
    print("Option 1: Connexion avec SSL désactivé (DEV)")
    print("Option 2: Configuration manuelle du token")
    print()
    
    choice = input("Choisis une option (1 ou 2): ").strip()
    
    if choice == "1":
        if try_railway_login():
            print()
            print("✅ Connexion réussie!")
        else:
            print()
            print("❌ Échec. Essaie l'option 2 (token manuel)")
            if input("Continuer avec option 2? (o/n): ").lower() == 'o':
                manual_token_setup()
    elif choice == "2":
        manual_token_setup()
    else:
        print("❌ Option invalide")
        sys.exit(1)


if __name__ == "__main__":
    main()
