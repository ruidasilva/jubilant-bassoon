import os
from datetime import datetime
import numpy as np
from transformers import pipeline

class ForensicReportGenerator:
    def __init__(self):
        # Initialize the text generation pipeline with a suitable model
        self.generator = pipeline('text-generation', 
                                model='mistralai/Mistral-7B-Instruct-v0.2',
                                device=-1)  # Use CPU
        
    def generate_report(self, comparison_results, file1_path, file2_path):
        """
        Generate a professional forensic report using local AI.
        
        Args:
            comparison_results (dict): Results from voice comparison analysis
            file1_path (str): Path to original audio file
            file2_path (str): Path to new audio file
            
        Returns:
            str: Generated report in markdown format
        """
        # Prepare the analysis data
        analysis_data = {
            'original_file': os.path.basename(file1_path),
            'new_file': os.path.basename(file2_path),
            'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'metrics': {
                'mfcc_similarity': comparison_results['mfcc_similarity'],
                'formant_similarity': comparison_results['formant_similarity'],
                'phase_difference': comparison_results['phase_difference'],
                'flatness_difference': comparison_results['flatness_difference'],
                'pitch_difference': comparison_results['pitch_difference'],
                'spectral_smoothness_diff': comparison_results['spectral_smoothness_diff'],
                'formant_stability_diff': comparison_results['formant_stability_diff']
            },
            'original_characteristics': {
                'duration': comparison_results['analysis1']['duration'],
                'pitch_mean': comparison_results['analysis1']['pitch_mean'],
                'phase_coherence': comparison_results['analysis1']['phase_coherence'],
                'spectral_flatness': float(np.mean(comparison_results['analysis1']['spectral_flatness']))
            },
            'new_characteristics': {
                'duration': comparison_results['analysis2']['duration'],
                'pitch_mean': comparison_results['analysis2']['pitch_mean'],
                'phase_coherence': comparison_results['analysis2']['phase_coherence'],
                'spectral_flatness': float(np.mean(comparison_results['analysis2']['spectral_flatness']))
            }
        }
        
        # Create the prompt for the AI
        prompt = f"""<s>[INST] You are a professional forensic audio analyst. Generate a detailed forensic report based on the following analysis data:

Analysis Date: {analysis_data['analysis_date']}
Original File: {analysis_data['original_file']}
New File: {analysis_data['new_file']}

Analysis Metrics:
- MFCC Similarity: {analysis_data['metrics']['mfcc_similarity']:.4f}
- Formant Similarity: {analysis_data['metrics']['formant_similarity']:.4f}
- Phase Coherence Difference: {analysis_data['metrics']['phase_difference']:.4f}
- Spectral Flatness Difference: {analysis_data['metrics']['flatness_difference']:.4f}
- Pitch Difference: {analysis_data['metrics']['pitch_difference']:.2f} Hz
- Spectral Smoothness Difference: {analysis_data['metrics']['spectral_smoothness_diff']:.4f}
- Formant Stability Difference: {analysis_data['metrics']['formant_stability_diff']:.4f}

Original Voice Characteristics:
- Duration: {analysis_data['original_characteristics']['duration']:.2f} seconds
- Average Pitch: {analysis_data['original_characteristics']['pitch_mean']:.2f} Hz
- Phase Coherence: {analysis_data['original_characteristics']['phase_coherence']:.4f}
- Average Spectral Flatness: {analysis_data['original_characteristics']['spectral_flatness']:.4f}

New Voice Characteristics:
- Duration: {analysis_data['new_characteristics']['duration']:.2f} seconds
- Average Pitch: {analysis_data['new_characteristics']['pitch_mean']:.2f} Hz
- Phase Coherence: {analysis_data['new_characteristics']['phase_coherence']:.4f}
- Average Spectral Flatness: {analysis_data['new_characteristics']['spectral_flatness']:.4f}

Please generate a professional forensic report in markdown format that includes:
1. Executive Summary
2. Analysis Methodology
3. Detailed Findings
4. Technical Analysis
5. Conclusion
6. Recommendations

The report should be accessible to both technical and non-technical readers. [/INST]</s>"""

        try:
            # Generate the report using the local model
            response = self.generator(prompt, 
                                    max_length=2000,
                                    num_return_sequences=1,
                                    temperature=0.7,
                                    do_sample=True,
                                    pad_token_id=self.generator.tokenizer.eos_token_id)
            
            # Extract the generated report
            report = response[0]['generated_text']
            
            # Clean up the report by removing the prompt
            report = report.replace(prompt, '').strip()
            
            # Save the report to a file
            report_filename = f"forensic_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(report_filename, 'w') as f:
                f.write(report)
            
            return report_filename
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return None 