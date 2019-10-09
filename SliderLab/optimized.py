import sys
import time
import random


def countinv(puzzle, goal):
    st = puzzle.replace('_', '')
    st2 = goal.replace('_', "")
    cnt = 0
    for i in range(len(st)):
        for j in range(i + 1, len(st)):
            if st2.index(st[j]) < st2.index(st[i]):
                cnt += 1
    return cnt


def imposs(puzzle, goal):
    if (len(puzzle) ** .5) % 2 == 1:
        return countinv(puzzle, goal) % 2 == 1
    elif goal.index('_') // (len(goal) ** .5) - (len(puzzle) ** 5) % 2 == 0:
        return (countinv(puzzle, goal) % 2 == 1 and (
                puzzle.index("_") // (len(puzzle) ** .5) - (len(puzzle) ** .5)) % 2 == 0) or (
                       countinv(puzzle, goal) % 2 == 0 and (
                       puzzle.index("_") // (len(puzzle) ** .5) - (len(puzzle) ** .5)) % 2 == 1)
    else:
        return (countinv(puzzle, goal) % 2 == 0 and (
                puzzle.index("_") // (len(puzzle) ** .5) - (len(puzzle) ** .5)) % 2 == 0) or (
                       countinv(puzzle, goal) % 2 == 1 and (
                       puzzle.index("_") // (len(puzzle) ** .5) - (len(puzzle) ** .5)) % 2 == 1)


def solve(puzzle, goal='12345678_'):
    if imposs(puzzle, goal):
        return -1
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
            t = list[st]
            if t not in dictSeen:
                if t == goal:
                    dictSeen[t] = prev
                    b = finish(dictSeen, goal)
                    return b
                k += 1
                parseMe[k] = t
                dictSeen[t] = prev
        b += 1


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
    return len(list) - 1
    # print("Steps: {}".format(len(list)-1))


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


tosol = []
for i in range(500):
    l = list('12345678_')
    random.shuffle(l)
    tosol.append("".join(l))
k = time.time()
impcount = 0
count = 0
i = 0
s=0
while i < len(tosol) and time.time() - k <= 90.0:
    b = solve(tosol[i])
    if b == -1:
        impcount += 1
    else:
        s += b
        count += 1
    i+=1
# if len(sys.argv) > 2:
#     b = solve(sys.argv[1], sys.argv[2])
# else:
#     b = solve(sys.argv[1])
k = time.time() - k
print("Impossible: {}".format(impcount))
print("Average Solvable: {}".format(s/count))
print("Time: {}s".format(round(k, 2)))
