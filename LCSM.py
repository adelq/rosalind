def parse(fasta):
	f = open(fasta, 'r')
	rawdna = ""
	for line in f:
		rawdna += line
	#Split file into fragments
	fragments = rawdna.split('\n')

	#Move fragments into separate array
	dnafrag = []
	for i in range(len(fragments)):
		if i % 2 != 0:
			dnafrag.append(fragments[i])
	return dnafrag

def parse_fasta(filename):
    f = open(filename)
    sequences = {}
    for line in f:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences[name] = ''
        else:
            sequences[name] = sequences[name] + line.rstrip('\n')
    return sequences.values()

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

#Test
print long_substr(parse_fasta('rosalind_lcsm.txt'))