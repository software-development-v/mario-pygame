from abc import ABC, abstractmethod
from src.design.settings.keyboard.command.command import Command


class ActionCommand(Command, ABC):
    @abstractmethod
    def execute(self):
        pass
