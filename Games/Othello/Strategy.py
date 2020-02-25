import sys


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
        val = -10000000000
        for i in range(len(temp)):
            t = play_to(temp[i], turn, board)
            b = heuristic(t, turn)
            if b > val:
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


def heuristic(brd, tkn):
    global convert, reverse
    my_tiles = 0
    opp_tiles = 0
    my_front_tiles = 0
    opp_front_tiles = 0
    V = [[] for i in range(8)]
    enemy = 'x' if tkn == 'o' else 'o'
    V[0] = [20, -3, 11, 8, 8, 11, -3, 20]
    V[1] = [-3, -7, -4, 1, 1, -4, -7, -3]
    V[2] = [11, -4, 2, 2, 2, 2, -4, 11]
    V[3] = [8, 1, 2, -3, -3, 2, 1, 8]
    V[4] = [8, 1, 2, -3, -3, 2, 1, 8]
    V[5] = [11, -4, 2, 2, 2, 2, -4, 11]
    V[6] = [-3, -7, -4, 1, 1, -4, -7, -3]
    V[7] = [20, -3, 11, 8, 8, 11, -3, 20]
    d = 0
    for i in range(8):
        for j in range(8):
            b = brd[convert[i][j]]
            if b == tkn:
                d += V[i][j]
                my_tiles += 1
            elif b == enemy:
                d -= V[i][j]
                opp_tiles += 1
    my_front_tiles = frontier(brd, tkn)
    opp_front_tiles = frontier(brd, enemy)
    if my_tiles > opp_tiles:
        p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
    elif opp_tiles > my_tiles:
        p = -(100.0 * my_tiles) / (my_tiles + opp_tiles)
    else:
        p = 0
    if my_front_tiles > opp_front_tiles:
        f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    elif opp_front_tiles > my_front_tiles:
        f = (100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    else:
        f = 0
    my_tiles = 0
    opp_tiles = 0
    if brd[convert[0][0]] == tkn:
        my_tiles += 1
    elif brd[convert[0][0]] == enemy:
        opp_tiles += 1
    if brd[convert[0][7]] == tkn:
        my_tiles += 1
    elif brd[convert[0][7]] == enemy:
        opp_tiles += 1
    if brd[convert[7][0]] == tkn:
        my_tiles += 1
    elif brd[convert[7][0]] == enemy:
        opp_tiles += 1
    if brd[convert[7][7]] == tkn:
        my_tiles += 1
    elif brd[convert[7][7]] == enemy:
        opp_tiles += 1
    c = 25 * (my_tiles - opp_tiles)
    my_tiles = opp_tiles = 0
    for i in near:
        for j in near[i]:
            if brd[j] == tkn:
                my_tiles += 1
            elif brd[j] == enemy:
                opp_tiles += 1
    l = -12.5 * (my_tiles - opp_tiles)
    my_tiles = len(show_moves(brd, tkn))
    opp_tiles = len(show_moves(enemy, tkn))
    if my_tiles > opp_tiles:
        m = (100.0 * my_tiles) / (my_tiles + opp_tiles)
    elif my_tiles < opp_tiles:
        m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        m = 0
    score = (10 * p) + (801.724 * c) + (382.026 * l) + (100000 * m) + (74.396 * f) + (10 * d)
    return score


def mid_alpha_beta(brd, tkn, level, lower, upper):
    global prev, saved_moves
    saved_lower = lower
    if (brd, tkn, lower, upper) in prev:
        return prev[(brd, tkn, lower, upper)]
    else:
        prev[(brd, tkn, lower, upper)] = {}
    enemy = 'o' if tkn == 'x' else 'x'
    if brd.count(enemy) == 0:
        return upper
    if level == 9:
        prev[(brd, tkn, lower, upper)] = [heuristic(brd, tkn)]
        return prev[(brd, tkn, lower, upper)]
    if (brd, tkn) in saved_moves:
        moves = saved_moves[(brd, tkn)]
    else:
        moves = show_moves(brd, tkn)
        saved_moves[(brd, tkn)] = moves
    best = [lower - 1]
    if len(moves) == 0:
        if (brd, enemy) in saved_moves:
            moves2 = saved_moves[(brd, enemy)]
        else:
            moves2 = show_moves(brd, enemy)
            saved_moves[(brd, enemy)] = moves2
        if len(moves2) == 0:
            prev[(brd, tkn, lower, upper)] = [heuristic(brd, tkn)]
            return prev[(brd, tkn, saved_lower, upper)]
        nm = mid_alpha_beta(brd, enemy, level + 1, (-1) * upper, (-1) * lower)
        score = (-1) * nm[0]
        if score > upper:
            prev[(brd, tkn, saved_lower, upper)] = [score]
            return prev[(brd, tkn, saved_lower, upper)]
        best = [score] + nm[1:] + [-1]
        prev[(brd, tkn, saved_lower, upper)] = best
        return best

    for mv in moves:
        nm = mid_alpha_beta(play_to(mv, tkn, brd), enemy, level + 1, (-1) * upper, (-1) * lower)
        score = (-1) * nm[0]
        if score > upper:
            prev[(brd, tkn, saved_lower, upper)] = [score]
            return prev[(brd, tkn, saved_lower, upper)]
        if score < lower:
            continue
        best = [score] + nm[1:] + [mv]
        # if level == 1:
        # print("Score: {} {}".format(best[0], str(best[1:])))
        lower = score + 1
    prev[(brd, tkn, saved_lower, upper)] = best
    return prev[(brd, tkn, saved_lower, upper)]


def alpha_beta(brd, tkn, level, lower, upper, submit=None, last=None):
    global fix, prev, saved_moves
    saved_lower = lower
    enemy = 'o' if tkn == 'x' else 'x'
    if (brd, tkn, lower, upper) in prev:
        return prev[(brd, tkn, lower, upper)]
    else:
        prev[(brd, tkn, lower, upper)] = {}
    if brd.count('x') == 0 or brd.count('o') == 0:
        prev[(brd, tkn, lower, upper)] = [brd.count(tkn) - brd.count(enemy)]
        return prev[(brd, tkn, lower, upper)]
    if (brd, tkn) in saved_moves:
        moves = saved_moves[(brd, tkn)]
    else:
        moves = show_moves(brd, tkn)
        saved_moves[(brd, tkn)] = moves
    best = [lower - 1]
    if len(moves) == 0:
        if (brd, enemy) in saved_moves:
            moves2 = saved_moves[(brd, enemy)]
        else:
            moves2 = show_moves(brd, enemy)
            saved_moves[(brd, enemy)] = moves2
        if len(moves2) == 0:
            prev[(brd, tkn, saved_lower, upper)] = [brd.count(tkn) - brd.count(enemy)]
            return prev[(brd, tkn, saved_lower, upper)]
        nm = alpha_beta(brd, enemy, level + 1, (-1) * upper, (-1) * lower)
        score = (-1) * nm[0]
        if score > upper:
            prev[(brd, tkn, saved_lower, upper)] = [score]
            return prev[(brd, tkn, saved_lower, upper)]
        best = [score]
        prev[(brd, tkn, saved_lower, upper)] = best
        return best

    for mv in moves:
        nm = alpha_beta(play_to(mv, tkn, brd), enemy, level + 1, (-1) * upper, (-1) * lower)
        score = (-1) * nm[0]
        if score > upper:
            prev[(brd, tkn, saved_lower, upper)] = [score]
            return prev[(brd, tkn, saved_lower, upper)]
        if score < lower:
            continue
        best = [score]
        if level == 1:
            best += [mv]
            submit.value = fix[mv]
        lower = score + 1
    prev[(brd, tkn, saved_lower, upper)] = best
    return prev[(brd, tkn, saved_lower, upper)]


class Strategy():
    global reverse, convert, saved_moves, prev, fix
    global corner, near, edges, cool
    corner = {0, 7, 56, 63}
    near = {0: [1, 8, 9], 7: [6, 14, 15], 56: [48, 49, 57], 63: [62, 54, 55]}
    edges = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 8, 16, 24, 32, 40, 48, 56], [7, 15, 23, 31, 39, 47, 55, 63],
             [56, 57, 58, 59, 60, 61, 62, 63]]
    global prev, saved_moves
    try:
        len(prev)
    except:
        prev = {}
    try:
        len(saved_moves)
    except:
        saved_moves = {}
    convert = [[x * 8 + y for y in range(8)] for x in range(8)]
    reverse = {}
    for i in range(len(convert)):
        for j in range(len(convert[i])):
            reverse[convert[i][j]] = (i, j)
    count = 0
    fix = {}
    for i in range(0, 10):
        for j in range(0, 10):
            b = i * 10 + j
            a = b // 10
            if a > 8 or a < 1:
                continue
            c = b % 10
            if c > 8 or c < 1:
                continue
            fix[count] = b
            count += 1
    cool = True

    def best_strategy(self, board, player, best_move, still_running=0):
        global prev, cool
        fix[-1] = -1
        brd = (''.join([x for x in [*board] if x != '?'])).replace('@', 'x')
        tkn = player.replace('@', 'x')
        m = show_moves(brd, tkn)
        if len(m) == 0:
            best_move.value = -1
        else:
            if board.count('.') > 14:
                best_move.value = fix[pick_ideal(m, brd, tkn)]
                best_move.value = fix[mid_alpha_beta(brd, tkn, 1, -100000000, 100000000)[-1]]
            else:
                if cool:
                    prev = {}
                    cool = False
                best_move.value = fix[pick_ideal(m, brd, tkn)]
                best_move.value = fix[alpha_beta(brd, tkn, 1, -64, 64, submit=best_move)[-1]]
