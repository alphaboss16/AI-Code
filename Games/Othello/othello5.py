import sys

global corner, near, edges
corner = {0, 7, 56, 63}
near = {0: [1, 8, 9], 7: [6, 14, 15], 56: [48, 49, 57], 63: [62, 54, 55]}
edges = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 8, 16, 24, 32, 40, 48, 56], [7, 15, 23, 31, 39, 47, 55, 63],
         [56, 57, 58, 59, 60, 61, 62, 63]]


def show_moves(board, turn):
    global convert, reverse
    opp = 'o' if turn == 'x' else 'x'
    moves = set()
    for i in range(len(board)):
        if board[i] == turn:
            if reverse[i][0] > 1:
                if board[convert[reverse[i][0] - 1][reverse[i][1]]] == opp:
                    row = reverse[i][0] - 2
                    col = reverse[i][1]
                    while row > -1:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row -= 1
            if reverse[i][0] < 6:
                if board[convert[reverse[i][0] + 1][reverse[i][1]]] == opp:
                    row = reverse[i][0] + 2
                    col = reverse[i][1]
                    while row < 8:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row += 1
            if reverse[i][1] > 1:
                if board[convert[reverse[i][0]][reverse[i][1] - 1]] == opp:
                    row = reverse[i][0]
                    col = reverse[i][1] - 2
                    while col > -1:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            col -= 1
            if reverse[i][1] < 6:
                if board[convert[reverse[i][0]][reverse[i][1] + 1]] == opp:
                    row = reverse[i][0]
                    col = reverse[i][1] + 2
                    while col < 8:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            col += 1
            if reverse[i][0] > 1 and reverse[i][1] > 1:
                if board[convert[reverse[i][0] - 1][reverse[i][1]] - 1] == opp:
                    row = reverse[i][0] - 2
                    col = reverse[i][1] - 2
                    while row > -1 and col > -1:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row -= 1
                            col -= 1
            if reverse[i][0] < 6 and reverse[i][1] > 1:
                if board[convert[reverse[i][0] + 1][reverse[i][1]] - 1] == opp:
                    row = reverse[i][0] + 2
                    col = reverse[i][1] - 2
                    while row < 8 and col > -1:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row += 1
                            col -= 1
            if reverse[i][0] < 6 and reverse[i][1] < 6:
                if board[convert[reverse[i][0] + 1][reverse[i][1]] + 1] == opp:
                    row = reverse[i][0] + 2
                    col = reverse[i][1] + 2
                    while row < 8 and col < 8:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row += 1
                            col += 1
            if reverse[i][0] > 1 and reverse[i][1] < 6:
                if board[convert[reverse[i][0] - 1][reverse[i][1]] + 1] == opp:
                    row = reverse[i][0] - 2
                    col = reverse[i][1] + 2
                    while row > -1 and col < 8:
                        if board[convert[row][col]] == '.':
                            moves.add(convert[row][col])
                            break
                        elif board[convert[row][col]] == turn:
                            break
                        elif board[convert[row][col]] == opp:
                            row -= 1
                            col += 1
    return moves


def play_to(pos, token, board):
    global convert, reverse
    turn = token
    opp = 'o' if turn == 'x' else 'x'
    row = reverse[pos][0]
    col = reverse[pos][1]
    play = {pos}
    if row - 1 > -1:
        if board[convert[row - 1][col]] == opp:
            crow = row - 1
            ccol = col
            temp = []
            s = False
            while crow > -1:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow -= 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if row + 1 < 8:
        if board[convert[row + 1][col]] == opp:
            crow = row + 1
            ccol = col
            temp = []
            s = False
            while crow < 8:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow += 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if col - 1 > -1:
        if board[convert[row][col - 1]] == opp:
            crow = row
            ccol = col - 1
            temp = []
            s = False
            while ccol > -1:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    ccol -= 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if col + 1 < 8:
        if board[convert[row][col + 1]] == opp:
            crow = row
            ccol = col + 1
            temp = []
            s = False
            while ccol < 8:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    ccol += 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if row + 1 < 8 and col - 1 > -1:
        if board[convert[row + 1][col - 1]] == opp:
            crow = row + 1
            ccol = col - 1
            temp = []
            s = False
            while crow < 8 and ccol > -1:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow += 1
                    ccol -= 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if row - 1 > -1 and col - 1 > -1:
        if board[convert[row - 1][col - 1]] == opp:
            crow = row - 1
            ccol = col - 1
            temp = []
            s = False
            while crow > -1 and ccol > -1:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow -= 1
                    ccol -= 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if row + 1 < 8 and col + 1 < 8:
        if board[convert[row + 1][col + 1]] == opp:
            crow = row + 1
            ccol = col + 1
            temp = []
            s = False
            while crow < 8 and ccol < 8:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow += 1
                    ccol += 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    if row - 1 > -1 and col + 1 < 8:
        if board[convert[row - 1][col + 1]] == opp:
            crow = row - 1
            ccol = col + 1
            temp = []
            s = False
            while crow > -1 and ccol < 8:
                if board[convert[crow][ccol]] == opp:
                    temp.append(convert[crow][ccol])
                    crow -= 1
                    ccol += 1
                elif board[convert[crow][ccol]] == token:
                    s = True
                    break
                elif board[convert[crow][ccol]] == '.':
                    s = False
                    break
            if s:
                for i in temp:
                    play.add(i)
    m = [*board]
    for i in range(len(m)):
        if i in play:
            m[i] = token
    return ''.join(m)


def check_neighbor(field, pos):
    global convert, reverse
    row = reverse[pos][0]
    col = reverse[pos][1]
    if row > 0:
        if field[convert[row - 1][col]] == '.':
            return True
        if col > 0:
            if field[convert[row][col - 1]] == '.':
                return True
            if field[convert[row - 1][col - 1]] == '.':
                return True
        if col < 7:
            if field[convert[row][col + 1]] == '.':
                return True
            if field[convert[row - 1][col + 1]] == '.':
                return True
    if row < 7:
        if field[convert[row + 1][col]] == '.':
            return True
        if col > 0:
            if field[convert[row + 1][col - 1]] == '.':
                return True
        if col < 7:
            if field[convert[row + 1][col + 1]] == '.':
                return True
    return False


def frontier(field, token):
    count = 0
    for i in range(len(field)):
        if field[i] == token:
            if check_neighbor(field, i):
                count += 1
    return count


def pick_ideal(moves, board, turn):
    opp = 'x' if turn == 'o' else 'o'
    for i in moves:
        if i in corner:
            return i
    temp = [x for x in moves]
    for i in corner:
        for j in near[i]:
            if j in moves:
                if board[i] == opp or board[i] == '.':
                    temp.remove(j)
    if len(temp) != 0:
        for i in temp:
            for j in edges:
                if i in j:
                    b = j.index(i)
                    if b != 1 or b != 6:
                        if board[b - 1] == opp:
                            count = 0
                            s = False
                            for k in range(b, len(j) - 1):
                                if board[j[k]] == opp:
                                    s = True
                                    break
                                elif board[j[k]] == turn:
                                    count = -1
                                    break
                                else:
                                    count += 1
                            if s and count % 2 == 1:
                                return i
                        if board[b + 1] == opp:
                            count = 0
                            s = False
                            for k in range(len(j) - 1, b - 1, -1):
                                if board[j[k]] == opp:
                                    s = True
                                    break
                                elif board[j[k]] == turn:
                                    count = -1
                                    break
                                else:
                                    count += 1
                            if s and count % 2 == 1:
                                return i
        tot = 0
        val = 99
        for i in range(len(temp)):
            t = play_to(temp[i], turn, board)
            b = frontier(t, turn)
            if b < val:
                tot = i
                val = b
        return temp[tot]

    else:
        tot = None
        val = 99
        for i in moves:
            t = play_to(i, turn, board)
            b = frontier(t, turn)
            if b < val:
                tot = i
                val = b
        return tot


def negamax(brd, tkn, level):
    global prev
    enemy = 'o' if tkn == 'x' else 'x'
    # return list of [guaranteed min score, reversed move score]
    if brd in prev:
        if tkn in prev[brd]:
            if len(prev[brd][tkn]) == 1:
                return prev[brd][tkn]
            return [prev[brd][tkn][0] * (-1)] + prev[brd][tkn][1:]
    moves = show_moves(brd, tkn)
    moves2 = show_moves(brd, enemy)
    if len(moves) == 0 and len(moves2) == 0:
        if brd not in prev:
            prev[brd] = {}
        if tkn not in prev[brd]:
            prev[brd][tkn] = [brd.count(tkn) - brd.count(enemy)]
        return [brd.count(tkn) - brd.count(enemy)]
    if len(moves) == 0:
        f = negamax(brd, enemy, level+1) + [-1]
        if brd not in prev:
            prev[brd] = {}
        if tkn not in prev[brd]:
            prev[brd][tkn] = f
        return [(-1) * f[0]] + f[1:]
    best = [len(brd)]
    if brd not in prev:
        prev[brd] = {}
    if tkn not in prev[brd]:
        for mv in moves:
            nm = negamax(play_to(mv, tkn, brd), enemy, level + 1) + [mv]
            if nm[0] < best[0]:
                best = nm
                if level == 1:
                    print("Score: {} {}".format((-1)*best[0], str(best[1:])))
        prev[brd][tkn] = best
    return [(-1) * best[0]] + best[1:]


def main():
    global convert, reverse, prev
    prev = {}
    if len(sys.argv) > 1:
        if len(sys.argv[1]) > 1:
            board = sys.argv[1].lower()
        else:
            board = '.' * 27 + "ox......xo" + '.' * 27
        if len(sys.argv) > 2:
            turn = sys.argv[2].lower()
        else:
            turn = 'x' if board.count('.') % 2 == 0 else 'o'


    else:
        board = '.' * 27 + "ox......xo" + '.' * 27
        turn = 'x'
    convert = [[x * 8 + y for y in range(8)] for x in range(8)]
    reverse = {}
    for i in range(len(convert)):
        for j in range(len(convert[i])):
            reverse[convert[i][j]] = (i, j)
    k = show_moves(board, turn)
    if len(k) == 0:
        print(board)
        print("No moves possible")
    else:
        z = pick_ideal(k, board, turn)
        # fin = [*board]
        # for i in k:
        #     fin[i] = '*'
        # print("".join(fin))
        print(k)
        print("My move is {}".format(z))
        if board.count('.') < 11:
            z = negamax(board, turn, 1)
            print("Score: {} {}".format(z[0], str(z[1:])))


if __name__ == '__main__':
    main()
