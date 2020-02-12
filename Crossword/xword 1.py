import sys
import re

global convert, reverse
table = {}
convert = {}
reverse = {}


def read_input():
    global convert, reverse
    dim = sys.argv[1]
    k = [int(x) for x in re.findall(r'\d+', dim)]
    m = []
    for i in range(k[0] * k[1]):
        m.append(i)
    rev = m[::-1]
    for i in range(len(m)):
        table[i] = rev[i]
    count = int(sys.argv[2])
    convert = [[x * k[1] + y for y in range(k[1])] for x in range(k[0])]
    reverse = {}
    for i in range(k[0]):
        for j in range(k[1]):
            reverse[convert[i][j]] = (i, j)
    return k, count


def add_implied(brd, dims):
    global convert, reverse
    t = set()
    for i in range(dims[0]):
        for j in range(dims[1]):
            if brd[convert[i][j]] == '#':
                if i + 3 >= dims[0]:
                    for z in range(1, 3):
                        if i + z < dims[0]:
                            if brd[convert[i + z][j]] == '-':
                                t.add(convert[i + z][j])

                if i - 3 < 0:
                    for z in range(1, 3):
                        if i - z > -1:
                            if brd[convert[i + z][j]] == '-':
                                t.add(convert[i + z][j])
                if j + 3 >= dims[1]:
                    for z in range(1, 3):
                        if j + z < dims[0]:
                            if brd[convert[i][j + z]] == '-':
                                t.add(convert[i][j + z])
                if j - 3 < 0:
                    for z in range(1, 3):
                        if j - z > -1:
                            if brd[convert[i][j - z]] == '-':
                                t.add(convert[i][j - z])
                up, down, left, right = set(), set(), set(), set()
                for m in range(1, 3):
                    if i + m < dims[0]:
                        if brd[convert[i + m][j]] == '-':
                            right.add(convert[i + m][j])
                        elif brd[convert[i + m][j]] == '#':
                            t = t.union(right)
                    if i - m > -1:
                        if brd[convert[i - m][j]] == '-':
                            left.add(convert[i - m][j])
                        elif brd[convert[i - m][j]] == '#':
                            t = t.union(left)
                    if j + m < dims[0]:
                        if brd[convert[i][j + m]] == '-':
                            up.add(convert[i][j + m])
                        elif brd[convert[i][j + m]] == '#':
                            t = t.union(up)
                    if j - m > -1:
                        if brd[convert[i][j - m]] == '-':
                            up.add(convert[i][j - m])
                        elif brd[convert[i][j - m]] == '#':
                            t = t.union(up)
    for i in t:
        brd[i] = '#'
    return brd


def achieve_constraints(dims):
    global convert, reverse
    to_place = sys.argv[4:]
    st = ['-' for x in range((dims[0] * dims[1]))]
    for i in to_place:
        orient = re.search(r'\w(?=\d)', i).group(0).lower()
        vert = int(re.search(r'\w\d*', i).group(0)[1:])
        horiz = int(re.search(r'x\d*', i).group(0)[1:])
        to_place = (re.search(r'\d[a-zA-Z#]*$', i).group(0)[1:]).lower()
        if to_place == '':
            to_place = '#'
        if orient == 'h':
            if horiz + len(to_place) < dims[1] and to_place != '#':
                to_place += '#'
            for b in range(len(to_place)):
                st[convert[vert][horiz + b]] = to_place[b]
        else:
            if vert + len(to_place) < dims[0] and to_place != '#':
                to_place += '#'
            for b in range(len(to_place)):
                st[convert[vert + b][horiz]] = to_place[b]
    # for i in range(dims[0]):
    #     for j in range(dims[1]):
    #         print(st[i * dims[1] + j], end='')
    #     print()
    f = add_implied(st, dims)
    return ''.join(f)


def main():
    b = read_input()
    z = achieve_constraints(b[0])
    if b[0][0] * b[0][1] == b[1]:
        print('#' * b[1])
    else:
        for i in range(b[0][0]):
            for j in range(b[0][1]):
                print(z[i * b[0][1] + j], end='')
            print()


if __name__ == '__main__':
    main()
