#!/usr/bin/env python3
"""
Script to create a custom dictionary from transcripts.
Extracts unique words and uses MFA's G2P model to generate pronunciations.
"""

import os
import re
from pathlib import Path

def extract_words_from_transcripts(transcript_dir):
    """Extract all unique words from transcripts."""
    words = set()
    transcript_files = list(Path(transcript_dir).glob('*.txt'))
    
    for transcript_file in transcript_files:
        with open(transcript_file, 'r', encoding='utf-8') as f:
            content = f.read().upper()
        
        # Split into words
        word_list = re.findall(r'\b[A-Z]+\b', content)
        words.update(word_list)
    
    return sorted(words)

def create_dictionary_file(words, output_path):
    """Create a dictionary file with words."""
    # Write words to a file (one per line) for G2P generation
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in words:
            f.write(f"{word}\n")
    
    print(f"Created word list with {len(words)} unique words: {output_path}")
    return output_path

if __name__ == "__main__":
    transcript_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    output_file = "/Users/pranavreddytalla/Desktop/Assignment/custom_words.txt"
    
    # Extract words
    print("Extracting words from transcripts...")
    words = extract_words_from_transcripts(transcript_dir)
    
    print(f"\nFound {len(words)} unique words:")
    print(f"Sample words: {', '.join(words[:20])}")
    
    # Create word list file
    create_dictionary_file(words, output_file)
    
    print(f"\nWord list saved to: {output_file}")
    print("\nNext step: Generate pronunciations using MFA G2P model:")
    print(f"  mfa g2p english_us_arpa {output_file} custom_dictionary.txt")

