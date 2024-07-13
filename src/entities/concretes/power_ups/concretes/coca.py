from src.enums import HeroLevel, PowerUpType
from src.utils import Position, power_ups

from ...hero import IHero
from ..abstractions import PowerUp


class Coca(PowerUp):
    def __init__(self, position: Position):
        super().__init__(position, power_ups[PowerUpType.COCA])

    def _handle_collision(self, hero: IHero) -> None:
        hero.grow(HeroLevel.COCA)
