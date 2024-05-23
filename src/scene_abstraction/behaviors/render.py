from abc import ABC, abstractmethod

from pygame import Surface

from src.state.game_state import GameState


class IRender(ABC):
    @abstractmethod
    def render(self, game_state: GameState, screen: Surface) -> None:
        pass
