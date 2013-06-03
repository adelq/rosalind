def mendel(k, m, n):
	n += 0.0
	k += 0.0
	m += 0.0
	n += 0.0
	population = k + m + n
	population += 0.0

	#Selecting homozygous dominant first
	dom1 = (k/population)
	
	#Selecting heterozygous first
	het1dom2 = (m/population)*(k/(population-1))
	het1het2 = (m/population)*((m-1)/(population-1))*(0.75)
	het1rec2 = (m/population)*(n/(population-1))*(0.5)
	het1 = het1dom2 + het1het2 + het1rec2

	#Selecting recessive first
	rec1dom2 = (n/population)*(k/(population-1))
	rec1het2 = (n/population)*(m/(population-1))*(0.5)
	rec1 = rec1dom2 + rec1het2

	return dom1 + het1 + rec1

#Test
print mendel(2, 2, 2)