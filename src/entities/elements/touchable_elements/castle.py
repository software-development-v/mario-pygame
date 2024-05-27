from src.entities.elements.element import Element
from src.enums.element_types.castle_sub_type import CastleSubTypeEnum
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class Castle(Element):
    def __init__(
        self,
        x: int,
        y: int,
        type: str = CastleSubTypeEnum.DEFAULT_CASTLE.value,
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(50, 50),
            image_configurations[ImageConfigTypeEnum.CASTLE.value][type],
        )
