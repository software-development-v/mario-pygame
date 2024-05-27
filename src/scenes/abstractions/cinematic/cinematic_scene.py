from abc import ABC
from typing import Optional

from src.managers import GameManager

from ..scene import Scene
from .cinematic_scene_render import CinematicSceneRender


class CinematicScene(Scene, ABC):
    def __init__(
        self,
        game_manager: GameManager,
        video_path: str,
        audio_path: str,
        next_scene: Optional["Scene"] = None,
    ):
        super().__init__(
            game_manager,
            CinematicSceneRender(video_path, audio_path),
            next_scene,
        )
