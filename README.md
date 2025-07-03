# Synthétiseur de Rêves

Une application Streamlit qui transforme vos récits de rêves oraux en images et analyse les émotions qui s'en dégagent.

## 🌟 Fonctionnalités

- 🎤 **Enregistrement Vocal** - Racontez votre rêve ou uploadez un fichier audio
- 📝 **Transcription** - Conversion automatique de la parole au texte avec Groq API
- 🧠 **Analyse** - Classification émotionnelle et extraction des thèmes avec Mistral AI
- 🖼️ **Visualisation** - Génération d'images représentant le rêve avec ClipDrop API
- 📊 **Tableau de Bord** - Historique et analyse des rêves enregistrés

## 🚀 Installation

1. Clonez le dépôt
   ```
   git clone https://github.com/votre-username/sandman.git
   cd sandman
   ```

2. Installez les dépendances
   ```
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` à la racine du projet et ajoutez vos clés API
   ```
   GROQ_API_KEY=votre_cle_groq
   CLIPDROP_API_KEY=votre_cle_clipdrop
   MISTRAL_API_KEY=votre_cle_mistral
   ```

## 🏃‍♂️ Exécution

Lancez l'application avec Streamlit:
```
streamlit run app.py
```

## 📁 Structure du Projet

```
sandman/
├── .env                    # Fichier de configuration (à créer)
├── .gitignore              # Fichiers à ignorer par Git
├── README.md               # Ce fichier
├── app.py                  # Point d'entrée de l'application
├── requirements.txt        # Dépendances Python
└── src/
    ├── config.py           # Configuration de l'application
    ├── components/
    │   ├── audio_input.py  # Composant d'entrée audio
    │   └── dream_dashboard.py # Tableau de bord des rêves
    ├── services/
    │   ├── image_generation.py # Service de génération d'images
    │   ├── speech_to_text.py   # Service de transcription
    │   └── text_analysis.py    # Service d'analyse de texte
    └── utils/
        └── helpers.py      # Fonctions utilitaires
```

## ⚙️ APIs Utilisées

- **Groq API** (Whisper) - Transcription audio en texte
- **Mistral AI** - Analyse de texte et classification émotionnelle
- **ClipDrop API** - Génération d'images à partir du texte

## 📝 Note

Cette application est conçue dans le cadre d'un projet académique pour explorer l'utilisation des technologies d'IA dans l'analyse et la visualisation des rêves.