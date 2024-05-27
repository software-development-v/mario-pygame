from abc import ABC
from typing import Optional

from src.managers import GameManager

from ...interfaces import IRender, ITick
from ..scene import Scene


class InteractScene(Scene, ABC):

    def __init__(
        self,
        game_manager: GameManager,
        scene_render: IRender,
        tick_handler: ITick,
        next_scene: Optional["Scene"] = None,
    ) -> None:
        super().__init__(game_manager, scene_render, next_scene)
        self.tick_handler = tick_handler

    def display(self):
        self.tick_handler.tick(self.game_manager)
        super().display()
