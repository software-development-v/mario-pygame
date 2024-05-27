from abc import ABC, abstractmethod
import pygame


class IEntity(ABC):
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass
