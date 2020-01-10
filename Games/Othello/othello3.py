import sys


def show_moves(turn):
    global board, convert, reverse
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


def play_to(pos, token):
    global board, convert, reverse
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
    return play


def print_board(game):
    global convert
    for i in convert:
        temp = []
        for j in i:
            temp.append(game[j])
        print(''.join(temp))


def main():
    global board, convert, turn, reverse
    convert = [[x * 8 + y for y in range(8)] for x in range(8)]
    reverse = {}
    for i in range(len(convert)):
        for j in range(len(convert[i])):
            reverse[convert[i][j]] = (i, j)
    board = None
    turn = None
    move = []
    translate = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) == 64:
            board = sys.argv[i].lower()
        elif sys.argv[i].lower() == 'x' or sys.argv[i].lower() == 'o':
            turn = sys.argv[i].lower()
        else:
            k = sys.argv[i].lower()
            if k[0] in translate:
                n = (int(k[1]) - 1) * 8 + translate[k[0]]
                move.append(n)
            elif int(k) > -1:
                n = int(k)
                move.append(n)
    if board is None:
        board = '.' * 27 + 'ox......xo' + '.' * 27
    if turn is None:
        if board.count('.') % 2 == 0:
            if len(show_moves('x')) > 0:
                turn = 'x'
            elif len(show_moves('o')) > 0:
                turn = 'o'
        else:
            if len(show_moves('o')) > 0:
                turn = 'o'
            elif len(show_moves('x')) > 0:
                turn = 'x'
    if len(move) == 0:
        k = show_moves(turn)
        fin = [*board]
        for i in k:
            fin[i] = '*'
        print_board("".join(fin))
        print("{} {}/{}".format(board, fin.count('x'), fin.count('o')))
        print("Possible Moves for {}: {}".format(turn, k))
    else:
        k = show_moves(turn)
        fin = [*board]
        for i in k:
            fin[i] = '*'
        print_board("".join(fin))
        print("{} {}/{}".format(board, fin.count('x'), fin.count('o')))
        print("Possible moves for {}: {}".format(turn, k))
        for j in move:
            print("{} plays to {}".format(turn, j))
            b = play_to(j, turn)
            fin = [*board]
            for i in b:
                fin[i] = turn
            board = ''.join(fin)
            k = show_moves('x' if turn == 'o' else 'o')
            if len(k) > 0:
                turn = 'x' if turn == 'o' else 'o'
                fin = [*board]
                for i in k:
                    fin[i] = '*'
                print_board("".join(fin))
                print("{} {}/{}".format(board, fin.count('x'), fin.count('o')))
                print("Possible moves for {}: {}".format(turn, k))
            else:
                b = show_moves(turn)
                if len(b) == 0:
                    print("{} {}/{}".format(board, fin.count('x'), fin.count('o')))
                    print_board(board)
                    break
                else:
                    fin = [*board]
                    for i in b:
                        fin[i] = '*'
                    print_board("".join(fin))
                    print("{} {}/{}".format(board, fin.count('x'), fin.count('o')))
                    print("Possible moves for {}: {}".format(turn, b))


if __name__ == '__main__':
    main()
