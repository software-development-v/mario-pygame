from src.enums.hero_state import HeroState
from ..interfaces import IHero


class DeadHandler:

    def __init__(self, hero: IHero) -> None:
        self.__hero = hero
        self.__jumped = False

    def handle_dead(self) -> bool:
        if self.__hero.get_hero_state() == HeroState.DEAD:
            self.__down_dead_hero()
            return True
        return False

    def __down_dead_hero(self) -> None:
        if not self.__jumped:
            self.__hero.add_vel_y(-40)
            self.__hero.add_y_rect(-100)
            self.__jumped = True
        else:
            if self.__hero.get_rect().y >= 900:
                self.__jumped = False
        self.__hero.add_y_rect(10)
        self.__hero.add_vel_y(90)
