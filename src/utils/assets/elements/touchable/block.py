from src.utils.assets.create_images import create_image
from src.utils.constants import GENERAL_SIZE
from src.utils.directories import (
    BRICK_DIR,
    MASTERY_BLOCK_DIR,
    TERRAIN_DIR,
    WALL_DIR,
)

OVERWORLD_BLOCK = create_image(BRICK_DIR + "overworld.png", GENERAL_SIZE)

WALL_BLOCK = create_image(WALL_DIR + "wall.png", GENERAL_SIZE)

MASTERY_BLOCK_1 = create_image(
    MASTERY_BLOCK_DIR + "mistery_block_1.png", GENERAL_SIZE
)

MASTERY_BLOCK_2 = create_image(
    MASTERY_BLOCK_DIR + "mistery_block_2.png", GENERAL_SIZE
)

MASTERY_BLOCK_3 = create_image(
    MASTERY_BLOCK_DIR + "mistery_block_3.png", GENERAL_SIZE
)

OVERWORLD_TERRAIN_BLOCK = create_image(
    TERRAIN_DIR + "overworld.png", GENERAL_SIZE
)
