from typing import Optional

from src.enums import ElementSubType, ElementType, SpriteEventType
from src.utils import Position, elements

from ....abstractions import InteractiveElement
from ....interfaces import ISprite


class Coin(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.COIN,
    ) -> None:
        super().__init__(
            position, elements[ElementType.COIN][element_sub_type], 100
        )

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        self._set_is_touchable(False)
        self.notify_observer(
            (
                self,
                [
                    SpriteEventType.COLLECTED_COIN,
                ],
            )
        )
        self.dispose()
