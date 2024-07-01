from ...abstractions.animation import Animation
from src.enums import ElementSubType
from src.enums import ElementType
from src.utils import Position, elements


class CollectedCoin(Animation):
    def __init__(self, position: Position):
        super().__init__(
            elements[ElementType.COIN][ElementSubType.COIN],
            transitions=[
                position,
                Position(position.x, position.y - 200),
                position,
            ],
            animation_interval=20,
        )
