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
from src.utils.assets import BG, ENEMY, ICON, OBSTACLE, PLAYER, POWER_UP
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
        render = GameRenderer(screen, PLAYER, ENEMY, OBSTACLE, POWER_UP)

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

    def run(self) -> None:
        pass
