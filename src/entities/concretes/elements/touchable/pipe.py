from src.enums import ElementSubType, ElementType
from src.utils import Position, elements

from ....abstractions import InteractiveElement


class Pipe(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.PIPE_HEAD_SMALL,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.PIPE][element_sub_type],
        )
