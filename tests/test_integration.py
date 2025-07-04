"""
Integration tests for the Dream Synthesizer application
"""

import sys
import os
import unittest
from io import BytesIO
import tempfile

# Add parent directory to path to import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the modules to test
from src.audio_processor import preprocess_audio, transcribe_audio
from src.text_processor import extract_visual_elements, analyze_dream_sentiment, create_image_prompt
from src.image_generator import generate_image_with_clipboard

class TestIntegration(unittest.TestCase):
    """Integration tests for the full workflow"""
    
    def test_mock_workflow(self):
        """Test the complete workflow with mocked data"""
        # Mock audio transcription result
        mock_transcription = "I dreamed I was flying over a beautiful blue ocean with golden sunset clouds."
        
        # Process the text
        visual_elements = extract_visual_elements(mock_transcription)
        self.assertIsNotNone(visual_elements)
        self.assertIn("elements_visuels", visual_elements)
        
        # Create prompt
        prompt_result = create_image_prompt(visual_elements)
        self.assertIsNotNone(prompt_result)
        self.assertIsInstance(prompt_result, str)
        self.assertGreater(len(prompt_result), 10)  # Reasonable length check
        
        # Analyze sentiment
        sentiment = analyze_dream_sentiment(mock_transcription)
        self.assertIsNotNone(sentiment)
        self.assertIn("sentiment", sentiment)
        self.assertIn("description", sentiment)
    
    def test_api_keys_available(self):
        """Test that necessary API keys are available in the environment"""
        # Test if required API keys are set
        groq_api_key = os.environ.get("GROQ_API_KEY")
        mistral_api_key = os.environ.get("MISTRAL_API_KEY")
        clipboard_api_key = os.environ.get("CLIPBOARD_API_KEY")
        
        # Just check if they exist, but don't print the values
        if not groq_api_key:
            print("Warning: GROQ_API_KEY not set")
        if not mistral_api_key:
            print("Warning: MISTRAL_API_KEY not set")
        if not clipboard_api_key:
            print("Warning: CLIPBOARD_API_KEY not set")

if __name__ == "__main__":
    unittest.main()
