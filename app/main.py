from fastapi import FastAPI, HTTPException
from app.models import SudokuRequest, SudokuResponse
from src.solver import solve_sudoku_with_timeout, TimeoutException
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app.main")

@app.post("/solve", response_model=SudokuResponse)
def solve_puzzle(request: SudokuRequest, timeout: int = 5):
    puzzle = request.puzzle
    logger.info(f"Received puzzle: {puzzle} with timeout: {timeout}")

    try:
        solution = solve_sudoku_with_timeout(puzzle, timeout)
        if solution:
            logger.info("Puzzle solved successfully.")
            return SudokuResponse(solved=True, solution=solution)
        else:
            logger.warning("Solver returned no solution for the puzzle.")
            return SudokuResponse(solved=False, solution=None)
    except TimeoutException as e:
        logger.error(f"Solver timed out: {e}")
        raise HTTPException(
            status_code=408,
            detail="The solver timed out before completing the puzzle. "
                   "Try increasing the timeout or simplifying the puzzle."
        )
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while solving the puzzle."
        )
