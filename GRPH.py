from collections import namedtuple
import itertools

Sequence = namedtuple('Sequence', ['label', 'seq'])


def parse_fasta(filename):
    f = open(filename)
    sequences = []
    label = ""
    sequence = ""
    for line in f:
        if line.startswith('>'):
            sequences.append(Sequence(label, sequence))
            label = line.strip()[1:]
            sequence = ""
        else:
            sequence += line.rstrip('\n')
    sequences.append(Sequence(label, sequence))
    return sequences[1:]


def is_k_overlap(s1, s2, k=3):
    return s1[-k:] == s2[:k]


def find_substring_set(sequences):
    edges = []
    for seq1, seq2 in itertools.permutations(sequences, 2):
        if is_k_overlap(seq1.seq, seq2.seq):
            edges.append(seq1.label + " " + seq2.label)
    return edges


def main(filename='test_grph.txt'):
    sequences = parse_fasta(filename)
    graph_set = find_substring_set(sequences)
    for fset in graph_set:
        print fset


if __name__ == '__main__':
    main()
