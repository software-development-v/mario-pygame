from src.utils.assets.players.create_images import create_image
from src.utils.constants import GENERAL_SIZE
from src.utils.directories import BLOCK_DIR, BRICK_DIR, BROKE_BRICK_DIR, MASTERY_BLOCK_DIR, PIECES_DIR, WALL_DIR

OVERWORLD_BLOCK = create_image(BLOCK_DIR + "overworld-block.png", GENERAL_SIZE)

OVERWORLD_BRICK = create_image(BRICK_DIR + "overworld.png", GENERAL_SIZE)

OVERWORLD_BROKE_BRICK = create_image(BROKE_BRICK_DIR + "brick.png", GENERAL_SIZE)

OVERWORLD_BROKE_PIECE_1 = create_image(PIECES_DIR + "1.png", GENERAL_SIZE)
OVERWORLD_BROKE_PIECE_2 = create_image(PIECES_DIR + "2.png", GENERAL_SIZE)

MASTERY_BLOCK_1 = create_image(MASTERY_BLOCK_DIR + "1.png", GENERAL_SIZE)
MASTERY_BLOCK_2 = create_image(MASTERY_BLOCK_DIR + "2.png", GENERAL_SIZE)

WALL = create_image(WALL_DIR + "wall.png", GENERAL_SIZE)
