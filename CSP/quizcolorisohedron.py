import sys

groups = {}
curr = set()
convert = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
x = 3


def isInvalid(puzzle, check):
    global groups
    if check == None:
        return False
    for k in groups[check]:
        if puzzle[check] == puzzle[k]:
            return True
    return False


def createbucks():
    global groups
    groups = {0: {1, 19, 10}, 1: {0, 2, 8}, 2: {1, 3, 6}, 3: {19, 4, 2}, 4: {5, 17, 3}, 5: {4, 6, 15}, 6: {7, 2, 5},
              7: {6, 8, 14}, 8: {9, 1, 7}, 9: {8, 13, 10}, 10: {9, 11, 0}, 11: {12, 18, 10}, 12: {16, 13, 11},
              13: {14, 9, 12}, 14: {7, 13, 15}, 15: {5, 14, 16}, 16: {12, 15, 17}, 17: {4, 16, 18}, 18: {17, 19, 11},
              19: {0, 3, 18}}


def bruteForce(puzzle, last):
    global convert
    global x
    if isInvalid(puzzle, last):
        return ""
    elif puzzle.count('.') == 0:
        return puzzle
    k = puzzle.index('.')
    for i in range(1, x + 1):
        b = bruteForce(puzzle[0:k] + convert[i] + puzzle[k + 1:], k)
        if b != "":
            return b
    return ""


def main():
    global x
    #x = int(sys.argv[1])
    check = createbucks()
    k = bruteForce("....................", None)
    print(k)


if __name__ == "__main__":
    main()
