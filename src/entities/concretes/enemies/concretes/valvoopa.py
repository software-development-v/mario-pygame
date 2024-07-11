from .enemy import Enemy
from src.enums import EnemyState, EnemyType
from src.utils import Position, enemies


class Valvoopa(Enemy):
    def __init__(self, position: Position):
        super().__init__(
            surfaces=enemies[EnemyType.VALVOOPA],
            position=position,
            enemyState=EnemyState.WALKING,
        )

    def update_state(self):
        pass
