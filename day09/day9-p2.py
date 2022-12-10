filename = "in.txt"
# filename = "ex.txt"

dirs = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def updateHead(headPos, move):
    return (headPos[0] + move[0], headPos[1] + move[1])


def updateTail(tailPos, headPos):
    moveCoords = (headPos[0]-tailPos[0], headPos[1]-tailPos[1])
    if (moveCoords[0] > 1 or moveCoords[0] < -1) and (moveCoords[1] > 1 or moveCoords[1] < -1):
        return(tailPos[0] + moveCoords[0] / 2, tailPos[1] + moveCoords[1] / 2)
    if moveCoords[0] > 1:
        return(tailPos[0] + moveCoords[0] - 1, tailPos[1] + moveCoords[1])
    if moveCoords[0] < -1:
        return(tailPos[0] + moveCoords[0] + 1, tailPos[1] + moveCoords[1])
    if moveCoords[1] > 1:
        return(tailPos[0] + moveCoords[0], tailPos[1] + moveCoords[1] - 1)
    if moveCoords[1] < -1:
        return(tailPos[0] + moveCoords[0], tailPos[1] + moveCoords[1] + 1)
    return tailPos


moves = []

with open(filename, "r") as f:
    for line in f:
        data = line.strip().split(' ')
        moves.append((dirs[data[0]], int(data[1])))

knots = []
for i in range(0, 10):
    knots.append((0, 0))
positions = []
for moveSet in moves:
    for i in range(0, moveSet[1]):
        knots[0] = updateHead(knots[0], moveSet[0])
        for j in range(1, 10):
            knots[j] = updateTail(knots[j], knots[j - 1])
            if j == 9 and knots[j] not in positions:
                positions.append(knots[j])
print(len(positions))
