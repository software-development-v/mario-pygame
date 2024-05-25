from enum import Enum


class Levels (Enum):
    LEVEL_1 = "Level 1"
    def __str__(self) -> str:
        return self.value

