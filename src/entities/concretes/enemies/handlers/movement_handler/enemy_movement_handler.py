from src.enums import EnemyState
from src.utils import Camera

from ...interfaces import IEnemy


class EnemyMovementHandler:
    def __init__(self, enemy: IEnemy):
        self.enemy = enemy
        self.enemy.set_face_right(False)

    def handle_movement(self, camera: Camera) -> tuple[float, float]:
        dx, dy = 0, 0

        if self.enemy.get_state() == EnemyState.WALKING:
            if self.enemy.get_rect().right > camera.get_left_edge():
                speed = self.enemy.get_speed()
                dx = speed if self.enemy.get_face_right() else -speed

        dy = self.enemy.get_vel_y()
        self.enemy.add_vel_y(0.1)
        if self.enemy.get_vel_y() > 10:
            self.enemy.set_vel_y(10)

        return dx, dy
