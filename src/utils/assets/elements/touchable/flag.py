from src.utils.assets.create_images import create_image
from src.utils.constants import FLAG_SIZE, FLAG_SUPPORT_SIZE, PIPE_FLAG_SIZE
from src.utils.directories import (
    FLAG_PIPE_DIR,
    FLAG_SUPPORT_DIR,
    FLAG_WIN_DIR,
)

FLAG_PIPE = create_image(FLAG_PIPE_DIR + "flag_pipe.png", PIPE_FLAG_SIZE)

FLAG_WIN = create_image(FLAG_WIN_DIR + "flag_win.png", FLAG_SIZE)

FLAG_SUPPORT = create_image(FLAG_SUPPORT_DIR + "support.png", FLAG_SUPPORT_SIZE)
