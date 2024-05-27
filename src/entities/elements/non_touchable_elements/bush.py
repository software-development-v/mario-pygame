from src.entities.elements.element import Element
from src.enums.element_types.bush_sub_type import BushSubTypeEnum
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class Bush(Element):
    def __init__(
        self, x: int, y: int, type: str = BushSubTypeEnum.SMALL_BUSH.value
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(100, 50),
            image_configurations[ImageConfigTypeEnum.BUSH.value][type],
            is_touchable=False,
        )
