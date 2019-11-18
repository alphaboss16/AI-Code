import sys

groups = {}
curr = set()


def isInvalid(puzzle, check):
    global groups
    for k in puzzle:
        if k == check:
            continue
        if k in groups[check]:
            return True
    return False


def createbucks():
    global groups
    groups = {0: {1, 19, 10}, 1: {0, 2, 8}, 2: {1, 3, 6}, 3: {19, 4, 2}, 4: {5, 17, 3}, 5: {4, 6, 15}, 6: {7, 2, 5},
              7: {6, 8, 14}, 8: {9, 1, 7}, 9: {8, 13, 10}, 10: {9, 11, 0}, 11: {12, 18, 10}, 12: {16, 13, 11},
              13: {14, 9, 12}, 14: {7, 13, 15}, 15: {5, 14, 16}, 16: {12, 15, 17}, 17: {4, 16, 18}, 18: {17, 19, 11},
              19: {0, 3, 18}}



def bruteForce(puzzle, check):
    global curr
    if isInvalid(puzzle, check) or len(puzzle)>20:
        return ""
    if len(puzzle) > len(curr):
        curr = puzzle
    for i in range(0, 20):
        if i not in puzzle:
            copy = set(puzzle)
            copy.add(i)
            b = bruteForce(copy, i)


def main():
    check = createbucks()
    bruteForce(set(), 0)
    print(curr)


if __name__ == "__main__":
    main()
