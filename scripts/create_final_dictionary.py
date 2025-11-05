#!/usr/bin/env python3
"""
Create a final custom dictionary by getting OOV words and generating pronunciations.
"""

import subprocess
import sys
from pathlib import Path

def get_oov_words():
    """Get OOV words from MFA validation."""
    oov_file = Path("/Users/pranavreddytalla/Documents/MFA/corpus/oovs_found.txt")
    if oov_file.exists():
        with open(oov_file, 'r', encoding='utf-8') as f:
            words = [line.strip().upper() for line in f if line.strip()]
        return words
    return []

def create_custom_dictionary(oov_words, output_file):
    """Create custom dictionary with OOV words."""
    if not oov_words:
        print("No OOV words found. Using base dictionary.")
        return None
    
    # Write OOV words to file
    word_list_file = Path(output_file).parent / "oov_words.txt"
    with open(word_list_file, 'w', encoding='utf-8') as f:
        for word in sorted(oov_words):
            f.write(f"{word}\n")
    
    print(f"Found {len(oov_words)} OOV words: {', '.join(oov_words[:20])}...")
    print(f"Created word list: {word_list_file}")
    
    # Generate pronunciations using G2P
    try:
        print(f"\nGenerating pronunciations using G2P...")
        result = subprocess.run(
            ['mfa', 'g2p', str(word_list_file), 'english_us_arpa', output_file],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        print(f"Generated dictionary: {output_file}")
        
        # Check if file was created
        if Path(output_file).exists() and Path(output_file).stat().st_size > 0:
            print(f"✓ Custom dictionary created successfully!")
            return output_file
        else:
            print("⚠ Dictionary file is empty")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error generating dictionary: {e}")
        print(e.stderr)
        return None

if __name__ == "__main__":
    # Get OOV words
    oov_words = get_oov_words()
    
    if oov_words:
        output_file = "/Users/pranavreddytalla/Desktop/Assignment/custom_dict_final.txt"
        result = create_custom_dictionary(oov_words, output_file)
        
        if result:
            print(f"\n✓ Custom dictionary ready: {result}")
            print(f"  Contains pronunciations for {len(oov_words)} OOV words")
    else:
        print("No OOV words to process. Base dictionary should be sufficient.")

