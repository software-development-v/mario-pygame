from pygame import Rect

from ....interfaces import IEnemy
from ..concretes import EnemyCollisionsHandler


class ValvoopaCollisionsHandler(EnemyCollisionsHandler):
    def __init__(self, enemy: IEnemy):
        super().__init__(enemy)

    def handle_hero_collision(self, hero_rect: Rect) -> bool:
        enemy_rect = self.enemy.get_rect()
        if hero_rect.colliderect(enemy_rect):
            if hero_rect.bottom < enemy_rect.centery:
                self.enemy.kill()
                return False
            else:
                return True
        return False
