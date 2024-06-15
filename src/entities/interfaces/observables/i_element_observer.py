from abc import ABC , abstractmethod

class IElementObserver(ABC):

    @abstractmethod
    def update(self , value:int):
        pass

    @abstractmethod
    def get_value(self) -> int:
        pass
