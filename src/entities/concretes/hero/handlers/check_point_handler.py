from ..interfaces import IHero


class CheckPointHandler:
    def __init__(self, hero: IHero) -> None:
        self.__hero = hero

    def handle_check_point(self) -> None:
        check_point = self.__hero.get_check_point()

        if check_point is None:
            return

        if (
            self.__hero.get_rect().x > check_point.x
            and not self.__hero.get_reach_check_point()
        ):
            self.__hero.set_reach_check_point(True)
