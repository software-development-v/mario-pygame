from typing import List
from pygame import Surface, transform
from src.entities import Element
from src.enums import ElementSubType, ElementType
from src.utils import Position, elements, SMALL_SIZE


class CoinIcon(Element):

    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.COIN_ICON,
    ) -> None:
        sprites = elements[ElementType.COIN_ICON][element_sub_type]
        new_sprites: List[Surface] = []
        for sprite in sprites:
            new_sprites.append(transform.scale(sprite, SMALL_SIZE))
        super().__init__(position, new_sprites)

