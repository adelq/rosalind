from Bio import SeqIO

def converter(fastq):
	SeqIO.convert(fastq, "fastq", "tfsq_fasta.txt", "fasta")

# Test
converter('fastq.txt')