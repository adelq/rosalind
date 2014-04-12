from collections import Counter

def main(s):
    l = s.split()
    c = Counter(l)
    for k,v in c.items():
        print(k,v)

if __name__ == "__main__":
    main("We tried list and we tried dicts also we tried Zen")