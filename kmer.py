import Bio
from Bio import SeqIO

#read in reads from a fastq file, as mostly outputted by a sequencer

reads=[]

for seq_record in SeqIO.parse('reads.fq', "fastq"):
    
    reads.append(str(seq_record.seq))

def build_k_mer(str,k):
    return [str[i:k+i] for i in range(0,len(str)-k+1)]

k_mer_len=20

for i in reads:
    kmers=[]
    kmers=kmers+build_k_mer(i,k_mer_len(20))

#read out file to kmers to feed to a kmer based assembler
