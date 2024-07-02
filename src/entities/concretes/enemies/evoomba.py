from src.enums import EnemyState, EnemyType
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
