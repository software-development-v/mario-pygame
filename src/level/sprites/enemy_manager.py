from typing import List

from src.entities.abstractions.sprite import Sprite

from ..abstractions import SpritesManager


class EnemyManager(SpritesManager[Sprite]):
    def __init__(
        self,
        enemies: List[Sprite],
    ) -> None:
        super().__init__(enemies)
