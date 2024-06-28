from src.entities import IElementObserver
from src.utils import COIN_LIMIT


class CoinObserver(IElementObserver):
    def __init__(self, value: int = 0) -> None:
        self.__value = value

    def update(self, value: int = 0) -> None:
        if self.__value <= COIN_LIMIT:
            self.__value += value
        else:
            self.__value = 0

    def get_value(self) -> int:
        return self.__value
