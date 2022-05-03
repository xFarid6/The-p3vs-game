import pygame
import time
import os
from states.blueprint import Blueprint
from states.settings import *
from typing import TypeVar, Dict, Tuple, List, Optional


class LevelLoader:
    def __init__(self, graphics: List[pygame.Surface], tile_size: int, layers: Dict[str, str]) -> None:
        # args
        self.graphics = graphics
        self.tile_size = tile_size
        self.layers = layers

        # setup
        self.layer_files = self.load_layers()
        self.level_groups = self.load_level_groups()


    def load_layers(self) -> Dict[str, List[List[str]]]:
        layers = {}
        for layer_name, layer_file in self.layers.items():
            layout = import_csv_layout_gc(layer_file)
            layers[layer_name] = layout

        return layers

    
    def create_tile_group(self, layout: List[List[str]]) -> pygame.sprite.Group:
        tile_group = pygame.sprite.Group()
        for y, row in enumerate(layout):
            for x, tile_name in enumerate(row):
                if tile_name != '':
                    tile_group.add(
                        Tile(
                            x * self.tile_size, y * self.tile_size,
                            self.graphics[int(tile_name)],
                        )
                    )
        return tile_group


    def load_level_groups(self, group_names: Optional[List[Tuple[str, str]]] = None) -> Dict[str, pygame.sprite.Group]:
        if group_names is None:
            print('all is good')
            # format: [([which tile ids], which group), ...]
        level_groups = {
            'all': pygame.sprite.Group(),
            # eventuali altri gruppi di default
        }
        # creare Tile() per ogni livello in layer_files
        for layer_name, layer_layout in self.layer_files.items():
            for row_index, row in enumerate(layer_layout):
                for tile_index, tile_name in enumerate(row):
                    if tile_name != '-1':
                        x = tile_index * self.tile_size
                        y = row_index * self.tile_size

                        # TODO: aggiungere qui una guardia per distinguere i tile statici da quelli animati

                        # Create a tile and associate the correct graphic, Static ones only, for now
                        sprite = StaticTile(x, y, self.tile_size, self.graphics[int(tile_name)])
                        # aggiungere il tile al Group() di appartenenza
                        level_groups['all'].add(sprite)
                        if layer_name in level_groups:
                            level_groups[layer_name].add(sprite)
                        else:
                            level_groups[layer_name] = pygame.sprite.Group()
                            level_groups[layer_name].add(sprite)
                        
                        if group_names is not None:
                            for tile_ids, group_name in group_names:
                                if int(tile_name) in tile_ids:
                                    level_groups[group_name].add(sprite)

        return level_groups


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.rect = self.image.get_rect(topleft = (x, y))
        
        self.image.fill('orange')


    def update(self, shift):
        self.rect.center += shift


class StaticTile(Tile):
    def __init__(self, x, y, size, surface):
        super().__init__(x, y, size)
        self.image: Surface = surface


class AnimatedTile(Tile):
    def __init__(self, x, y, size, surface):
        super().__init__(x, y, size)
        self.image: List[Surface] = surface

    
    def animate(self, delta_time: float):
        pass
