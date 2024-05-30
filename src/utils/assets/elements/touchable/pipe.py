from pygame import image, transform

from src.utils.directories import PIPE_DIR

BIG_PIPE = transform.scale(image.load(PIPE_DIR + "big-pipe.png"), (100, 200))
MEDIUM_PIPE = transform.scale(
    image.load(PIPE_DIR + "medium-pipe.png"), (100, 150)
)
SMALL_PIPE = transform.scale(
    image.load(PIPE_DIR + "small-pipe.png"), (100, 100)
)
