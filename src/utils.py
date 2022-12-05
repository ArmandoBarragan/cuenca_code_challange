from typing import List
from src.settings.database import Session
from src.models.models import Solution, Position


def save_solutions(solutions: List, board_size: int, session: Session):
    for index, solution in enumerate(solutions):
        solution_instance = Solution(table_size=board_size)

        session.add(solution_instance)
        session.commit()
        session.refresh(solution_instance)

        for position in solution:
            position_instance = Position(
                x_position=position["x"],
                y_position=position["y"],
                solution_pk=solution_instance.id
            )
            session.add(position_instance)

    session.commit()


def format_solutions(solutions: List, session: Session) -> List:
    formatted_solutions = []

    for solution in solutions:
        formatted_solutions.append(
            session.query(Position).
            filter(Position.solution_pk == solution).all()
        )

    return formatted_solutions
