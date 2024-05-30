from src.enums import ElementSubType, ElementType
from src.utils.classes import Position, Size
from src.utils.constants import BLOCK_HEIGHT, BLOCK_WIDTH
from src.utils.mappings import image_mappings

from ....abstractions import Element


class Pipe(Element):
    def __init__(
        self,
        position: Position,
        element_sub_type: ElementSubType = ElementSubType.SMALL_PIPE,
    ) -> None:
        size = Size(BLOCK_WIDTH*2, BLOCK_HEIGHT*2)
        if element_sub_type == ElementSubType.MEDIUM_PIPE:
            size = Size(BLOCK_WIDTH*2, BLOCK_HEIGHT*3)

        if element_sub_type == ElementSubType.BIG_PIPE:
            size = Size(BLOCK_WIDTH*2,BLOCK_HEIGHT*4)

        super().__init__(
            position,
            size,
            image_mappings[ElementType.PIPE][element_sub_type],
        )
