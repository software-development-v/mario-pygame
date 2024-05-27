from abc import ABC, abstractmethod

from src.managers import GameManager


class ITick(ABC):
    @abstractmethod
    def tick(
        self,
        game_manager: GameManager,
    ) -> None:
        pass
