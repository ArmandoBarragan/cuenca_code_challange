from pydantic import BaseModel


class PositionSchema(BaseModel):
    x_position: int
    y_position: int

class SolutionSchema(BaseModel):
    