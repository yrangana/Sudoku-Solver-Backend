from pydantic import BaseModel, Field
from typing import List, Optional


class SudokuRequest(BaseModel):
    puzzle: List[List[int]] = Field(
        ..., description="A 9x9 Sudoku puzzle grid with integers 0-9"
    )


class SudokuResponse(BaseModel):
    solved: bool
    solution: Optional[List[List[int]]]
