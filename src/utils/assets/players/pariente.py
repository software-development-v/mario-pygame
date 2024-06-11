from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import PARIENTE_DIR

PARIENTE_IDLE = transform.scale(
    image.load(PARIENTE_DIR + "idle.png"), PLAYER_SIZE
)

# == Walk Animation ==
PARIENTE_WALK_ANIMATION_1 = transform.scale(
    image.load(PARIENTE_DIR + "walk_cycle_1.png"), PLAYER_SIZE
)

PARIENTE_WALK_ANIMATION_2 = transform.scale(
    image.load(PARIENTE_DIR + "walk_cycle_2.png"), PLAYER_SIZE
)

PARIENTE_WALK_ANIMATION_3 = transform.scale(
    image.load(PARIENTE_DIR + "walk_cycle_3.png"), PLAYER_SIZE
)
