from __future__ import print_function


def wabbits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return wabbits(n-1, k) + k*wabbits(n-2, k)


def wabbits_dynamic(n, k):
    """Dynamic programming solution"""
    prev_vals = [0, 1]
    for i in range(2, n + 1):
        next_val = k * prev_vals[0] + prev_vals[1]
        prev_vals[0] = prev_vals[1]
        prev_vals[1] = next_val
    return prev_vals[1]


# Test
print(wabbits(5, 3))
