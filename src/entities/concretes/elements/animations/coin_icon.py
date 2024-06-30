from typing import List
from pygame import Surface, transform
from src.entities import Element
from src.enums import ElementSubType, ElementType
from src.utils import Position, elements, Camera


class CoinIcon(Element):

    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.COIN_ICON,
    ) -> None:
        sprites = elements[ElementType.COIN_ICON][element_sub_type]
        new_sprites: List[Surface] = []
        for sprite in sprites:
            new_sprites.append(transform.scale(sprite, (30, 30)))
        super().__init__(position, new_sprites)

    def draw(
        self,
        screen: Surface,
        camera: Camera | None = None,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        self.animate()
        return super().draw(screen, camera, x_rect_percent, y_rect_percent)
