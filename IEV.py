def offspring(hdhd, hdht, hdhr, htht, hthr, hrhr):
	population = hdhd + hdht + hdhr + htht + hthr + hrhr
	freqdom = hdhd + hdht + hdhr + 0.75*htht + 0.5*hthr
	return freqdom*2

#Test
print offspring(1, 0, 0, 1, 0, 1)