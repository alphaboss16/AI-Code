import sys
import time


def set_look_up(win, height, width):
    global total
    convert = [[x * width + y for y in range(width)] for x in range(height)]
    sets = []
    for i in range(len(convert)):
        for j in range(len(convert[i])):
            if i + win <= height:
                temp = []
                for b in range(i, i + win):
                    temp.append(convert[b][j])
                sets.append(temp)
            if j + win <= width:
                temp = []
                for b in range(j, j + win):
                    temp.append(convert[i][b])
                sets.append(temp)
            if i + win <= height and j + win <= width:
                temp = []
                for b in range(win):
                    temp.append(convert[i + b][j + b])
                sets.append(temp)
            if i - win >= -1 and j + win <= width:
                temp = []
                for b in range(win):
                    temp.append(convert[i - b][j + b])
                sets.append(temp)
    total = {x: [] for x in range(width * height)}
    for i in range(width * height):
        for j in sets:
            if i in j:
                total[i].append(j)


def is_win(board, last):
    global total
    if last is not None:
        for j in total[last]:
            k = {board[x] for x in j}
            if len(k) == 1:
                if k == {'x'}:
                    return True, 'x'
                elif k == {'o'}:
                    return True, 'o'
    return False, None


def neighbors(board, lastmove):
    neighbors = []
    if lastmove == 'x':
        for i in range(len(board)):
            if board[i] == '.':
                neighbors.append((board[:i] + 'o' + board[i + 1:], i, 'o'))
    else:
        for i in range(len(board)):
            if board[i] == '.':
                neighbors.append((board[:i] + 'x' + board[i + 1:], i, 'x'))
    return neighbors


def recurse(board, lastmove, lastchanged, tofill):
    global cache, xwin, owin, end, ties
    if board in cache:
        return cache[board]
    z = is_win(board, lastchanged)
    if z[0]:
        if z[1] == 'x':
            xwin += 1
            end += 1
            cache[board] = 1
            return cache[board]
        else:
            owin += 1
            end += 1
            cache[board] = 1
            return cache[board]
    if tofill == 0:
        ties += 1
        end += 1
        cache[board] = 1
        return cache[board]
    else:
        z = neighbors(board, lastmove)
        s = 0
        for k in z:
            s += recurse(k[0], k[2], k[1], tofill - 1)
        cache[board] = s
        return s


def main():
    global cache, xwin, owin, end, ties
    m = time.time()
    cache = {}
    xwin = 0
    owin = 0
    end = 0
    ties = 0
    set_look_up(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    b = '.' * (int(sys.argv[2]) * int(sys.argv[3]))
    k = recurse(b, 'o', None, len(b))
    print("Number of Games: {}".format(k))
    print("Number of Boards: {}".format(len(cache)))
    print("Number of Terminal Boards: {}".format(end))
    print("Boards where X wins: {}".format(xwin))
    print("Boards where O wins: {}".format(owin))
    print("Boards with a tie: {}".format(ties))
    print("Time taken: {}s".format(round(time.time() - m, 3)))


if __name__ == '__main__':
    main()