elves = []
s = 0
with open("in.txt", "r") as f:
    for line in f:
        if line == "\n":
            elves.append(s)
            s = 0
        else:
            s += int(line)
elves.sort(reverse=True)
sum = sum(elves[:3])
print(sum)
