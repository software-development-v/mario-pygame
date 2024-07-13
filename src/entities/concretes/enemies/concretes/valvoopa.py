from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies

from ..handlers import ValvoopaCollisionsHandler
from .enemy import Enemy


class Valvoopa(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.VALVOOPA],
            position=position,
            enemyState=EnemyState.WALKING,
            collision_handler=ValvoopaCollisionsHandler(self),
            value=200,
        )

    def update_state(self):
        pass
