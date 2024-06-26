from pygame import Surface

from src.utils import get_centered_message


from ..abstracts import LevelState

class GameOverState(LevelState):


    def render(self, screen: Surface) -> None:
        message, message_rect = get_centered_message("GAME OVER")
        screen.blit(message, (message_rect.x, message_rect.y))
