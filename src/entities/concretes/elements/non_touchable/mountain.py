from src.enums import ElementSubType, ElementType
from src.utils.classes import Position, Size
from src.utils.constants import BLOCK_WIDTH, BLOCK_HEIGHT
from src.utils.mappings import image_mappings

from ....abstractions import Element


class Mountain(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.DEFAULT_MOUNTAIN,
    ) -> None:
        super().__init__(
            position,
            Size(BLOCK_WIDTH,BLOCK_HEIGHT),
            image_mappings[ElementType.MOUNTAIN][element_sub_type],
            is_touchable=False,
        )
