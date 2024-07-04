from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies

from ...abstractions import Enemy


class Evoomba(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.EVOOMBA],
            position=position,
            initial_state=EnemyState.WALKING,
        )

    def update_state(self):
        pass
