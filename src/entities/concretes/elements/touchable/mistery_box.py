from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class MisteryBox(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.MASTERY_BLOCK,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.MISTERY_BOX][element_sub_type],
        )
