from Bio import SeqIO
import unittest

# List of base pairs that are considered transitions or transversions
transition_bases = [['A', 'G'], ['C', 'T']]
transversion_bases = [['A', 'C'], ['G', 'T']]

def ratio(x,y):
	assert len(x) == len(y)

	transition = 0
	transversion = 0

	for char in range(len(x)):
		if x[char] != y[char]:
			switched_bases = sorted([x[char], y[char]])
			if switched_bases in transition_bases:
				transition += 1
			else:
				transversion += 1

	return transition / transversion

def main(filename):
	fasta = SeqIO.parse(filename, "fasta")
	fasta = list(fasta)
	x = fasta[0].seq
	y = fasta[1].seq

	return ratio(x,y)

class TestTran(unittest.TestCase):
	def testTran(self):
		self.assertAlmostEqual(
			main("tran.txt"),
			1.21428571429)

if __name__ == "__main__":
	print(main("tran.txt"))
	unittest.main()