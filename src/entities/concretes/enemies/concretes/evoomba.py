from .enemy import Enemy
from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies


class Evoomba(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.EVOOMBA],
            position=position,
            enemyState=EnemyState.WALKING,
        )

    def update_state(self):
        pass
