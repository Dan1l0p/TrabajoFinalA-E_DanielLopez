from __future__ import annotations

solucion = []

def pos_valida(board : list[list[int]], row: int, column: int) -> bool:
    for i in range(len(board)):
        if board[row][i]== 1:
            return False
    for i in range(len(board)):
        if board[i][column] ==1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j]== 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] ==1:
            return False
    return True

def resuelto(board: list[list[int]], row: int) -> bool:
    if row >= len(board):
        solucion.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        if pos_valida(board, row, i):
            board[row][i]= 1
            resuelto(board, row + 1)
            board[row][i] = 0
    return False

def printboard (board: list[list[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]== 1:
                print("R", end= "")
            else:
                print(".", end = "")
        print()

n = 8
board = [[0 for i in range(n)]for j in range(n)]
resuelto(board,0)
print("Las soluciones posibles son: ", len(solucion))

if __name__ =="__main__":
    import doctest
    doctest.testmod()
    printboard(10)