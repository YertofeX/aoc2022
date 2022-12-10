filename = "in.txt"
# filename = "ex.txt"


def overlaps(pair):
    [[e1s, e1e], [e2s, e2e]] = pair
    for i in range(e1s, e1e + 1):
        for j in range(e2s, e2e + 1):
            if i == j:
                return True
    return False


count = 0
with open(filename, "r") as f:
    for line in f:
        [[e1s, e1e], [e2s, e2e]] = map(lambda x: map(
            lambda y: int(y), x.split('-')), line.split(","))
        if overlaps([[e1s, e1e], [e2s, e2e]]):
            count += 1
print(count)
