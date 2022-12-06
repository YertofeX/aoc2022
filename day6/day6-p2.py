from collections import deque
import copy

filename = "in.txt"
# filename = "ex.txt"


def allUnique(b):
    for j in range(0, len(b)):
        substr = copy.deepcopy(b)
        del substr[j]
        if b[j] in substr:
            return False
    return True


def findMarker(line):
    i = 0
    buff = deque([])
    for ch in line:
        if len(buff) == 14:
            buff.popleft()
        buff.append(ch)
        if i >= 13 and allUnique(buff):
            return i + 1
        i += 1
    return (-1)


with open(filename, "r") as f:
    for line in f:
        print(findMarker(line))
