import pygame
import time
from states.blueprint import Blueprint

class Title(Blueprint):
    def __init__(self, base_class):
        self.base_class = base_class
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        self.base_class.draw_text(surface,
                                  'Progress Exploration',
                                  (0, 0, 0),
                                  self.base_class.GAME_W//2,
                                  self.base_class.GAME_H//2)
