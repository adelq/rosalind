def failure_array(seq):
    """
    Calculate the Knuth-Morris-Pratt failure array (also known as partial
    match table) based on the longest substring matching the prefix of the
    sequence.

    :param seq: the input pattern sequence
    :returns: list for failure array of sequence
    """
    arr = [0] * len(seq)
    arr[0] = 0
    for i in range(1, len(seq)):
        j = arr[i - 1]
        while j > 0 and seq[i] != seq[j]:
            j = arr[j - 1]
        if seq[i] == seq[j]:
            j += 1
        arr[i] = j
    return arr


with open("/tmp/rosalind_kmp.txt", "r") as f:
    seq = "".join(f.read().strip().split('\n')[1:])
    with open("/tmp/rosalind_out.txt", "w") as fr:
        fr.write(" ".join(str(z) for z in failure_array(seq)))

print(failure_array("CAGCATGGTATCACAGCAGAG"))
