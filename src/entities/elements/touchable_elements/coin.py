from src.entities.elements.element import Element
from src.enums.element_types.coin_sub_type import CoinSubTypeEnum
from src.enums.element_types.element_type import ImageConfigTypeEnum
from src.utils.image_mappings import image_configurations
from src.utils.position import Position
from src.utils.size import Size


class Coin(Element):
    def __init__(
        self,
        x: int,
        y: int,
        type: CoinSubTypeEnum = CoinSubTypeEnum.DEFAULT_COIN,
    ) -> None:
        super().__init__(
            Position(x, y),
            Size(50, 50),
            image_configurations[ImageConfigTypeEnum.COIN.value][type.value],
        )
