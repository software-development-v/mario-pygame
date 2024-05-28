from src.enums import ElementSubType, ElementType
from src.utils.classes import Position, Size
from src.utils.constants import NON_TOUCHABLE_HEIGHT, NON_TOUCHABLE_WIDTH
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
            Size(NON_TOUCHABLE_WIDTH, NON_TOUCHABLE_HEIGHT),
            image_mappings[ElementType.MOUNTAIN][element_sub_type],
            is_touchable=False,
        )
