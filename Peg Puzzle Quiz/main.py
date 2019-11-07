import sys


def setLookup():
    global moves
    moves = {0: [(3, 1, '/'), (5, 2, '\\')], 1: [(6, 3, '/'), (8, 4, '\\')], 2: [(7, 4, '/'), (9, 5, '\\')],
             3: [(12, 7, '\\'), (10, 6, '/'), (5, 4, '-'), (0, 1, '/')], 4: [(11, 7, '/'), (13, 8, '\\')],
             5: [(0, 2, '\\'), (3, 4, '-'), (12, 8, '/'), (14, 9, '\\')],
             6: [(1, 3, '/'), (8, 7, '-')], 7: [(2, 4, '/'), (9, 8, '-')], 8: [(1, 4, '\\'), (6, 7, '-')],
             9: [(2, 5, '\\'), (7, 8, '-')],
             10: [(3, 6, '/'), (12, 11, '-')],
             11: [(4, 7, '/'), (13, 12, '-')], 12: [(10, 11, '-'), (3, 7, '\\'), (5, 8, '/'), (14, 13, '-')],
             13: [(4, 8, '\\'), (11, 12, '-')],
             14: [(5, 9, '\\'), (12, 13, '-')]}


def neighbors(puzzle):
    holes = []
    nbrs = []
    for i in range(len(puzzle)):
        if puzzle[i] == ".":
            holes.append(i)
    for i in holes:
        check = moves[i]
        for j in check:
            if puzzle[j[0]] == '1' and puzzle[j[1]] == '1':
                pzl = list(puzzle)
                pzl[j[0]] = '.'
                pzl[j[1]] = '.'
                pzl[i] = '1'
                nbrs.append(("".join(pzl), str(j[1])+j[2]))
    return nbrs

def atGoal(puzzle, startpos):
    return not (puzzle.index('1') == startpos) and puzzle.count("1") == 1


def getPath(dictSeen, final):
    curr = final
    toret = []
    while dictSeen[curr][0] != "":
        toret.append(dictSeen[curr][1])
        curr = dictSeen[curr][0]
    return toret[::-1]


def solve(puzzle):
    startpos = puzzle.index(".")
    dictSeen = {puzzle: ("", str(startpos))}
    parseMe = [puzzle]
    while parseMe:
        curr = parseMe.pop(0)
        for i in neighbors(curr):
            if atGoal(i[0], startpos):
                dictSeen[i[0]] = (curr, i[1])
                l = getPath(dictSeen, i[0])
                print("done")
                return l
            if i[0] not in dictSeen:
                dictSeen[i[0]] = (curr, i[1])
                parseMe.append(i[0])
    print("impossible")


setLookup()
puzzle = sys.argv[1]
z = solve(puzzle)

z = [str(puzzle.index('.'))]+z
print(" ".join(z))
