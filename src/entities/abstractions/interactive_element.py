from typing import List, Optional

from pygame import Surface

from src.enums import SpriteEventType
from src.utils import Position

from ..interfaces import ISprite
from .element import Element


class InteractiveElement(Element):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        value: int = 0,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
        is_touchable: bool = True,
    ) -> None:
        super().__init__(
            position,
            images,
            x_rect_percent=x_rect_percent,
            y_rect_percent=y_rect_percent,
            is_touchable=is_touchable,
            value=value,
        )

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        if self.get_value() > 0:
            self.notify_observer((self, [SpriteEventType.COLLECTED_SCORE]))
