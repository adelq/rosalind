def symbolscount(dna):
	A = 0
	G = 0
	C = 0
	T = 0
	for i in dna:
		if i == "A":
			A += 1
		if i == "T":
			T += 1
		if i == "G":
			G += 1
		if i == "C":
			C += 1
	return str(A) + " " + str(C) + " " + str(G) + " " + str(T)

#Test
print symbolscount("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")