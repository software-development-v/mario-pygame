from typing import Any, Dict, List

from pygame import (
    JOYAXISMOTION,
    JOYBUTTONDOWN,
    JOYBUTTONUP,
    JOYDEVICEADDED,
    JOYDEVICEREMOVED,
    Event,
    joystick,
)

from src.enums import ControllerInput, GameEvent
from src.utils.constants import (
    DEFAULT_HORIZONTAL_AXIS_VALUE,
    DEFAULT_MIN_SENSIBILITY,
    DEFAULT_R_TWO_SENSIBILITY,
    DEFAULT_R_TWO_VALUE,
    DEFAULT_TRIGGER_SENSIBILITY,
    DEFAULT_VERTICAL_AXIS_VALUE,
)

from ..interfaces import IInputHandler


class ControllerInputHandler(IInputHandler):
    def __init__(self) -> None:
        joystick.init()

        self.joysticks: List[joystick.JoystickType] = [
            joystick.Joystick(i) for i in range(joystick.get_count())
        ]

        self.control_input: Dict[int, GameEvent] = {
            ControllerInput.UP_ARROW.value: GameEvent.UP,
            ControllerInput.DOWN_ARROW.value: GameEvent.DOWN,
            ControllerInput.LEFT_ARROW.value: GameEvent.LEFT,
            ControllerInput.RIGHT_ARROW.value: GameEvent.RIGHT,
            ControllerInput.X.value: GameEvent.JUMP,
            ControllerInput.LEFT_STICK_PRESS.value: GameEvent.RUN,
            ControllerInput.R_TWO.value: GameEvent.ATTACK,
            ControllerInput.OPTIONS.value: GameEvent.PAUSE,
        }

        self.sensibility: Dict[int, float] = {
            ControllerInput.HORIZONTAL_AXIS.value: DEFAULT_HORIZONTAL_AXIS_VALUE,
            ControllerInput.VERTICAL_AXIS.value: DEFAULT_VERTICAL_AXIS_VALUE,
            ControllerInput.R_TWO.value: DEFAULT_R_TWO_VALUE,
        }

    def check_button_in_keys(self, button: Any) -> bool:
        return (
            button in self.control_input
            and button != ControllerInput.R_TWO
            and button != ControllerInput.HORIZONTAL_AXIS
            and button != ControllerInput.VERTICAL_AXIS
        )

    def check_axis(
        self,
        game_events: Dict[GameEvent, bool],
        axis: int,
        left_index: ControllerInput,
        right_index: ControllerInput,
    ) -> None:
        if abs(self.sensibility[axis]) <= DEFAULT_MIN_SENSIBILITY:
            return

        if self.sensibility[axis] < -DEFAULT_TRIGGER_SENSIBILITY:
            game_events[self.control_input[left_index.value]] = True
        else:
            game_events[self.control_input[left_index.value]] = False

        if self.sensibility[axis] > DEFAULT_TRIGGER_SENSIBILITY:
            game_events[self.control_input[right_index.value]] = True
        else:
            game_events[self.control_input[right_index.value]] = False

    def handle(
        self, events: List[Event], game_events: Dict[GameEvent, bool]
    ) -> None:
        for e in events:
            if e.type == JOYDEVICEADDED or e.type == JOYDEVICEREMOVED:
                self.joysticks = [
                    joystick.Joystick(i) for i in range(joystick.get_count())
                ]

            if len(self.joysticks) == 0:
                break

            if e.type == JOYBUTTONDOWN and self.check_button_in_keys(e.button):
                game_events[self.control_input[e.button]] = True

            if e.type == JOYBUTTONUP and self.check_button_in_keys(e.button):
                game_events[self.control_input[e.button]] = False

            if e.type != JOYAXISMOTION:
                continue

            if e.axis not in [0, 1, 5]:
                continue

            self.sensibility[e.axis] = e.value

            self.check_axis(
                game_events,
                ControllerInput.HORIZONTAL_AXIS.value,
                ControllerInput.LEFT_ARROW,
                ControllerInput.RIGHT_ARROW,
            )

            self.check_axis(
                game_events,
                ControllerInput.VERTICAL_AXIS.value,
                ControllerInput.UP_ARROW,
                ControllerInput.DOWN_ARROW,
            )

            if (
                self.sensibility[ControllerInput.R_TWO.value]
                > DEFAULT_R_TWO_SENSIBILITY
            ):
                game_events[
                    self.control_input[ControllerInput.R_TWO.value]
                ] = True
            else:
                game_events[
                    self.control_input[ControllerInput.R_TWO.value]
                ] = False
