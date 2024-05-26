from src.entities.elements.element import Element
from src.utils.image_mappings import image_configurations


class Coin(Element):
    def __init__(self, x: int, y: int, level: int = 1) -> None:
        super().__init__(x, y, 25, 25, image_configurations["Castle"][level])
