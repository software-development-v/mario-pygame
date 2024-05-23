from abc import ABC

from src.scene_abstraction.behaviors.render import IRender
from src.scene_abstraction.behaviors.tick import ITick
from src.scene_abstraction.scene import Scene
from src.state.game_state import GameState


class InteractScene(Scene, ABC):

    def __init__(
        self,
        game_state: GameState,
        window_render: IRender,
        tick_handler: ITick,
        next_window: Scene,
    ) -> None:
        super().__init__(game_state, window_render, next_window)
        self.tick_handler = tick_handler

    def display(self):
        self.tick_handler.tick(self.game_state)
        self.window_render.render(self.game_state, self.screen)
