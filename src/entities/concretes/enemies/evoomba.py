from src.enums.enemy_state import EnemyState
from src.enums.enemy_type import EnemyType
from src.utils import Position, enemies

from ...abstractions.enemy import Enemy


class Evoomba(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            enemies[EnemyType.EVOOMBA],
            position,
            EnemyState.WALKING,
        )

    def update_state(self):
        pass
