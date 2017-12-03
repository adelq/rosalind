from Bio.Seq import Seq


def find_max_orf(seq):
    """
    Find the longest protein string that can be translated from the ORF of seq.
    """
    bseq = Seq(seq)
    rbseq = bseq.reverse_complement()
    biggest_orf = ""
    biggest_orf_len = 0
    for s in bseq, rbseq:
        for i in range(3):
            translates = str(s[i:].translate()).split('*')
            orfs = [o[o.find("M"):] for o in translates]
            big_orf = max(orfs, key=lambda x: len(x))
            orf_len = len(big_orf)
            if orf_len > biggest_orf_len:
                biggest_orf_len = orf_len
                biggest_orf = big_orf
    return biggest_orf


find_max_orf("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
