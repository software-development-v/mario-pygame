from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import InteractiveElement


class Pipe(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.PIPE_HEAD,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.PIPE][element_sub_type],
        )
