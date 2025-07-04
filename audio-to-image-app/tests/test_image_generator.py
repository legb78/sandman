"""
Unit tests for the image generator module
"""

import sys
import os
import unittest
from io import BytesIO
from PIL import Image
import tempfile

# Add parent directory to path to import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module to test
from src.image_generator import (
    generate_image_with_clipboard,
    get_available_styles,
    preview_styled_prompt
)

class TestImageGenerator(unittest.TestCase):
    """Tests for image_generator.py functions"""
    
    def test_get_available_styles(self):
        """Test getting available image styles"""
        styles = get_available_styles()
        # Check that we get a list of styles
        self.assertIsInstance(styles, list)
        # Check that the list contains the expected default styles
        self.assertIn("automatic", styles)
        self.assertIn("photographic", styles)
    
    def test_preview_styled_prompt(self):
        """Test the preview styled prompt function"""
        test_prompt = "A beautiful mountain landscape"
        test_style = "anime"
        
        styled_prompt = preview_styled_prompt(test_prompt, test_style)
        
        # The styled prompt should include both the original prompt and style information
        self.assertIn(test_prompt, styled_prompt)
        self.assertIn("anime", styled_prompt.lower())
    
    def test_invalid_api_key(self):
        """Test behavior with invalid API key"""
        # Temporarily set an invalid API key
        original_api_key = os.environ.get("CLIPBOARD_API_KEY", "")
        os.environ["CLIPBOARD_API_KEY"] = ""
        
        try:
            result = generate_image_with_clipboard("Test prompt")
            # Should return an error dict
            self.assertFalse(result["success"])
            self.assertIn("error", result)
            self.assertIn("API", result["error"])
        finally:
            # Restore original API key
            os.environ["CLIPBOARD_API_KEY"] = original_api_key

if __name__ == "__main__":
    unittest.main()
