filename = "in.txt"
# filename = "ex.txt"


def getSameChar(a, b):
    for ch in a:
        if ch in b:
            return ch


def getVal(ch):
    if ch.isupper():
        return ord(ch)-38
    return ord(ch)-96


vals = []

with open(filename, "r") as f:
    for line in f:
        vals.append(
            getVal(getSameChar(line[:len(line.strip()) // 2], line[len(line.strip()) // 2:])))

print(sum(vals))
