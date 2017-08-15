from math import factorial

def perfect_matchings(rna):
    """Find number of perfect matchings in a string of RNA.

    >>> perfect_matchings("AGCUAGUCAU")
    12
    """
    return factorial(rna.count("A")) * factorial(rna.count("C"))

def test_main():
    assert perfect_matchings("AGCUAGUCAU") == 12

if __name__ == '__main__':
    test_main()
