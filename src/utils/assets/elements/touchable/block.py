from pygame import image, transform

from src.utils.directories import BRICK_DIR, WALL_DIR, MYSTERY_BLOCK_DIR

OVERWORLD_BLOCK = transform.scale(
    image.load(BRICK_DIR + "overworld.png"), (50, 50)
)

WALL_BLOCK = transform.scale(
    image.load(WALL_DIR + "wall.png"), (50, 50)
)

MYSTERY_BLOCK = transform.scale(
    image.load(MYSTERY_BLOCK_DIR + "1.png"), (50, 50)
)
