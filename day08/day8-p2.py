from math import prod

filename = "in.txt"
# filename = "ex.txt"


def isVisible(row, col, val):
    # top
    top = True
    for nrow in reversed(range(0, row)):
        if grid[nrow][col] >= val:
            top = False
    if top:
        return True

    # bottom
    bot = True
    for nrow in range(row + 1, len(grid)):
        if grid[nrow][col] >= val:
            bot = False
    if bot:
        return True

    # left
    left = True
    for ncol in reversed(range(0, col)):
        if grid[row][ncol] >= val:
            left = False
    if left:
        return True

    # right
    right = True
    for ncol in range(col + 1, len(grid[0])):
        if grid[row][ncol] >= val:
            right = False
    if right:
        return True


def calcScenic(row, col, val):
    counts = []
    # top
    count = 0
    for nrow in reversed(range(0, row)):
        count += 1
        if grid[nrow][col] >= val:
            break
    if count != 0:
        counts.append(count)

    # bottom
    count = 0
    for nrow in range(row + 1, len(grid)):
        count += 1
        if grid[nrow][col] >= val:
            break
    if count != 0:
        counts.append(count)

    # left
    count = 0
    for ncol in reversed(range(0, col)):
        count += 1
        if grid[row][ncol] >= val:
            break
    if count != 0:
        counts.append(count)

    # right
    count = 0
    for ncol in range(col + 1, len(grid[0])):
        count += 1
        if grid[row][ncol] >= val:
            break
    if count != 0:
        counts.append(count)
    return prod(counts)


grid = []
scores = []
with open(filename, "r") as f:
    for line in f:
        grid.append([int(x) for x in [*line.strip()]])

visibleCount = (len(grid) + (len(grid[0]) - 2)) * 2
for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        if row != 0 and col != 0 and row != len(grid) - 1 and col != len(grid[0]) - 1:
            curr = grid[row][col]
            if isVisible(row, col, grid[row][col]):
                scores.append(calcScenic(row, col, grid[row][col]))
print(max(scores))
