from __future__ import print_function


def hamming(s, t):
    """
    Returns hamming distance for 2 given DNA sequences
    """
    ham = 0
    for character in range(len(s)):
        if s[character] != t[character]:
            ham += 1
    return ham


# Test
print(hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
