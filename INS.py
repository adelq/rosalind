def swap(l, a, b):
    """Swap items at positions `a` and `b` in list `l`."""
    l[b], l[a] = l[a], l[b]
    return l

def insert_sort(unsorted_list):
    """Insert sort based on psuedocode on unsorted list."""
    number_of_swaps = 0

    for i in range(1, len(unsorted_list)):
        k = i
        while k > 0 and unsorted_list[k] < unsorted_list[k-1]:
            unsorted_list = swap(unsorted_list, k-1, k)
            number_of_swaps += 1
            k -= 1

    return number_of_swaps

if __name__ == '__main__':
    input = "6 10 4 5 1 2"
    input_list = list(map(int, input.split()))
    print(insert_sort(input_list))
