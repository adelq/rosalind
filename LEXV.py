from itertools import product


def main(alpha, num):
    orderedalpha = alpha.replace(" ", "")
    alphabet = " " + orderedalpha
    # Generate all the permutations
    permtuple = []
    for i in range(1, num+1):
        permtuple += ([x for x in product(orderedalpha, repeat=i)])

    # Output permutations properly formatted
    permlist = []
    permlist = map(lambda e: "".join(e), permtuple)
    sorted_list = sorted(permlist, key=lambda w: [alphabet.index(c) for c in w[0]])

    for i in sorted_list:
        print(i)


# Test
main("D N A", 3)
