install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	pytest

run:
	uvicorn app.main:app --reload

format:
	black app tests

lint:
	pylint app tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete