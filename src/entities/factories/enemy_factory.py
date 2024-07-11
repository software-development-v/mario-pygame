from src.enums import EnemyType
from src.utils import Position

from ..concretes import Enemy, Evoomba, Valvoopa


class EnemyFactory:
    def __init__(self) -> None:
        self.factory = {
            EnemyType.EVOOMBA: Evoomba,
            EnemyType.VALVOOPA: Valvoopa,
        }

    def create(
        self,
        enemy_type: EnemyType,
        position: Position,
    ) -> Enemy:
        enemy_class = self.factory[enemy_type]
        return enemy_class(position)
