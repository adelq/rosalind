from Bio import SeqIO

def average(l):
	return sum(l) / float(len(l))

def qthreshold(threshold, fastq):
	# Create handle based on data in file
	handle = SeqIO.parse(fastq, "fastq")
	
	# Iterate through records and add to counter number that fail threshold
	belowthreshold = 0
	for record in handle:
		if average(record.letter_annotations["phred_quality"]) < threshold:
			belowthreshold += 1

	return belowthreshold

print qthreshold(17, "fastq.txt")