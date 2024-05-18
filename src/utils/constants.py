from os import path

from pygame import image

TITLE = "Mario"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30

IMG_DIR = path.join(path.dirname(__file__), "..", "assets")
ICON = image.load("src/assets/logo.png")

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
