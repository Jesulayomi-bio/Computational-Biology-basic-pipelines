"""
Pairwise alignment and determine the % of similariteis and difference 
"""

from Bio.Align import PairwiseAligner 
from Bio import SeqIO


aligner = PairwiseAligner()
aligner.mode = "local"
 
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -0.5
aligner.extend_gap_score = -1

# seq1 - A/20 and seq2 - A/22

record1_iterator = SeqIO.parse("C:/Users/Jesulayomi/Downloads/sequence (4).gb", "genbank")    #extract file 
record2_iterator = SeqIO.parse("C:/Users/Jesulayomi/Downloads/sequence (5).gb", "genbank")    #extract file
# get details of organism
seq1 = next(record1_iterator)
seq1_name = seq1.annotations["keywords"]    #get organism keywords 
seq2 = next(record2_iterator)
seq2_name = seq2.annotations["keywords"]    #get organism keywords

# get organism sequence 
seq1_seq = seq1.seq
seq2_seq = seq2.seq



alignment = aligner.align(seq1_seq,seq2_seq)[0]
print(alignment)

# get alignment seq
aligned_seq1 = alignment[0]
aligned_seq2 = alignment[1]


# get matches and alignment length

matches = 0
mismatch = 0
for a,b in zip(aligned_seq1,aligned_seq2):
    if a == b:
        matches += 1
    elif a != b:
        mismatch += 1

print(matches)
print(mismatch)

align_len = matches + mismatch

similarity = 100 * matches/align_len

print(f"Similarity: {seq1_name} is {similarity:.1f}% similar with {seq2_name}")