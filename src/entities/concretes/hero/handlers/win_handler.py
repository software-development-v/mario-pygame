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
        elif (
            11890 <= self.__hero.get_rect().x < 12480
            and 660 <= self.__hero.get_rect().y <= 720
        ):
            self.__hero.set_face_right(True)
            self.__move_to_door()
            return True
        elif self.__hero.get_rect().x >= 12480:
            self.__hero.set_hero_state(HeroState.IDLE)
            self.__hero.set_vel_x(0)
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
        elif x_position == FLAG_POSITION or self.__is_near(self.__hero):
            self.__move_to_other_place_of_the_pipe(self.__hero)
            self.__hero.set_face_right(True)
            self.__hero.add_y_rect(9)
            self.__hero.set_actions(
                {
                    HeroAction.IDLE: False,
                    HeroAction.WIN: False,
                    HeroAction.JUMPING: False,
                    HeroAction.RUNNING: True,
                    HeroAction.DEAD: False,
                }
            )
            self.__hero.set_hero_state(HeroState.RUN)
            self.__hero.set_vel_x(-2)
        else:
            self.__hero.set_face_right(True)
            self.__move_to_door()

    def __is_near(self, hero: IHero) -> bool:
        x_position = hero.get_rect().x

        return (
            FLAG_POSITION - 20 <= x_position <= FLAG_POSITION + 10
            and hero.get_hero_level() is HeroLevel.NORMAL
            or hero.get_hero_level() is HeroLevel.BORRACHO_SMALL
        ) or (
            FLAG_POSITION - 60 <= x_position <= FLAG_POSITION + 10
            and hero.get_hero_level() is HeroLevel.BIG
            or hero.get_hero_level() is HeroLevel.COCA
            or hero.get_hero_level() is HeroLevel.BORRACHO_BIG
        )

    def __move_to_other_place_of_the_pipe(self, hero: IHero) -> None:
        if (
            hero.get_hero_level() is HeroLevel.NORMAL
            or hero.get_hero_level() is HeroLevel.BORRACHO_SMALL
        ):
            self.__hero.add_x_rect(60)
        else:
            self.__hero.add_x_rect(100)

    def __move_to_door(self) -> None:
        self.__hero.set_hero_state(HeroState.RUN)
        self.__hero.add_x_rect(2)
