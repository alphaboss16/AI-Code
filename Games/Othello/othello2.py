import sys


def show_moves():
    global board, convert, turn, reverse
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

def play_on_board()

def main():
    global board, convert, turn, reverse
    for i in range(1,len(sys.argv)):
        if len(sys.argv[i])==64:
            board = sys.argv[i]
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
    k = show_moves()
    if len(k) == 0:
        print(board)
        print("No moves possible")
    else:
        fin = [*board]
        for i in k:
            fin[i] = '*'
        print("".join(fin))
        print(k)


if __name__ == '__main__':
    main()