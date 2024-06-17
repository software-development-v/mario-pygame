from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import InteractiveElement


class Flag(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.FLAG_PIPE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.FLAG][element_sub_type],
        )
