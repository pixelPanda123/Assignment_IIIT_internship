#!/usr/bin/env python3
"""
Script to normalize transcripts for better MFA alignment.
- Removes punctuation
- Converts to lowercase
- Expands common abbreviations
- Normalizes spacing
- Handles numbers and special cases
"""

import os
import re
from pathlib import Path

def expand_abbreviations(text):
    """Expand common abbreviations."""
    expansions = {
        "S.J.C.": "SJC",
        "S.J.C": "SJC",
        "SJC's": "SJC",
        "WBUR's": "WBUR",
        "WBUR": "W B U R",
    }
    for abbrev, expansion in expansions.items():
        text = text.replace(abbrev, expansion)
    return text

def normalize_text(text):
    """Normalize text for MFA."""
    # Convert to uppercase (MFA dictionaries often use uppercase)
    text = text.upper()
    
    # Expand abbreviations
    text = expand_abbreviations(text)
    
    # Remove punctuation but keep spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Handle numbers (e.g., "seventy" should stay as is, but "70" -> "seventy")
    # For now, we'll leave numbers as they appear in the transcript
    
    return text

def normalize_transcripts(source_dir, target_dir):
    """Normalize all transcript files."""
    source = Path(source_dir)
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    
    transcript_files = list(source.glob('*.txt')) + list(source.glob('*.TXT'))
    
    print(f"Normalizing {len(transcript_files)} transcript files...\n")
    
    for transcript_file in transcript_files:
        # Read original transcript
        with open(transcript_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Normalize
        normalized = normalize_text(content)
        
        # Create output filename
        base_name = transcript_file.stem
        output_file = target / f"{base_name}.txt"
        
        # Write normalized transcript
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(normalized)
        
        print(f"Normalized: {transcript_file.name}")
        print(f"  Original: {content[:80]}...")
        print(f"  Normalized: {normalized[:80]}...")
        print()
    
    print(f"Normalized {len(transcript_files)} transcript files.")
    return len(transcript_files)

if __name__ == "__main__":
    # Set paths
    source_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/transcripts"
    target_dir = "/Users/pranavreddytalla/Desktop/Assignment/data/corpus"
    
    # Normalize transcripts
    normalize_transcripts(source_dir, target_dir)
    
    # Also update corpus directory
    print("\nUpdating corpus directory...")
    for txt_file in Path(target_dir).glob("*.txt"):
        wav_file = Path("/Users/pranavreddytalla/Desktop/Assignment/data/audio") / f"{txt_file.stem}.wav"
        if wav_file.exists():
            print(f"  Corpus ready: {txt_file.stem}")

