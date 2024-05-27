from src.entities.elements.element import Element
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.enums.element_types.pipe_sub_type import PipeSubTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class MediumPipe(Element):
    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(50, 50),
            image_configurations[ImageConfigTypeEnum.PIPE.value][
                PipeSubTypeEnum.MEDIUM_PIPE.value
            ],
        )
