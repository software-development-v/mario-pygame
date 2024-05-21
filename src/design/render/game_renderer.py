from typing import List, Tuple

from pygame import Surface, display

from src.utils.colors import WHITE_COLOR


class GameRenderer:
    def __init__(
        self,
        screen: Surface,
        player_sprite: Surface,
        enemy_sprite: Surface,
        obstacle_sprite: Surface,
        power_up_sprite: Surface,
    ):
        self.screen = screen
        self.player_sprite = player_sprite
        self.enemy_sprite = enemy_sprite
        self.obstacle_sprite = obstacle_sprite
        self.power_up_sprite = power_up_sprite
        self.player_pos: Tuple[int, int] = (200, 100)
        self.enemies_pos: List[Tuple[int, int]] = [(500, 200), (550, 250)]
        self.obstacles_pos: List[Tuple[int, int]] = [(800, 300), (850, 350)]
        self.power_ups_pos: List[Tuple[int, int]] = [(1100, 400), (1150, 450)]

    def render(self) -> None:
        self.screen.fill(WHITE_COLOR)

        self.screen.blit(self.player_sprite, self.player_pos)

        for enemy_pos in self.enemies_pos:
            self.screen.blit(self.enemy_sprite, enemy_pos)

        for obstacle_pos in self.obstacles_pos:
            self.screen.blit(self.obstacle_sprite, obstacle_pos)

        for power_up_pos in self.power_ups_pos:
            self.screen.blit(self.power_up_sprite, power_up_pos)

        display.flip()
