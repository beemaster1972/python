def convert_chess_2_list(addr: str) -> tuple:
    row = 8 - int(addr[1]) if addr[1].isdigit() else False
    column = ord(addr[0].lower()) - ord('a') if addr[0].isalpha() else False
    return (row, column)


def get_knight_moves(coord: tuple, chessboard: list) -> list:

    r = coord[0]  # row
    c = coord[1]  # column
    chessboard[r][c] = 'N'
    moves = []
    for i in (-2,2):
        for j in (-1,1):
            moves.append((r+i,c+j))
            moves.append((r+j,c+i))
    for move in moves:
        if 8 > move[0] >= 0 and 8 > move[1] >= 0 :
            chessboard[move[0]][move[1]] = '*'

board = [['.']*8 for i in range(8)]
get_knight_moves(convert_chess_2_list(input()), board)
for row in board:
    print(*row)

