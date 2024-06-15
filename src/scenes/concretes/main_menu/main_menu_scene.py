from typing import Callable, Dict

from src.enums import SceneAction

from ...abstractions import Scene
from .main_menu_render import MainMenuRender
from .main_menu_tick import MainMenuTick


class MainMenuScene(Scene):
    def __init__(
        self,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ):
        render = MainMenuRender()
        tick = MainMenuTick(render, dispatcher)
        super().__init__(render, tick, dispatcher)
