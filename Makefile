# Makefile for Jarvis-bubble project

.PHONY: help install test run clean lint format

help:
	@echo "Jarvis-bubble - Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make run          - Run Jarvis assistant"
	@echo "  make test         - Run unit tests"
	@echo "  make test-verbose - Run tests with verbose output"
	@echo "  make lint         - Check code style"
	@echo "  make format       - Format code"
	@echo "  make clean        - Clean up temporary files"
	@echo "  make demo-orb     - Demo the orb visualization"
	@echo "  make demo-config  - Demo the configuration system"

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Starting Jarvis Assistant..."
	python main.py

test:
	@echo "Running tests..."
	python -m unittest discover -s . -p "test_*.py"

test-verbose:
	@echo "Running tests (verbose)..."
	python -m unittest discover -s . -p "test_*.py" -v

lint:
	@echo "Checking code style..."
	python -m py_compile *.py
	@echo "✓ All files compile successfully"

format:
	@echo "Formatting code..."
	@python -m black . --line-length 100 2>/dev/null || echo "Install black: pip install black"

clean:
	@echo "Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info
	@echo "✓ Cleanup complete"

demo-orb:
	@echo "Running orb visualization demo..."
	python orb_visualization.py

demo-config:
	@echo "Running configuration demo..."
	python config_manager.py

demo-logger:
	@echo "Running logger demo..."
	python logger.py

# Development helpers
setup-dev:
	@echo "Setting up development environment..."
	pip install -r requirements.txt
	pip install black flake8 pytest

watch:
	@echo "Watching for changes..."
	@echo "Press Ctrl+C to stop"
	while true; do \
		clear; \
		python -m unittest discover -s . -p "test_*.py" 2>&1; \
		inotifywait -e modify -r . 2>/dev/null; \
	done
