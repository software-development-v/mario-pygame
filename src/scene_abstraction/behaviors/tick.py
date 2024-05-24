from abc import ABC, abstractmethod

from src.state.game_state import GameState


class ITick(ABC):
    @abstractmethod
    def tick(
        self,
        game_state: GameState,
    ) -> None:
        pass
