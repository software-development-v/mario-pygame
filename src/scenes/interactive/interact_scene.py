from abc import ABC

from src.scenes.render import IRender
from src.scenes.tick import ITick
from src.scenes.scene import Scene
from src.state.game_state import GameState


class InteractScene(Scene, ABC):

    def __init__(
        self,
        game_state: GameState,
        window_render: IRender,
        tick_handler: ITick
    ) -> None:
        super().__init__(game_state, window_render)
        self.tick_handler = tick_handler

    def display(self):
        self.tick_handler.tick(self.game_state)
        self.window_render.render(self.game_state, self.screen)
