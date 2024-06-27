from src.entities import IElementObserver
from src.utils import SCORE_LIMIT
from src.utils.high_score_manager import read_high_score, write_high_score


class ScoreObserver(IElementObserver):
    def __init__(self, score: int = 0) -> None:
        self.__score = score
        self.__high_score = read_high_score()

    def update(self, value: int) -> None:
        if self.__score < SCORE_LIMIT:
            self.__score += value
        if self.__score > self.__high_score:
            self.__high_score = self.__score
            write_high_score(self.__high_score)

    def get_value(self) -> int:
        return self.__score

    def get_high_score(self) -> int:
        return self.__high_score
