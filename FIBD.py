from __future__ import print_function


def wabbits(n, m):
    """
    Return the total number of rabbits that remain after n months if all
    rabbits live for m months.
    """
    prev_vals = [1] + (m - 1) * [0]
    for i in range(2, n + 1):
        next_val = sum(prev_vals[1:])
        prev_vals = [next_val] + prev_vals[:-1]
    return sum(prev_vals)


print(wabbits(6, 3))
