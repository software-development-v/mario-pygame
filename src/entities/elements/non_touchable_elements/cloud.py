from src.entities.elements.element import Element
from src.enums.element_types.cloud_sub_type import CloudSubTypeEnum
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class Cloud(Element):
    def __init__(
        self,
        x: int,
        y: int,
        type: CloudSubTypeEnum = CloudSubTypeEnum.SMALL_CLOUD,
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(100, 50),
            image_configurations[ImageConfigTypeEnum.CLOUD.value][type.value],
            is_touchable=False,
        )