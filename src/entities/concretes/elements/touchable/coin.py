from src.enums import CollectedType, ElementSubType, ElementType
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
        super().notify_observers()
        self.observers[CollectedType.COLLECTED_COIN].update(1)
