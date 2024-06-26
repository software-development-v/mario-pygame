from abc import ABC, abstractmethod


class IDamageHandler(ABC):
    @abstractmethod
    def handle_damage(self):
        pass
