filename = "in.txt"
# filename = "ex.txt"

table = {
    'AX': 3,
    'BX': 1,
    'CX': 2,
    'AY': 4,
    'BY': 5,
    'CY': 6,
    'AZ': 8,
    'BZ': 9,
    'CZ': 7
}


def calc(p1, p2):
    return table[p1 + p2]


score = 0

with open(filename, "r") as f:
    for line in f:
        ps = line.strip().split(' ')
        score += calc(ps[0], ps[1])

print(score)
