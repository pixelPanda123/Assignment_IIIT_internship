#!/usr/bin/env python3
"""
Script to merge custom dictionary with base dictionary.
"""

from pathlib import Path

def merge_dictionaries(base_dict_path, custom_dict_path, output_path):
    """Merge base dictionary with custom dictionary."""
    # Read base dictionary
    base_words = {}
    if Path(base_dict_path).exists():
        with open(base_dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split(None, 1)
                    if len(parts) >= 2:
                        word = parts[0].upper()
                        pron = parts[1]
                        base_words[word] = pron
    
    print(f"Base dictionary: {len(base_words)} entries")
    
    # Read custom dictionary
    custom_words = {}
    if Path(custom_dict_path).exists():
        with open(custom_dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split(None, 1)
                    if len(parts) >= 2:
                        word = parts[0].upper()
                        pron = parts[1]
                        custom_words[word] = pron
    
    print(f"Custom dictionary: {len(custom_words)} entries")
    
    # Merge (custom overrides base)
    merged = {**base_words, **custom_words}
    
    print(f"Merged dictionary: {len(merged)} entries")
    
    # Write merged dictionary
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in sorted(merged.keys()):
            f.write(f"{word}\t{merged[word]}\n")
    
    print(f"Saved merged dictionary to: {output_path}")
    return len(merged)

if __name__ == "__main__":
    # We'll use the custom dictionary directly since english_us_arpa is built-in
    # Just validate the custom dictionary format
    custom_dict = Path("/Users/pranavreddytalla/Desktop/Assignment/custom_dictionary.txt")
    
    if custom_dict.exists():
        print(f"Custom dictionary created: {custom_dict}")
        print(f"Entries: {sum(1 for _ in open(custom_dict))}")
        print("\nFirst 10 entries:")
        with open(custom_dict, 'r') as f:
            for i, line in enumerate(f):
                if i >= 10:
                    break
                print(f"  {line.strip()}")

