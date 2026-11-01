# Computational-Biology-basic-pipelines
I am an aspiring computational biologist, these are basic pipelines I created while growing.


## align and % similarity.py
### Biopython Pairwise Sequence Alignment Tool
This Python script performs a local pairwise sequence alignment between two biological sequences extracted from GenBank files using the Biopython library. It calculates the similarity percentage and highlights differences between the two sequences (e.g., influenza strains A/20 and A/22).

**Prerequisites & Dependencies:** Make sure you have Biopython installed in your Python environment: *pip install biopython*

🚀 **How the Code Works**
[] Initialization (PairwiseAligner):
Sets up a local alignment aligner.
Configures scoring parameters:
  Match score: 1 (rewards matching bases)
  Mismatch score: -1 (penalizes differing bases)
  Open gap score: -0.5 (penalty for starting a gap)
  Extend gap score: -1 (penalty for extending an existing gap)

[] Sequence Extraction (SeqIO):
Parses two GenBank files (sequence (4).gb and sequence (5).gb).
Extracts metadata (such as organism keywords/names) and the actual nucleotide/protein sequences (seq1.seq and seq2.seq).

[] Alignment & Analysis:
Runs aligner.align() to find the optimal local alignment between the two sequences and selects the top alignment result ([0]).
Iterates through the aligned sequences position-by-position to count matches and mismatches.

[] Similarity Calculation:
Computes the percentage similarity using the formula:$$\text{Similarity (\%)} = \left(\frac{\text{Matches}}{\text{Total Alignment Length}}\right) \times 100$$Prints out the final alignment, match/mismatch counts, and a formatted similarity statement.
