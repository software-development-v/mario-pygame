from pygame import image, transform

from src.utils.directories import TREE_BACKGROUND_DIR

BIG_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "big_tree.png"), (400, 300)
)
MEDIUM_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "medium_tree.png"), (200, 250)
)
SMALL_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "small_tree.png"), (120, 145)
)
