from abc import ABC, abstractmethod

from src.inputs import IEventManager

from .i_scene_manager import ISceneManager


class ITick(ABC):
    @abstractmethod
    def tick(
        self,
        events_manager: IEventManager,
        scene_manager: ISceneManager,
    ) -> None:
        pass
