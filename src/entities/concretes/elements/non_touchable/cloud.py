from src.enums import ElementSubType, ElementType
from src.utils import Position, elements

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
            type_element = ElementType.CLOUD
        )
