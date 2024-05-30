from src.enums import ElementSubType, ElementType
from src.utils.classes import Position, Size
from src.utils.constants import BLOCK_HEIGHT, BLOCK_WIDTH
from src.utils.mappings import image_mappings

from ....abstractions import Element


class Block(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.OVERWORLD_BLOCK,
    ) -> None:
        super().__init__(
            position,
            Size(BLOCK_WIDTH, BLOCK_HEIGHT),
            image_mappings[ElementType.BLOCK][element_sub_type],
        )
