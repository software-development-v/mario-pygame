from pygame import Surface

from src.utils import get_centered_message, write_high_score

from ..abstracts import LevelState


class GameOverState(LevelState):

    def render(self, screen: Surface) -> None:
        message, message_rect = get_centered_message("GAME OVER")
        write_high_score(self.level_manager.get_score())
        screen.blit(message, (message_rect.x, message_rect.y))
