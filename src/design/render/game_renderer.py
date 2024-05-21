from pygame import Surface


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
