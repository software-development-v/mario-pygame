from src.entities.concretes.hero import Hero
from src.entities.concretes.hero.interfaces.i_hero import IHero
from src.entities.interfaces.i_sprite import ISprite
from src.enums import ElementSubType, ElementType
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

    def verify_x_player_position(self, hero: IHero):
        if not hero.get_rect().x == 11811:
            hero.add_x_rect(-hero.get_rect().x)
            hero.add_x_rect(11811 + 30)

        if hero.get_rect().y < self.get_rect().y:
            hero.add_y_rect(-hero.get_rect().y)
            hero.add_y_rect(self.get_rect().y)

    def notify_observers(self, hero: ISprite) -> None:
        if isinstance(hero, Hero):
            hero.set_action(HeroAction.WIN, True)
            self.verify_x_player_position(hero)
