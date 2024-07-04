from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies
from ...abstractions.enemy import Enemy
from src.utils import ANIMATION_INTERVAL, Position


class Evoomba(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.EVOOMBA],
            position=position,
            initial_state=EnemyState.WALKING,
            animation_interval=ANIMATION_INTERVAL,
            x_rect_percent=1,
            y_rect_percent=1,
        )

    def update_state(self):
        pass
