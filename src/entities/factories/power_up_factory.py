from src.enums import PowerUpType
from src.utils import Position

from ..concretes import Caiman, Coca, IPowerUp, Pastel


class PowerUpFactory:
    def __init__(self) -> None:
        self.__factory = {
            PowerUpType.COCA: Coca,
            PowerUpType.CAIMAN: Caiman,
            PowerUpType.PASTEL: Pastel,
        }

    def create(
        self, position: Position, power_up_type: PowerUpType
    ) -> IPowerUp:
        power_up = self.__factory[power_up_type]

        return power_up(position)
