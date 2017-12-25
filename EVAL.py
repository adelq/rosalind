def substr_prob(gen_length, gc_content, seq_string):
    prob = 1
    for base in seq_string:
        if base in "GC":
            prob *= gc_content * 0.5
        else:
            prob *= (1 - gc_content) * 0.5
    return prob * (gen_length - (len(seq_string) - 1))


def seq_prob_list(n, seq_string, gc_content_list):
    return [substr_prob(n, gc, seq_string) for gc in gc_content_list]


def main():
    print(" ".join(str(p) for p in seq_prob_list(10, "AG", [0.25, 0.5, 0.75])))
