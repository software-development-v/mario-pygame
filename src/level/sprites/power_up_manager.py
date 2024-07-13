from typing import List

from ...entities import IPowerUp
from ..abstractions import SpritesManager


class PowerUpManager(SpritesManager[IPowerUp]):
    def __init__(
        self,
        power_ups: List[IPowerUp],
    ) -> None:
        self.__power_ups = power_ups
        super().__init__(self.__power_ups)
