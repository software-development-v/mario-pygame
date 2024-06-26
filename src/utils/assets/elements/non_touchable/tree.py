from pygame import image, transform

from ....constants import BIG_TREE_SIZE, MEDIUM_TREE_SIZE, SMALL_TREE_SIZE
from ....directories import TREE_BACKGROUND_DIR

BIG_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "big_tree.png"),
    (BIG_TREE_SIZE),
)

MEDIUM_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "medium_tree.png"),
    (MEDIUM_TREE_SIZE),
)

SMALL_TREE = transform.scale(
    image.load(TREE_BACKGROUND_DIR + "small_tree.png"),
    (SMALL_TREE_SIZE),
)
