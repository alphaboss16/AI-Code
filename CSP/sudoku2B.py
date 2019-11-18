import time
import sys


def setglobals(puzzle):
    global N, SYMSET, subBlockHeight, subBlockWidth, CONSTRAINTS, CONSTRAINT_SETS
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
    subBlockHeight = int(check)
    subBlockWidth = N // subBlockHeight
    for i in range(N // subBlockWidth):
        for j in range(N // subBlockHeight):
            sub = []
            for k in range(subBlockHeight):
                for l in range(subBlockWidth):
                    sub.append((i * subBlockWidth + l) + (j * subBlockHeight + k) * N)
            total.append(sub)
    CONSTRAINT_SETS = total
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
            return SYMSET - check[pos[i]], pos.pop(i), True
        if len(check[pos[i]]) > len(check[pos[minpos]]):
            minpos = i
    t1 = SYMSET - check[pos[minpos]]
    t = len(t1)
    for j in CONSTRAINT_SETS:
        for m in SYMSET - {puzzle[k] for k in j}:
            locations = {loc for loc in j if puzzle[loc] == '.' and m not in {puzzle[z] for z in CONSTRAINTS[loc]}}
            if len(locations) < t:
                return locations, m, False
    return t1, pos.pop(minpos), True


def bruteForce(puzzle, positions):
    if len(positions) == 0:
        return puzzle
    copy = positions[:]
    k = getPossible(puzzle, copy)
    if k is None:
        return ""
    if not k[2]:
        for i in k[0]:
            copy2 = positions[:]
            copy2.remove(i)
            b = bruteForce(puzzle[0:i] + k[1] + puzzle[i + 1:], copy2)
            if b != "":
                return b
        return ""
    else:
        for i in k[0]:
            b = bruteForce(puzzle[0:k[1]] + i + puzzle[k[1] + 1:], copy)
            if b != "":
                return b
        return ""


def main():
    k = time.time()
    file = open(sys.argv[1])
    count = 1
    for line in file:
        z = time.time()
        periods = []
        puzzle = line[0:-1] if line[-1]=='\n' else line
        for i in range(len(puzzle)):
            if puzzle[i] == '.':
                periods.append(i)
        setglobals(puzzle)
        done = bruteForce(puzzle, periods)
        chk = checksum(done)
        print(
            "Puzzle Count: {}\n{}\n{}\nChecksum: {}\nTime: {}s".format(count, puzzle, done,
                                                                       chk, round(time.time() - z, 2)))
        count += 1
        # z = time.time()
        # periods = []
        # puzzle = "48.3............71.2.......7.5....6....2..8.............1.76...3.....4......5...."
        # for i in range(len(puzzle)):
        #     if puzzle[i] == '.':
        #         periods.append(i)
        # setglobals(puzzle)
        # done = bruteForce(puzzle, periods)
        # chk = checksum(done)
        # print(
        #     "Puzzle Count: {} {} {} Time: {}s Checksum: {}".format(count, puzzle, done, round(time.time() - z, 2),
        #                                                            chk))
    print("Time: {}s".format(round(time.time() - k, 2)))


if __name__ == "__main__":
    main()
