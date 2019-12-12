import sys


def checkBlock(table, position, block, box):
    global rowcolconvert, reverse
    row = reverse[position][0]
    col = reverse[position][1]
    if (row + block[0]) > box[0] or (col + block[1]) > box[1]:
        return False
    for i in range(block[0]):
        for j in range(block[1]):
            if table[rowcolconvert[row + i][col + j]] != ".":
                return False
    return True


def getPossible(table, total, box, count):
    check = {}
    final = []
    for i in range(len(total)):
        if total[i][2] > count:
            return None
        for j in range(len(table)):
            if table[j] == '.':
                if checkBlock(table, j, total[i], box):
                    if total[i][3] not in check:
                        check[total[i][3]] = {j}
                    else:
                        check[total[i][3]].add(j)
        if total[i][3] in check:
            final.append((len(check[total[i][3]]), total[i], check[total[i][3]], i))
        if total[i][3] not in check and total[i][0]!=total[i][1]:
            opp = total[i][1], total[i][0], total[i][2], chr(ord(total[i][3]) + 1)
            for j in range(len(table)):
                if checkBlock(table, j, opp, box):
                    if opp[3] not in check:
                        check[opp[3]] = {j}
                    else:
                        check[opp[3]].add(j)
            if opp[3] in check:
                final.append((len(check[opp[3]]), opp, check[opp[3]], i))
            if opp[3] not in check and total[i][3] not in check:
                return ""
    return sorted(final)


def placeBlock(table, pos, block):
    global rowcolconvert, reverse
    row = reverse[pos][0]
    col = reverse[pos][1]
    k = list(table)
    for i in range(block[0]):
        for j in range(block[1]):
            k[rowcolconvert[row + i][col + j]] = block[3]
    return ''.join(k)


def print2d(board, x, y):
    for i in range(x):
        for j in range(y):
            print(board[y * i + j] if board[x * i + j] != ' ' else '-', end='', sep='')
        print()
    print()


def bruteForce(table, total, box, count):
    if len(total) == 0:
        return table
    k = getPossible(table, total, box, count)
    if k is None or len(k) == 0:
        return ""
    for j in k:
        copy = [(x[0], x[1], x[2], x[3]) for x in total]
        copy.pop(j[3])
        for b in j[2]:
            fix = placeBlock(table, b, j[1])
            #print2d(fix, box[0], box[1])
            z = bruteForce(fix, copy, box, count - j[1][2])
            if z != "" and z is not None:
                return z


def main():
    global rowcolconvert, reverse
    #enter = ['4x7', '7x4']
    enter = sys.argv[1:]
    b = None
    totalcontain = []
    reptodim = {}
    inc = 65
    s = 0
    for i in range(len(enter)):
        if b:
            totalcontain.append((int(b), int(enter[i]), int(b) * int(enter[i]), chr(inc)))
            reptodim[chr(inc)] = totalcontain[-1]
            s+=totalcontain[-1][2]
            inc += 1
            reptodim[chr(inc)] = totalcontain[-1][1], totalcontain[-1][0], totalcontain[-1][2], chr(inc)
            inc += 1
            b = None
        elif 'x' in enter[i] or 'X' in enter[i]:
            enter[i] = enter[i].lower()
            z = enter[i].index('x')
            totalcontain.append(
                (int(enter[i][:z]), int(enter[i][z + 1:]), int(enter[i][:z]) * int(enter[i][z + 1:]), chr(inc)))
            reptodim[chr(inc)] = totalcontain[-1]
            s+=totalcontain[-1][2]
            inc += 1
            reptodim[chr(inc)] = (totalcontain[-1][1], totalcontain[-1][0], totalcontain[-1][2], chr(inc))
            inc += 1
        else:
            b = enter[i]
    box = totalcontain.pop(0)
    table = '.' * box[2]
    if s-box[2]<=box[2]:
        rowcolconvert = [[x * box[1] + y for y in range(box[1])] for x in range(box[0])]
        reverse = {}
        for i in range(len(rowcolconvert)):
            for j in range(len(rowcolconvert[i])):
                reverse[rowcolconvert[i][j]] = (i, j)
        #print2d(table, box[0], box[1])
        bF = bruteForce(table, totalcontain, box, box[2])
        fin = []
        if bF is not None or bF:
            for i in bF:
                if i not in fin and i!='.':
                    fin.append(i)
                elif i =='.':
                    fin.append(i)
            reptodim['.']=(1, 1)
            print("Decomposition: ", end='')
            for j in fin:
                print(reptodim[j][0], reptodim[j][1], sep='x', end=' ')
        else:
            print("No Solution")
    else:
        print("No Solution")

if __name__ == '__main__':
    main()
