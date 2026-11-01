# Computational-Biology-basic-pipelines
I am an aspiring computational biologist, these are basic pipelines I created while growing.


## align and % similarity.py
### Biopython Pairwise Sequence Alignment Tool
This Python script performs a local pairwise sequence alignment between two biological sequences extracted from GenBank files using the Biopython library. It calculates the similarity percentage and highlights differences between the two sequences (e.g., influenza strains A/20 and A/22).

**Prerequisites & Dependencies:** Make sure you have Biopython installed in your Python environment: *pip install biopython*

🚀 **How the Code Works**

- [ ] Initialization (PairwiseAligner):

> Sets up a local alignment aligner.

> Configures scoring parameters:
>> Match score: 1 (rewards matching bases)
>> Mismatch score: -1 (penalizes differing bases)
>> 
>> Open gap score: -0.5 (penalty for starting a gap)
>> 
>> Extend gap score: -1 (penalty for extending an existing gap)

- [ ] Sequence Extraction (SeqIO):

> Parses two GenBank files (sequence (4).gb and sequence (5).gb).

> Extracts metadata (such as organism keywords/names) and the actual nucleotide/protein sequences (seq1.seq and seq2.seq).

- [ ] Alignment & Analysis:
      
> Runs aligner.align() to find the optimal local alignment between the two sequences and selects the top alignment result ([0]).

> Iterates through the aligned sequences position-by-position to count matches and mismatches.

- [ ] Similarity Calculation:
      
> Computes the percentage similarity using the formula:

$$\text{Similarity (\%)} = \left(\frac{\text{Matches}}{\text{Total Alignment Length}}\right) \times 100$$

> Prints out the **final alignment**, **match/mismatch counts**, and a **formatted similarity statement**.


## motif search.py
### FASTA/GenBank Parser & Nucleotide Motif Searcher
This Python script allows users to interactively parse either a FASTA or GenBank sequence file, extract key metadata and sequence information, and search for specific nucleotide motifs using regular expressions (re).

**Prerequisites & Dependencies:** Make sure you have Biopython installed in your Python environment: *pip install biopython*

🚀 **How the Code Works**

- [ ] User Interaction & File Loading::

> Prompts the user to specify the file format (f for FASTA, g for GenBank).
>
> Prompts the user to provide the file path.
>
> Uses Biopython's SeqIO.parse() to read the file based on the user's format selection.

- [ ] Metadata & Sequence Extraction:

> Loops through the records in the file.
>
>Extracts and prints the organism's name and source from the record annotations.
>
>Converts the sequence into a string representation using repr().

- [ ] Motif Searching:

> Prompts the user to enter a nucleotide motif (regular expression pattern).

> Uses Python's *re.search()* to scan the sequence for the target motif.

> If found, it prints confirmation and displays the start and end character positions (*m.start()* and *m.end()*). If not found, it reports that the motif is absent.
