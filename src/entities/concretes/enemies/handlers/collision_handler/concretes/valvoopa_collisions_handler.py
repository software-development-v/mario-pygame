from ....interfaces import IEnemy
from ..concretes import EnemyCollisionsHandler
from .....hero import IHero
import time


class ValvoopaCollisionsHandler(EnemyCollisionsHandler):
    def __init__(self, enemy: IEnemy):
        super().__init__(enemy)

    def handle_hero_collision(self, hero: IHero) -> bool:
        if not self.enemy.get_is_touchable():
            return False

        enemy_rect = self.enemy.get_rect()
        hero_rect = hero.get_rect()
        if hero_rect.colliderect(enemy_rect):
            if hero_rect.bottom < enemy_rect.centery:
                self.enemy.kill()
                return False
            else:
                return True
        return False

    def check_dispose(self):
        if self.dispose_time and time.time() >= self.dispose_time:
            self.enemy.dispose()
            self.dispose_time = None
