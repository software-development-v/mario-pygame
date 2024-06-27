from src.enums import HeroState
from src.utils import DEAD_FALL_THRESHOLD, SCREEN_HEIGHT

from ....interfaces import IHero
from ..interfaces import IDamageHandler


class DamageHandler(IDamageHandler):
    def __init__(self, hero: IHero) -> None:
        self.__hero = hero

    def handle_damage(self):
        if self.__hero.get_rect().top > SCREEN_HEIGHT + DEAD_FALL_THRESHOLD:
            self.__hero.set_hero_state(HeroState.DEAD)
