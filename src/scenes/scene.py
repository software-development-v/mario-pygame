from abc import ABC
from pygame import display

from src.scenes.render import IRender
from src.state.game_state import GameState


class Scene(ABC):
    def __init__(
        self,
        game_sate: GameState,
        window_render: IRender,
    ) -> None:
        self.game_state = game_sate
        self.screen = display.get_surface()
        self.window_render = window_render

    def display(self) -> None:
        self.window_render.render(self.game_state, self.screen)
