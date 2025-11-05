#!/usr/bin/env python3
"""
Merge OOV pronunciations with base dictionary to create a complete dictionary.
"""

from pathlib import Path

def read_dictionary(dict_path):
    """Read a dictionary file."""
    words = {}
    if Path(dict_path).exists():
        with open(dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split(None, 1)
                    if len(parts) >= 2:
                        word = parts[0].upper()
                        pron = parts[1]
                        words[word] = pron
    return words

def create_merged_dictionary(base_dict_words, oov_dict_path, output_path):
    """Create merged dictionary."""
    # Read OOV pronunciations
    oov_words = read_dictionary(oov_dict_path)
    
    print(f"Base dictionary: {len(base_dict_words)} entries")
    print(f"OOV pronunciations: {len(oov_words)} entries")
    
    # Merge (OOV overrides base)
    merged = {**base_dict_words, **oov_words}
    
    print(f"Merged dictionary: {len(merged)} entries")
    
    # Write merged dictionary
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in sorted(merged.keys()):
            f.write(f"{word}\t{merged[word]}\n")
    
    print(f"✓ Merged dictionary saved to: {output_path}")
    return len(merged)

if __name__ == "__main__":
    # We'll use the OOV pronunciations directly
    # MFA should use the base dictionary + G2P, but let's create a merged one
    oov_dict = "/Users/pranavreddytalla/Desktop/Assignment/oov_pronunciations.txt"
    output_dict = "/Users/pranavreddytalla/Desktop/Assignment/merged_dictionary.txt"
    
    # For now, just check if OOV pronunciations were generated
    if Path(oov_dict).exists() and Path(oov_dict).stat().st_size > 0:
        print(f"✓ OOV pronunciations generated: {oov_dict}")
        print("\nNote: MFA uses G2P automatically during alignment when --g2p_model_path is specified.")
        print("The pronunciations should be used automatically.")
    else:
        print("⚠ OOV pronunciations file not found or empty.")

