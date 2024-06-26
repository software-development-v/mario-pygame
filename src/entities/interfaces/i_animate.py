from abc import ABC, abstractmethod


class IAnimate(ABC):

    @abstractmethod
    def animate(self) -> None:
        pass
