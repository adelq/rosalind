from math import log10

def probability(dna, probarray):
	""" Not sure if needed at all
	#Calculate GC-content of original DNA using helper function
	gco = calculategc(dna)*0.5
	ato = (1-(gco*2))*0.5 """
	
	#Parse probability array
	probarray = map(float, probarray.split())

	#Calculate probability of DNA happening randomly
	randomchance = []
	
	for percentage in probarray:
		chancedna = 1.0
		gc = percentage*0.5
		at = (1-(gc*2))*0.5
		
		for char in dna:
			if char == "A":
				chancedna *= at
			if char == "T":
				chancedna *= at
			if char == "G":
				chancedna *= gc
			if char == "C":
				chancedna *= gc
		randomchance.append(log10(chancedna))
	return " ".join(map(str, randomchance))

def calculategc(dna):
	gc = 0.0
	for i in dna:
		if i == "G":
			gc += 1.0
		if i == "C":
			gc += 1.0
	gc = gc/len(dna)
	return gc

#Test
print probability("ACGATACAA", "0.129 0.287 0.423 0.476 0.641 0.742 0.783")