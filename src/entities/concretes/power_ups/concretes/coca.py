from src.enums import PowerUpType
from src.utils import Position, power_ups

from ..abstractions import PowerUp


class Coca(PowerUp):
    def __init__(self, position: Position):
        super().__init__(position, power_ups[PowerUpType.COCA])
