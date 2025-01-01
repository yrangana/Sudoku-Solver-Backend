[![Build Status](https://github.com/yrangana/Sudoku-Solver-Backend/actions/workflows/makefile.yml/badge.svg)](https://github.com/yrangana/Sudoku-Solver-Backend/actions/workflows/makefile.yml) 
[![Docker Build](https://github.com/yrangana/Sudoku-Solver-Backend/actions/workflows/validate_dockerfile.yml/badge.svg)](https://github.com/yrangana/Sudoku-Solver-Backend/actions/workflows/validate_dockerfile.yml)

## Overview
The Sudoku Solver Backend is a FastAPI-based application designed to solve Sudoku puzzles programmatically. It integrates with a core Sudoku solving library to provide solutions via RESTful API endpoints. This project is containerized with Docker, making it easy to deploy and test.

## Features
- **RESTful API**: Provides an endpoint to solve Sudoku puzzles.
- **Timeout Handling**: Ensures unsolvable puzzles don't hang the server.
- **Validation**: Validates puzzles to ensure they conform to Sudoku rules.
- **Dockerized Deployment**: Simplifies testing and deployment.
- **API Documentation**: Includes Swagger/OpenAPI documentation.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker (optional for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yrangana/Sudoku-Solver-Backend.git
   cd Sudoku-Solver-Backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   uvicorn app.main:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

4. Access the Swagger documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t sudoku-solver-backend .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 sudoku-solver-backend
   ```

3. Access the application at:
   ```
   http://127.0.0.1:8000
   ```

## Makefile Instructions

This project includes a `Makefile` to simplify common tasks. Below are the available commands:

- **Install dependencies**:
  ```bash
  make install
  ```

- **Run the application locally**:
  ```bash
  make run
  ```

- **Run tests**:
  ```bash
  make test
  ```

- **Build the Docker image**:
  ```bash
  make docker-build
  ```

- **Run the Docker container**:
  ```bash
  make docker-run
  ```

- **Clean up Docker artifacts**:
  ```bash
  make clean
  ```

## API Endpoints

### POST `/solve`
Solve a given Sudoku puzzle.

- **Request Body**:
  ```json
  {
    "puzzle": [
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
  }
  ```

- **Response**:
  ```json
  {
    "solved": true,
    "solution": [
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
  }
  ```

- **Errors**:
  - `400 Bad Request`: Invalid Sudoku puzzle.
  - `408 Request Timeout`: Puzzle solving exceeded timeout.

## Testing

### Run Tests
Execute the test suite using `pytest`:
```bash
pytest tests/
```

### Run Tests in Docker
To run tests inside a Docker container:
```bash
docker build -t sudoku-solver-backend-test .
docker run sudoku-solver-backend-test pytest tests/
```

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

