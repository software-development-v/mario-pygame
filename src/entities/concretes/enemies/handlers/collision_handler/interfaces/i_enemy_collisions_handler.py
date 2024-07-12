from abc import ABC, abstractmethod
from typing import List, Tuple

from pygame import Rect

from src.entities import Element

from .....hero import IHero
from ....interfaces import IEnemy


class IEnemyCollisionsHandler(ABC):
    @abstractmethod
    def __init__(self, enemy: IEnemy):
        self.enemy = enemy

    @abstractmethod
    def handle_collisions(
        self,
        enemy_rect: Rect,
        obstacles: List[Element],
        enemies: List[IEnemy],
        dx: float,
        dy: float,
    ) -> Tuple[float, float]:
        pass

    @abstractmethod
    def handle_hero_collision(self, hero: IHero) -> bool:
        pass

    @abstractmethod
    def check_dispose(self):
        pass
