#!/usr/bin/env python3
"""
Create a pronunciation dictionary by combining base dictionary with G2P-generated pronunciations.
"""

import re
from pathlib import Path

def read_words_from_file(word_file):
    """Read words from file."""
    words = []
    with open(word_file, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().upper()
            if word:
                words.append(word)
    return words

def create_dictionary_from_transcripts(transcript_dir, output_file):
    """Create a dictionary file with words from transcripts."""
    words = set()
    
    # Extract all words from transcripts
    for txt_file in Path(transcript_dir).glob('*.txt'):
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read().upper()
        
        # Extract words
        word_list = re.findall(r'\b[A-Z]+\b', content)
        words.update(word_list)
    
    # Write to file for G2P
    word_list_file = Path(output_file).parent / "words_for_g2p.txt"
    with open(word_list_file, 'w', encoding='utf-8') as f:
        for word in sorted(words):
            f.write(f"{word}\n")
    
    print(f"Created word list: {word_list_file} ({len(words)} words)")
    return word_list_file, words

if __name__ == "__main__":
    transcript_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    output_dir = "/Users/pranavreddytalla/Desktop/Assignment"
    
    word_list_file, words = create_dictionary_from_transcripts(transcript_dir, output_dir)
    
    print(f"\nFound {len(words)} unique words in transcripts")
    print(f"\nTo generate pronunciations, run:")
    print(f"  mfa g2p {word_list_file} english_us_arpa {output_dir}/custom_dictionary.txt")

