# Audio to Image App

This project is a Streamlit application that transforms audio into text and then generates images based on that text. The application is designed to provide an interactive interface for users to upload audio files, process them, and visualize the results.

## Project Structure

```
audio-to-image-app
├── src
│   ├── app.py                # Main entry point for the Streamlit application
│   ├── audio_processor.py     # Functions for processing audio files
│   ├── text_processor.py      # Functions for transforming text data
│   ├── image_generator.py     # Functions for generating images from text
│   └── utils
│       └── helpers.py        # Utility functions used across the application
├── requirements.txt           # Project dependencies
├── .streamlit
│   └── config.toml           # Streamlit configuration settings
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd audio-to-image-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Upload an audio file or record audio directly using the provided interface.
- The application will transcribe the audio to text using Groq's Whisper API.
- The text is analyzed with Mistral AI to extract key visual elements and emotions.
- Finally, the app generates an image based on the analysis using Clipboard API (Stable Diffusion).
- You can select different image styles to customize the output.

## Testing

Run the unit tests with:
```
python -m unittest discover -s tests
```

## Maintenance

A cleanup script is provided to remove temporary files created by the application:
```
python scripts/cleanup.py
```

Options:
- `--max-age`: Maximum age of files to keep in hours (default: 24)
- `--dry-run`: Show what would be deleted without actually deleting
- `--path`: Path to clean (defaults to project directory)

## Data Privacy & GDPR

For information about GDPR compliance and data privacy considerations, please see [GDPR_COMPLIANCE.md](GDPR_COMPLIANCE.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
- Explore the generated images and download them if needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.