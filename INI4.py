def oddsum(num1, num2):
	sumo = 0
	for i in range(num1, num2):
		if i % 2 != 0:
			sumo += i
	return sumo

#Test
print oddsum(100, 200)