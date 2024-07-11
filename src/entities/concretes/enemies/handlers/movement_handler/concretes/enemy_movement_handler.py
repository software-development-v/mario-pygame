from src.enums import EnemyState
from src.utils import Camera

from ....interfaces import IEnemy
from ..interfaces import IEnemyMovementHandler


class EnemyMovementHandler(IEnemyMovementHandler):
    UPDATE_INTERVAL = 2

    def __init__(self, enemy: IEnemy):
        self.enemy = enemy
        self.enemy.set_face_right(False)
        self.is_active = False
        self.update_counter = 0

    def handle_movement(self, camera: Camera) -> tuple[float, float]:
        dx, dy = 0, 0

        self.update_counter += 1

        if self.update_counter % self.UPDATE_INTERVAL == 0:
            enemy_rect = self.enemy.get_rect()
            camera_left = camera.get_left_edge()
            camera_right = camera_left + (camera.viewport_width + 700)

            if (
                camera_left - 100 <= enemy_rect.right
                and enemy_rect.left <= camera_right + 100
            ):
                self.is_active = True
            else:
                self.is_active = False

            if self.is_active and self.enemy.get_state() == EnemyState.WALKING:
                speed = self.enemy.get_speed() * self.UPDATE_INTERVAL
                dx = speed if self.enemy.get_face_right() else -speed

        dy = self.enemy.get_vel_y()
        self.enemy.add_vel_y(0.1)
        if self.enemy.get_vel_y() > 10:
            self.enemy.set_vel_y(10)

        return dx, dy
