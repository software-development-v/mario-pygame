import json
import os

from src.utils import HIGH_LEVEL_SCORE_FILE


def read_high_score() -> int:
    if not os.path.exists(HIGH_LEVEL_SCORE_FILE):
        return 0
    with open(HIGH_LEVEL_SCORE_FILE, "r") as file:
        data = json.load(file)
        return data.get("high_score", 0)


def write_high_score(high_score: int) -> None:
    with open(HIGH_LEVEL_SCORE_FILE, "w") as file:
        json.dump({"high_score": high_score}, file)
