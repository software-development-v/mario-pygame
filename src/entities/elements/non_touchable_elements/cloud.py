from src.entities.elements.element import Element
from src.utils.image_mappings import image_configurations


class Cloud(Element):
    def __init__(self, x: int, y: int, level: int) -> None:
        super().__init__(
            x,
            y,
            100,
            50,
            image_configurations["Cloud"][level],
            is_touchable=False,
        )
