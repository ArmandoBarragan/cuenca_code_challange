from typing import List, Dict
from pydantic import BaseModel, Field


class BoardSizePayloadSchema(BaseModel):
    size: int = Field(...)


class SolutionSchema(BaseModel):
    queens: List[Dict]


class AllSolutionsSchema(BaseModel):
    solutions: List[SolutionSchema]
