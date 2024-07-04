from src.enums import AnimationType, ElementSubType, ElementType
from src.utils import Position, elements

from ....abstractions import InteractiveElement


class Coin(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.COIN,
    ) -> None:
        super().__init__(
            position, elements[ElementType.COIN][element_sub_type], 100
        )

    def notify_observers(self) -> None:
        self._set_is_touchable(False)
        self.animation_oberservers.notify(
            (
                self,
                [AnimationType.COLLECTED_COIN, AnimationType.COLLECTED_SCORE],
            )
        )
        super().notify_observers()
        self.dispose()
