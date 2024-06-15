from typing import Dict, List

from pygame import KEYDOWN, KEYUP, Event

from src.enums import GameEvent, KeyboardInput

from ..interfaces import IInputHandler


class KeyboardInputHandler(IInputHandler):
    def __init__(self) -> None:
        self.keyboard_input: Dict[int, GameEvent] = {
            KeyboardInput.KEY_UP.value: GameEvent.UP,
            KeyboardInput.KEY_W.value: GameEvent.UP,
            KeyboardInput.KEY_DOWN.value: GameEvent.DOWN,
            KeyboardInput.KEY_S.value: GameEvent.DOWN,
            KeyboardInput.KEY_LEFT.value: GameEvent.LEFT,
            KeyboardInput.KEY_A.value: GameEvent.LEFT,
            KeyboardInput.KEY_RIGHT.value: GameEvent.RIGHT,
            KeyboardInput.KEY_D.value: GameEvent.RIGHT,
            KeyboardInput.KEY_SPACE.value: GameEvent.JUMP,
            KeyboardInput.KEY_SHIFT.value: GameEvent.RUN,
            KeyboardInput.KEY_R.value: GameEvent.ATTACK,
            KeyboardInput.KEY_ESCAPE.value: GameEvent.PAUSE,
        }

    def handle(
        self, events: List[Event], game_events: Dict[GameEvent, bool]
    ) -> None:
        for e in events:
            if e.type == KEYDOWN:
                if e.key in self.keyboard_input:
                    game_events[self.keyboard_input[e.key]] = True

            if e.type == KEYUP:
                if e.key in self.keyboard_input:
                    game_events[self.keyboard_input[e.key]] = False
