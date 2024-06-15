from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import InteractiveElement


class Block(InteractiveElement):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.OVERWORLD_BLOCK,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.BLOCK][element_sub_type],
        )
        self.type_element = ElementType.BLOCK
