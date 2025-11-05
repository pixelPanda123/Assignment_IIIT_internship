#!/usr/bin/env python3
"""
Extract all unique words from transcripts for G2P pronunciation generation.
"""

import re
from pathlib import Path

def extract_words(transcript_dir):
    """Extract all unique words from transcripts."""
    words = set()
    
    for txt_file in Path(transcript_dir).glob('*.txt'):
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read().upper()
        
        # Extract words (only alphabetic)
        word_list = re.findall(r'\b[A-Z]+\b', content)
        words.update(word_list)
    
    return sorted(words)

if __name__ == "__main__":
    transcript_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    output_file = "/Users/pranavreddytalla/Desktop/Assignment/oov_words.txt"
    
    words = extract_words(transcript_dir)
    
    print(f"Extracted {len(words)} unique words from transcripts")
    print(f"Sample: {', '.join(words[:20])}...")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in words:
            f.write(f"{word}\n")
    
    print(f"\n✓ Word list saved to: {output_file}")
    print(f"\nNext: Generate pronunciations using G2P")
    print(f"  mfa g2p {output_file} english_us_arpa custom_dict.txt")

