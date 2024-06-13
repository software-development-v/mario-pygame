from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import HIJITA_DIR

HIJITA_IDLE = transform.scale(image.load(HIJITA_DIR + "idle.png"), PLAYER_SIZE)

# == Walk Animation ==
HIJITA_WALK_ANIMATION_1 = transform.scale(
    image.load(HIJITA_DIR + "walk_cycle_1.png"), PLAYER_SIZE
)

HIJITA_WALK_ANIMATION_2 = transform.scale(
    image.load(HIJITA_DIR + "walk_cycle_2.png"), PLAYER_SIZE
)

HIJITA_WALK_ANIMATION_3 = transform.scale(
    image.load(HIJITA_DIR + "walk_cycle_3.png"), PLAYER_SIZE
)

HIJITA_JUMP = transform.scale(image.load(HIJITA_DIR + "jump.png"), PLAYER_SIZE)

HIJITA_DIE = transform.scale(image.load(HIJITA_DIR + "die.png"), PLAYER_SIZE)
