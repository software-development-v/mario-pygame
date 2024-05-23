from abc import ABC
from typing import Optional

from pygame import display

from src.scene_abstraction.behaviors.render import IRender
from src.state.game_state import GameState


class Scene(ABC):
    def __init__(
        self,
        game_sate: GameState,
        window_render: IRender,
        next: Optional["Scene"] = None,
    ) -> None:
        self.game_state = game_sate
        self.screen = display.get_surface()
        self.window_render = window_render
        self.next = next

    def next_scene(self) -> Optional["Scene"]:
        return self.next

    def display(self) -> None:
        self.window_render.render(self.game_state, self.screen)
