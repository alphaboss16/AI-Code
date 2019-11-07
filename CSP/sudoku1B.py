import time


def setglobals(puzzle):
    global N, SYMSET, subBlockHeight, subBlockWidth, CONSTRAINTS
    N = int(len(puzzle) ** .5)
    total = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    SYMSET = total[0:N]
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
    CONSTRAINTS = {x: set() for x in range(int(N ** 2))}
    for i in range(int(N ** 2)):
        for k in total:
            if i in k:
                for z in k:
                    CONSTRAINTS[i].add(z)



def isInvalid(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i] != '.':
            count = 0
            for j in CONSTRAINTS[i]:
                if puzzle[j] == puzzle[i]:
                    count += 1
                if count > 1:
                    return True
    return False

def checksum(puzzle):
    s = 0
    for i in range(len(puzzle)):
        s+=ord(puzzle[i])
    return s-48*(int(N**2))

def bruteForce(puzzle):
    if isInvalid(puzzle):
        return ""
    elif puzzle.count('.') == 0:
        return puzzle
    k = puzzle.index('.')
    for i in SYMSET:
        b = bruteForce(puzzle[0:k] + i + puzzle[k + 1:])
        if b != "":
            return b
    return ""


def main():
    k = time.time()
    file = open('puzzles.txt')
    count = 1
    for line in file:
        z = time.time()
        puzzle = line[:-1]
        setglobals(puzzle)
        done = bruteForce(puzzle)
        chk= checksum(done)
        print("Puzzle Count: {} {} Time: {}s Checksum: {}".format(count, done, round(time.time() - z, 2), chk))
        count += 1
    print("Time: {}".format(round(time.time() - k, 2)))


if __name__ == "__main__":
    main()
