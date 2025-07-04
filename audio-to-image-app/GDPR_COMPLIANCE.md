# GDPR and Data Privacy

## Overview
This document provides information about GDPR compliance and data privacy considerations when using the Dream Synthesizer application. Please review this information before using the application in a production environment.

## API Services Used

### Groq (Whisper API)
- **Purpose**: Audio transcription
- **Data Processing**: Audio files are sent to Groq's API for transcription
- **Data Storage**: According to Groq's documentation, they process data on servers located in the United States
- **GDPR Compliance**: Check [Groq's Privacy Policy](https://groq.com/legal/privacy-policy/) for the most current information

### Mistral AI
- **Purpose**: Text analysis and prompt generation
- **Data Processing**: Text from transcriptions is sent to Mistral AI for analysis
- **Data Storage**: Mistral AI is based in France and operates within the EU, making it subject to GDPR regulations
- **GDPR Compliance**: Check [Mistral AI's Privacy Policy](https://mistral.ai/privacy/) for the most current information

### Clipboard API (Stable Diffusion)
- **Purpose**: Image generation from text prompts
- **Data Processing**: Text prompts are sent to generate images
- **Data Storage**: ClipDrop's parent company, Stability AI, operates servers in various locations
- **GDPR Compliance**: Check [Stability AI's Privacy Policy](https://stability.ai/privacy-policy) for the most current information

## Recommendations for GDPR Compliance

1. **Obtain User Consent**: Before processing personal data, ensure you have explicit consent from users.
2. **Data Minimization**: Only collect and process necessary data.
3. **Privacy Policy**: Create a privacy policy disclosing how data is used.
4. **Data Storage**: Use the application's temp file cleanup script to remove sensitive data regularly.
5. **Right to Be Forgotten**: Implement mechanisms to delete user data upon request.

## Data Retention

The application creates temporary files during normal operation:
- Audio recordings
- Generated images
- Transcription texts

You can use the provided cleanup script (`scripts/cleanup.py`) to automatically remove temporary files after a specified period:

```
python scripts/cleanup.py --max-age 24
```

## Server Location Considerations

For EU/EEA data subjects, consider:
1. Informing users that data may be processed outside the EU
2. Implementing additional safeguards if necessary
3. Evaluating whether data transfer agreements are required under GDPR

## Disclaimer

This document is provided for informational purposes only and does not constitute legal advice. Organizations should consult with legal professionals to ensure full GDPR compliance.
