import sys
import time
def solve(puzzle, goal='12345678_'):
    parseMe = {0: puzzle}
    dictSeen = {puzzle: ''}
    if puzzle == goal:
        finish(dictSeen, goal)
        return
    b = 0
    k = 0
    while b < len(parseMe):
        prev = parseMe[b]
        list = neighbor(prev)
        for st in list:
            if st not in dictSeen:
                if st == goal:
                    dictSeen[st] = prev
                    finish(dictSeen, goal)
                    return
                k += 1
                parseMe[k] = st
                dictSeen[st] = prev
        b += 1
    print("Steps: -1")
    printg(puzzle, k=True)
    return -1


def finish(dict, goal):
    curr = goal
    list = [goal]
    while dict[curr] != '':
        list.append(dict[curr])
        curr = dict[curr]
    printg(list[::-1])


def neighbor(puzzle):
    num = int(len(puzzle) ** .5)
    sub = num - 1
    list = set()
    i = puzzle.index('_')
    if i - 1 > -1 and i % num != 0:
        list.add(puzzle[0:i - 1] + puzzle[i] + puzzle[i - 1] + puzzle[i + 1:])
    if i + 1 < len(puzzle) and i % num != sub:
        list.add(puzzle[0:i] + puzzle[i + 1] + puzzle[i] + puzzle[i + 2:])
    if i - num > -1:
        list.add(puzzle[0:i - num] + puzzle[i] + puzzle[i - sub:i] + puzzle[i - num] + puzzle[i + 1:])
    if i + num < len(puzzle):
        list.add(puzzle[0:i] + puzzle[i + num] + puzzle[i + 1:i + num] + puzzle[i] + puzzle[i + num + 1:])
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
        if len(list)%10:
            for z in range(0, num ** 2, num):
                s = ""
                for i in range(d * 10, d*10+len(list) % 10):
                    s += list[i][z:z + num] + "\t\t"
                print(s)

        print("Steps: {}".format(m - 1))
    else:
        num = int(len(list) ** .5)
        print(list[0:num] + '\n' + list[num:num + num] + '\n' + list[num + num:])


k = time.time()
if len(sys.argv) > 2:
    b = solve(sys.argv[1], sys.argv[2])
else:
    b = solve(sys.argv[1])
k = time.time() - k
print("Time: {}s".format(round(k, 2)))
