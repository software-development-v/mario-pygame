import pygame
from pygame.locals import K_p, K_LEFT, K_RIGHT, K_x, K_SPACE
from pygame import Surface, error, image, transform

from src.scenes.abstractions.scene import Scene
from .enums import GameState, Level, World
from .utils.assets import (
    PLAYER_PARIENTE, PLAYER_PARIENTE1, PLAYER_PARIENTE2, 
    PLAYER_HIJITA, PLAYER_HIJITA1, PLAYER_HIJITA2
)
from .utils.constants import CENTER_X, CENTER_Y
from .managers import GameManager
from .scenes.concretes.level import LevelScene
from .utils.constants import FPS

class Game:
    def __init__(self) -> None:
        self.game_manager: GameManager = GameManager()
        self.scene: Scene = self.reset_game()

        self.character_animations = {
            "PARIENTE": [PLAYER_PARIENTE, PLAYER_PARIENTE1, PLAYER_PARIENTE2],
            "HIJITA": [PLAYER_HIJITA, PLAYER_HIJITA1, PLAYER_HIJITA2]
        }
        self.character_names = ["PARIENTE", "HIJITA"]
        self.current_character_index = 0
        self.current_character_name = self.character_names[self.current_character_index]
        self.current_animation_frame = 0
        self.facing_right = True 
        self.image: Surface = self.get_current_image()
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (CENTER_X, CENTER_Y)

    def get_current_image(self) -> Surface:
        animation_frames = self.character_animations[self.current_character_name]
        current_image = animation_frames[self.current_animation_frame]
        return current_image if self.facing_right else transform.flip(current_image, True, False)

    def load_image(self, path: str) -> Surface:
        try:
            loaded_image = image.load(path)
            return loaded_image
        except error as e:
            print(f"Error cargando la imagen en {path}: {e}")
            raise SystemExit(e)

    def reset_game(self) -> Scene:
        return LevelScene(
            self.game_manager,
            World.ONE,
            Level.FIRST,
            None
        )

    def handle_display(self) -> None:
        self.scene.display()

        self.game_manager.screen.blit(self.image, self.image_rect)
        
        self.game_manager.display.update()
        self.game_manager.clock.tick(FPS)

    def handle_events(self) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[K_LEFT]:
            if self.facing_right:
                self.facing_right = False
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.character_animations[self.current_character_name])
            self.image = self.get_current_image()
            self.image_rect.x -= 5
        
        elif keys[K_RIGHT]:
            if not self.facing_right:
                self.facing_right = True
            self.current_animation_frame = (self.current_animation_frame + 1) % len(self.character_animations[self.current_character_name])
            self.image = self.get_current_image()
            self.image_rect.x += 5 
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    self.current_character_index = (self.current_character_index + 1) % len(self.character_names)
                    self.current_character_name = self.character_names[self.current_character_index]
                    self.current_animation_frame = 0
                    self.image = self.get_current_image()
                elif event.key == K_x or event.key == K_SPACE:
                    self.game_manager.game_state = GameState.QUIT # type: ignore

    def run(self) -> None:
        while self.game_manager.game_state == GameState.RUNNING:
            self.handle_events()
            self.handle_display()

        self.run()
