def modfind(protein):
	#Create a codon frequency dictionary
	poscodons = {'A': 4,'C': 2,'D': 2,'E': 2,'F': 2,'G': 4,'H': 2,'I': 3,'K': 2,'L': 6,'M': 1,'N': 2,'P': 4,'Q': 2,'R': 6,'S': 6,'T': 4,'V': 4,'W': 1,'Y': 2}
	possiblerna = 1
	for aminoacid in protein:
		possiblerna *= poscodons[aminoacid]
	return 3*possiblerna % 1000000

# Test
print modfind("MA")