from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Coin(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_COIN,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.COIN][element_sub_type],
        )
