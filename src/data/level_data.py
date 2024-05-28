
from typing import Dict, Tuple

from pygame import Surface
from src.data.background.i_background import IBackground
from src.entities.abstractions.elements.element import Element
from src.entities.interfaces.i_entity import IEntity
from src.enums.level import Level
from src.enums.world import World
from src.utils.classes.position import Position


class LevelData:
    world:World
    level:Level
    time = 0
    background:IBackground
    background_music:str # TODO : Implement a music manager to handle this in #2 US
    player_start_position: Tuple[int, int]
    enemies:Dict[Position,IEntity]
    elements:Dict[Position,Element]
    power_ups : Dict[Position,IEntity]
    def __init__(self,
                 world:World,
                 level:Level,
                 time:int,
                 background:IBackground,
                 background_music:str,
                 player_start_position:Tuple[int,int],
                 enemies:Dict[Position,IEntity],
                 elements:Dict[Position,Element],
                 power_ups:Dict[Position,IEntity]
                 ) -> None:

        self.world = world
        self.level = level
        self.time = time
        self.background = background
        self.background_music = background_music
        self.player_start_position = player_start_position
        self.enemies = enemies
        self.elements = elements
        self.power_ups = power_ups


    def get_background(self)->Surface:
        return self.background.get_background()
