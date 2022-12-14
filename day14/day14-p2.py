import numpy as np

filename = "in.txt"
# filename = "ex.txt"


def printGrid(rowRange, colRange, grid):
    for row in rowRange:
        line = ''
        for col in colRange:
            if row == 0 and col == 500:
                line += '+'
            elif grid[row, col] == 0:
                line += '.'
            elif grid[row, col] == 1:
                line += '#'
            elif grid[row, col] == 2:
                line += 'o'
        print(line)


def draw(sCoords, eCoords, grid):
    for row in range(min(sCoords[1], eCoords[1]), max(sCoords[1], eCoords[1]) + 1):
        for col in range(min(sCoords[0], eCoords[0]), max(sCoords[0], eCoords[0]) + 1):
            grid[row, col] = 1
    return grid


def spawnSand(grid):
    global over
    currCoords = (0, 500)
    while True:
        if grid[currCoords[0] + 1, currCoords[1]] == 0:
            currCoords = (currCoords[0] + 1, currCoords[1])
        elif grid[currCoords[0] + 1, currCoords[1] - 1] == 0:
            currCoords = (currCoords[0] + 1, currCoords[1] - 1)
        elif grid[currCoords[0] + 1, currCoords[1] + 1] == 0:
            currCoords = (currCoords[0] + 1, currCoords[1] + 1)
        else:
            grid[currCoords[0], currCoords[1]] = 2
            if currCoords == (0, 500):
                over = True
            return grid


grid = np.full((170, 1000), 0)

maxDepth = 0
with open(filename, "r") as f:
    for line in f:
        data = [[int(y) for y in x.split(',')]
                for x in line.strip().split(' -> ')]
        print(data)
        for i in range(len(data) - 1):
            grid = draw(data[i], data[i + 1], grid)
        mD = max([x[1] for x in data])
        if mD > maxDepth:
            maxDepth = mD

grid = draw((0, maxDepth + 2), (len(grid[0]) - 1, maxDepth + 2), grid)

# printGrid(range(20), range(490, len(grid[0])), grid)
# printGrid(range(len(grid)), range(420, len(grid[0])), grid)

over = False
count = 0
while not over:
    grid = spawnSand(grid)
    count += 1
    # printGrid(range(20), range(480, 540), grid)

print(count)
