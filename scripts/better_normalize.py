#!/usr/bin/env python3
"""
Better normalization for transcripts - removes all punctuation, handles numbers, etc.
"""

import re
from pathlib import Path

def better_normalize(text):
    """Better normalization for MFA."""
    # Convert to uppercase
    text = text.upper()
    
    # Remove all punctuation except spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Handle numbers - convert written numbers to words if possible
    # For now, just keep them as digits or words
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip
    text = text.strip()
    
    return text

def normalize_all_transcripts(source_dir, target_dir):
    """Normalize all transcripts."""
    source = Path(source_dir)
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    
    transcript_files = list(source.glob('*.txt'))
    
    for txt_file in transcript_files:
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        normalized = better_normalize(content)
        
        output_file = target / txt_file.name
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(normalized)
        
        print(f"Normalized: {txt_file.name}")
        print(f"  {content[:60]}... -> {normalized[:60]}...")
    
    print(f"\nNormalized {len(transcript_files)} files.")

if __name__ == "__main__":
    source = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    target = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    
    normalize_all_transcripts(source, target)

