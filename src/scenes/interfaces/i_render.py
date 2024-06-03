from abc import ABC, abstractmethod

from .i_scene_manager import ISceneManager


class IRender(ABC):
    @abstractmethod
    def render(self, scene_manager: ISceneManager) -> None:
        pass
