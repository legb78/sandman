"""
Script de test pour l'API Clipboard
Teste différents formats de requête pour diagnostiquer l'erreur 500
"""

import os
import requests
from dotenv import load_dotenv

# Charger le .env depuis le dossier src
load_dotenv("src/.env")

CLIPBOARD_API_KEY = os.getenv("CLIPBOARD_API_KEY")
CLIPBOARD_BASE_URL = "https://clipdrop-api.co"

def test_simple_prompt():
    """Test avec un prompt très simple"""
    
    if not CLIPBOARD_API_KEY:
        print("❌ Clé API manquante")
        return
    
    url = f"{CLIPBOARD_BASE_URL}/text-to-image/v1"
    headers = {"x-api-key": CLIPBOARD_API_KEY}
    
    # Test 1: Prompt très simple avec files
    print("🧪 Test 1: Prompt simple avec form-data")
    files = {'prompt': (None, 'a simple red apple')}
    
    try:
        response = requests.post(url, headers=headers, files=files)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        if response.status_code != 200:
            print(f"Erreur: {response.text}")
        else:
            print("✅ Succès!")
            
    except Exception as e:
        print(f"Exception: {str(e)}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Prompt simple avec data
    print("🧪 Test 2: Prompt simple avec data")
    data = {'prompt': 'a simple red apple'}
    
    try:
        response = requests.post(url, headers=headers, data=data)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        if response.status_code != 200:
            print(f"Erreur: {response.text}")
        else:
            print("✅ Succès!")
            
    except Exception as e:
        print(f"Exception: {str(e)}")
    
    print("\n" + "="*50 + "\n")
    
    # Test 3: Vérifier les informations de l'API
    print("🧪 Test 3: Informations sur l'API")
    print(f"URL: {url}")
    print(f"Clé API: {CLIPBOARD_API_KEY[:10]}..." if CLIPBOARD_API_KEY else "Aucune")

if __name__ == "__main__":
    test_simple_prompt()
