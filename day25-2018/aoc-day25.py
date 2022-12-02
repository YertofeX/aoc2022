# filename = "ex.txt"
filename = "in.txt"


def mandist(coords, constcoords):
    sub = []
    for i in range(0, 4):
        sub.append(abs(coords[i] - constcoords[i]))
    return sum(sub)


def reconstruct(indexes, coords):
    newconst = [coords]
    for i in indexes:
        for c in consts[i]:
            newconst.append(c)
    newconsts = [newconst]
    for j in range(0, len(consts)):
        if j not in indexes:
            newconsts.append(consts[j])
    return newconsts


consts = []
first = True
progress = 0
with open(filename, "r") as f:
    for line in f:
        progress += 1
        if progress % 100 == 0:
            print(f"{progress / 1478.0:.3f}%")
        coords = list(map(lambda x: int(x), line.strip().split(",")))
        inconst = False
        inindexes = []
        if first:
            consts.append([coords])
            first = False
        else:
            for i in range(0, len(consts)):  # constellation
                for j in range(0, len(consts[i])):  # coordinates
                    if mandist(consts[i][j], coords) < 4:
                        inindexes.append(i)
                        break
            consts = reconstruct(inindexes, coords)
print(len(consts))
