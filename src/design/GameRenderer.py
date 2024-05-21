import pygame

class GameRenderer:
    def __init__(self, screen: pygame.Surface, player_sprite: pygame.Surface,
                 enemy_sprite: pygame.Surface, obstacle_sprite: pygame.Surface,
                 power_up_sprite: pygame.Surface):
        self.screen = screen
        self.player_sprite = player_sprite
        self.enemy_sprite = enemy_sprite
        self.obstacle_sprite = obstacle_sprite
        self.power_up_sprite = power_up_sprite

        # Render the player on the screen
        # Render an enemy on the screen
        # Render an obstacle on the screen
        # Render a power-up on the screen
