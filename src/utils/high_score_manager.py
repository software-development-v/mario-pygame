import json
import os

from src.utils import HIGH_LEVEL_SCORE_FILE


def read_high_score() -> int:
    if not os.path.exists(HIGH_LEVEL_SCORE_FILE):
        create_high_score_file()
        return 0

    with open(HIGH_LEVEL_SCORE_FILE, "r") as file:
        data = json.load(file)
        return data.get("high_score", 0)


def write_high_score(high_score: int) -> None:
    create_high_score_file()
    with open(HIGH_LEVEL_SCORE_FILE, "w") as file:
        json.dump({"high_score": high_score}, file)

def create_high_score_file():
    os.makedirs(os.path.dirname(HIGH_LEVEL_SCORE_FILE), exist_ok=True)
