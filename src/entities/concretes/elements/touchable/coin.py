from src.enums import ElementSubType, ElementType
from src.enums import CollectedType
from src.utils import Position, elements
from pygame import mixer

from src.utils import COLLECTED_COIN_SOUND
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
        self.sound = mixer.Sound(COLLECTED_COIN_SOUND)

    def notify_observers(self) -> None:
        self.sound.play()
        super().notify_observers()
        self.observers[CollectedType.COLLECTED_COIN].update(1)
        self.dispose()
