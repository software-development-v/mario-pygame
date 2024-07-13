from pygame import mixer

from src.entities import IElementObserver
from src.utils import COIN_LIMIT, COLLECTED_COIN_SOUND

from ..interfaces import ILevelManager


class CoinObserver(IElementObserver[int]):
    def __init__(self, level_manager: "ILevelManager") -> None:
        self.__level_manager = level_manager
        self.sound = mixer.Sound(COLLECTED_COIN_SOUND)

    def notify(self, value: int) -> None:
        self.sound.play()
        coins = self.__level_manager.get_coins()
        coins = coins + value
        if coins > COIN_LIMIT:
            self.__level_manager.set_lives(self.__level_manager.get_lives() + 1)
            coins = 0

        self.__level_manager.set_coins(coins)
