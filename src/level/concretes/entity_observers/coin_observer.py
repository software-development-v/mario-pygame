from src.entities import IElementObserver
from ...interfaces.i_level_manager import ILevelManager
from src.utils import COIN_LIMIT

from pygame import mixer
from src.utils import COLLECTED_COIN_SOUND

class CoinObserver(IElementObserver[int]):
    def __init__(self, level_manager:ILevelManager) -> None:
        self.__level_manager = level_manager
        self.sound = mixer.Sound(COLLECTED_COIN_SOUND)

    def notify(self, value: int) -> None:
        self.sound.play()
        coins = self.__level_manager.get_coins()
        if coins <= COIN_LIMIT:
            self.__level_manager.set_coins(coins+value)
        else:
            self.__level_manager.set_lives(self.__level_manager.get_lives()+1)
            self.__level_manager.set_coins(0)


