from typing import Dict, List

from pygame import KEYDOWN, KEYUP
from pygame.event import Event

from src.enums.custom_event import CustomEvent
from src.enums.user_input import KeyboardUserInput
from src.events.behaviors.input_handler import IInputHandler


class KeyboardHandler(IInputHandler):
    def __init__(self) -> None:
        self.keyboard_input: Dict[int, CustomEvent] = {
            KeyboardUserInput.KEY_UP.value: CustomEvent.UP,
            KeyboardUserInput.KEY_W.value: CustomEvent.UP,
            KeyboardUserInput.KEY_DOWN.value: CustomEvent.DOWN,
            KeyboardUserInput.KEY_S.value: CustomEvent.DOWN,
            KeyboardUserInput.KEY_LEFT.value: CustomEvent.LEFT,
            KeyboardUserInput.KEY_A.value: CustomEvent.LEFT,
            KeyboardUserInput.KEY_RIGHT.value: CustomEvent.RIGHT,
            KeyboardUserInput.KEY_D.value: CustomEvent.RIGHT,
            KeyboardUserInput.KEY_SPACE.value: CustomEvent.JUMP,
            KeyboardUserInput.KEY_SHIFT.value: CustomEvent.RUN,
            KeyboardUserInput.KEY_R.value: CustomEvent.ATTACK,
            KeyboardUserInput.KEY_P.value: CustomEvent.PAUSE,
        }

    def handle(
        self, events: List[Event], game_events: Dict[CustomEvent, bool]
    ) -> None:
        for e in events:
            if e.type == KEYDOWN:
                if e.key in self.keyboard_input:
                    game_events[self.keyboard_input[e.key]] = True

            if e.type == KEYUP:
                if e.key in self.keyboard_input:
                    game_events[self.keyboard_input[e.key]] = False
