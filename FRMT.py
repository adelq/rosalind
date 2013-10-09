from Bio import Entrez
from Bio import SeqIO

def genbank(ids):
	Entrez.email = "adelq@sas.upenn.edu"
	ids = ids.replace(" ", ", ")

	# Fetch data from GenBank server
	handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
	records = list(SeqIO.parse(handle, "fasta"))

	# Find shortest string
	min = 9999999999
	id = 0
	for i in range(len(records)):
		if len(records[i].seq) < min:	
			min = len(records[i].seq)
			id = i

	# Printing
	print ">" + records[id].description
	print records[id].seq

# Tests
genbank("FJ817486 JX069768 JX469983")
