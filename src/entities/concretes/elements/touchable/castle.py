from src.enums import ElementSubType, ElementType
from src.utils import Position, elements

from ....abstractions import InteractiveElement


class Castle(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_CASTLE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.CASTLE][element_sub_type],
        )
        self.type_element = ElementType.CASTLE
