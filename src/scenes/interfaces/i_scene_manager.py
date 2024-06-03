from abc import ABC, abstractmethod

from pygame import Surface

from .i_scene import IScene


class ISceneManager(ABC):
    @abstractmethod
    def reset_scene(self) -> IScene:
        pass

    @abstractmethod
    def next_scene(self) -> None:
        pass

    @abstractmethod
    def set_next_scene(self, scene: IScene) -> None:
        pass

    @abstractmethod
    def display_current_scene(self) -> None:
        pass

    @abstractmethod
    def get_screen(self) -> Surface:
        pass

    @abstractmethod
    def set_frame_rate(self, frame_rate: float) -> None:
        pass

    @abstractmethod
    def reset_frame_rate(self) -> None:
        pass
