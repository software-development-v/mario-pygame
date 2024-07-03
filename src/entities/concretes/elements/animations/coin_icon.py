from src.entities import Element
from src.enums import ElementSubType, ElementType
from src.utils import Position, elements


class CoinIcon(Element):

    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.COIN_ICON,
    ) -> None:
        super().__init__(
            position, elements[ElementType.COIN_ICON][element_sub_type]
        )
