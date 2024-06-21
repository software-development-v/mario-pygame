from src.data.game_data import GameData
from src.enums.level import Level
from src.enums.world import World
from src.utils.camera import Camera
from src.utils.constants import (
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_HEIGHT,
    SCREEN_VIEW_PLAY_WIDTH,
)


game_data = GameData()
world = World.ONE
level = Level.FIRST
level_data = game_data.get_level_data(world, level)

camera = Camera(
    level_data.get_screen_width(),
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_WIDTH,
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_VIEW_PLAY_HEIGHT,
)
