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

