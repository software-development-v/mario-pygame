from src.utils.constants import GENERAL_HEIGHT
from ...abstractions.animation import Animation
from src.enums import ElementSubType,ElementType
from src.utils import Position, elements


class CollectedCoin(Animation):
    def __init__(self, position: Position):
        super().__init__(
            elements[ElementType.COIN][ElementSubType.COIN],
            transitions=[
                position,
                Position(position.x, position.y - (GENERAL_HEIGHT*3)),
                position,
            ],
            animation_interval=20,
        )
