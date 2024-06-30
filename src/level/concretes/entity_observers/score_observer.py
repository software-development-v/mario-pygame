from src.entities import IElementObserver
from src.utils import SCORE_LIMIT
from ...interfaces.i_level_manager import ILevelManager

class ScoreObserver(IElementObserver):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.__level_manager = level_manager

    def notify(self, value: object) -> None:
        if not isinstance(value, int):
            return
        
        score= self.__level_manager.get_score()
        if score < SCORE_LIMIT:
            self.__level_manager.set_score(score + value)

