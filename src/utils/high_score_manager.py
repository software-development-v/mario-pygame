from json import dump, load
from os import makedirs, path

from src.utils import HIGH_LEVEL_SCORE_FILE


def read_high_score() -> int:
    if not path.exists(HIGH_LEVEL_SCORE_FILE):
        write_high_score(0)
        return 0
    with open(HIGH_LEVEL_SCORE_FILE, "r") as file:
        data = load(file)
        return data.get("high_score", 0)


def write_high_score(high_score: int) -> None:
    makedirs(path.dirname(HIGH_LEVEL_SCORE_FILE), exist_ok=True)

    with open(HIGH_LEVEL_SCORE_FILE, "w") as file:
        dump({"high_score": high_score}, file)
