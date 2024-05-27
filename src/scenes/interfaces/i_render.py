from abc import ABC, abstractmethod

from src.managers import GameManager


class IRender(ABC):
    @abstractmethod
    def render(
        self,
        game_manager: GameManager,
    ) -> None:
        pass
