from typing import List, Dict

def position_is_available(position: Dict, queens: List) -> bool:
    """position is a bidimensional array where 0 is x and 1 is y"""
    if queens[0] is None:
        return True

    for row in range(position["y"]): # Vertical comparison
        if position["x"] == queens[row]["x"]:
            return False

        if abs(position["y"] - row) == abs(position["x"] - queens[row]["x"]): # Diagonal comparison
            return False

    return True


def place_queen(row, queens, n, solutions):
    if row == n:
        solutions.append(queens.copy())

    else:
        for col in range(n):
            position = {"x": col, "y": row}

            if position_is_available(position, queens):
                queens[row] = position
                place_queen(row + 1, queens, n, solutions)


def get_solutions(n):
    queens = [None] * 4
    solutions = []
    row = 0
    place_queen(row, queens, n, solutions)
    return solutions