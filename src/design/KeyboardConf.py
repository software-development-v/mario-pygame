from typing import Any, Dict

from src.design.command.steering_controls.MoveDownCommand import MoveDownCommand
from src.design.command.steering_controls.MoveLeftCommand import MoveLeftCommand
from src.design.command.steering_controls.MoveRightCommand import MoveRightCommand
from src.design.command.steering_controls.MoveUpCommand import MoveUpCommand

class KeyboardConf:
    def __init__(self):
        self.key_mapping: Dict[str, Any] = {}

    def set_key(self, key: str, command: Any) -> None:
        # Set a key mapping for a specific command
        self.key_mapping[key] = command

    def press_key(self, key: str) -> None:
        # Execute the command associated with the pressed key
        if key in self.key_mapping:
            command = self.key_mapping[key]
            command.execute()

# Example usage
if __name__ == "__main__":
    keyboard_conf = KeyboardConf()

    # Configure keys with corresponding commands
    keyboard_conf.set_key("W", MoveUpCommand())
    keyboard_conf.set_key("S", MoveDownCommand())
    keyboard_conf.set_key("A", MoveLeftCommand())
    keyboard_conf.set_key("D", MoveRightCommand())

    # Simulate pressing keys
    keyboard_conf.press_key("W")
    keyboard_conf.press_key("S")
    keyboard_conf.press_key("A")
