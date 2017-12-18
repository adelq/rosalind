from collections import Counter
from itertools import product


def kmer_counter(seq, k=4):
    """
    Calculate the number of each k-mer with fixed length k.

    :param seq: the input pattern sequence
    :param k: a fixed positive integer for the k-mer length
    :returns: list of the number of times the m-th k-mer appears in s
    """
    c = Counter()
    for i in range(len(seq) - k + 1):
        c[seq[i:i+k]] += 1

    kmer_counts = []
    kmer_gen = ("".join(s) for s in product("ACGT", repeat=k))
    for kmer in kmer_gen:
        kmer_counts.append(c[kmer])

    return kmer_counts


with open("/tmp/rosalind_kmer.txt", "r") as f:
    seq = "".join(f.read().strip().split('\n')[1:])
    print(kmer_counter(seq))
    with open("/tmp/rosalind_out.txt", "w") as fr:
        fr.write(" ".join(str(z) for z in kmer_counter(seq)))
