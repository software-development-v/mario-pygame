from os import path

from pygame import image

IMG_DIR = path.join(path.dirname(__file__), "../../", "assets")

ICON = image.load(path.join(IMG_DIR, "logo.png"))
BG = image.load(path.join(IMG_DIR, "background.png"))
PLAYER = image.load(path.join(IMG_DIR, "player.png"))
ENEMY = image.load(path.join(IMG_DIR, "enemy.png"))
OBSTACLE = image.load(path.join(IMG_DIR, "obstacle.png"))
POWER_UP = image.load(path.join(IMG_DIR, "power-up.png"))
