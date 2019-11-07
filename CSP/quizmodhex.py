import sys


def isInvalid(puzzle, check):
    for i in range(len(puzzle)):
        if puzzle[i] != '.':
            for j in check[i]:
                count = 0
                for k in j:
                    if puzzle[k] == puzzle[i]:
                        count += 1
                    if count > 1:
                        return True
    return False


def verify(puzzle):
    count = 0
    for i in range(1, 7):
        if puzzle.count(convert[i]) == 5:
            count += 1
        if count > 2:
            return False
    return count == 2


def bruteForce(puzzle, choice, check):
    if isInvalid(puzzle, check):
        return ""
    elif puzzle.count('.') == 0 and verify(puzzle):
        return puzzle
    elif choice == 'A':
        k = puzzle.index('.')
        for i in range(1, 7):
            b = bruteForce(puzzle[0:k] + convert[i] + puzzle[k + 1:], choice, check)
            if b != "":
                return b
        return ""
    else:
        k = puzzle.index('.')
        for i in range(1, 8):
            b = bruteForce(puzzle[0:k] + str(i) + puzzle[k + 1:], choice, check)
            if b != "":
                return b
        return ""


def createbucks(type):
    if type == "B":
        groups = [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16],
                  [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23], [0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23], [5, 12, 13, 19, 20],
                  [0, 6, 7, 14, 15, 21, 22], [1, 2, 8, 9, 16, 17, 23], [3, 4, 10, 11, 18], [2, 5, 6, 0, 1],
                  [19, 13, 14, 7, 8, 2, 3], [20, 21, 15, 16, 9, 10, 4], [22, 23, 17, 18, 11]]
    else:
        groups = [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16],
                  [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]]
    toret = {i: [] for i in range(24)}
    for i in toret:
        for g in groups:
            if i in g:
                if toret[i] is None:
                    toret[i] = [g]
                else:
                    toret[i].append(g)
    return toret


def main():
    global convert
    convert = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"}
    if len(sys.argv) > 2:
        choice = sys.argv[2]
    else:
        choice = "A"
    puzzle = sys.argv[1]
    check = createbucks(choice)
    done = bruteForce(puzzle, choice, check)
    if done == "":
        print("No Solution")
    else:
        print(done)
        print(" " + done[:5])
        print(done[5:12])
        print(done[12:19])
        print(" " + done[19:])


if __name__ == "__main__":
    main()
