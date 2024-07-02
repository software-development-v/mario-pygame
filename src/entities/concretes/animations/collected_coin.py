from ...abstractions.animation import Animation
from src.enums import ElementSubType,ElementType
from src.utils import Position, elements,GENERAL_HEIGHT


class CollectedCoin(Animation):
    def __init__(self, position: Position):
        position.y-=GENERAL_HEIGHT
        super().__init__(
            elements[ElementType.COIN][ElementSubType.COIN],
            transitions=[
                position,
                Position(position.x, int(position.y - (GENERAL_HEIGHT*2))),
                position,
            ],
            animation_interval=20,
        )
