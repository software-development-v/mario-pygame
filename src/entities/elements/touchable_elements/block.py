from src.entities.elements.element import Element
from src.utils.image_mappings import image_configurations


class Block(Element):
    def __init__(self, x: int, y: int, level: int) -> None:
        super().__init__(x, y, 50, 50, image_configurations["Block"][level])
