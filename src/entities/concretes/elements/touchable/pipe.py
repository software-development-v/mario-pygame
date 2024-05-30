from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Pipe(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.SMALL_PIPE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.PIPE][element_sub_type],
        )
