filename = "in.txt"
# filename = "ex.txt"


class Node:
    def __init__(self, name, size, parent, isDir):
        self.name = name
        self.size = size
        self.parent = parent
        self.isDir = isDir
        self.children = []


def getSize(node):
    sum = 0
    for child in node.children:
        # dir
        if child.isDir:
            sum += getSize(child)
        # file
        else:
            sum += child.size
    return sum


def getSizeOfSmall(node):
    goodNodes = []
    for child in node.children:
        if child.isDir:
            subGoodNodes = getSizeOfSmall(child)
            goodNodes.append(subGoodNodes)
            subSize = getSize(child)
            if subSize <= 100000:
                goodNodes.append(subSize)
    return sum(goodNodes)


root = None
first = True
isListing = False
with open(filename, "r") as f:
    currNode = None
    for line in f:
        data = line.strip().split(' ')
        # command
        if data[0] == '$':
            isListing = False
            # dir change
            if data[1] == 'cd':
                # creating /
                if first and data[2] == '/':
                    currNode = Node('/', 0, None, True)
                    root = currNode
                    first = False
                # new dir
                elif data[2] != '..':
                    newNode = Node(data[2], 0, currNode, True)
                    currNode.children.append(newNode)
                    currNode = newNode
                # ..
                else:
                    currNode = currNode.parent
            # list
            elif data[1] == 'ls':
                isListing = True
        elif isListing:
            # new file
            if data[0] != 'dir':
                currNode.children.append(
                    Node(data[1], int(data[0]), currNode, False))

print(getSizeOfSmall(root))
