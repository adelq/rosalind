from Bio.Seq import Seq

def basecount(dna):
	sequence = Seq(dna)
	print str(sequence.count("A")) + " " + str(sequence.count("C")) + " " + str(sequence.count("G")) + " " + str(sequence.count("T"))

# Test
basecount("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")