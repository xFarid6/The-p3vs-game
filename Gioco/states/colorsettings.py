import pygame
import os
from blueprint import Blueprint
from typing import TypeVar, Dict
# from assets.color_codes import names, color_codes

main_class_ref = TypeVar("reference to class in main")


# It's a class that inherits from the Blueprint class, and it's used to display the color settings
# menu.
class ColorSettings(Blueprint):
    def __init__(self, base_class: main_class_ref) -> None:
        Blueprint.__init__(self, base_class)

        self.font: Font = pygame.font.Font(
            "assets\Comfortaa\Comfortaa-VariableFont_wght.ttf", 10)

    def update(self, delta_time: float, actions: Dict[str, bool]) -> None:
        """
        If the back button is pressed, remove the current state from the stack and set the back button
        to false
        
        :param delta_time: The time in seconds since the last update
        :param actions: A dictionary of actions that the user has performed
        """
        if actions['back']:
            self.base_class.state_stack.pop()
            actions['back'] = False

    def render(self, surface: pygame.Surface) -> None:
        """
        It draws a text on the screen
        
        :param surface: the surface to draw the text on
        """
        surface.fill(color_codes['crimson'])
        self.draw_text(surface, 'saved for a future update',
                       (0, 0, 0), 30, 135)
