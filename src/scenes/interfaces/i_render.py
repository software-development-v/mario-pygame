from abc import ABC, abstractmethod
from typing import Callable, Dict

from pygame import Surface, display

from src.enums import SceneAction

from .i_scene import IScene


class IRender(ABC):
    def __init__(self):
        self._screen: Surface = display.get_surface()

    @abstractmethod
    def render(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        pass
