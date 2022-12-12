from copy import deepcopy
from collections import deque
import time
import math

filename = "in.txt"
# filename = "ex.txt"

st = time.time()
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
grid = []


def heur(coords):
    (row, col) = coords
    # return abs(eRow - row) + abs(eCol - col)
    # return (eRow - row)*(eRow - row) + (eCol - col)*(eCol - col) + (grid[eRow][eCol] - grid[row][col])*(grid[eRow][eCol] - grid[row][col])
    return (grid[eRow][eCol] - grid[row][col])*(grid[eRow][eCol] - grid[row][col])


def findShortestPath(node):
    global found
    global queue
    global nodes
    (sRow, sCol, w) = node
    if (sRow, sCol) == (eRow, eCol):
        found = True
        return
    else:
        for dir in dirs:
            [row, col] = dir
            if (sRow + row >= 0 and sRow + row < len(grid) and
                sCol + col >= 0 and sCol + col < len(grid[0]) and
                nodes[(sRow + row, sCol + col)] == math.inf and
                    grid[sRow + row][sCol + col] <= grid[sRow][sCol] + 1):
                newNode = (sRow + row, sCol + col,
                           grid[sRow + row][sCol + col])
                nodes[(sRow + row, sCol + col)] = nodes[(sRow, sCol)] + 1
                queue.append(newNode)


sRow = -1
sCol = -1
eRow = -1
eCol = -1
with open(filename, "r") as f:
    rowIndex = 0
    for line in f:
        grid.append([ord(x) if x != 'S' and x != 'E' else ord('a')
                     if x == 'S' else ord('z') for x in [*line.strip()]])
        if 'S' in line:
            for i in range(len(line)):
                if line[i] == 'S':
                    sCol = i
                    sRow = rowIndex
        if 'E' in line:
            for i in range(len(line)):
                if line[i] == 'E':
                    eCol = i
                    eRow = rowIndex
        rowIndex += 1

nodes = {}
for row in range(len(grid)):
    for col in range(len(grid[0])):
        nodes[(row, col)] = math.inf
nodes[(sRow, sCol)] = 0

queue = deque([(sRow, sCol, 0)])
found = False
while len(queue) > 0 and not found:
    queue = deque(sorted(queue, key=lambda x: x[2]))
    queue = deque(
        sorted(queue, key=lambda x: x[2] * heur((x[0], x[1]))))
    findShortestPath(queue.popleft())

print("length:", nodes[(eRow, eCol)])

print("time: ", time.time()-st)

max = (0, 0)
maxvalue = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if nodes[(row, col)] != math.inf and nodes[(row, col)] > maxvalue:
            max = (row, col)
            maxvalue = nodes[(row, col)]
print("max", maxvalue)
s = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for row in range(len(grid)):
    line = ''
    for col in range(len(grid[0])):
        line += s[0 if nodes[(row, col)] ==
                  math.inf else int(nodes[(row, col)] / maxvalue * (len(s)-1))]
    print(line)
