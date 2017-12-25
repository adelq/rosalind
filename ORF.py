import re
from Bio import SeqIO

ORF_REGEX = re.compile(r"(?=(M\w*\*))")


def orf_finder(seq):
    orfs = set()
    for strand, nuc in [(1, seq.seq), (-1, seq.seq.reverse_complement())]:
        for frame in range(3):
            length = 3 * ((len(seq) - frame) // 3)
            translated = str(nuc[frame:frame+length].translate())
            for pro in ORF_REGEX.finditer(translated):
                orfs.add(pro.group(1)[:-1])
    return orfs


def main():
    orfs = orf_finder(SeqIO.read("/tmp/rosalind_orf.txt", "fasta"))
    for orf in orfs:
        print(orf)
