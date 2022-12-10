from collections import deque

filename = "in.txt"
# filename = "ex.txt"

stacks = []
moves = []

with open(filename, "r") as f:
    for line in f:
        if len(line) > 1 and line[1] == '1':
            stackCount = int(line.strip()[-1])
            for i in range(0, stackCount):
                stacks.append(deque([]))
with open(filename, "r") as f:
    for line in f:
        if 'move' in line:
            splitLine = line.strip().split(' ')
            moves.append([int(splitLine[1]), int(
                splitLine[3]), int(splitLine[5])])
        else:
            if line != '\n' and line[1] != '1':
                stripLine = line.strip().split(' ')
                for i in range(0, stackCount):
                    if stripLine[i][1] != '.':
                        stacks[i].append(stripLine[i][1])

# print("stacks: ", stacks)
# print("moves: ", moves)

for move in moves:
    for i in range(0, move[0]):
        el = stacks[move[1] - 1].popleft()
        stacks[move[2] - 1].appendleft(el)

# print("stacks: ", stacks)
# print("moves: ", moves)

sol = ''
for j in range(0, stackCount):
    sol += stacks[j][0]
print(sol)
