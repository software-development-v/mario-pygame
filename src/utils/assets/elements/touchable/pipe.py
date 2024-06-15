from src.utils.assets.create_images import create_image
from src.utils.constants import BIG_SIZE
from src.utils.directories import PIPE_BODY_DIR, PIPE_HEAD_DIR


PIPE_BODY_STYLE_1 = create_image(PIPE_BODY_DIR + "style_1.png", BIG_SIZE)
PIPE_BODY_STYLE_2 = create_image(PIPE_BODY_DIR + "style_2.png", BIG_SIZE)
PIPE_BODY_STYLE_3 = create_image(PIPE_BODY_DIR + "style_3.png", BIG_SIZE)
PIPE_BODY_STYLE_4 = create_image(PIPE_BODY_DIR + "style_4.png", BIG_SIZE)

PIPE_HEAD = create_image(PIPE_HEAD_DIR + "head.png", BIG_SIZE)
