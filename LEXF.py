from itertools import product

def main(alpha, num):
	orderedalpha = alpha.replace(" ", "")
	permlist = ([x for x in product(orderedalpha, repeat=num)])
	for i in permlist:
		print ''.join(map(str, i))

# Test
main("T A G C", 2)

main("N G H F I U J", 3)