from typing import List

from app.schemas import BoardSizePayloadSchema, AllSolutionsSchema, SolutionSchema
from app.settings.database import Session
from app.models import Solution, Position
from app import n_queens


class APIController:
    def make_solutions(self, payload: BoardSizePayloadSchema):
        """Takes the board size and if the solutions for it are already in the database, it pulls them from it.
        Otherwise, it calls for the method get_solutions from n_queens."""
        with Session() as session:
            solutions = (
                session.query(Solution)
                .filter(Solution.table_size == payload.size)
                .all()
            )

            if len(solutions) != 0:
                return self.format_solutions(solutions, session)

            else:
                solutions = n_queens.get_solutions(payload.size)
                return self.save_solutions(solutions, payload.size, session)

    def save_solutions(self, solutions: List, board_size: int, session: Session) -> List:
        all_solutions = []

        for solution in solutions:
            solution_instance = Solution(table_size=board_size)

            session.add(solution_instance)
            session.commit()
            session.refresh(solution_instance)

            queens = []
            for position in solution:
                position_instance = Position(
                    x_position=position["x"],
                    y_position=position["y"],
                    solution_pk=solution_instance.id,
                )

                queens.append({"x": position["x"], "y": position["y"]})

                session.add(position_instance)
                all_solutions.append(SolutionSchema(queens=queens))

        session.commit()
        return all_solutions

    def format_solutions(self, solutions: List, session: Session) -> List:
        """Gives solutions the [[{}], [{}]] format when they were pulled from the database."""
        all_solutions = []

        for solution in solutions:
            positions = (
                session.query(Position)
                .filter(Position.solution_pk == solution.id)
                .all()
            )

            queens = []

            for position in positions:
                queens.append({"x": position.x_position, "y": position.y_position})

            all_solutions.append(SolutionSchema(queens=queens))

        return all_solutions
