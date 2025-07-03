import osimport requestsimport base64from io import BytesIOfrom PIL import Imagefrom dotenv import load_dotenv# Charger les variables d'environnementload_dotenv()# Configuration pour l'API ClipboardCLIPBOARD_API_KEY = os.getenv("CLIPBOARD_API_KEY")CLIPBOARD_BASE_URL = "https://clipdrop-api.co"def generate_image_with_clipboard(prompt, style="automatic", width=1024, height=1024):    """    Génère une image avec l'API Clipboard        Args:        prompt (str): Le prompt pour générer l'image        style (str): Le style de l'image (automatic, realistic, artistic, etc.)        width (int): Largeur de l'image        height (int): Hauteur de l'image            Returns:        dict: Résultat avec l'image générée ou une erreur    """        if not CLIPBOARD_API_KEY:        return {            "success": False,            "error": "Clé API Clipboard manquante. Ajoutez CLIPBOARD_API_KEY dans votre fichier .env"        }        # Adapter le prompt selon le style choisi    styled_prompt = adapt_prompt_for_style(prompt, style)        try:        # URL de l'endpoint pour text-to-image        url = f"{CLIPBOARD_BASE_URL}/text-to-image/v1"                # Headers avec authentification
        headers = {
            "x-api-key": CLIPBOARD_API_KEY,
        }
        
        # Données pour la requête
        data = {
            "prompt": styled_prompt,
            "width": width,
            "height": height,
        }
        
        # Faire la requête POST
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            # Convertir la réponse en image
            image = Image.open(BytesIO(response.content))
            
            # Sauvegarder temporairement l'image
            temp_path = save_temp_image(image)
            
            return {
                "success": True,
                "image_path": temp_path,
                "image": image,
                "prompt_used": styled_prompt,
                "style": style
            }
        else:
            return {
                "success": False,
                "error": f"Erreur API Clipboard: {response.status_code} - {response.text}"
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": f"Erreur lors de la génération: {str(e)}"
        }

def adapt_prompt_for_style(prompt, style):
    """
    Adapte le prompt selon le style choisi par l'utilisateur
    """
    
    style_modifiers = {
        "automatic": "",  # Garde le prompt tel quel
        "realistic": ", photorealistic, high detail, professional photography",
        "artistic": ", digital art, artistic style, creative interpretation",
        "dreamlike": ", dreamlike, surreal, ethereal, magical atmosphere",
        "abstract": ", abstract art, non-representational, artistic abstraction",
        "surreal": ", surreal, bizarre, dreamlike, Salvador Dali style",
        "fantasy": ", fantasy art, magical, mystical, enchanted world",
        "impressionist": ", impressionist style, soft brushstrokes, light and color",
        "cinematic": ", cinematic lighting, movie scene, dramatic composition",
        "anime": ", anime style, manga art, Japanese animation style",
        "oil_painting": ", oil painting, classical art, fine art style",
        "watercolor": ", watercolor painting, soft colors, artistic technique"
    }
    
    modifier = style_modifiers.get(style, "")
    
    if style == "automatic":
        return prompt  # Utilise le prompt optimisé par Mistral tel quel
    else:
        return f"{prompt}{modifier}"

def save_temp_image(image, filename_prefix="dream_image"):
    """
    Sauvegarde temporairement l'image générée
    """
    import tempfile
    import time
    
    # Créer un nom de fichier unique
    timestamp = int(time.time())
    filename = f"{filename_prefix}_{timestamp}.png"
    
    # Utiliser le dossier temporaire du système
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, filename)
    
    # Sauvegarder l'image
    image.save(temp_path, "PNG")
    
    return temp_path

def get_available_styles():
    """
    Retourne la liste des styles disponibles avec leurs descriptions
    """
    return {
        "automatic": "Style automatique (recommandé par l'IA)",
        "realistic": "Réaliste et photographique",
        "artistic": "Art digital créatif",
        "dreamlike": "Onirique et éthéré",
        "abstract": "Art abstrait",
        "surreal": "Surréaliste",
        "fantasy": "Fantastique et magique", 
        "impressionist": "Style impressionniste",
        "cinematic": "Style cinématographique",
        "anime": "Style anime/manga",
        "oil_painting": "Peinture à l'huile",
        "watercolor": "Aquarelle"
    }

def validate_image_parameters(width, height):
    """
    Valide les paramètres d'image pour l'API Clipboard
    """
    # Contraintes typiques de l'API Clipboard
    min_size = 512
    max_size = 1024
    
    # Ajuster si nécessaire
    if width < min_size:
        width = min_size
    if width > max_size:
        width = max_size
        
    if height < min_size:
        height = min_size
    if height > max_size:
        height = max_size
    
    return width, height

def preview_styled_prompt(original_prompt, style):
    """
    Prévisualise comment le prompt sera modifié selon le style
    """
    styled_prompt = adapt_prompt_for_style(original_prompt, style)
    
    return {
        "original_prompt": original_prompt,
        "styled_prompt": styled_prompt,
        "style": style,
        "modifications_applied": styled_prompt != original_prompt
    }
