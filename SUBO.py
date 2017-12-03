from HAMM import hamming


def count_hamming(pat, seq, dist=3):
    """Count number of matches within dist mismatches."""
    count = 0
    pat_len = len(pat)
    for i in range(len(seq) - pat_len + 1):
        if hamming(seq[i:i + pat_len], pat) < 4:
            count += 1
    return count


if __name__ == "__main__":
    import sys
    pattern = sys.argv[1]
    files = sys.argv[2:]
    for filen in files:
        with open(filen, "r") as f:
            seq = "".join(f.read().strip().split('\n')[1:])
            c = count_hamming(pattern, seq)
            print(f"File: {filen}    Count: {c}")
