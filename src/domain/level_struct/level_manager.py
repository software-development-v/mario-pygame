from typing import List

from src.domain.level_struct.level import Level


class LevelManager:
    def __init__(self, levels: List[Level]):
        self.levels = levels
        self.current_level = None

    def load_level(self, level_number: int) -> None:
        if 0 <= level_number < len(self.levels):
            return

        self.current_level = self.levels[level_number]

    def next_level(self) -> None:
        if self.current_level is None:
            return

        current_index = self.levels.index(self.current_level)
        if current_index + 1 < len(self.levels):
            self.current_level = self.levels[current_index + 1]
