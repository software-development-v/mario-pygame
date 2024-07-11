from abc import ABC, abstractmethod
from typing import Tuple
from src.utils import Camera
from ....interfaces import IEnemy


class IEnemyMovementHandler(ABC):
    @abstractmethod
    def __init__(self, enemy: IEnemy):
        self.enemy = enemy

    @abstractmethod
    def handle_movement(self, camera: Camera) -> Tuple[float, float]:
        pass
