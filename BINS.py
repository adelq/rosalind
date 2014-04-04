import unittest
from bisect import bisect_left

def parse(filename):
    with open(filename, 'r') as f:
        raw = f.read().split('\n')
        n = int(raw[0])
        m = int(raw[1])
        A = list(map(int, raw[2].split()))
        B = list(map(int, raw[3].split()))
    return (n, m, A, B)

def search(n, L):
    """
    Do a binary search on list L to find index of element n.
    Return index of element n or -1 if it is not found
    """
    low = 0
    high = len(L)
    position = bisect_left(L, n, low, high)
    return (position + 1 if position != high and L[position] == n else -1)

def main(filename):
    n, m, A, B = parse(filename)
    result = ""
    for i in B:
        result += str(search(i, A)) + " "
    return result.strip()

class TestBinarySearch(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(
            parse("BINS.txt"),
            (5, 6, [10, 20, 30, 40, 50], [40, 10, 35, 15, 40, 20]))

    def test_search1(self):
        self.assertEqual(search(40, [10, 20, 30, 40, 50]), 4)
    def test_search2(self):
        self.assertEqual(search(10, [10, 20, 30, 40, 50]), 1)
    def test_search3(self):
        self.assertEqual(search(35, [10, 20, 30, 40, 50]), -1)
    def test_search4(self):
        self.assertEqual(search(15, [10, 20, 30, 40, 50]), -1)
    def test_search5(self):
        self.assertEqual(search(20, [10, 20, 30, 40, 50]), 2)

    def test_main(self):
        self.assertEqual(
            main("BINS.txt"),
            "4 1 -1 -1 4 2")

if __name__ == "__main__":
    print(main("BINS.txt"))
    unittest.main()