from src.entities.abstractions.sprite import Sprite
from src.entities.concretes.hero import Hero
from src.enums import ElementSubType, ElementType
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

    def verify_x_player_position(self, hero: Hero):
        if hero.get_rect().x is self.get_rect().x:
            print("b")

    def notify_observers(self, sprite: Sprite) -> None:
        print("a")
        print("X:", sprite.get_rect().x, self.get_rect().x)
        print("Y:", sprite.get_rect().y, self.get_rect().y)
        if isinstance(sprite, Hero):
            if sprite.get_rect().x == 11811:
                sprite.hero_win()
                self.verify_x_player_position(sprite)
