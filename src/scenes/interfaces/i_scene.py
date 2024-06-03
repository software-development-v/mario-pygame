from abc import ABC, abstractmethod
from typing import Optional


class IScene(ABC):
    @abstractmethod
    def next_scene(self) -> Optional["IScene"]:
        pass

    @abstractmethod
    def set_next_scene(self, scene: "IScene") -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass
