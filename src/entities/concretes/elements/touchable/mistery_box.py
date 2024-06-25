from src.enums import ElementSubType, ElementType
from src.utils import Position, elements

from ....abstractions import InteractiveElement


class MisteryBox(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_MISTERY_BOX,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.MISTERY_BOX][element_sub_type],
        )
        self.type_element = ElementType.MISTERY_BOX
