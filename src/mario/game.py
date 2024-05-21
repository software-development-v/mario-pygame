from typing import List, Tuple
import pygame
from pygame import display, init, time

from src.design.infraestructure import Infrastructure
from src.design.render.game_renderer import GameRenderer
from src.design.settings.keyboard.keyboard_conf import KeyboardConf
from src.design.settings.settings import Settings
from src.domain.game_manager import GameManager
from src.domain.level_struct.entity.entity import Entity
from src.domain.level_struct.entity.obstacle import Obstacle
from src.domain.level_struct.entity.platform import Platform
from src.domain.level_struct.entity.powerup import PowerUp
from src.domain.level_struct.level import Level
from src.domain.level_struct.level_manager import LevelManager
from src.domain.level_struct.timer.timer import Timer
from src.driven.game_controller import GameController
from src.utils.assets import BG, ICON
from src.utils.constants import TEST_PICTURE_WIDTH, TEST_PICTURE_HEIGHT
from src.utils.constants import (
    DEFAULT_EFFECTS_VOLUME,
    DEFAULT_MUSIC_VOLUME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
)

class Game:
    def __init__(self) -> None:
        init()

        display.set_caption(TITLE)
        display.set_icon(ICON)

        screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player_sprite = pygame.transform.scale(pygame.image.load("assets/player.png").convert_alpha(), (TEST_PICTURE_WIDTH, TEST_PICTURE_HEIGHT))
        self.enemy_sprite = pygame.transform.scale(pygame.image.load("assets/enemy.png").convert_alpha(), (TEST_PICTURE_WIDTH, TEST_PICTURE_HEIGHT))
        self.obstacle_sprite = pygame.transform.scale(pygame.image.load("assets/obstacle.png").convert_alpha(), (TEST_PICTURE_WIDTH, TEST_PICTURE_HEIGHT))
        self.power_up_sprite = pygame.transform.scale(pygame.image.load("assets/power-up.png").convert_alpha(), (TEST_PICTURE_WIDTH, TEST_PICTURE_HEIGHT))

        render = GameRenderer(screen, self.player_sprite, self.enemy_sprite, self.obstacle_sprite, self.power_up_sprite)

        keyboard_conf = KeyboardConf()
        game_settings = Settings(
            DEFAULT_MUSIC_VOLUME, DEFAULT_EFFECTS_VOLUME, keyboard_conf
        )

        infrastructure = Infrastructure(game_settings, render)

        obstacle = Obstacle()
        platform = Platform()
        entity = Entity()
        power_up = PowerUp()
        timer = Timer()
        level_one = Level(
            [obstacle], [platform], [entity], [power_up], BG, timer
        )
        level_manager = LevelManager([level_one])

        game_manager = GameManager(level_manager)

        self.clock = time.Clock()
        self.game_controller = GameController(game_manager, infrastructure)

    player_pos : Tuple[int, int] = (200, 100)
    enemies_pos : List[Tuple[int, int]] = [(500, 200), (550, 250)]
    obstacles_pos : List[Tuple[int, int]] = [(800, 300), (850, 350)]
    power_ups_pos : List[Tuple[int, int]] = [(1100, 400), (1150, 450)]

    def run(self) -> None:
        infrastructure : Infrastructure = self.game_controller.get_infrastructure()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        running = False

            # TODO: Process other events (e.g., keyboard inputs)
            self.game_controller.update()

            game_renderer: GameRenderer = infrastructure.get_game_render()
            game_renderer.render(self.player_pos, self.enemies_pos, self.obstacles_pos, self.power_ups_pos)

            display.flip()
            self.clock.tick(60)

        pygame.quit()
