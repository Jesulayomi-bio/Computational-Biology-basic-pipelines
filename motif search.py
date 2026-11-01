"""
parse fasta files or genbank files: extract certain information and search for nucleotides motif
"""
from Bio import SeqIO
import re

user_input = input("for fasta file - (f), for genbank file - (g)  ")  #decison 
file_path = input("paste file path  ")  #data location

file = ""
if user_input == "f":
    file = SeqIO.parse(file_path, "fasta")  #fasta code
elif user_input == "g":
    file = SeqIO.parse(file_path,"genbank")  #genbank code
else:
    print("Incorrect input")
        
# C:/users/jesulayomi/Downloads/sequence (2).gb
sequence = ""
for record in file:
    name = record.annotations["organism"]  #data name
    source = record.annotations["source"]  #data source
    sequence = repr(record.seq)  #data sequence
    print(f"Name: {name}")  #print data     
    print(f"Source: {source}")  #print  data source
    
    # search for motiffs in the sequence
print(sequence)  #print sequence
user_motif = input("Input motif:  ")  #input motif

if re.search(user_motif,sequence):  #search motif
    m = re.search(user_motif,sequence)
    print("motif present")  
    print(f"motiff location: {m.start()} - {m.end()}")  #motif location in the sequence
else:
    print("motif abscent")