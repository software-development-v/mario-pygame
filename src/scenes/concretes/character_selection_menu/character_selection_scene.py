# En un archivo nuevo, por ejemplo, character_selection_scene.py

from typing import Callable, Dict

from src.enums import SceneAction

from ...abstractions import Scene
from .character_selection_render import CharacterSelectionRender
from .character_selection_tick import CharacterSelectionTick


class CharacterSelectionScene(Scene):
    def __init__(
        self,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ):
        render = CharacterSelectionRender()
        tick = CharacterSelectionTick(render, dispatcher)
        super().__init__(render, tick, dispatcher)
