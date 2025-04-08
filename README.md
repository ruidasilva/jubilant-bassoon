# Voice Forensic Analyzer v2.0.0

A forensic analysis tool for detecting AI-generated voice content and potential copyright infringement in audio recordings. This tool employs advanced audio analysis techniques to identify patterns consistent with AI voice cloning and unauthorized voice synthesis.

## Version History

- v2.0.0: Added local AI-powered forensic report generation
- v1.0.0: Initial release with basic voice analysis features

## Overview

This forensic tool provides a comprehensive suite of audio analysis methods to detect AI voice synthesis and cloning, particularly useful for:

- Detecting unauthorized AI voice cloning
- Identifying potential copyright infringement
- Providing forensic evidence of voice manipulation
- Supporting copyright protection efforts
- Generating professional forensic reports using local AI

## Features

- Mel-frequency Cepstral Coefficients (MFCC) analysis for voice fingerprinting
- Formant frequency analysis for vocal tract comparison
- Phase coherence detection for AI synthesis artifacts
- Spectral pattern analysis for voice manipulation detection
- Pitch and harmonic analysis for voice authenticity verification
- Temporal pattern analysis for audio integrity checking
- Local AI-powered forensic report generation

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/voice-forensic-analyzer.git
cd voice-forensic-analyzer
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Note: The first time you run the analysis, it will download the AI model (approximately 14GB). This is a one-time download.

## Usage

1. Place your audio files in the `Vocals for Comparison` directory
2. Run the analysis:

```bash
python voicecompare.py
```

3. Review the generated forensic analysis report in the console output
4. Find the detailed AI-generated forensic report in the generated markdown file

## Analysis Methods

### 1. MFCC Analysis

- Creates unique voice fingerprints
- Identifies subtle differences in voice characteristics
- Detects artificial smoothing patterns typical of AI synthesis

### 2. Formant Analysis

- Examines vocal tract characteristics
- Detects unnatural stability in formant patterns
- Provides quantitative comparison for forensic evidence

### 3. Phase Coherence Detection

- Analyzes phase relationships across frequency bands
- Identifies artificial phase patterns
- Helps detect AI synthesis artifacts

### 4. Spectral Pattern Analysis

- Examines frequency distribution
- Analyzes energy patterns
- Detects artificial smoothing and manipulation

### 5. Pitch and Harmonic Analysis

- Investigates fundamental frequency
- Analyzes harmonic structure
- Identifies unnatural pitch variations

### 6. Temporal Pattern Analysis

- Examines time-domain characteristics
- Analyzes energy distribution
- Detects unnatural temporal patterns

## Requirements

- Python 3.8+
- librosa
- numpy
- scipy
- matplotlib
- resemblyzer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for forensic analysis and copyright protection purposes only. Users are responsible for:

- Ensuring compliance with local laws and regulations regarding audio analysis
- Obtaining necessary permissions for audio analysis
- Using the tool in accordance with copyright laws
- Maintaining proper chain of custody for forensic evidence
- Following proper documentation procedures for legal proceedings

## Legal Notice

This tool is intended for use in:

- Copyright infringement investigations
- Voice cloning detection
- Forensic audio analysis
- Copyright protection efforts

Users should consult with legal professionals regarding the admissibility of analysis results in their jurisdiction.
