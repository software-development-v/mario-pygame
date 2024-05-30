from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Castle(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_CASTLE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.CASTLE][element_sub_type],
        )
