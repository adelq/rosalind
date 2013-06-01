def humptydumpty(inputstring):
	input_array = inputstring.split()
	inputstring = input_array[0]
	return inputstring[int(input_array[1]):1+int(input_array[2])] + " "  + inputstring[int(input_array[3]):1+int(input_array[4])]

#Test
print humptydumpty("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain. 22 27 97 102")