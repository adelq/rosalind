from Bio import Entrez

def refseq(species, a, b, date):
	Entrez.email = "adelq@sas.upenn.edu"
	term = '%s[Organism] AND (%s[Sequence Length] : %s[Sequence Length]) AND (1000/01/01[Publication Date] : %s[Publication Date]) AND srcdb_refseq[PROP]' % (species, a, b, date)
	handle = Entrez.esearch(db="nucleotide", term=term)
	record = Entrez.read(handle)
	return record["Count"]

# Test
print refseq("Glycine max", "500", "800", "2012/12/27")
# Problem given
print refseq("Pectobacterium", "841", "993", "2012/03/12")