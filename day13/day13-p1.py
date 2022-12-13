filename = "in.txt"
# filename = "ex.txt"


def switched(pair):
    (fst, snd) = pair
    if isinstance(fst, int) and isinstance(snd, int):
        return snd < fst
    elif isinstance(fst, int):
        return switched(([fst], snd))
    elif isinstance(snd, int):
        return switched((fst, [snd]))
    else:
        length = len(fst) if len(fst) < len(snd) else len(snd)
        i = 0
        while i < length and fst[i] == snd[i]:
            i += 1
        if i < length:
            return switched((fst[i], snd[i]))
        else:
            return len(snd) < len(fst)


pairs = []
with open(filename, "r") as f:
    curr = []
    for line in f:
        if line != '\n':
            curr.append(line.strip())
        else:
            pairs.append((eval(curr[0]), eval(curr[1])))
            curr = []

swaps = 0
correct = []
i = 1
for pair in pairs:
    (fst, snd) = pair
    if switched(pair):
        pair = (snd, fst)
        swaps += 1
    else:
        correct.append(i)
    i += 1

# print(correct)
print(sum(correct))
