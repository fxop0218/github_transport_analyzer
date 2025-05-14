# run.py
import sys
import os

# Add app/ to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

from app.main import app

if __name__ == "__main__":
    # Pass CLI arguments from sys.argv
    app(prog_name="run.py")
