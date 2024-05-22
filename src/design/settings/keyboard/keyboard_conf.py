from typing import Dict

from src.design.settings.keyboard.command.command import Command
from src.design.settings.keyboard.command.steering_controls.move_down import MoveDown
from src.design.settings.keyboard.command.steering_controls.move_left import MoveLeft
from src.design.settings.keyboard.command.steering_controls.move_right import MoveRight
from src.design.settings.keyboard.command.steering_controls.move_up import MoveUp
from src.design.settings.keyboard.command.action_controls.action_jump import Jump
from src.design.settings.keyboard.command.action_controls.action_run import Run
from src.design.settings.keyboard.command.action_controls.action_shoot import Shoot
from src.design.settings.keyboard.command.action_controls.action_crounch import Crouch

class KeyboardConf:
    def __init__(self):
        self.key_mapping: Dict[str, Command] = {}
        self.set_keys()

    def set_keys(self) -> None:
        self.set_key("W", MoveUp())
        self.set_key("S", MoveDown())
        self.set_key("A", MoveLeft())
        self.set_key("D", MoveRight())
        self.set_key("SPACE", Jump())
        self.set_key("LSHIFT", Run())
        self.set_key("LCTRL", Shoot())
        self.set_key("C", Crouch())

    def set_key(self, key: str, command: Command) -> None:
        self.key_mapping[key] = command

    def press_key(self, key: str) -> None:
        if key in self.key_mapping:
            command = self.key_mapping[key]
            command.execute()
