filename = "in.txt"
# filename = "ex.txt"

insts = []
with open(filename, "r") as f:
    for line in f:
        data = line.strip().split(' ')
        if data[0] == "addx":
            insts.append((1, data[0], int(data[1])))
        else:
            insts.append((0, data[0]))

x = 1
instIndex = 0
strengths = []
for tick in range(0, 220):
    if (tick + 1 - 20) % 40 == 0:
        strengths.append((tick + 1) * x)
    if insts[instIndex][0] == 0:
        if insts[instIndex][1] == "addx":
            x += insts[instIndex][2]
        instIndex += 1
    else:
        insts[instIndex] = (insts[instIndex][0] - 1,
                            insts[instIndex][1], insts[instIndex][2])

print(sum(strengths))
