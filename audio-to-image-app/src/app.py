import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Ajouter le chemin actuel au path Python pour assurer l'importation du module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importer les fonctions des modules
try:
    from audio_processor import preprocess_audio, transcribe_audio
    from text_processor import extract_visual_elements, analyze_dream_sentiment, create_image_prompt
    import_success = True
except ImportError as e:
    import_success = False
    import_error = str(e)

# Charger les variables d'environnement
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Dream Synthesizer",
    page_icon="�",
    layout="centered"
)

# Interface principale
st.title("� Synthétiseur de Rêves")
st.subheader("Transformez vos rêves parlés en images")

# Vérifier que l'importation des modules a réussi
if not import_success:
    st.error(f"Erreur lors de l'importation des modules: {import_error}")
    st.stop()

# Section d'upload de fichier audio
st.markdown("### 1. Racontez votre rêve")
audio_input = st.file_uploader("Choisir un fichier MP3 ou WAV", type=["mp3", "wav", "m4a", "ogg"])

if audio_input is not None:
    # Afficher un lecteur audio pour le fichier téléchargé
    st.audio(audio_input)
    
    # Bouton pour traiter l'audio
    if st.button("Transcrire l'audio"):
        with st.spinner("Traitement de l'audio en cours..."):
            try:
                # Prétraiter l'audio
                audio_path = preprocess_audio(audio_input)
                
                # Transcrire l'audio
                transcript = transcribe_audio(audio_path)
                
                # Afficher la transcription
                st.markdown("### 2. Transcription de votre rêve")
                st.text_area("Texte transcrit", transcript, height=150, key="transcription_display")
                
                # Sauvegarder dans la session
                st.session_state.dream_transcript = transcript
                
            except Exception as e:
                st.error(f"Une erreur s'est produite: {str(e)}")

# Si une transcription existe dans la session, afficher la section d'analyse
if 'dream_transcript' in st.session_state:
    st.markdown("### 3. Analyse et traitement du rêve")
    
    # Permettre à l'utilisateur de modifier la transcription si nécessaire
    modified_transcript = st.text_area(
        "Vous pouvez modifier le texte avant l'analyse:",
        st.session_state.dream_transcript,
        height=150,
        key="transcript_editor"
    )
    
    # Bouton pour analyser le texte
    if st.button("Analyser le rêve avec Mistral"):
        with st.spinner("Analyse du rêve en cours..."):
            try:
                # Extraire les éléments visuels
                visual_analysis = extract_visual_elements(modified_transcript)
                
                # Analyser le sentiment
                sentiment_analysis = analyze_dream_sentiment(modified_transcript)
                
                # Sauvegarder les analyses
                st.session_state.visual_analysis = visual_analysis
                st.session_state.sentiment_analysis = sentiment_analysis
                
                # Afficher les résultats
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🎨 Éléments visuels détectés")
                    st.json(visual_analysis["elements_visuels"])
                    
                    st.markdown("#### 🎭 Ambiance du rêve")
                    st.json(visual_analysis["ambiance"])
                
                with col2:
                    st.markdown("#### 😊 Analyse émotionnelle")
                    st.json(sentiment_analysis)
                    
                    st.markdown("#### 🎨 Style recommandé")
                    st.write(f"**{visual_analysis.get('style_recommande', 'artistique')}**")
                
                # Afficher le prompt optimisé
                st.markdown("#### 📝 Description optimisée pour l'image")
                st.write(visual_analysis.get("prompt_optimise", ""))
                
            except Exception as e:
                st.error(f"Erreur lors de l'analyse: {str(e)}")
    
    # Si les analyses existent, afficher la section de génération d'image
    if 'visual_analysis' in st.session_state:
        st.markdown("### 4. Génération d'image")
        
        # Options de style
        style_options = ["automatique", "dreamlike", "realistic", "abstract", "surreal", "fantasy", "impressionist"]
        selected_style = st.selectbox(
            "Choisissez un style d'image:", 
            style_options,
            help="'automatique' utilise le style recommandé par l'analyse"
        )
        
        # Créer le prompt final
        image_prompt_data = create_image_prompt(
            st.session_state.visual_analysis, 
            selected_style
        )
        
        # Afficher le prompt qui sera utilisé
        st.markdown("#### 🖼️ Prompt pour la génération d'image")
        st.code(image_prompt_data["prompt_principal"])
        
        # Bouton de génération (placeholder pour l'instant)
        if st.button("Générer l'image"):
            st.info("🚧 La génération d'images sera implémentée dans la prochaine phase...")
            
            # Afficher les détails du prompt
            with st.expander("Voir les détails du prompt"):
                st.json(image_prompt_data)
            
            # Placeholder image
            st.image("https://via.placeholder.com/512x512?text=Votre+Rêve+Visualisé", 
                    caption=f"Futur rendu en style {selected_style}")
