from ....interfaces import IEnemy
from .....hero import IHero
from ..concretes import EnemyCollisionsHandler
from src.enums import EnemyState
import time


class EvoombaCollisionsHandler(EnemyCollisionsHandler):
    def __init__(self, enemy: IEnemy):
        super().__init__(enemy)

    def handle_hero_collision(self, hero: IHero) -> bool:
        if not self.enemy.get_is_touchable():
            return False

        enemy_rect = self.enemy.get_rect()
        hero_rect = hero.get_rect()

        if hero_rect.colliderect(enemy_rect):
            if hero_rect.bottom < enemy_rect.centery:
                self.enemy.set_index(0)
                self.enemy.set_state(EnemyState.DEAD)
                self.enemy.set_is_touchable(False)
                hero.set_vel_y(-20)  # TODO: Improve jump managment
                self.dispose_time = time.time() + 1
                return False
            else:
                return True
        return False
