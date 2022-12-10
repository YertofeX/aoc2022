filename = "in.txt"
# filename = "ex.txt"


def getSameChar(a, b, c):
    for ch in a:
        if ch in b and ch in c:
            return ch


def getVal(ch):
    if ch.isupper():
        return ord(ch)-38
    return ord(ch)-96


vals = []
lines = []
i = 0

# Vesztettem

with open(filename, "r") as f:
    for line in f:
        if i > 1 and (i + 1) % 3 == 0:
            vals.append(
                getVal(getSameChar(lines[0], lines[1], line)))
            lines = []
        else:
            lines.append(line)
        i += 1

print(sum(vals))
