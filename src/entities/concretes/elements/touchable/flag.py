from src.enums import ElementSubType, ElementType
from src.utils.classes import Position, Size
from src.utils.constants import TOUCHABLE_HEIGHT, TOUCHABLE_WIDTH
from src.utils.mappings import image_mappings

from ....abstractions import Element


class Flag(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_FLAG,
    ) -> None:
        super().__init__(
            position,
            Size(TOUCHABLE_WIDTH, TOUCHABLE_HEIGHT),
            image_mappings[ElementType.FLAG][element_sub_type],
        )
