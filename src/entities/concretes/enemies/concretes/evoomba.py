from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies

from ..handlers import EvoombaCollisionsHandler
from .enemy import Enemy


class Evoomba(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.EVOOMBA],
            position=position,
            enemyState=EnemyState.WALKING,
            collision_handler=EvoombaCollisionsHandler(self),
            value=100
        )

    def update_state(self):
        pass
