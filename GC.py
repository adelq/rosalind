def calculategc(dna):
	gc = 0.0
	for i in dna:
		if i == "G":
			gc += 1.0
		if i == "C":
			gc += 1.0
	gc = gc/len(dna)*100
	return gc

def gccontent(fasta):
	f = open(fasta, 'r')
	rawdna = ""
	for line in f:
		rawdna += line
	#Split file into fragments
	fragments = rawdna.split('\n')
	fragmentgc = []
	#Calculate the GC for each fragment
	for i in range(len(fragments)):
		fragmentgc.append(calculategc(fragments[i]))
	#Return the label, aka index-1 of the fragment with max GC
	print fragments[fragmentgc.index(max(fragmentgc))-1].strip('>')
	print max(fragmentgc)
	#f = open('ini5_output.txt', 'w')
	#f.write(blablabla)
	#f.close()

#Test
gccontent('rosalind_gc.txt')