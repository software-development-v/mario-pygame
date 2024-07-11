from typing import List

from pygame import Rect

from src.entities import Element

from ...interfaces import IEnemy


class EnemyCollisionsHandler:
    def __init__(self, enemy: IEnemy):
        self.enemy = enemy

    def handle_collisions(
        self,
        enemy_rect: Rect,
        obstacles: List[Element],
        enemies: List[IEnemy],
        dx: float,
        dy: float,
    ) -> tuple[float, float]:
        dx = self.__handle_x_collisions(enemy_rect, obstacles, enemies, dx)
        dy = self.__handle_y_collisions(enemy_rect, obstacles, dy)
        return dx, dy

    def __handle_x_collisions(
        self,
        enemy_rect: Rect,
        obstacles: List[Element],
        enemies: List[IEnemy],
        dx: float,
    ) -> float:
        if dx == 0:
            return dx

        for obstacle in obstacles + enemies:
            if obstacle == self.enemy:
                continue

            if (
                isinstance(obstacle, Element)
                and not obstacle.get_is_touchable()
            ):
                continue

            obstacle_rect = obstacle.get_rect()

            if obstacle_rect.colliderect(
                enemy_rect.x + dx,
                enemy_rect.y,
                enemy_rect.width,
                enemy_rect.height,
            ):
                self.enemy.set_face_right(not self.enemy.get_face_right())
                return -dx

        return dx

    def __handle_y_collisions(
        self,
        enemy_rect: Rect,
        obstacles: List[Element],
        dy: float,
    ) -> float:
        if dy == 0:
            return dy

        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            obstacle_rect = obstacle.get_rect()

            if obstacle_rect.colliderect(
                enemy_rect.x,
                enemy_rect.y + dy,
                enemy_rect.width,
                enemy_rect.height,
            ):
                if dy > 0:  # Falling
                    return obstacle_rect.top - enemy_rect.bottom
                elif dy < 0:  # Moving upwards
                    return obstacle_rect.bottom - enemy_rect.top

        return dy
