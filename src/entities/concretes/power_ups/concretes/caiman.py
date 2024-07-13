from src.enums import PowerUpType
from src.utils import Position, power_ups

from ...hero import IHero
from ..abstractions import PowerUp


class Caiman(PowerUp):
    def __init__(self, position: Position):
        super().__init__(position, power_ups[PowerUpType.CAIMAN])

    def _handle_collision(self, hero: IHero) -> None:
        hero.borracho()
