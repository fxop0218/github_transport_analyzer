@echo off

REM Create and activate virtual environment
python -m venv .venv
call .venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run default search
python run.py taxi -l python -s stars -n 5

REM Run tests
pytest -v
