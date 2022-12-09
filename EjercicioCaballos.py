from __future__ import annotations

def posicion(position: tuple[int, int], n:int) -> list[tuple[int, int]]:
    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]

    posiciones = []

    for position in positions:
        y_test, x_test = position
        if 0 <= y_test < n and 0 <= x_test < n:
            posiciones.append(position)
    
    return posiciones

def completado(board: list[list[int]]) -> bool:
    return not any (elemento ==0 for row in board for elemento in row)

def caballo_ayuda(board : list[list[int]], posi : tuple[int, int], curr: int)-> bool:

    if completado(board):
        return True

    for position in posicion(posi, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr +1
            if caballo_ayuda (board,position,curr +1):
                return True
            board[y][x]= 0
    return False

def caballo(n :int)-> list[list[int]]:
    board = [[0 for i in range(n)]for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j]= 1
            if caballo_ayuda(board,(i,j),1):
                return board
            board[i][j]= 0
            
    raise ValueError(f"No es posible realizar el movimiento {n}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

