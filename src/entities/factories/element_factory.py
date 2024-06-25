from src.enums import ElementSubType, ElementType
from src.utils import Position

from ..abstractions import Element
from ..concretes import (
    Block,
    Bush,
    Castle,
    Cloud,
    Coin,
    Flag,
    MisteryBox,
    Mountain,
    Pipe,
    Tree,
)


class ElementFactory:
    def __init__(self) -> None:
        self.factory = {
            ElementType.BUSH: Bush,
            ElementType.CLOUD: Cloud,
            ElementType.MOUNTAIN: Mountain,
            ElementType.BLOCK: Block,
            ElementType.CASTLE: Castle,
            ElementType.COIN: Coin,
            ElementType.FLAG: Flag,
            ElementType.TREE: Tree,
            ElementType.MISTERY_BOX: MisteryBox,
            ElementType.PIPE: Pipe,
        }

    def create(
        self,
        element_type: ElementType,
        position: Position,
        subtype: ElementSubType,
    ) -> Element:
        element = self.factory[element_type]

        return element(position, subtype)
