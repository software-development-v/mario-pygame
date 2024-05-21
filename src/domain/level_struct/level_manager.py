from typing import List
from src.domain.level_struct.level import Level

class LevelManager:
    def __init__(self, levels: List[Level]):
        # Initialize the LevelManager with a list of levels
        self.levels = levels
        self.current_level = None

    def load_level(self, level_number: int) -> None:
        # Load the specified level
        if 0 <= level_number < len(self.levels):
            self.current_level = self.levels[level_number]
            # Implement logic to load the specified level
            # For example:
            # self.current_level.load()
            print(f"Level {level_number + 1} loaded.")
        else:
            print("Invalid level number.")

    def next_level(self) -> None:
        # Load the next level
        if self.current_level is not None:
            current_index = self.levels.index(self.current_level)
            if current_index + 1 < len(self.levels):
                self.current_level = self.levels[current_index + 1]
                # Implement logic to load the next level
                # For example:
                # self.current_level.load()
                print(f"Next level loaded.")
            else:
                print("No more levels.")
        else:
            print("No level loaded yet.")
