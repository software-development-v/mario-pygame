import pygame
from pygame import Surface
from typing import List, Tuple

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

    def render(
        self,
        player_pos: Tuple[int, int],
        enemies_pos: List[Tuple[int, int]],
        obstacles_pos: List[Tuple[int, int]],
        power_ups_pos: List[Tuple[int, int]]
    ) -> None:
        # TODO: Implement this method the render logic
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.player_sprite, player_pos)

        for enemy_pos in enemies_pos:
            self.screen.blit(self.enemy_sprite, enemy_pos)

        for obstacle_pos in obstacles_pos:
            self.screen.blit(self.obstacle_sprite, obstacle_pos)

        for power_up_pos in power_ups_pos:
            self.screen.blit(self.power_up_sprite, power_up_pos)

        pygame.display.flip()
