from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies, ANIMATION_INTERVAL

from ...abstractions.enemy import Enemy


class Valvoopa(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.VALVOOPA],
            position=position,
            initial_state=EnemyState.WALKING,
            animation_interval=ANIMATION_INTERVAL,
            x_rect_percent=1,
            y_rect_percent=1,
        )

    def update_state(self):
        pass
