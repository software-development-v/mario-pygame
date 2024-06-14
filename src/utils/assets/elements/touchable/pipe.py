from pygame import image, transform

from src.utils.directories import PIPE_BODY_DIR, PIPE_HEAD_DIR

PIPE_HEAD = transform.scale(
    image.load(PIPE_HEAD_DIR + "head.png"), (100, 100)
)

PIPE_BODY = transform.scale(image.load(PIPE_BODY_DIR + "style_2.png"), (100, 50))
