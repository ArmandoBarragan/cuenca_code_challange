from sqlalchemy import Column, Integer, ForeignKey
from src.settings.settings import Base


class Solution(Base):
    __tablename__ = "solutions"
    id =  Column(Integer, primary_key=True)
    table_size = Column(Integer)


class Position(Base):
    __tablename__ = "positions"
    id =  Column(Integer, primary_key=True)
    x_position = Column(Integer)
    y_position = Column(Integer)
    solution_pk = Column(ForeignKey("solutions.id"))
