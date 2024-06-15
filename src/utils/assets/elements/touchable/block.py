from pygame import image, transform

from src.utils.constants import GENERAL_SIZE
from src.utils.directories import BRICK_DIR, WALL_DIR, MYSTERY_BLOCK_DIR

OVERWORLD_BLOCK = transform.scale(
    image.load(BRICK_DIR + "overworld.png"), GENERAL_SIZE
)

WALL_BLOCK = transform.scale(
    image.load(WALL_DIR + "wall.png"), GENERAL_SIZE
)

MYSTERY_BLOCK_1 = transform.scale(
    image.load(MYSTERY_BLOCK_DIR + "mistery_block_1.png"), GENERAL_SIZE
)

MYSTERY_BLOCK_2 = transform.scale(
    image.load(MYSTERY_BLOCK_DIR + "mistery_block_2.png"), GENERAL_SIZE
)
