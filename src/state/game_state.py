from typing import Dict

from src.enums.custom_event import CustomEvent
from src.enums.state import State


class GameState:
    def __init__(self) -> None:
        self.state = State.RUNNING
        self.events: Dict[CustomEvent, bool] = {
            CustomEvent.UP: False,
            CustomEvent.DOWN: False,
            CustomEvent.LEFT: False,
            CustomEvent.RIGHT: False,
            CustomEvent.JUMP: False,
            CustomEvent.RUN: False,
            CustomEvent.ATTACK: False,
            CustomEvent.PAUSE: False,
        }

    def reset(self) -> None:
        self.state = State.RUNNING
        for event in self.events:
            self.events[event] = False
