import math


def seq_prob(num_constructed, gc_content, seq_string):
    prob = 1
    for base in seq_string:
        if base in "GC":
            prob *= gc_content * 0.5
        else:
            prob *= (1 - gc_content) * 0.5
    return 1 - math.pow(1 - prob, num_constructed)


def main():
    print(seq_prob(90000, 0.6, "ATAGCCGA"))
