from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC

def reversecomplement(dna):
	handle = SeqIO.parse(dna, "fasta")

	# Counter for matching reverse complements
	rvcomplement = 0
	for record in handle:
		if str(record.seq) == str(record.seq.reverse_complement()):
			rvcomplement += 1

	return rvcomplement

# Tests
print reversecomplement("fasta.txt")