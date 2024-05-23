from typing import Any, Dict, List

from pygame import JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP
from pygame.event import Event

from src.enums.custom_event import CustomEvent
from src.enums.user_input import ControlUserInput
from src.events.behaviors.input_handler import IInputHandler
from src.settings.control import ControlSettings
from src.utils.constants import (
    DEFAULT_HORIZONTAL_AXIS_VALUE,
    DEFAULT_MIN_SENSIBILITY,
    DEFAULT_R_TWO_SENSIBILITY,
    DEFAULT_R_TWO_VALUE,
    DEFAULT_TRIGGER_SENSIBILITY,
    DEFAULT_VERTICAL_AXIS_VALUE,
)


class ControlHandler(IInputHandler):
    def __init__(self, control_settings: ControlSettings) -> None:
        self.control_input: Dict[int, CustomEvent] = {
            ControlUserInput.UP_ARROW.value: CustomEvent.UP,
            ControlUserInput.DOWN_ARROW.value: CustomEvent.DOWN,
            ControlUserInput.LEFT_ARROW.value: CustomEvent.LEFT,
            ControlUserInput.RIGHT_ARROW.value: CustomEvent.RIGHT,
            ControlUserInput.X.value: CustomEvent.JUMP,
            ControlUserInput.LEFT_STICK_PRESS.value: CustomEvent.RUN,
            ControlUserInput.R_TWO.value: CustomEvent.ATTACK,
            ControlUserInput.OPTIONS.value: CustomEvent.PAUSE,
        }

        self.sensibility: Dict[int, float] = {
            ControlUserInput.HORIZONTAL_AXIS.value: DEFAULT_HORIZONTAL_AXIS_VALUE,
            ControlUserInput.VERTICAL_AXIS.value: DEFAULT_VERTICAL_AXIS_VALUE,
            ControlUserInput.R_TWO.value: DEFAULT_R_TWO_VALUE,
        }

        self.control_settings = control_settings

    def check_button_in_keys(self, button: Any) -> bool:
        return (
            button in self.control_input
            and button != ControlUserInput.R_TWO
            and button != ControlUserInput.HORIZONTAL_AXIS
            and button != ControlUserInput.VERTICAL_AXIS
        )

    def check_axis(
        self,
        game_events: Dict[CustomEvent, bool],
        axis: int,
        left_index: ControlUserInput,
        right_index: ControlUserInput,
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
        self, events: List[Event], game_events: Dict[CustomEvent, bool]
    ) -> None:
        for e in events:
            if e.type == JOYBUTTONDOWN:
                if self.check_button_in_keys(e.button):
                    game_events[self.control_input[e.button]] = True

            if e.type == JOYBUTTONUP:
                if self.check_button_in_keys(e.button):
                    game_events[self.control_input[e.button]] = False

            if e.type != JOYAXISMOTION:
                continue

            if e.axis not in [0, 1, 5]:
                continue

            self.sensibility[e.axis] = e.value

            self.check_axis(
                game_events,
                ControlUserInput.HORIZONTAL_AXIS.value,
                ControlUserInput.LEFT_ARROW,
                ControlUserInput.RIGHT_ARROW,
            )

            self.check_axis(
                game_events,
                ControlUserInput.VERTICAL_AXIS.value,
                ControlUserInput.UP_ARROW,
                ControlUserInput.DOWN_ARROW,
            )

            if (
                self.sensibility[ControlUserInput.R_TWO.value]
                > DEFAULT_R_TWO_SENSIBILITY
            ):
                game_events[
                    self.control_input[ControlUserInput.R_TWO.value]
                ] = True
            else:
                game_events[
                    self.control_input[ControlUserInput.R_TWO.value]
                ] = False
