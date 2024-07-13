import time

from pygame import Rect

from src.enums import EnemyState, HeroState

from .....hero import IHero
from ....interfaces import IEnemy
from ..concretes import EnemyCollisionsHandler


class ValvoopaCollisionsHandler(EnemyCollisionsHandler):
    HERO_BOUNCE_VELOCITY = -20
    DISPOSE_DELAY = 1

    __slots__ = ("enemy", "dispose_time", "_temp_rect")

    def __init__(self, enemy: IEnemy):
        super().__init__(enemy)
        self._temp_rect = Rect(0, 0, 0, 0)
        self.enemy_state = EnemyState.DEAD

    def handle_hero_collision(self, hero: IHero) -> bool:
        if not self.enemy.get_is_touchable():
            return False

        enemy_rect = self.enemy.get_rect()
        hero_rect = hero.get_rect()

        self._temp_rect.update(hero_rect)

        if self._temp_rect.colliderect(enemy_rect):
            if (
                self._temp_rect.bottom < enemy_rect.centery
                and hero.get_hero_state() != HeroState.DEAD
            ):
                self.enemy.set_index(0)
                self.enemy.set_state(self.enemy_state)
                self.enemy.set_is_touchable(False)
                hero.set_vel_y(self.HERO_BOUNCE_VELOCITY)
                self.dispose_time = time.time() + self.DISPOSE_DELAY
                return False
            else:
                return True
        return False
