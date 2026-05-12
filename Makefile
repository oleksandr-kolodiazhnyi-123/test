# Makefile for Django Test Project development tasks

VENV_BIN = venv/bin

# Automatically use virtual environment binaries if they exist, otherwise fall back to system binaries
ifeq ($(wildcard $(VENV_BIN)/python),)
    PYTHON = python3
    PIP = pip3
    BLACK = black
    FLAKE8 = flake8
    ISORT = isort
    PYLINT = pylint
    PYTEST = pytest
else
    PYTHON = $(VENV_BIN)/python
    PIP = $(VENV_BIN)/pip
    BLACK = $(VENV_BIN)/black
    FLAKE8 = $(VENV_BIN)/flake8
    ISORT = $(VENV_BIN)/isort
    PYLINT = $(VENV_BIN)/pylint
    PYTEST = $(VENV_BIN)/pytest
endif

.PHONY: install dev test lint format migrate clean

install:
	python3 -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

dev:
	$(PYTHON) manage.py runserver

test:
	$(PYTEST)

lint:
	$(BLACK) --check .
	$(FLAKE8) .
	$(ISORT) --check-only .
	$(PYLINT) config/ tests/

format:
	$(BLACK) .
	$(ISORT) .

migrate:
	$(PYTHON) manage.py migrate

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .coverage htmlcov db.sqlite3 logs/*.log
