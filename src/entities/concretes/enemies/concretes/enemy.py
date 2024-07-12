from abc import ABC
from typing import Dict, List

from pygame import Rect, Surface

from src.enums import EnemyState
from src.utils import Camera, Position

from ....abstractions import Element
from ...enemies.handlers import EnemyMovementHandler
from ...enemies.handlers.collision_handler import IEnemyCollisionsHandler
from ..interfaces import IEnemy


class Enemy(IEnemy, ABC):
    def __init__(
        self,
        position: Position,
        enemyState: EnemyState,
        surfaces: Dict[EnemyState, List[Surface]],
        collision_handler: IEnemyCollisionsHandler,
    ):
        self.surfaces = surfaces
        self.state = enemyState
        self.initial_state = enemyState
        self.initial_position = position
        self.face_right = True
        self.__is_touchable = True
        self.speed = 2
        self.vel_y = 0
        self.collisions_handler = collision_handler
        self.movement_handler = EnemyMovementHandler(self)
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.surfaces[self.state]

    def get_state(self):
        return self.state

    def set_state(self, state: EnemyState):
        self.state = state

    def get_face_right(self):
        return self.face_right

    def set_face_right(self, face_right: bool):
        self.face_right = face_right

    def get_speed(self):
        return self.speed

    def get_vel_y(self):
        return self.vel_y

    def set_vel_y(self, vel_y: float):
        self.vel_y = vel_y

    def add_vel_y(self, vel_y: float):
        self.vel_y += vel_y

    def get_is_touchable(self) -> bool:
        return self.__is_touchable

    def _set_is_touchable(self, is_touchable: bool) -> None:
        self.__is_touchable = is_touchable

    def update(
        self, obstacles: List[Element], enemies: List[IEnemy], camera: Camera
    ):
        if self.state == EnemyState.GO_AWAY:
            return

        dx, dy = self.movement_handler.handle_movement(camera)
        dx, dy = self.collisions_handler.handle_collisions(
            self.get_rect(), obstacles, enemies, dx, dy
        )
        self.add_x_rect(dx)
        self.add_y_rect(dy)

    def get_hero_collision(self, hero_rect: Rect) -> bool:
        return self.collisions_handler.handle_hero_collision(hero_rect)

    def reset(self) -> None:
        self.state = self.initial_state
        self.set_rect(self.initial_position)
        self.face_right = False
        self.__is_touchable = True
        self.speed = 2
        self.vel_y = 0
        self.appear()

    def kill(self):
        self.__is_touchable = False
        self.disappear()
