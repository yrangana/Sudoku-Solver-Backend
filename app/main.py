from fastapi import FastAPI, HTTPException
from app.models import SudokuRequest, SudokuResponse
from src.solver import solve_sudoku_with_timeout  # Import updated core logic

app = FastAPI()


@app.post("/solve", response_model=SudokuResponse)
def solve_puzzle(request: SudokuRequest, timeout: int = 5):
    """
    API endpoint to solve a Sudoku puzzle with optional timeout.
    """
    puzzle = request.puzzle

    try:
        solution = solve_sudoku_with_timeout(puzzle, timeout)
        if solution:
            return SudokuResponse(solved=True, solution=solution)
        else:
            return SudokuResponse(solved=False, solution=None)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))  # Invalid puzzle
    except TimeoutError:
        raise HTTPException(
            status_code=408, detail="The solver timed out before completing the puzzle."
        )
