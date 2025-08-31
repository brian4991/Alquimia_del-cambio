#!/usr/bin/env python3
"""
Script pour tester les endpoints de validation des modules
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_validation_endpoints():
    """Tester les endpoints de validation"""
    
    print("🧪 Test des endpoints de validation des modules")
    print("="*50)
    
    # Simuler un token admin (vous devrez remplacer par un vrai token)
    headers = {
        "Authorization": "Bearer YOUR_ADMIN_TOKEN_HERE",
        "Content-Type": "application/json"
    }
    
    try:
        # Test 1: Récupérer tous les modules (admin)
        print("\n1️⃣ Test GET /auth/admin/modules")
        response = requests.get(f"{BASE_URL}/auth/admin/modules", headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            modules = response.json()
            print(f"✅ {len(modules)} modules trouvés")
            for module in modules:
                print(f"   - ID: {module['id']}, Titre: {module['title']}")
        else:
            print(f"❌ Erreur: {response.text}")
        
        # Test 2: Récupérer les stats utilisateurs
        print("\n2️⃣ Test GET /auth/admin/users/stats")
        response = requests.get(f"{BASE_URL}/auth/admin/users/stats", headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ {len(data['users'])} utilisateurs trouvés")
            for user in data['users']:
                validated = user.get('validated_modules', [])
                print(f"   - ID: {user['id']}, Username: {user['username']}")
                print(f"     Modules validés: {validated}")
        else:
            print(f"❌ Erreur: {response.text}")
        
        # Test 3: Valider un module pour l'utilisateur 1
        user_id = 1
        module_id = 3
        print(f"\n3️⃣ Test POST /auth/admin/users/{user_id}/validate-module/{module_id}")
        response = requests.post(f"{BASE_URL}/auth/admin/users/{user_id}/validate-module/{module_id}", headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ {result['message']}")
            print(f"   Modules validés: {result['validated_modules']}")
        else:
            print(f"❌ Erreur: {response.text}")
        
        # Test 4: Vérifier la sauvegarde
        print(f"\n4️⃣ Vérification de la sauvegarde")
        response = requests.get(f"{BASE_URL}/auth/admin/users/stats", headers=headers)
        if response.status_code == 200:
            data = response.json()
            user = next((u for u in data['users'] if u['id'] == user_id), None)
            if user:
                print(f"✅ Utilisateur {user_id} trouvé")
                print(f"   Modules validés: {user.get('validated_modules', [])}")
            else:
                print(f"❌ Utilisateur {user_id} non trouvé")
        
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter au serveur backend")
        print("   Vérifiez que le serveur fonctionne sur http://localhost:8000")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")

def get_admin_token():
    """Récupérer un token admin pour les tests"""
    print("\n🔑 Pour tester avec un vrai token:")
    print("1. Connectez-vous en tant qu'admin sur le frontend")
    print("2. Ouvrez les outils de développement (F12)")
    print("3. Dans la console, tapez: localStorage.getItem('token')")
    print("4. Copiez le token et remplacez 'YOUR_ADMIN_TOKEN_HERE' dans ce script")

if __name__ == "__main__":
    print("🔧 Test des endpoints de validation des modules\n")
    
    # Instructions pour obtenir un token
    get_admin_token()
    
    # Tests (nécessite un token valide)
    test_validation_endpoints()
    
    print("\n" + "="*50)
    print("✅ Tests terminés !")
    print("\n💡 Si les tests échouent:")
    print("   1. Vérifiez que le serveur backend fonctionne")
    print("   2. Remplacez 'YOUR_ADMIN_TOKEN_HERE' par un vrai token admin")
    print("   3. Vérifiez les logs du serveur pour les erreurs")
