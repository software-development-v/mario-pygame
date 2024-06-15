from src.entities import IElementObserver
from src.utils.constants import SCORE_LIMIT

class ScoreObserver(IElementObserver):
    def __init__(self, score: int=0) -> None:
        self.__score = score

    def update(self, value: int) -> None:
        if(self.__score < SCORE_LIMIT):
            self.__score += value

    def get_value(self) -> int:
        return self.__score

