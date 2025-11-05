#!/usr/bin/env python3
"""
Improve transcripts for better MFA alignment:
- Remove punctuation
- Handle abbreviations
- Normalize text
- Keep original transcripts intact
"""

import re
from pathlib import Path

def normalize_transcript(text):
    """Normalize transcript for MFA dictionary lookup."""
    # Convert to uppercase (MFA dictionaries use uppercase)
    text = text.upper()
    
    # Handle specific abbreviations
    text = text.replace("S.J.C.", "SJC")
    text = text.replace("S.J.C", "SJC")
    text = text.replace("SJC'S", "SJC")
    text = text.replace("WBUR'S", "WBUR")
    
    # Remove all punctuation except spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip
    text = text.strip()
    
    return text

def improve_transcripts(source_dir, target_dir):
    """Improve transcripts and save to target directory."""
    source = Path(source_dir)
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    
    transcript_files = list(source.glob('*.txt'))
    
    print(f"Improving {len(transcript_files)} transcript files...\n")
    
    for txt_file in transcript_files:
        # Read original
        with open(txt_file, 'r', encoding='utf-8') as f:
            original = f.read()
        
        # Normalize
        normalized = normalize_transcript(original)
        
        # Write to target (same filename)
        output_file = target / txt_file.name
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(normalized)
        
        print(f"Improved: {txt_file.name}")
        print(f"  Original: {original[:70]}...")
        print(f"  Normalized: {normalized[:70]}...")
        print()
    
    print(f"✓ Improved {len(transcript_files)} transcript files.")
    return len(transcript_files)

if __name__ == "__main__":
    source_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    target_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    
    improve_transcripts(source_dir, target_dir)

