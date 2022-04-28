import pygame
import os
from states.blueprint import Blueprint
from assets.color_codes import names, color_codes


class ColorSettings(Blueprint):
    def __init__(self, base_class):
        Blueprint.__init__(self, base_class)

        self.font = pygame.font.Font(
            "assets\Comfortaa\Comfortaa-VariableFont_wght.ttf", 10)

    def update(self, delta_time, actions):
        if actions['back']:
            self.base_class.state_stack.pop()
            actions['back'] = False

    def render(self, surface):
        surface.fill(color_codes['crimson'])
        self.draw_text(surface, 'saved for a future update',
                       (0, 0, 0), 30, 135)

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, False, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.midleft = (x, y)
        surface.blit(text_surface, text_rect)
