from itertools import product


def main(alpha, num):
    orderedalpha = alpha.replace(" ", "")

    # Generate all the permutations
    permtuple = []
    for i in range(1, num + 1):
        permtuple += list(product(orderedalpha, repeat=i))

    # Sort list by lexicographic ordering
    permlist = ["".join(word) for word in permtuple]
    permlist.sort(key=lambda word: [orderedalpha.index(c) for c in word])

    # Output formatted list
    for word in permlist:
        print word

# Test
main("D N A", 3)
