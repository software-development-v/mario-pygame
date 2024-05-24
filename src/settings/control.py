from typing import List

from pygame import joystick


class ControlSettings:
    def __init__(self):
        self.joysticks: List[joystick.JoystickType] = []

        for i in range(joystick.get_count()):
            js = joystick.Joystick(i)
            js.init()
            self.joysticks.append(js)
