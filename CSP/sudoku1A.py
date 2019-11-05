import sys
global N, SYMSET, subBlockHeight, subBlockWidth, CONSTRAINTS
def setglobals(puzzle):
    N=int(len(puzzle)**.5)
    total=["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    SYMSET=total[0:N]
    check=int(N ** .5)
    while N%check!=0:
        check-=1
    subBlockHeight=check
    subBlockWidth=N/subBlockHeight
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


def bruteForce(puzzle, choice, check):
    if isInvalid(puzzle, check):
        return ""
    elif puzzle.count('.') == 0:
        return puzzle
    elif choice == 'A':
        k = puzzle.index('.')
        for i in range(1, 7):
            b = bruteForce(puzzle[0:k] + str(i) + puzzle[k + 1:], choice, check)
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


def createbucks(puzzle):
    groups = []
    checker=[]
    sub=[]
    for i in range(N):
        sub=[]
        for j in range(N):
            sub.append(j*N+i)
        groups.append(sub)
    for i in range(N):
        sub=[]
        for j in range(N):
            sub.append(i*N+j)
        groups.append(sub)
    for i in range(N/subBlockHeight):
        for j in range(N/subBlockWidth):
            sub=[]
            for w in range(subBlockHeight):
                for z in range(subBlockWidth):
                    sub.append(w*z+)




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
        print(" "+done[:5])
        print(done[5:12])
        print(done[12:19])
        print(" "+done[19:])


if __name__ == "__main__":
    main()
