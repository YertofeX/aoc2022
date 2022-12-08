filename = "in.txt"
# filename = "ex.txt"


def isVisible(row, col, val):
    # top
    top = True
    for nrow in range(0, row):
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
    for ncol in range(0, col):
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


grid = []
with open(filename, "r") as f:
    for line in f:
        grid.append([int(x) for x in [*line.strip()]])

visibleCount = (len(grid) + (len(grid[0]) - 2)) * 2
for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        if row != 0 and col != 0 and row != len(grid) - 1 and col != len(grid[0]) - 1:
            curr = grid[row][col]
            if isVisible(row, col, grid[row][col]):
                visibleCount += 1
print(visibleCount)
