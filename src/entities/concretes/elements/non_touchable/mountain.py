from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Mountain(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_MOUNTAIN,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.MOUNTAIN][element_sub_type],
            is_touchable=False,
            type_element = ElementType.MOUNTAIN
        )
