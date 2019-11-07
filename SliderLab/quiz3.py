import sys
import time


def solve(puzzle, goal='12345678_'):
    parseMe = {0: (puzzle, 0)}
    numPaths = {puzzle: 1}
    dictSeen = {puzzle: ''}
    minPathLen = {puzzle: 0}
    b = 0
    k = 0
    while b < len(parseMe):
        prev = parseMe[b]
        list = neighbor(prev[0])
        for st in list:
            t = list[st]
            if t not in dictSeen:
                k += 1
                parseMe[k] = (t, prev[1]+1)
                dictSeen[t] = prev[0]
                minPathLen[t]=prev[1]+1
                numPaths[t]=1
            elif minPathLen[t]==prev[1]+1:
                numPaths[t]+=1
        b += 1
    return numPaths


def finish(dict, goal):
    curr = goal
    count = 0
    while dict[curr] != '':
        count += 1
        curr = dict[curr]
    list = {count: goal}
    curr = goal
    for i in range(count - 1, -1, -1):
        list[i] = dict[curr]
        curr = dict[curr]
    printg(list)


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


def printg(list, k=False):
    if not k:
        d = len(list) // 10
        num = int(len(list[0]) ** .5)
        m = len(list)
        for i in range(d):
            for j in range(0, num ** 2, num):
                s = ""
                for k in range(0, 10):
                    s += list[i * 10 + k][j:j + num] + "\t\t"
                print(s)
        if len(list) % 10:
            for z in range(0, num ** 2, num):
                s = ""
                for i in range(d * 10, d * 10 + len(list) % 10):
                    s += list[i][z:z + num] + "\t\t"
                print(s)

        print("Steps: {}".format(m - 1))
    else:
        num = int(len(list) ** .5)
        print(list[0:num] + '\n' + list[num:num + num] + '\n' + list[num + num:])

k = solve(sys.argv[1])
finaldict={}
for item in k:
    if k[item] in finaldict:
        finaldict[k[item]]+=1
    else:
        finaldict[k[item]]=1
sum = 0
sum2= 0
for item in finaldict:
    sum2+=finaldict[item]
    sum+=finaldict[item]*item
print(finaldict)
print(sum2)
print(sum)

