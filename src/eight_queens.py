from typing import List, Dict
from pdb import set_trace

def position_is_available(position: Dict, queens: List) -> bool:
    """position is a bidimensional array where 0 is x and 1 is y"""
    if len(queens) == 0:
        return True

    for row in range(position["y"] + 1): # Vertical comparison
        # set_trace()
        if position["x"] == queens[row]["x"]:
            return False

        if abs(position["y"] - row) == abs(position["x"] - queens[row]["x"]): # Diagonal comparison
            return False

    return True


def position_queen(queens: List, n: int, row: int) -> Dict:
    for column in range(n - 1):
        position = {"x": column, "y": row}
        if position_is_available(position, queens):
            return position


def get_queens(n: int, solutions: List, queens: List)-> List:
    for i in range(n - 1):
        queens.append(position_queen(queens, n, i))

        if len(queens) < n:
            solutions = get_queens(n, solutions, queens)
        else:
            solutions.append(queens)

    return solutions


def get_solutions(n: int) -> List:
    solutions = get_queens(n, [], [])

    return solutions