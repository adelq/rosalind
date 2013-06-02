def reversecomplement(dna):
	reversedna = dna[::-1]
	complement = reversedna.replace('A', 't').replace('T','a').replace('G', 'c').replace('C', 'g').upper()
	return complement

#Test
print reversecomplement("AAAACCCGGT")
