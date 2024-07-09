from src.enums import HeroAction, HeroLevel
from src.enums.hero_state import HeroState
from src.utils import FLAG_POSITION

from ..interfaces import IHero


class WinHandler:
    LIMIT_BIG = 650
    LIMIT_SMALL = 710

    def __init__(self, hero: IHero) -> None:
        self.__hero = hero

    def handle_win(self) -> bool:
        if self.__hero.get_actions()[HeroAction.WIN]:
            self.__hero_down()
            return True
        elif 11894 <= self.__hero.get_rect().x <= 12480 and self.__hero.get_rect().y == 720:
            self.__move_to_door()
            return True
        return False

    def __hero_down(self):
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
        elif x_position == FLAG_POSITION or self.__is_near(x_position):
            self.__hero.add_x_rect(60)
            self.__hero.set_face_right(True)
            self.__hero.add_y_rect(9)
            self.__hero.set_actions(
                {
                    HeroAction.IDLE: False,
                    HeroAction.WIN: False,
                    HeroAction.JUMPING: False,
                    HeroAction.RUNNING: True,
                }
            )
            self.__hero.set_hero_state(HeroState.RUN)
        else:
            self.__move_to_door()

    def __is_near(self, x_position: int) -> bool:
        return (
            FLAG_POSITION - 20 <= x_position <= FLAG_POSITION + 20
        )

    def __move_to_door(self) -> None:
        self.__hero.set_hero_state(HeroState.RUN)
        self.__hero.add_x_rect(5)
