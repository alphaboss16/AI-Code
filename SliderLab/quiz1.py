import sys
import time


def solve(puzzle):
    parseMe = {0: (puzzle, 0)}
    finalDict = {0: 1}
    dictSeen = {puzzle: ""}
    b = 0
    k = 0
    while b < len(parseMe):
        prev = parseMe[b]
        l = neighbor(prev[0])
        for st in l:
            t = l[st]
            if t not in dictSeen:
                if prev[1] + 1 not in finalDict:
                    finalDict[prev[1] + 1] = []
                k += 1
                parseMe[k] = (t, prev[1] + 1)
                dictSeen[t] = prev[0]
                finalDict[prev[1] + 1].append(t)
        b += 1
        st=""
    for i in list(finalDict.values()):
        st+=str(len(i))+", "
    print(st)
    return -1


def neighbor(puzzle):
    num = int(len(puzzle) ** .5)
    sub = num - 1
    list = {}
    i = puzzle.index('_')
    if i - 1 > -1 and i % num != 0:
        list[0] = (puzzle[0:i - 1] + puzzle[i] + puzzle[i - 1] + puzzle[i + 1:])
    if i + 1 < len(puzzle) and i % num != sub:
        list[1] = (puzzle[0:i] + puzzle[i + 1] + puzzle[i] + puzzle[i + 2:])
    if i - num > -1:
        list[2] = (puzzle[0:i - num] + puzzle[i] + puzzle[i - sub:i] + puzzle[i - num] + puzzle[i + 1:])
    if i + num < len(puzzle):
        list[3] = (puzzle[0:i] + puzzle[i + num] + puzzle[i + 1:i + num] + puzzle[i] + puzzle[i + num + 1:])
    return list


k = time.time()
b = solve(sys.argv[1])
k = time.time() - k
print("Time: {}s".format(round(k, 2)))
