from typing import List

from src.entities import IHero

from ...entities import IPowerUp
from ..abstractions import SpritesManager


class PowerUpManager(SpritesManager[IPowerUp]):
    def __init__(
        self,
        power_ups: List[IPowerUp],
    ) -> None:
        self.__power_ups = power_ups
        super().__init__(self.__power_ups)

    def update(self, hero: IHero) -> None:
        for power_up in self.__power_ups:
            power_up.update(hero)

    def reset_power_ups(self) -> None:
        for power_up in self.__power_ups:
            power_up.reset()
