from abc import ABC, abstractmethod

class IElementObserver(ABC):

    @abstractmethod
    def notify(self, value: object):
        pass
