def parse_table(table_text):
    # Remove whitespace
    table = table_text.strip()
    # Split into rows on newline
    rows = table.split('\n')[1:]
    return [[float(e) for e in col.split()[1:]] for col in rows]


def parse(text):
    path, states_raw, table = text.split('--------')
    # Remove trailing whitespace
    path = path.strip()
    # List of states
    states = states_raw.split()
    matrix = parse_table(table)
    return prob_calc(path, states, matrix)


def prob_calc(path, states, matrix):
    prob = 0.5
    for i in range(len(path) - 1):
        el1, el2 = path[i], path[i + 1]
        prob *= matrix[states.index(el1)][states.index(el2)]
    return prob


def main(filename='ba10a.txt'):
    with open(filename) as f:
        text = f.read()
    return parse(text)
