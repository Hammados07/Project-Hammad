"""Shared helper: finds the labs/data and labs/output folders from any lab."""
from pathlib import Path

try:
    LABS = Path(__file__).resolve().parents[1]
except NameError:  # pasted into a notebook cell
    LABS = Path.cwd()
    if not (LABS / "data").exists() and (LABS.parent / "data").exists():
        LABS = LABS.parent

DATA = LABS / "data"
OUTPUT = LABS / "output"
OUTPUT.mkdir(exist_ok=True)
