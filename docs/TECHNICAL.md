# Technical Documentation

## Analysis Methods

### 1. Mel-frequency Cepstral Coefficients (MFCC) Analysis

The MFCC analysis is a fundamental component of voice analysis that captures the spectral envelope of the voice signal. This method:

- Converts the audio signal to the frequency domain using Short-Time Fourier Transform (STFT)
- Applies a mel-scale filterbank to simulate human auditory perception
- Computes the cepstral coefficients using Discrete Cosine Transform (DCT)

Parameters:

- Window size: 25ms
- Hop length: 10ms
- Number of MFCCs: 13
- Sample rate: 16kHz

### 2. Formant Frequency Analysis

Formant analysis examines the resonant frequencies of the vocal tract:

- Uses Welch's method for power spectral density estimation
- Identifies the first three formant frequencies (F1, F2, F3)
- Analyzes formant stability and transitions

Parameters:

- Window size: 1024 points
- Overlap: 50%
- Frequency resolution: 15.625 Hz

### 3. Phase Coherence Detection

Phase coherence analysis examines the relationships between frequency components:

- Computes STFT with phase information
- Analyzes phase differences between adjacent time frames
- Detects artificial phase patterns typical in AI synthesis

Parameters:

- FFT size: 2048 points
- Window type: Hann
- Hop length: 512 points

### 4. Spectral Pattern Analysis

Spectral analysis examines the frequency distribution and energy patterns:

- Spectral centroid: Measures the "brightness" of the sound
- Spectral flatness: Indicates the noise-like vs. tonal nature
- Spectral rolloff: Measures the frequency distribution

Parameters:

- FFT size: 2048 points
- Overlap: 50%
- Window type: Hann

### 5. Pitch and Harmonic Analysis

Pitch analysis examines the fundamental frequency and harmonic structure:

- Uses YIN algorithm for pitch tracking
- Computes harmonic-to-noise ratio
- Analyzes pitch stability and variations

Parameters:

- Frame size: 1024 points
- Hop length: 256 points
- Minimum frequency: 20 Hz
- Maximum frequency: 2000 Hz

### 6. Temporal Pattern Analysis

Temporal analysis examines time-domain characteristics:

- Zero-crossing rate: Measures signal frequency
- RMS energy: Measures signal amplitude
- Temporal envelope: Analyzes amplitude modulation

Parameters:

- Window size: 25ms
- Hop length: 10ms
- Window type: Hann

## Statistical Analysis

The tool employs various statistical measures to identify AI synthesis:

1. Similarity Metrics:

   - Cosine similarity for MFCC comparison
   - Euclidean distance for formant analysis
   - Pearson correlation for temporal patterns

2. Stability Measures:

   - Standard deviation of pitch
   - Formant stability index
   - Phase coherence variance

3. Pattern Recognition:
   - Spectral smoothness index
   - Harmonic structure analysis
   - Temporal pattern matching

## Quality Control

The analysis includes several quality control measures:

1. Signal Preprocessing:

   - DC offset removal
   - High-pass filtering (20Hz cutoff)
   - Normalization to -23 LUFS

2. Validation:

   - Cross-validation across methods
   - Comparison with natural voice samples
   - Statistical significance testing

3. Error Handling:
   - Graceful degradation for corrupted audio
   - Robust parameter estimation
   - Comprehensive error reporting

## Performance Considerations

The tool is optimized for:

- Real-time analysis of audio streams
- Batch processing of multiple files
- Memory-efficient processing of long recordings

## Limitations

Current limitations include:

- Minimum audio duration: 1 second
- Maximum audio duration: 30 minutes
- Supported sample rates: 16kHz, 44.1kHz, 48kHz
- Supported formats: WAV, MP3, M4A, AAC
