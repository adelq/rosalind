from itertools import product

def main(alpha, num):
	orderedalpha = alpha.replace(" ", "")
	
	# Generate all the permutations
	permtuple = []
	for i in range(1, num+1):
		permtuple += ([x for x in product(orderedalpha, repeat=i)])

	# Output permutations properly formatted
	permlist = []
	for i in permtuple:
		permlist += ''.join(map(str, i))
	print permlist

# Test
main("D N A", 3)