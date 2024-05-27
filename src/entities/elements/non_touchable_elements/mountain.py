from src.entities.elements.element import Element
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.enums.element_types.mountain_sub_type import MountainSubTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class Mountain(Element):
    def __init__(
        self,
        x: int,
        y: int,
        type: MountainSubTypeEnum = MountainSubTypeEnum.DEFAULT_MOUNTAIN,
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(100, 50),
            image_configurations[ImageConfigTypeEnum.MOUNTAIN.value][
                type.value
            ],
            is_touchable=False,
        )
