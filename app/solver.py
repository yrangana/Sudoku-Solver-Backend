from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
from src.solver import solve_sudoku_with_timeout as core_solve_sudoku


def solve_sudoku_with_timeout(puzzle, timeout=5):
    """
    Solve the Sudoku puzzle with a timeout using concurrent.futures.

    Args:
        puzzle (list): 9x9 Sudoku grid.
        timeout (int): Time limit in seconds.

    Returns:
        list[list[int]]: Solved Sudoku grid if solved within timeout.
        None: If unsolvable or timeout exceeded.
    """

    def solve():
        board = [row[:] for row in puzzle]
        if core_solve_sudoku(board):
            return board
        return None

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(solve)
        try:
            return future.result(timeout=timeout)
        except FutureTimeoutError:
            return None
