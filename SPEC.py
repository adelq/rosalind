MASSTABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


def closest_amino(weight):
    """Finds closest amino acid based on weight."""
    return min(MASSTABLE.items(), key=lambda x: abs(x[1] - weight))[0]


def pref_spec(prefix_weights):
    diffs = [i - j for j, i in zip(prefix_weights, prefix_weights[1:])]
    return "".join([closest_amino(w) for w in diffs])


with open("/tmp/rosalind_spec.txt", "r") as f:
    weights = [float(n) for n in f.read().strip().split('\n')]
    print(pref_spec(weights))


sample = [3524.8542, 3710.9335, 3841.974, 3970.0326, 4057.0646]
print(pref_spec(sample))
