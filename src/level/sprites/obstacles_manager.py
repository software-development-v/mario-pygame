from typing import List

from src.entities import Element

from ..abstractions import SpritesManager


class ObstaclesManager(SpritesManager[Element]):
    def __init__(
        self,
        elements: List[Element],
    ) -> None:
        self.__elements = elements
        super().__init__(self.__elements)
