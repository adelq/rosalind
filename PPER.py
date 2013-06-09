from math import factorial

def number_permutations(n, k):
	return factorial(n)/factorial(n-k) % 1000000

# Test
print number_permutations(21, 7)