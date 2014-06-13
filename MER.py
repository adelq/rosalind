def merge_two_sorted_lists(a, b):
    """Merge two lists that are already sorted."""
    c = []

    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    # One of the arrays is now empty
    if a and not b:
        c.extend(a)
    elif b and not a:
        c.extend(b)

    return list(map(str, c))

if __name__ == '__main__':
    input_a = "2 4 10 18"
    input_b = "-5 11 12"
    a = list(map(int, input_a.split()))
    b = list(map(int, input_b.split()))
    with open('mer_solution.txt', 'w') as f:
        f.write(" ".join(merge_two_sorted_lists(a, b)))
