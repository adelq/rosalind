def hyp_square(inputstring):
	input_array = inputstring.split()
	return int(input_array[0])**2 + int(input_array[1])**2

#Test
print hyp_square("3 5")