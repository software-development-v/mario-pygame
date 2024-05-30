from pygame import image, transform

from src.utils.directories import BLOCK_DIR

OVERWORLD_BLOCK = transform.scale(
    image.load(BLOCK_DIR + "overworld-block.png"), (50, 50)
)
