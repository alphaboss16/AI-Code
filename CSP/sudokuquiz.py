import time
import sys


def setglobals(puzzle):
    global N, SYMSET, subBlockHeight, subBlockWidth, CONSTRAINTS
    N = int(len(puzzle) ** .5)
    total = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    SYMSET = set(total[0:N])
    total = []
    check = int(N ** .5)
    while N % check != 0:
        check -= 1
    CONSTRAINTS = []
    for i in range(N):
        sub = []
        sub2 = []
        for j in range(N):
            sub.append(i * N + j)
            sub2.append(j * N + i)
        total.append(sub)
        total.append(sub2)
    new = [[0, 1, 2, 3, 4, 9, 10, 18, 27], [5, 6, 7, 8, 16, 17, 26, 35, 44], [11, 12, 13, 14, 19, 20, 23, 32, 33],
           [15, 24, 25, 34, 43, 50, 51, 52, 59], [21, 28, 29, 30, 37, 46, 55, 56, 65],
           [22, 31, 38, 39, 40, 41, 42, 49, 58], [36, 45, 54, 63, 64, 72, 73, 74, 75],
           [47, 48, 57, 60, 61, 66, 67, 68, 69], [53, 62, 70, 71, 76, 77, 78, 79, 80]]
    for i in new:
        total.append(i)
    CONSTRAINTS = {x: set() for x in range(int(N ** 2))}
    for i in range(int(N ** 2)):
        for k in total:
            if i in k:
                for z in k:
                    CONSTRAINTS[i].add(z)


def checksum(puzzle):
    s = 0
    for i in range(len(puzzle)):
        s += ord(puzzle[i])
    return s - 48 * (int(N ** 2))


def getPossible(puzzle, pos):
    check = {}
    minpos = 0
    for i in range(len(pos)):
        check[pos[i]] = {puzzle[k] for k in CONSTRAINTS[pos[i]] if puzzle[k] != '.'}
        if len(check[pos[i]]) == len(SYMSET):
            return None
        if len(check[pos[i]]) == len(SYMSET) - 1:
            return SYMSET - check[pos[i]], pos.pop(i)
        if len(check[pos[i]]) > len(check[pos[minpos]]):
            minpos = i
    return SYMSET - check[pos[minpos]], pos.pop(minpos)


def bruteForce(puzzle, positions):
    if len(positions) == 0:
        return puzzle
    copy = positions[:]
    k = getPossible(puzzle, copy)
    if k is None:
        return ""
    for i in k[0]:
        b = bruteForce(puzzle[0:k[1]] + i + puzzle[k[1] + 1:], copy)
        if b != "":
            return b
    return ""


def main():
    k = time.time()
    puzzle = sys.argv[1]
    setglobals(puzzle)
    periods = []
    for i in range(len(puzzle)):
        if puzzle[i] == '.':
            periods.append(i)
    st = bruteForce(puzzle, periods)
    print(st)


if __name__ == "__main__":
    main()
