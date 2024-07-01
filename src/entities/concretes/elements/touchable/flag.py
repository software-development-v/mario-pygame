from typing import Optional
from src.entities.concretes.hero import Hero
from src.entities.concretes.hero.interfaces.i_hero import IHero
from src.entities.interfaces.i_sprite import ISprite
from src.enums import ElementSubType, ElementType
from src.enums.collected_type import CollectedType
from src.enums.hero_action import HeroAction
from src.utils import Position, elements
from src.utils.constants import FLAG_POSITION

from ....abstractions import InteractiveElement


class Flag(InteractiveElement):

    FIRST_RANGE = [240, 299]
    SECOND_RANGE = [300, 359]
    THIRD_RANGE = [360, 419]
    FOURTH_RANGE = [420, 539]
    FIFTH_RANGE = [540, 659]
    FINAL_RANGE = 660

    SCORE_FIRST_RANGE = 2000
    SCORE_SECOND_RANGE = 1000
    SCORE_THIRD_RANGE = 800
    SCORE_FOURTH_RANGE = 400
    SCORE_FIFTH_RANGE = 200
    SCORE_FINAL_RANGE = 100
    SCORE_DEFAULT = 5000

    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.FLAG_PIPE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.FLAG][element_sub_type],
            x_rect_percent=(
                0.145 if element_sub_type == ElementSubType.FLAG_SUPPORT else 1
            ),
        )
        self.__points = self.__get_points()

    def __get_points(self) -> int:
        y_position = self.get_rect().y

        if self.FIRST_RANGE[0] <= y_position <= self.FIRST_RANGE[1]:
            return self.SCORE_FIRST_RANGE
        elif self.SECOND_RANGE[0] <= y_position <= self.SECOND_RANGE[1]:
            return self.SCORE_SECOND_RANGE
        elif self.THIRD_RANGE[0] <= y_position <= self.THIRD_RANGE[1]:
            return self.SCORE_THIRD_RANGE
        elif self.FOURTH_RANGE[0] <= y_position <= self.FOURTH_RANGE[1]:
            return self.SCORE_FOURTH_RANGE
        elif self.FIFTH_RANGE[0] <= y_position <= self.FIFTH_RANGE[1]:
            return self.SCORE_FIFTH_RANGE
        elif self.FINAL_RANGE <= y_position:
            return self.SCORE_FINAL_RANGE
        else:
            return self.SCORE_DEFAULT

    def verify_player_position(self, hero: IHero):
        if hero.get_rect().x > FLAG_POSITION:
            difference_position = hero.get_rect().x - FLAG_POSITION
            hero.add_x_rect(-difference_position)

        if hero.get_rect().y < self.get_rect().y:
            hero.add_y_rect(-hero.get_rect().y)
            hero.add_y_rect(self.get_rect().y)

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        if isinstance(sprite, Hero) and not sprite.get_collided_win():
            sprite.set_action(HeroAction.WIN, True)
            self.verify_player_position(sprite)
            self.observers[CollectedType.COLLECTED_SCORE].update(self.__points)
            sprite.set_collided_win(True)
            sprite.set_face_right(True)
