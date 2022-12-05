from fastapi import FastAPI, HTTPException, status
from src.eight_queens.eight_queens import n_queens
from src.settings.database import Session
from src.models import Solution
from src.utils import save_solutions, format_solutions


app = FastAPI()


@app.post('/solutions/',
          status_code=status.HTTP_200_OK)
def get_solutions(board_size: int):
    """ Takes the board size and if the solutions for it are already in the database, it pulls them from it.
    Otherwise, it calculates them and stores them."""
    if board_size < 4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Board size has to be equal or greater than 4x4")

    with Session() as session:
        solutions = session.query(Solution).filter(Solution.table_size == board_size).all()

        if len(solutions) != 0:
            return format_solutions(solutions, session)

        else:
            solutions = n_queens(board_size)
            save_solutions(solutions, board_size, session)
            return solutions