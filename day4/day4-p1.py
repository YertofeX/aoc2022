filename = "in.txt"
# filename = "ex.txt"

count = 0
with open(filename, "r") as f:
    for line in f:
        [[e1s, e1e], [e2s, e2e]] = map(lambda x: map(
            lambda y: int(y), x.split('-')), line.split(","))
        if (e1s >= e2s and e1e <= e2e) or (e2s >= e1s and e2e <= e1e):
            count += 1
print(count)
