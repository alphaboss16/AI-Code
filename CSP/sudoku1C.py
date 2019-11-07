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
    CONSTRAINTS = total

def isInvalid(puzzle):
    for j in CONSTRAINTS:
        count = 0
        m = set()
        for k in j:
            if puzzle[k]==".":
                count+=1
            m.add(puzzle[k])
        if count!= 0 and len(m)+count-1!=len(j):
            return True
        elif count ==0 and len(m)!=len(j):
            return True
    return False



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
