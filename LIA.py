def independence(k, n):
	children = 2**k
	n -= 1
	return 1 - prob(n, 0.25, children)

def factorial(n): 
	if n < 2: return 1
	return reduce(lambda x, y: x*y, xrange(2, int(n)+1))

def prob(s, p, n):
	x = 1.0 - p

	a = n - s
	b = s + 1

	c = a + b - 1

	prob = 0

	for j in xrange(a, c + 1):
		prob += factorial(c) / (factorial(j)*factorial(c-j)) \
				* x**j * (1 - x)**(c-j)

	return prob

# Test
print independence(2, 1)

print independence(6, 19)