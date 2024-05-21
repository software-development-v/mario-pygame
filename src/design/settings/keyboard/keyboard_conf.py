from typing import Dict

from src.design.settings.keyboard.command.command import Command
from src.design.settings.keyboard.command.steering_controls.move_down import MoveDown
from src.design.settings.keyboard.command.steering_controls.move_left import MoveLeft
from src.design.settings.keyboard.command.steering_controls.move_right import MoveRight
from src.design.settings.keyboard.command.steering_controls.move_up import MoveUp


class KeyboardConf:
    def __init__(self):
        self.key_mapping: Dict[str, Command] = {}
        self.set_key("W", MoveUp())
        self.set_key("S", MoveDown())
        self.set_key("A", MoveLeft())
        self.set_key("D", MoveRight())

    def set_key(self, key: str, command: Command) -> None:
        self.key_mapping[key] = command

    def press_key(self, key: str) -> None:
        if key in self.key_mapping:
            command = self.key_mapping[key]
            command.execute()
