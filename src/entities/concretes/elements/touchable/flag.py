from typing import Optional
from src.entities.concretes.hero import Hero
from src.entities.concretes.hero.interfaces.i_hero import IHero
from src.entities.interfaces.i_sprite import ISprite
from src.enums import ElementSubType, ElementType
from src.enums.collected_type import CollectedType
from src.enums.hero_action import HeroAction
from src.utils import Position, elements

from ....abstractions import InteractiveElement


class Flag(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.FLAG_PIPE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.FLAG][element_sub_type],
            x_rect_percent=(
                0.11 if element_sub_type == ElementSubType.FLAG_SUPPORT else 1
            ),
        )
        self.__points = self.__get_points()

    def __get_points(self) -> int:
        y_position = self.get_rect().y

        if 240 <= y_position <= 299:
            return 2000
        elif 300 <= y_position <= 359:
            return 1000
        elif 360 <= y_position <= 419:
            return 800
        elif 420 <= y_position <= 539:
            return 400
        elif 540 <= y_position <= 659:
            return 200
        elif 660 <= y_position:
            return 100
        else:
            return 5000

    def verify_x_player_position(self, hero: IHero):
        if hero.get_rect().x != 11811:
            hero.add_x_rect(-hero.get_rect().x)
            hero.add_x_rect(11811 + 30)

        if hero.get_rect().y < self.get_rect().y:
            hero.add_y_rect(-hero.get_rect().y)
            hero.add_y_rect(self.get_rect().y)

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        if isinstance(sprite, Hero) and not sprite.get_collided_win():
                sprite.set_action(HeroAction.WIN, True)
                self.verify_x_player_position(sprite)
                self.observers[CollectedType.COLLECTED_SCORE].update(self.__points)
                sprite.set_collided_win(True)
