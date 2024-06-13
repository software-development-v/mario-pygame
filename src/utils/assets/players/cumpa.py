from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import CUMPA_DIR

CUMPA_IDLE = transform.scale(image.load(CUMPA_DIR + "idle.png"), PLAYER_SIZE)

# == Walk Animation ==
CUMPA_WALK_ANIMATION_1 = transform.scale(
    image.load(CUMPA_DIR + "walk_cycle_1.png"), PLAYER_SIZE
)

CUMPA_WALK_ANIMATION_2 = transform.scale(
    image.load(CUMPA_DIR + "walk_cycle_2.png"), PLAYER_SIZE
)

CUMPA_WALK_ANIMATION_3 = transform.scale(
    image.load(CUMPA_DIR + "walk_cycle_3.png"), PLAYER_SIZE
)

CUMPA_JUMP = transform.scale(image.load(CUMPA_DIR + "jump.png"), PLAYER_SIZE)

CUMPA_DIE = transform.scale(image.load(CUMPA_DIR + "die.png"), PLAYER_SIZE)
