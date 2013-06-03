def mainparse(fasta):
	f = open(fasta, 'r')
	rawdna = ""
	for line in f:
		rawdna += line
	#Split file into fragments
	fragments = rawdna.split('\n')

	#Move id and fragments into separate arrays
	rosaid = []
	dnafrag = []
	for i in range(len(fragments)):
		if i % 2 == 0:
			rosaid.append(fragments[i])
		else:
			dnafrag.append(fragments[i])

	#Use helper function to print consensus
	consensus(dnafrag)

	#Use helper function to print profile
	profile(dnafrag)

def profile(fragmentarray):
	print profilecount(fragmentarray, "A")
	print profilecount(fragmentarray, "C")
	print profilecount(fragmentarray, "G")
	print profilecount(fragmentarray, "T")

def profilecount(fragmentarray, base):
	basecount = base + ":"
	for stringslice in range(len(fragmentarray[0])):
		count = 0
		for frag in fragmentarray:
			if frag[stringslice] == base:
				count += 1
		basecount += " "
		basecount += str(count)
	return basecount

def consensus(fragmentarray):
	basemax = []
	for i in range(len(fragmentarray[0])):
		basemax.append(consensuscount(fragmentarray, i))
	consensusstring = ""
	for base in basemax:
		if base == 0:
			consensusstring += "A"
		if base == 1:
			consensusstring += "C"
		if base == 2:
			consensusstring += "G"
		if base == 3:
			consensusstring += "T"
	print consensusstring

def consensuscount(fragmentarray, position):
	basecount = [0, 0, 0, 0]
	for frag in fragmentarray:
		if frag[position] == "A":
			basecount[0] += 1
		if frag[position] == "C":
			basecount[1] += 1
		if frag[position] == "G":
			basecount[2] += 1
		if frag[position] == "T":
			basecount[3] += 1
	return basecount.index(max(basecount))

#Test
mainparse("rosalind_cons.txt")