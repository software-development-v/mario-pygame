from sys import exit
from typing import Dict, List

from pygame import QUIT, event, quit

from src.enums import GameEvent

from .concretes import ControllerInputHandler, KeyboardInputHandler
from .interfaces import IEventManager, IInputHandler


class EventManager(IEventManager):
    def __init__(self) -> None:
        self.__events: Dict[GameEvent, bool] = {
            GameEvent.UP: False,
            GameEvent.DOWN: False,
            GameEvent.LEFT: False,
            GameEvent.RIGHT: False,
            GameEvent.JUMP: False,
            GameEvent.RUN: False,
            GameEvent.ATTACK: False,
            GameEvent.PAUSE: False,
        }

        self.__inputs_handler: List[IInputHandler] = [
            KeyboardInputHandler(),
            ControllerInputHandler(),
        ]

    def reset_events(self) -> None:
        for key in self.__events:
            self.__events[key] = False

    def handle_events(self) -> None:
        events = event.get()

        for e in events:
            if e.type == QUIT:
                quit()
                exit()

        for handler in self.__inputs_handler:
            handler.handle(events, self.__events)

    def get_events(self) -> Dict[GameEvent, bool]:
        return self.__events
