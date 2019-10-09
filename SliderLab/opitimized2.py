import sys
import time


def goalDict(goal, width):
    toret = {}
    for i in range(len(goal)):
        toret[goal[i]] = (i % width, i // width)
    return toret


def modulotable(width):
    d = {}
    for i in range(width ** 2):
        d[i] = (i % width, i // width)
    return d


def Manhat(puzzle, pos, modulos):
    st = puzzle
    count = 0
    for z in range(len(st)):
        if st[z] != '_':
            m = pos[st[z]]
            x = modulos[z][0]
            y = modulos[z][1]
            count += (abs((m[0]) - x) + abs((m[1]) - y))
    return count


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


def get_f(puzzle, lvl, goal, tables):
    return lvl + int(Manhat(puzzle, goal, tables)) + 1


def solve(puzzle, goal='12345678_'):
    width = int(len(puzzle) ** .5)
    tables = modulotable(width)
    if imposs(puzzle, goal):
        return -1
    if puzzle == goal:
        return 0
    ideal = goalDict(goal, width)
    first = get_f(puzzle, 0, ideal, tables)
    nbrcalc=calcneighbors(width)
    openset = {first: [(puzzle, 0)]}
    clsdset = {}
    while True:
        for item in openset[first]:
            prev = item
            if prev[0] not in clsdset:
                clsdset[prev[0]] = prev[1]
                nbr = neighbor(prev[0], width, nbrcalc)
                for st in nbr:
                    t=nbr[st]
                    if t not in clsdset:
                        if t == goal:
                            clsdset[t] = prev[1] + 1
                            return clsdset[t]
                        f = get_f(t, prev[1] + 1, ideal, tables)
                        if f in openset:
                            openset[f].append((t, prev[1] + 1))
                        else:
                            openset[f] = [(t, prev[1] + 1)]
        first += 1
        while first not in openset:
            first += 1


def calcneighbors(width):
    toret = {}
    for i in range(width ** 2):
        toret[i]=[]
        if i - 1 > -1 and i % width != 0:
            toret[i].append((i, i - 1))
        if i + 1 < width ** 2 and i % width != width - 1:
            toret[i].append((i, i + 1))
        if i - width > -1:
            toret[i].append((i, i - width))
        if i + width < width ** 2:
            toret[i].append((i, i + width))
    return toret
def swap(l, i, i2):
    l[i], l[i2]=l[i2], l[i]
    return l
def neighbor(puzzle, width, calcs):
    s = {i:"" for i in range(4)}
    cnt=0
    i = puzzle.index('_')
    for b in calcs[i]:
        s[cnt]=("".join(swap(list(puzzle), b[0], b[1])))
        cnt+=1
    return s
    # num = int(len(puzzle) ** .5)
    # sub = num - 1
    # list = {}
    # i = puzzle.index('_')
    # if i - 1 > -1 and i % num != 0:
    #     list[0] = (puzzle[0:i - 1] + puzzle[i] + puzzle[i - 1] + puzzle[i + 1:])
    # if i + 1 < len(puzzle) and i % num != sub:
    #     list[1] = (puzzle[0:i] + puzzle[i + 1] + puzzle[i] + puzzle[i + 2:])
    # if i - num > -1:
    #     list[2] = (puzzle[0:i - num] + puzzle[i] + puzzle[i - sub:i] + puzzle[i - num] + puzzle[i + 1:])
    # if i + num < len(puzzle):
    #     list[3] = (puzzle[0:i] + puzzle[i + num] + puzzle[i + 1:i + num] + puzzle[i] + puzzle[i + num + 1:])
    # return list


k = time.time()
impcount = 0
count = 0
i = 0
s = 0

with open('words.txt', 'r') as f:
    sol = f.readline()[0:-1]
    for line in f:
        b = solve(line[0:-1], sol)
        print("Steps: {}".format(b), "Time: {}".format(round(time.time() - k, 2)), sep="\t")
        if time.time() - k > 120.0:
            break
# b=solve('ABCDEFGHIJ_LMNKO',"ABCDEFGHIJKLMNO_")
# if len(sys.argv) > 2:
#     b = solve(sys.argv[1], sys.argv[2])
# else:
#     b = solve(sys.argv[1])
