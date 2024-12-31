# Install all required dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Run all tests with verbose output
test:
	python -m pytest -vv

# Run the FastAPI server
run:
	uvicorn app.main:app --reload

# Format code using Black
format:
	black app/*.py tests/*.py

# Lint code using Pylint
lint:
	pylint --disable=R,C app/*.py tests/*.py

# Clean up temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Display help information
help:
	@echo "Available commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run tests with pytest"
	@echo "  make run         - Start the FastAPI server"
	@echo "  make format      - Format code using Black"
	@echo "  make lint        - Lint code using Pylint"
	@echo "  make clean       - Remove temporary files"
	@echo "  make all         - Run install, lint, format, and test"

# Run all necessary tasks for development
all: help install lint format test
