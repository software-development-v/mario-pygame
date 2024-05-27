from abc import ABC
from typing import Optional

from src.managers import GameManager

from ..interfaces import IRender


class Scene(ABC):
    def __init__(
        self,
        game_manager: GameManager,
        scene_render: IRender,
        next_scene: Optional["Scene"] = None,
    ) -> None:
        self.game_manager = game_manager
        self.scene_render = scene_render
        self.next = next_scene

    def next_scene(self) -> Optional["Scene"]:
        return self.next

    def display(self) -> None:
        self.scene_render.render(self.game_manager)
