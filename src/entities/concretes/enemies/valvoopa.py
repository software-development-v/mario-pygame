from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies

from ...abstractions.enemy import Enemy


class Valvoopa(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            enemies[EnemyType.VALVOOPA],
            position,
            EnemyState.WALKING,
        )

    def update_state(self):
        pass
