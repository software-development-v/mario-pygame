from typing import List

from src.utils.camera import Camera

from ...entities import Element, IEnemy
from ..abstractions import SpritesManager


class EnemyManager(SpritesManager[IEnemy]):
    def __init__(
        self,
        enemies: List[IEnemy],
    ) -> None:
        self.__enemies = enemies
        super().__init__(enemies)

    def update(self, camera: Camera, obstacles: List[Element]):
        for enemy in self.__enemies:
            enemy.update(obstacles, self.__enemies, camera)
