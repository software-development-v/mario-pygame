from typing import Optional
from src.scenes.scene import Scene
class SceneDeck():
    def __init__(self,scenes: list[Scene]=[]) -> None:
        self.scenes = scenes
        self.current_scene = 0

    def next_scene(self) -> Optional["Scene"]:
        if self.current_scene + 1 < len(self.scenes):
            self.current_scene += 1
            return self.scenes[self.current_scene]
        return None

    def add(self, scene: Scene) -> None:
        self.scenes.append(scene)

    def pop(self) -> None:
        self.scenes.pop(self.current_scene)

    def display(self) -> None:
        self.scenes[self.current_scene].display()


