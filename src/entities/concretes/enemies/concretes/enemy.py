from abc import ABC
from typing import Dict, List
from pygame import Surface
from src.enums import EnemyState
from src.utils import Position, Camera
from ...enemies.handlers import EnemyCollisionsHandler, EnemyMovementHandler
from ..interfaces import IEnemy
from ....abstractions import Element


class Enemy(IEnemy, ABC):
    def __init__(
        self,
        position: Position,
        enemyState: EnemyState,
        surfaces: Dict[EnemyState, List[Surface]],
    ):
        self.surfaces = surfaces
        self.state = enemyState
        self.face_right = True
        self.speed = 2
        self.vel_y = 0
        self.collisions_handler = EnemyCollisionsHandler(self)
        self.movement_handler = EnemyMovementHandler(self)
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.surfaces[self.state]

    def update(
        self, obstacles: List[Element], enemies: List[IEnemy], camera: Camera
    ):
        dx, dy = self.movement_handler.handle_movement(camera)
        dx, dy = self.collisions_handler.handle_collisions(
            self.get_rect(), obstacles, enemies, dx, dy
        )
        self.add_x_rect(dx)
        self.add_y_rect(dy)

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

    def kill(self):
        # Implement enemy removal logic here
        pass
