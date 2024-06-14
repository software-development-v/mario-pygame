from src.enums import ElementSubType, ElementType
from src.utils.classes import Position
from src.utils.surfaces import elements

from ....abstractions import Element


class Tree(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.SMALL_TREE,
    ) -> None:
        super().__init__(
            position,
            elements[ElementType.TREE][element_sub_type],
            is_touchable=False,
        )
