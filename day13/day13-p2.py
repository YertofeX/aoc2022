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


def bubbleSort(packets):
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if switched((packets[j], packets[j + 1])):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]


packets = [[[2]], [[6]]]
with open(filename, "r") as f:
    for line in f:
        if line != '\n':
            packets.append((eval(line)))

bubbleSort(packets)

i = 1
indices = []
for packet in packets:
    # print(packet)
    if packet == [[6]] or packet == [[2]]:
        indices.append(i)
    i += 1
print(indices[0]*indices[1])
