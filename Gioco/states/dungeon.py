import pygame
import time
import os
from states.blueprint import Blueprint
from states.settings import *
from typing import TypeVar, Dict, Tuple, List
from states.level_loader import LevelLoader


class Dungeon(Blueprint):
    def __init__(self, base_class) -> None:
        # basic
        self.base_class: object = base_class
        self.prev_state: object = None
        self.world_shift: Vector2 = pygame.math.Vector2(0, 0)
        self.dungeon_graphics_size: int = 16

        # map
        # the graphics and the layers will have to be redefined at each new level
        self.graphics = import_cut_graphics(
            os.path.join(
                os.getcwd(), 'Gioco', 'maps', 'dungeon', '0x72_16x16DungeonTileset.v3.png'), 
                16)
        self.layers: Dict[str, str] = {
            'bottom floor': "Gioco\maps\dungeon\dungeon_Bottom floor.csv",
            'map border': "Gioco\maps\dungeon\dungeon_Map border.csv",
            'columns': "Gioco\maps\dungeon\dungeon_Columns.csv",
            'walls': "Gioco\maps\dungeon\dungeon_Walls.csv",
        }

        # using the level loader to load all the tiles of all the groups and distributing them in layers
        self.level_loader = LevelLoader(self.graphics, self.dungeon_graphics_size, self.layers)
        self.level_groups: Dict[str, pygame.sprite.Group] = self.level_loader.load_level_groups()


    def update(self, delta_time: float, actions: Dict[str, bool]) -> None:
        if self.world_shift.magnitude() != 0:
            self.world_shift = self.world_shift.normalize()
        
        if actions['left']:
            self.world_shift.x += 1
        elif actions['right']:
            self.world_shift.x -= 1
        elif actions['up']:
            self.world_shift.y += 1
        elif actions['down']:
            self.world_shift.y -= 1
        else: 
            self.world_shift.y = 0
            self.world_shift.x = 0
        for group in self.level_groups.values():
            group.update(self.world_shift)


    def render(self, surface: pygame.Surface) -> None:
        for group in self.level_groups.values():
            group.draw(surface)
            