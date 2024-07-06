from typing import Optional

from src.enums import CollectedType, ElementSubType, ElementType, HeroAction
from src.utils import FLAG_POSITION, Position, elements

from ....abstractions import InteractiveElement
from ....interfaces import ISprite
from ...hero import Hero, IHero


class Flag(InteractiveElement):
    RANGES = [
        (240, 299),  # FIRST FLAG POSITION
        (300, 359),  # SECOND FLAG POSITION
        (360, 419),  # THIRD FLAG POSITION
        (420, 539),  # FOURTH FLAG POSITION
        (540, 659),  # FIFTH FLAG POSITION
        (660, 0),  # FINAL FLAG POSITION
    ]

    SCORES = [
        2000,  # SCORE FIRST RANGE
        1000,  # SCORE SECOND RANGE
        800,  # SCORE THIRD RANGE
        400,  # SCORE FOURTH RANGE
        200,  # SCORE FIFTH RANGE
        100,  # SCORE FINAL RANGE
    ]

    DEFAULT_SCORE = 5000

    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.FLAG_PIPE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.FLAG][element_sub_type],
            x_rect_percent=self.__define_x_collider(element_sub_type),
            is_touchable=(
                False if element_sub_type is ElementSubType.FLAG_WIN else True
            ),
        )
        self.__points = self.__get_points()
        self.__element_sub_type = element_sub_type

    def __define_x_collider(self, subtype: ElementSubType) -> float:
        collider = 1
        if subtype is ElementSubType.FLAG_SUPPORT:
            collider = 0.145
        elif subtype is ElementSubType.FLAG_LIMITER:
            collider = 0.45
        return collider


    def __get_points(self) -> int:
        y_position = self.get_rect().y

        if self.RANGES[0][0] <= y_position <= self.RANGES[0][1]:
            return self.SCORES[0]
        elif self.RANGES[1][0] <= y_position <= self.RANGES[1][1]:
            return self.SCORES[1]
        elif self.RANGES[2][0] <= y_position <= self.RANGES[2][1]:
            return self.SCORES[2]
        elif self.RANGES[3][0] <= y_position <= self.RANGES[3][1]:
            return self.SCORES[3]
        elif self.RANGES[4][0] <= y_position <= self.RANGES[4][1]:
            return self.SCORES[4]
        elif self.RANGES[5][0] <= y_position:
            return self.SCORES[5]
        else:
            return self.DEFAULT_SCORE

    def __fix_hero_position(self, hero: IHero):
        if self.__element_sub_type is ElementSubType.FLAG_SUPPORT:
            hero.add_y_rect(-61)
        else:

            if hero.get_rect().x > FLAG_POSITION:
                difference_position = hero.get_rect().x - FLAG_POSITION
                hero.add_x_rect(-difference_position)

            if hero.get_rect().y < self.get_rect().y:
                hero.add_y_rect(-hero.get_rect().y)
                hero.add_y_rect(self.get_rect().y)

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        if isinstance(sprite, Hero) and not sprite.get_collided_win():
            sprite.set_action(HeroAction.WIN, True)
            self.__fix_hero_position(sprite)
            self.get_observer()[CollectedType.COLLECTED_SCORE].notify(
                self.__points
            )
            sprite.set_collided_win(True)
            sprite.set_face_right(True)
