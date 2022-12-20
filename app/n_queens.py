from typing import List, Dict


def position_is_available(position: Dict, queens: List) -> bool:
    """position is a bi-dimensional array where 0 is x and 1 is y"""
    if queens[0] is None:
        return True

    for row in range(position["y"]):  # Vertical comparison
        if position["x"] == queens[row]["x"]:
            return False

        if abs(position["y"] - row) == abs(
            position["x"] - queens[row]["x"]
        ):  # Diagonal comparison
            return False

    return True


def place_queen(row, queens, n, solutions):
    """The main function to generate the solutions using recursion."""
    if row == n:
        solutions.append(queens.copy())
        return 1
    else:
        total_solutions = 0

        for col in range(n):
            position = {"x": col, "y": row}

            if position_is_available(position, queens):
                queens[row] = position
                total_solutions += place_queen(row + 1, queens, n, solutions)

        return total_solutions


def get_solutions(n):
    queens = [None for i in range(n)]
    solutions = []
    row = 0
    place_queen(row, queens, n, solutions)
    return solutions
