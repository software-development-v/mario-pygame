from typing import List

from pygame import Rect

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

    def if_there_a_collide_with_enemy(
        self,
        hero_rect: Rect,
    ) -> bool:
        for enemy in self.__enemies:
            if enemy.get_hero_collision(hero_rect):
                return True
        return False

    def reset_enemies(self) -> None:
        for enemy in self.__enemies:
            enemy.reset()
