def encoding(rna):
	#Create a codon dictionary
	bases = ['u', 'c', 'a', 'g']
	codontable = [a+b+c for a in bases for b in bases for c in bases]
	amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	codondict = dict(zip(codontable, amino_acids))
	
	#Create list of codons in RNA
	rna = rna.lower()
	codonfrags = [rna[i:i+3] for i in range(0, len(rna),3)]
	
	#Translate RNA to protein
	protein = ""
	for codon in codonfrags:
		protein += codondict[codon]
	return protein[:-1]

#Test
print encoding("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")