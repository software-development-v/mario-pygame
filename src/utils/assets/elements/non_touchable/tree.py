from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import TREE_BACKGROUND_DIR

BIG_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "big_tree.png"), (
        ((GENERAL_WIDTH * 6) + (GENERAL_WIDTH / 1.5)),
        GENERAL_HEIGHT * 5
    )
)

MEDIUM_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "medium_tree.png"), (
        ((GENERAL_WIDTH * 4) - (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 5) - (GENERAL_HEIGHT / 6))
    )
)

SMALL_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "small_tree.png"), (
        ((GENERAL_WIDTH * 2) + (GENERAL_WIDTH / 2)),
        ((GENERAL_HEIGHT * 3) + (GENERAL_HEIGHT / 12))
    )
)
