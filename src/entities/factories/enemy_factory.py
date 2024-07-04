from src.enums import EnemyType
from src.utils import Position

from ..abstractions.enemy import Enemy
from ..concretes.enemies.evoomba import Evoomba
from ..concretes.enemies.valvoopa import Valvoopa


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
