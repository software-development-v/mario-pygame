from src.utils.constants import GENERAL_HEIGHT
from ...abstractions.animation import Animation
from src.enums import ElementSubType,ElementType
from src.utils import Position, elements


class CollectedCoin(Animation):
    def __init__(self, position: Position, height: float=GENERAL_HEIGHT*2):
        position.y-=GENERAL_HEIGHT
        super().__init__(
            elements[ElementType.COIN][ElementSubType.COIN],
            transitions=[
                position,
                Position(position.x, int(position.y - height)),
                position,
            ],
            animation_interval=20,
        )
