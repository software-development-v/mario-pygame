from typing import List

from pygame import Rect

from src.entities import Element, InteractiveElement
from src.enums import HeroAction

from ....interfaces import IHero
from ..interfaces import ICollisionsHandler


class CollisionsHandler(ICollisionsHandler):
    def __init__(self, hero: IHero):
        self.hero = hero

    def __handle_x_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dx: float
    ) -> float:
        if dx == 0:
            return dx

        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            obstacle_rect: Rect = obstacle.get_rect()

            if not obstacle_rect.colliderect(
                hero_rect.x + dx, hero_rect.y, hero_rect.width, hero_rect.height
            ):
                continue

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers(self.hero)

            if dx > 0:
                dx = obstacle_rect.left - hero_rect.right
            elif dx < 0:
                dx = obstacle_rect.right - hero_rect.left

            break

        return dx

    def __handle_y_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dy: float
    ) -> float:
        if dy == 0:
            return dy

        floor_collide: bool = False

        for obstacle in obstacles:
            if not obstacle.get_is_touchable():
                continue

            obstacle_rect: Rect = obstacle.get_rect()

            if not obstacle_rect.colliderect(
                hero_rect.x, hero_rect.y + dy, hero_rect.width, hero_rect.height
            ):
                continue

            if self.hero.get_vel_y() < 0:
                dy = obstacle_rect.bottom - hero_rect.top
                self.hero.set_vel_y(0)
            elif self.hero.get_vel_y() >= 0:
                floor_collide = True
                dy = obstacle_rect.top - hero_rect.bottom
                self.hero.set_vel_y(0)
                self.hero.set_action(HeroAction.JUMPING, False)

            if isinstance(obstacle, InteractiveElement):
                obstacle.notify_observers(self.hero)

            break

        if not floor_collide:
            self.hero.set_action(HeroAction.JUMPING, True)

        return dy

    def handle_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dx: float, dy: float
    ) -> tuple[float, float]:
        dx = self.__handle_x_collisions(hero_rect, obstacles, dx)
        dy = self.__handle_y_collisions(hero_rect, obstacles, dy)
        return dx, dy
