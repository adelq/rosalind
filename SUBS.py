def hay(s, t):
	repeatlist = [n for n in xrange(len(s)) if s.find(t, n) == n]
	repeats = ""
	for i in repeatlist:
		repeats += str(i + 1) + " "
	return repeats[:-1]

#Test
print hay("GATATATGCATATACTT", "ATAT")