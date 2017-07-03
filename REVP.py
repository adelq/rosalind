from __future__ import print_function
from Bio import SeqIO

def reverse_palindrome(s):
    for i in range(len(s)):
        for l in range(4, 13):
            if i + l > len(s):
                continue

            s1 = s[i:i+l]
            s2 = s1.reverse_complement()

            if s1.seq == s2.seq:
                print("%s %s" % (i + 1, l))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_seq = next(SeqIO.parse(f, "fasta"))
    reverse_palindrome(input_seq)
