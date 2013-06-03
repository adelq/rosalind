import itertools

def perm(posint):
	leads = ''
	for i in range(1,posint+1):
		leads += str(i)
	permlist = ([x for x in itertools.permutations(leads)])
	print len(permlist)
	for i in permlist:
		print ' '.join(map(str, i))

#Test
perm(3)