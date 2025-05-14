#!/bin/bash

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run default search
python run.py taxi -l python -s stars -n 5

# Run tests
pytest -v
