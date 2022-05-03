import pygame
import time
import os
from states.blueprint import Blueprint
from states.settings import *
from typing import TypeVar, Dict, Tuple, List


class Dungeon(Blueprint):
    def __init__(self, base_class) -> None:
        # basic
        self.base_class: object = base_class
        self.prev_state: object = None
        self.world_shift: Tuple[int, int] = (0, 0)

        # map
        self.graphics = import_cut_graphics(
            os.path.join(
                os.getcwd(), 'Gioco', 'maps', 'dungeon', '0x72_16x16DungeonTileset.v3.png'), 
                16)


    def update(self, delta_time: float, actions: Dict[str, bool]) -> None:
        pass


    def render(self, surface: pygame.Surface) -> None:
        pass