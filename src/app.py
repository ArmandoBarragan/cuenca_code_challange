from fastapi import FastAPI, HTTPException, status
from src.eight_queens.eight_queens import n_queens
from src.settings.database import Session
from src.models.models import Solution
from src.utils import save_solutions


app = FastAPI()


@app.post('/solutions/')
def get_solutions(board_size: int):
    if board_size < 4:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Board size has to be equal or greater than 4x4")


    with Session() as session:
        solutions = session.query(Solution).filter(Solution.table_size == board_size).all()

        if len(solutions) != 0:
            return solutions

        else:
            solutions = n_queens(board_size)
            save_solutions(solutions, board_size, session)

            return solutions