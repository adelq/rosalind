def wabbits(n, k):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return wabbits(n-1, k) + k*wabbits(n-2, k)

#Test
print wabbits(5, 3)