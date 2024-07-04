from src.enums import HeroAction, HeroLevel
from src.utils import FLAG_POSITION

from ..interfaces import IHero


class WinHandler:
    LIMIT_BIG = 650
    LIMIT_SMALL = 710

    def __init__(self, hero: IHero) -> None:
        self.__hero = hero

    def handle_win(self) -> bool:
        if self.__hero.get_actions()[HeroAction.WIN]:
            self.__dow_hero()
            return True

        return False

    def __dow_hero(self):
        y_position = self.__hero.get_rect().y
        x_position = self.__hero.get_rect().x

        if (
            (
                self.__hero.get_hero_level() is HeroLevel.NORMAL
                or self.__hero.get_hero_level() is HeroLevel.BORRACHO_SMALL
            )
            and y_position < self.LIMIT_SMALL
        ) or (
            (
                self.__hero.get_hero_level() is HeroLevel.BIG
                or self.__hero.get_hero_level() is HeroLevel.COCA
                or self.__hero.get_hero_level() is HeroLevel.BORRACHO_BIG
            )
            and y_position < self.LIMIT_BIG
        ):
            self.__hero.set_vel_y(self.__hero.get_vel_y() + 0.4)
            self.__hero.add_y_rect(5)
        elif x_position == FLAG_POSITION or x_position == FLAG_POSITION - 2:
            self.__hero.add_x_rect(60)
            self.__hero.set_face_right(False)
            self.__hero.set_action(HeroAction.WIN, False)
