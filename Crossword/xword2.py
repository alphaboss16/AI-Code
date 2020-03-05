import sys
import re
import random

global convert, reverse, words, to_fill
table = {}
convert = {}
reverse = {}
rev = []
words = 0
to_fill = {'-': [('', 0)] * 100000}
everything = set()
nice = 0


def count_vowels(word):
    return word.count('A') * 3 + word.count('E') * 3 + word.count('O') + word.count('R') + word.count(
        'S') * 2 + word.count(
        'T') - word.count('Q') * 3 - word.count('Z') * 2 - word.count('X') * 2 - word.count('J')


def print_board(dims, st):
    k = ""
    for i in range(dims[0]):
        for j in range(dims[1]):
            print(st[i * dims[1] + j], end='')
            k += st[i * dims[1] + j]
        print()
        k += "\n"
    return k


def read_input():
    global convert, reverse, rev
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


def add_implied(brd, dims, added=None):
    global convert, reverse
    temp = -1
    if len(brd) % 2 != 0:
        temp = len(brd) // 2
    t = set()
    if not added:
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
                                if brd[convert[i - z][j]] == '-':
                                    t.add(convert[i - z][j])
                    if j + 3 >= dims[1]:
                        for z in range(1, 3):
                            if j + z < dims[1]:
                                if brd[convert[i][j + z]] == '-':
                                    t.add(convert[i][j + z])
                    if j - 3 < 0:
                        for z in range(1, 3):
                            if j - z > -1:
                                if brd[convert[i][j - z]] == '-':
                                    t.add(convert[i][j - z])
                    up, down, left, right = set(), set(), set(), set()
                    for m in range(1, 4):
                        if i + m < dims[0]:
                            if brd[convert[i + m][j]] == '-':
                                down.add(convert[i + m][j])
                            elif brd[convert[i + m][j]] == '#':
                                t = t.union(down)
                        if i - m > -1:
                            if brd[convert[i - m][j]] == '-':
                                up.add(convert[i - m][j])
                            elif brd[convert[i - m][j]] == '#':
                                t = t.union(up)
                        if j + m < dims[1]:
                            if brd[convert[i][j + m]] == '-':
                                right.add(convert[i][j + m])
                            elif brd[convert[i][j + m]] == '#':
                                t = t.union(right)
                        if j - m > -1:
                            if brd[convert[i][j - m]] == '-':
                                left.add(convert[i][j - m])
                            elif brd[convert[i][j - m]] == '#':
                                t = t.union(left)
        for i in t:
            if brd[i] == '-':
                brd[i] = '#'
            elif brd[i] != "#":
                return None
        if temp in t:
            return brd, True, len(t)
        return brd, False, len(t)
    for d in added:
        i = reverse[d][0]
        j = reverse[d][1]
        if i + 3 >= dims[0]:
            for z in range(1, 3):
                if i + z < dims[0]:
                    if brd[convert[i + z][j]] == '-':
                        t.add(convert[i + z][j])
        if i - 3 < 0:
            for z in range(1, 3):
                if i - z > -1:
                    if brd[convert[i - z][j]] == '-':
                        t.add(convert[i - z][j])
        if j + 3 >= dims[1]:
            for z in range(1, 3):
                if j + z < dims[1]:
                    if brd[convert[i][j + z]] == '-':
                        t.add(convert[i][j + z])
        if j - 3 < 0:
            for z in range(1, 3):
                if j - z > -1:
                    if brd[convert[i][j - z]] == '-':
                        t.add(convert[i][j - z])
        up, down, left, right = set(), set(), set(), set()
        for m in range(1, 4):
            if i + m < dims[0]:
                if brd[convert[i + m][j]] != '#':
                    down.add(convert[i + m][j])
                elif brd[convert[i + m][j]] == '#':
                    t = t.union(down)
            if i - m > -1:
                if brd[convert[i - m][j]] != '#':
                    up.add(convert[i - m][j])
                elif brd[convert[i - m][j]] == '#':
                    t = t.union(up)
            if j + m < dims[1]:
                if brd[convert[i][j + m]] != '#':
                    right.add(convert[i][j + m])
                elif brd[convert[i][j + m]] == '#':
                    t = t.union(right)
            if j - m > -1:
                if brd[convert[i][j - m]] != '#':
                    left.add(convert[i][j - m])
                elif brd[convert[i][j - m]] == '#':
                    t = t.union(left)
        for i in t:
            if brd[i] == '-':
                brd[i] = '#'
            elif brd[i] != "#":
                return None
        # print_board(dims, brd)
    if temp in t:
        return brd, True, len(t)
    return brd, False, len(t)


def area_fill(brd, dims, r, c):
    global convert
    if not (r < 0 or c < 0 or r >= dims[0] or c >= dims[1] or brd[convert[r][c]] == '*' or brd[convert[r][c]] == "#"):
        brd[convert[r][c]] = '*'
        area_fill(brd, dims, r - 1, c)
        area_fill(brd, dims, r + 1, c)
        area_fill(brd, dims, r, c - 1)
        area_fill(brd, dims, r, c + 1)


def recurse(brd, count, dims):
    global convert, reverse, rev, words
    if count - brd.count('#') == 0:
        z = brd.index('-')
        m = [*brd]
        area_fill(m, dims, reverse[z][0], reverse[z][1])
        if m.count('*') == (brd.count('-') + words):
            return brd
        else:
            return None
    pos_list = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            if brd[convert[i][j]] == '-' and brd[rev[convert[i][j]]] == '-':
                x, y = i, j
                up, down, left, right = 0, 0, 0, 0
                x -= 1
                while x > -1:
                    if brd[convert[x][y]] != '#':
                        up += 1
                    else:
                        break
                    x -= 1
                x = i
                x += 1
                while x < dims[0]:
                    if brd[convert[x][y]] != '#':
                        down += 1
                    else:
                        break
                    x += 1
                y -= 1
                x = i
                while y > -1:
                    if brd[convert[x][y]] != '#':
                        left += 1
                    else:
                        break
                    y -= 1
                y = j
                y += 1
                while y < dims[1]:
                    if brd[convert[x][y]] != '#':
                        right += 1
                    else:
                        break
                    y += 1
                pos_list.append((up * down + left * right, i, j))
    pos_list.sort(reverse=True)
    for m in pos_list:
        i, j = m[1], m[2]
        refix = brd[0:convert[i][j]] + '#' + brd[convert[i][j] + 1:]
        refix = refix[0:rev[convert[i][j]]] + "#" + refix[rev[convert[i][j]] + 1:]
        b = add_implied([*refix], dims)
        if not b:
            continue
        fake = False
        for e in range(len(rev) // 2):
            if b[0][e] == '#':
                if b[0][rev[e]] != '#':
                    fake = True
                    break
            elif b[0][rev[e]] == '#':
                if b[0][e] != "#":
                    fake = True
                    break
        if count - b[0].count('#') < 0:
            continue
        if fake:
            continue
        if b[1]:
            b = add_implied(b[0], dims)
        z = b[0].index('-')
        m = [x for x in b[0]]
        area_fill(m, dims, reverse[z][0], reverse[z][1])
        if m.count('*') != (b[0].count('-') + words):
            continue
        temp = recurse(''.join(b[0]), count, dims)
        if temp:
            return temp
    # for i in range(dims[0]):
    #     for j in range(dims[1]):
    #         if brd[convert[i][j]] == '-' and brd[rev[convert[i][j]]] == '-':
    #             refix = brd[0:convert[i][j]] + '#' + brd[convert[i][j] + 1:]
    #             refix = refix[0:rev[convert[i][j]]] + "#" + refix[rev[convert[i][j]] + 1:]
    #             b = add_implied([*refix], dims)
    #             if not b:
    #                 continue
    #             fake = False
    #             for e in range(len(rev) // 2):
    #                 if b[0][e] == '#':
    #                     if b[0][rev[e]] != '#':
    #                         fake = True
    #                         break
    #                 elif b[0][rev[e]] == '#':
    #                     if b[0][e] != "#":
    #                         fake = True
    #                         break
    #             if fake:
    #                 continue
    #             if b[1]:
    #                 b = add_implied(b[0], dims)
    #             z = b[0].index('-')
    #             m = [x for x in b[0]]
    #             area_fill(m, dims, reverse[z][0], reverse[z][1])
    #             if m.count('*') != (b[0].count('-') + words):
    #                 continue
    #             if count - b[0].count('#') < 0:
    #                 continue
    #             temp = recurse(''.join(b[0]), count, dims)
    #             if temp:
    #                 return temp
    return None


def most_constrained(brd, dims):
    global convert, to_fill, everything
    best_word = '-'
    found_index = 0
    found = False
    total = []
    total_set = set()
    for i in range(dims[0]):
        row = brd[convert[i][0]:convert[i][dims[1] - 1] + 1]
        z = row.split('#')
        while '' in z:
            z.remove('')
        for j in range(len(z)):
            if z[j].count('-') == 0:
                if z[j] in everything:
                    total.append(z[j])
                    total_set.add(z[j])
                    continue
                else:
                    return None
            if z[j] != '':
                if z[j] in to_fill:
                    if len(to_fill[z[j]]) == 0:
                        return None
                    if len(to_fill[z[j]]) < len(to_fill[best_word]):
                        best_word = z[j]
                        found = True
                        found_index = j
                elif len(z[j]) > 5:
                    temp = z[j]
                    removed = []
                    for b in range(len(temp)):
                        if temp[b] != '-':
                            removed.append((temp[b], b))
                            temp = temp[0:b] + '-' + temp[b + 1:]
                            if temp in to_fill:
                                break
                        if temp.count('-') == len(temp) - 1:
                            break
                    check = {*to_fill[temp]}
                    combine = []
                    ensure = False
                    for rem in removed:
                        st = (rem[1]) * '-' + rem[0] + '-' * (len(z[j]) - rem[1] - 1)
                        if st in to_fill:
                            for u in to_fill[st]:
                                if u in check:
                                    combine.append(u)
                                    ensure = True
                        else:
                            to_fill[st] = []
                            return None
                        temp = temp[0:rem[1]] + rem[0] + temp[rem[1] + 1:]
                        if not ensure:
                            to_fill[temp] = []
                            return None
                        check = {*combine}
                        ensure = False
                        to_fill[temp] = sorted(combine, key=lambda x: x[1], reverse=True)
                    if len(to_fill[z[j]]) < len(to_fill[best_word]):
                        best_word = z[j]
                        found = True
                        found_index = j
                else:
                    return None
        if found:
            in_word = False
            starts = {}
            count = 0
            for b in range(len(row)):
                if row[b] != '#' and in_word is False:
                    in_word = True
                    starts[count] = b
                    count += 1
                if row[b] == '#' and in_word is True:
                    in_word = False
            found_index = (i, starts[found_index], 'H', best_word)
            found = False
    for i in range(dims[1]):
        col = ''.join([brd[convert[x][i]] for x in range(len(convert))])
        z = col.split('#')
        while '' in z:
            z.remove('')
        for j in range(len(z)):
            if z[j].count('-') == 0:
                if z[j] in everything:
                    total.append(z[j])
                    total_set.add(z[j])
                    continue
                else:
                    return None
            if z[j] != '':
                if z[j] in to_fill:
                    if len(to_fill[z[j]]) == 0:
                        return None
                    if len(to_fill[z[j]]) < len(to_fill[best_word]):
                        best_word = z[j]
                        found = True
                        found_index = j
                elif len(z[j]) > 5:
                    temp = z[j]
                    removed = []
                    for b in range(len(temp)):
                        if temp[b] != '-':
                            removed.append((temp[b], b))
                            temp = temp[0:b] + '-' + temp[b + 1:]
                        if temp in to_fill:
                            break
                        if temp.count('-') == len(temp) - 1:
                            break
                    check = {*to_fill[temp]}
                    combine = []
                    ensure = False
                    for rem in removed:
                        st = (rem[1]) * '-' + rem[0] + '-' * (len(z[j]) - rem[1] - 1)
                        if st in to_fill:
                            for u in to_fill[st]:
                                if u in check:
                                    combine.append(u)
                                    ensure = True
                        else:
                            to_fill[st] = []
                            return None
                        temp = temp[0:rem[1]] + rem[0] + temp[rem[1] + 1:]
                        if not ensure:
                            to_fill[temp] = []
                            return None
                        check = {*combine}
                        ensure = False
                        to_fill[temp] = sorted(combine, key=lambda x: x[1], reverse=True)
                    if len(to_fill[z[j]]) < len(to_fill[best_word]):
                        best_word = z[j]
                        found = True
                        found_index = j
                else:
                    return None
        if found:
            found = False
            in_word = False
            starts = {}
            count = 0
            for b in range(len(col)):
                if col[b] != '#' and in_word is False:
                    in_word = True
                    starts[count] = b
                    count += 1
                if col[b] == '#' and in_word is True:
                    in_word = False
            found_index = (starts[found_index], i, 'V', best_word)
    if len(total) == len(total_set):
        return found_index
    return None


def place_words(brd, dims, added):
    global to_fill, convert, reverse, everything, nice
    if brd.count('-') == 0:
        z = []
        found = set()
        for i in range(dims[0]):
            row = brd[convert[i][0]:convert[i][dims[1] - 1] + 1]
            z = row.split('#')
            while '' in z:
                z.remove('')
            for m in z:
                if m in found:
                    return None
                found.add(m)
                if m not in everything:
                    return None
        for j in range(dims[1]):
            col = ''.join([brd[convert[x][j]] for x in range(len(convert))])
            z = col.split('#')
            while '' in z:
                z.remove('')
            for m in z:
                if m in found:
                    return None
                found.add(m)
                if m not in everything:
                    return None
        print()
        print_board(dims, brd)
        return brd
    full = [*brd]
    b = most_constrained(brd, dims)
    if b is None:
        return None
    x, y = b[0], b[1]
    if b[2] == 'H':
        for r in range(len(to_fill[b[3]])):
            new_word = to_fill[b[3]][r][0]
            if new_word in added:
                continue
            for i in range(y, y + len(b[3])):
                full[convert[x][i]] = new_word[i - y]
            added.add(new_word)
            k = ''.join(full)
            if len(added)>nice:
                nice = len(added)
                print()
                print_board(dims, k)
            m = place_words(k, dims, added)
            if m is not None:
                return m
            added.remove(new_word)
            full = [*brd]
    else:
        for r in range(len(to_fill[b[3]])):
            new_word = to_fill[b[3]][r][0]
            if new_word in added:
                continue
            for i in range(x, x + len(b[3])):
                full[convert[i][y]] = new_word[i - x]
            added.add(new_word)
            k = ''.join(full)
            if len(added)>nice:
                nice = len(added)
                print()
                print_board(dims, k)
            m = place_words(k, dims, added)
            if m is not None:
                return m
            added.remove(new_word)
            full = [*brd]
    return None


def achieve_constraints(dims):
    global convert, reverse, rev, words
    to_place = sys.argv[4:]
    st = ['-' for x in range((dims[0] * dims[1]))]
    for i in to_place:
        orient = re.search(r'\w(?=\d)', i).group(0).lower()
        vert = int(re.search(r'\w\d*', i).group(0)[1:])
        horiz = int(re.search(r'x\d*', i).group(0)[1:])
        to_place = (re.search(r'\d[a-zA-Z#]*$', i).group(0)[1:]).upper()
        if to_place == '':
            to_place = '#'
        if orient == 'h':
            for b in range(len(to_place)):
                st[convert[vert][horiz + b]] = to_place[b]
        else:
            for b in range(len(to_place)):
                st[convert[vert + b][horiz]] = to_place[b]
    for i in range(len(rev)):
        if st[i] == "#":
            st[rev[i]] = '#'
    print_board(dims, st)
    f = add_implied(st, dims)
    if f[1]:
        f = add_implied(f[0], dims)
    print()
    words = len(re.findall(r'[a-zA-Z]', ''.join(f[0])))
    return ''.join(f[0])


done = set()


def get_subs(word):
    global done
    if word in done:
        return {}
    if word.count('-') == len(word):
        return {word}
    b = {word}
    done.add(word)
    for i in range(len(word)):
        if word[i] != '-':
            b = b.union(get_subs(word[0:i] + '-' + word[i + 1:]))
    return b


def save_dict(to_read, dims):
    global done, to_fill, everything
    f = open(to_read)
    k = ''.join(f.readlines()).split('\n')[:-1]
    for i in k:
        if (len(i) <= dims[0] or len(i) <= dims[1]) and len(i) > 2:
            i = i.upper()
            everything.add(i)
            m = (i, count_vowels(i))
            if len(i) <= 5:
                done = set()
                x = get_subs(i)
                for j in x:
                    if j in to_fill:
                        to_fill[j].append(m)
                    else:
                        to_fill[j] = [m]
            else:
                for j in range(len(i)):
                    st = len(i[0:j]) * '-' + i[j] + '-' * len(i[j + 1:])
                    if st in to_fill:
                        to_fill[st].append(m)
                    else:
                        to_fill[st] = [m]
                st = '-' * len(i)
                if st in to_fill:
                    to_fill[st].append(m)
                else:
                    to_fill[st] = [m]
    for i in to_fill:
        to_fill[i].sort(key=lambda b: b[1], reverse=True)


def count_words(brd, dims):
    global convert
    words = []
    for i in range(len(convert)):
        row = brd[convert[i][0]:convert[i][dims[1] - 1] + 1]
        z = row.split('#')
        for j in z:
            if j != '':
                words.append(len(j))
          
    # for i in range(len(convert[0])):
    #     col =''.join([brd[convert[x][i]] for x in range(len(convert))])
    #     z = col.split('#')
    #     for j in z:
    #         if j!='':
    #             words.append(j)
    return max(words)


def main():
    global convert, reverse, rev
    b = read_input()
    if b[0][0] * b[0][1] == b[1]:
        ans = '#' * b[1]
        print('#' * b[1])
    else:
        z = achieve_constraints(b[0])
        ans = z
        if z.count('#') != b[1]:
            ans = recurse(z, b[1], b[0])
            if not ans:
                m = [*z]
                d = m.index('-')
                area_fill(m, b[0], reverse[d][0], reverse[d][1])
                x = m.count('-')
                if x + m.count('#') <= b[1]:
                    for q in range(len(m)):
                        if m[q] == '*':
                            m[q] = z[q]
                        elif m[q] == '-':
                            m[q] = '#'
                    ans = recurse(''.join(m), b[1], b[0])
            print()
    print_board(b[0], ans)
    save_dict(sys.argv[3], b[0])
    dims = b[0]
    b = place_words(ans, b[0], set())
    print()
    print_board(dims, b)


if __name__ == '__main__':
    main()
