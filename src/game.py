from .enums import GameState, HeroType, Level, World
from .managers import GameManager
from .scenes import FinalCinematicScene, ModeSelectionScene, Scene, TransitionLevelScene
from .utils.constants import FPS


class Game:
    def __init__(self) -> None:
        self.game_manager: GameManager = GameManager()
        self.scene: Scene = self.reset_game()

    def reset_game(self) -> Scene:
        return ModeSelectionScene(
            self.game_manager,
            TransitionLevelScene(
                self.game_manager,
                World.ONE,
                Level.FIRST,
                HeroType.HIJITA,
                FinalCinematicScene(self.game_manager),
            ),
        )

    def handle_display(self) -> None:
        self.scene.display()
        self.game_manager.display.update()
        self.game_manager.clock.tick(FPS)

    def next_scene(self) -> None:
        next_scene: Scene | None = self.scene.next_scene()

        if next_scene is None:
            self.scene = self.reset_game()
        else:
            self.scene = next_scene

        self.game_manager.game_state = GameState.RUNNING

    def run(self) -> None:
        while self.game_manager.game_state == GameState.RUNNING:
            self.game_manager.handle_events()
            self.handle_display()

        self.game_manager.handle_states(self.next_scene)

        self.run()
