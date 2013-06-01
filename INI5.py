def oddlines(filename):
	f = open(filename, 'r')
	story = f.readlines()
	novel = []
	for line in range(len(story)):
		if line % 2 != 0:
			novel.append(story[line])
	novella = ""
	for item in novel:
		novella += item
	print novella
	f = open('ini5_output.txt', 'w')
	f.write(novella)
	f.close()

#Test
oddlines('ini5_input.txt')
