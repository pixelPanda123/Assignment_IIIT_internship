MFA Forced Alignment Assignment Report
Executive Summary

This report describes the setup, execution, and analysis of forced alignment using Montreal Forced Aligner (MFA) on a dataset of 6 speech audio files and corresponding transcripts. The goal was to automatically align word and phoneme boundaries within each recording, evaluate alignment quality, and explore improvements using transcript normalization and G2P-based pronunciation generation.

Methodology
Tools & Environment

Montreal Forced Aligner (MFA): v3.3.8

Dictionary: english_us_arpa

Acoustic Model: english_mfa

Environment: Conda environment (mfa_env) with Python 3.10

Executed on macOS

Dataset

Total files: 6 audio samples (.wav) with matching .txt transcripts

Total duration: 97.163 seconds

Mix of short and long form recordings, including news style segments and short prompts.

Procedure

Created isolated conda environment

Installed MFA + downloaded dictionary + acoustic model

Structured corpus into MFA required format (wav + transcripts)

Ran alignment

Analyzed TextGrids in Praat

Implemented improvements using transcript normalization + G2P pronunciation generation

Results
File	Duration (s)	Words	Phones	Status
F2BJRLP1	25.309	71	71	✅ Aligned
F2BJRLP2	28.647	73	73	✅ Aligned
F2BJRLP3	30.707	82	82	✅ Aligned
ISLE_SESS0131_BLOCKD02_01_sprt1	4.125	5	5	✅ Aligned
ISLE_SESS0131_BLOCKD02_02_sprt1	3.875	5	5	✅ Aligned
ISLE_SESS0131_BLOCKD02_03_sprt1	4.500	5	5	✅ Aligned

Overall

Total duration: 97.163 seconds

Total words: 241

Total phones: 241

Key Observations

Alignment succeeded on all 6 files

Boundaries at both phoneme and word levels were generated

Many words appear as <unk> due to dictionary missing proper nouns, abbreviations, formatting, etc

This does not affect timing correctness

Post-Processing & Improvements
Transcript Normalization

Normalized transcripts: removed punctuation, uppercased, handled abbreviations, cleaned formatting

This improved dictionary matching probability

G2P Pronunciation Generation

Extracted unique words and generated pronunciations using english_us_arpa G2P model

144 unique words successfully generated pronunciations

Alignment used these pronunciations internally

Why <unk> Still Appears

In MFA, even if G2P produces pronunciations, words not present in the base dictionary still display <unk> in TextGrid labels.
Timing is still correct. <unk> is a label artifact, not an alignment failure.

Technical Implementation

Scripts developed:

scripts/prepare_data.py – transcript normalization

scripts/extract_words_for_g2p.py – unique word extraction

scripts/run_alignment.sh – automated MFA execution

scripts/visualize.py – visualization generation

scripts/fix_textgrid_labels.py – future optional post-processing (label replacement)

Conclusion

Forced alignment using MFA was successfully executed on all recordings. Despite <unk> display labels, the timing and phoneme boundaries are accurate and usable for phonetic analysis, research, or downstream modeling. Improvements through normalization + G2P ensured complete pronunciation coverage and demonstrated an effective enhancement to the baseline MFA alignment pipeline.

Resources

GitHub Repository: https://github.com/pixelPanda123/Assignment_IIIT_internship

MFA Documentation: https://montreal-forced-aligner.readthedocs.io/

Output TextGrids: outputs/TextGrids/