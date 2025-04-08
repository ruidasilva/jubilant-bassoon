from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
from scipy.spatial.distance import cosine
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
from scipy import signal
from report_generator import ForensicReportGenerator

def load_audio(file_path):
    """
    Load and preprocess an audio file.
    
    Args:
        file_path (str): Path to the audio file
        
    Returns:
        tuple: (preprocessed audio, sample rate, duration)
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        wav = preprocess_wav(Path(file_path))
        y, sr = librosa.load(file_path, sr=16000)
        duration = librosa.get_duration(y=y, sr=sr)
        return wav, y, sr, duration
    except Exception as e:
        raise Exception(f"Error processing audio file {file_path}: {str(e)}")

def analyze_ai_patterns(audio_path, title):
    """
    Analyze audio for AI synthesis patterns.
    
    Args:
        audio_path (str): Path to the audio file
        title (str): Title for the analysis
        
    Returns:
        dict: Analysis results
    """
    try:
        _, y, sr, duration = load_audio(audio_path)
        
        # Calculate basic features
        rms = librosa.feature.rms(y=y)[0]
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
        
        # Calculate MFCCs
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        
        # Calculate pitch and harmonics
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch_mean = np.mean(pitches[magnitudes > np.max(magnitudes)/2])
        
        # Calculate spectral flatness (indicator of naturalness)
        spectral_flatness = librosa.feature.spectral_flatness(y=y)[0]
        
        # Calculate phase coherence (indicator of AI synthesis)
        stft = librosa.stft(y)
        phase = np.angle(stft)
        phase_diff = np.diff(phase, axis=1)
        phase_coherence = np.mean(np.abs(phase_diff))
        
        # Calculate formant frequencies
        formants = []
        for i in range(0, len(y), 1024):
            segment = y[i:i+1024]
            if len(segment) < 1024:
                continue
            f, p = signal.welch(segment, sr)
            peaks, _ = signal.find_peaks(p, height=np.max(p)*0.1)
            if len(peaks) >= 3:
                formants.append(f[peaks[:3]])
        
        formants = np.array(formants)
        formant_mean = np.mean(formants, axis=0) if len(formants) > 0 else np.zeros(3)
        
        return {
            'duration': duration,
            'rms': rms,
            'spectral_centroid': spectral_centroid,
            'spectral_bandwidth': spectral_bandwidth,
            'spectral_rolloff': spectral_rolloff,
            'zero_crossing_rate': zero_crossing_rate,
            'mfccs': mfccs,
            'pitch_mean': pitch_mean,
            'spectral_flatness': spectral_flatness,
            'phase_coherence': phase_coherence,
            'formants': formant_mean
        }
    except Exception as e:
        print(f"Error analyzing audio {audio_path}: {str(e)}")
        return None

def compare_ai_patterns(file1, file2):
    """
    Compare two audio files for AI synthesis patterns.
    
    Args:
        file1 (str): Path to first audio file
        file2 (str): Path to second audio file
        
    Returns:
        dict: Comparison results
    """
    try:
        # Load and analyze both files
        analysis1 = analyze_ai_patterns(file1, "Original")
        analysis2 = analyze_ai_patterns(file2, "New")
        
        if analysis1 is None or analysis2 is None:
            return None
            
        # Calculate similarity scores for different features
        # For MFCCs, we'll compare the mean values across time
        mfcc1_mean = np.mean(analysis1['mfccs'], axis=1)
        mfcc2_mean = np.mean(analysis2['mfccs'], axis=1)
        mfcc_similarity = 1 - cosine(mfcc1_mean, mfcc2_mean)
        
        # Compare formants
        formant_similarity = 1 - cosine(analysis1['formants'], analysis2['formants'])
        
        # Calculate differences in AI indicators
        phase_diff = abs(analysis1['phase_coherence'] - analysis2['phase_coherence'])
        flatness_diff = abs(np.mean(analysis1['spectral_flatness']) - np.mean(analysis2['spectral_flatness']))
        
        # Calculate additional AI indicators
        # 1. Spectral smoothness (AI voices tend to have smoother spectra)
        spectral_smoothness1 = np.mean(np.diff(analysis1['spectral_centroid']))
        spectral_smoothness2 = np.mean(np.diff(analysis2['spectral_centroid']))
        
        # 2. Formant stability (AI voices often have more stable formants)
        formant_stability1 = np.std(analysis1['formants'])
        formant_stability2 = np.std(analysis2['formants'])
        
        return {
            'mfcc_similarity': mfcc_similarity,
            'formant_similarity': formant_similarity,
            'phase_difference': phase_diff,
            'flatness_difference': flatness_diff,
            'pitch_difference': abs(analysis1['pitch_mean'] - analysis2['pitch_mean']),
            'spectral_smoothness_diff': abs(spectral_smoothness1 - spectral_smoothness2),
            'formant_stability_diff': abs(formant_stability1 - formant_stability2),
            'analysis1': analysis1,
            'analysis2': analysis2
        }
    except Exception as e:
        print(f"Error comparing AI patterns: {str(e)}")
        return None

def main():
    # Define paths to your audio files
    vocals_dir = "Vocals for Comparison"
    file1 = os.path.join(vocals_dir, "Touch Me Original Version.wav")
    file2 = os.path.join(vocals_dir, "Touch Me New Version.wav")

    # Compare AI patterns
    comparison = compare_ai_patterns(file1, file2)
    
    if comparison is not None:
        print("\nAI Voice Synthesis Analysis Results:")
        print("-----------------------------------")
        print(f"MFCC Similarity: {comparison['mfcc_similarity']:.4f}")
        print(f"Formant Similarity: {comparison['formant_similarity']:.4f}")
        print(f"Phase Coherence Difference: {comparison['phase_difference']:.4f}")
        print(f"Spectral Flatness Difference: {comparison['flatness_difference']:.4f}")
        print(f"Pitch Difference: {comparison['pitch_difference']:.2f} Hz")
        print(f"Spectral Smoothness Difference: {comparison['spectral_smoothness_diff']:.4f}")
        print(f"Formant Stability Difference: {comparison['formant_stability_diff']:.4f}")
        
        print("\nOriginal Voice Characteristics:")
        print(f"Duration: {comparison['analysis1']['duration']:.2f} seconds")
        print(f"Average Pitch: {comparison['analysis1']['pitch_mean']:.2f} Hz")
        print(f"Phase Coherence: {comparison['analysis1']['phase_coherence']:.4f}")
        print(f"Average Spectral Flatness: {np.mean(comparison['analysis1']['spectral_flatness']):.4f}")
        
        print("\nNew Voice Characteristics:")
        print(f"Duration: {comparison['analysis2']['duration']:.2f} seconds")
        print(f"Average Pitch: {comparison['analysis2']['pitch_mean']:.2f} Hz")
        print(f"Phase Coherence: {comparison['analysis2']['phase_coherence']:.4f}")
        print(f"Average Spectral Flatness: {np.mean(comparison['analysis2']['spectral_flatness']):.4f}")
        
        # Generate forensic report
        print("\nGenerating forensic report...")
        report_generator = ForensicReportGenerator()
        report_file = report_generator.generate_report(comparison, file1, file2)
        
        if report_file:
            print(f"\nForensic report generated successfully: {report_file}")
        else:
            print("\nError generating forensic report. Please check your OpenAI API key and try again.")

if __name__ == "__main__":
    main()