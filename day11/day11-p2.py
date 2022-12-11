filename = "in.txt"
# filename = "ex.txt"


def printMonkeys(monkeys):
    i = 0
    for monkey in monkeys:
        line = f'Monkey {i}: '
        for item in monkey[0]:
            line += f'{item}, '
        print(line)
        i += 1


def printMonkeyScores(monkeys):
    i = 0
    for monkey in monkeys:
        print(f'Monkey {i}: {monkey[4]}')
        i += 1


monkeys = []
with open(filename, "r") as f:
    index = 0
    for line in f:
        if "Starting items" in line:
            monkeys.append(
                [[int(x) for x in line.strip().split(': ')[1].split(', ')]])
        elif "Operation" in line:
            tmp = line.strip().split('old ')[1].split(' ')
            monkeys[index].append((tmp[0], tmp[1]))
        elif "Test" in line:
            monkeys[index].append(int(line.strip().split('by ')[1]))
        elif "true" in line:
            monkeys[index].append([int(line.strip().split('monkey ')[1])])
        elif "false" in line:
            monkeys[index][3].append(int(line.strip().split('monkey ')[1]))
            monkeys[index].append(0)
        elif line == '\n':
            index += 1

for i in range(0, 10000):
    if i % 100 == 0:
        print(f'{i//100}%')
    if i % 1000 == 0:
        print(f'{i}')
        printMonkeyScores(monkeys)
    for monkey in monkeys:
        monkey[4] += len(monkey[0])
        for item in monkey[0]:
            worry = item
            factor = worry if monkey[1][1] == 'old' else int(monkey[1][1])
            if monkey[1][0] == '*':
                worry = worry * factor
            elif monkey[1][0] == '+':
                worry = worry + factor
            if worry % monkey[2] == 0:
                monkeys[monkey[3][0]][0].append(
                    worry % (2*3*5*7*11*13*17*19*23))
            else:
                monkeys[monkey[3][1]][0].append(
                    worry % (2*3*5*7*11*13*17*19*23))
        monkey[0] = []

scores = []
for monkey in monkeys:
    scores.append(monkey[4])
scores.sort()
scores.reverse()
print(scores[0] * scores[1])
print()
