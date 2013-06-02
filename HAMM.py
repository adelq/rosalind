def hamming(s, t):
	ham = 0
	for character in range(len(s)):
		if s[character] != t[character]:
			ham += 1
	return ham

#Test
print hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")