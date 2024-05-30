from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Cloud(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.SMALL_CLOUD,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.CLOUD][element_sub_type],
            is_touchable=False,
        )
