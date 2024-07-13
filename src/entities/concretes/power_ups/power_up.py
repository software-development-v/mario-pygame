# from abc import ABC
# from typing import Dict, List
#
# from pygame import Surface
#
# from src.enums import EnemyState
# from src.utils import Position
#
#
# class Enemy(IEnemy, ABC):
#     __slots__ = (
#         "surfaces",
#         "state",
#         "initial_state",
#         "initial_position",
#         "face_right",
#         "is_touchable",
#         "speed",
#         "vel_y",
#         "collisions_handler",
#         "movement_handler",
#         "_rect",
#     )
#
#     def __init__(
#         self,
#         position: Position,
#         enemyState: EnemyState,
#         surfaces: Dict[EnemyState, List[Surface]],
#         value: int = 0,
#     ):
#         self.surfaces = surfaces
#         self.state = enemyState
#         self.initial_state = enemyState
#         self.initial_position = position
#         self.face_right = True
#         self.is_touchable = True
#         self.speed = 2
#         self.vel_y = 0
#         self.collisions_handler = collision_handler
#         self.movement_handler = EnemyMovementHandler(self)
#         super().__init__(position, value=value)
