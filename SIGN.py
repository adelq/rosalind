import itertools

def perm(posint):
	leads = []
	for i in range(1,posint+1):
		leads.append(i)
		leads.append(-i)
	print leads
	permlist = ([x for x in itertools.permutations(leads, posint)])
	
	all_solutions = []
	for element in permlist:
		flag=0
		for j in element:
			if ((j in element) & ((j*-1) in element)):
				flag = 1
				break
		if flag == 0:
			all_solutions.append(element)

	print len(all_solutions)
	for i in all_solutions:
		print ' '.join(map(str, i))

#Test
perm(4)