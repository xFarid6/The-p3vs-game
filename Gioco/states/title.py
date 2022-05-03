import pygame
import time
from states.blueprint import Blueprint
from states.menu import Menu
from states.settings import *
from typing import TypeVar, Dict

main_class_ref = TypeVar("reference to class in main")


class Title(Blueprint):
    def __init__(self, base_class: main_class_ref) -> None:
        """
        A constructor for the class.
        
        :param base_class: The class that we're going to be modifying
        """
        self.base_class: main_class_ref = base_class
        self.prev_state: object = None

        self.progress_fac: float = 0.0


    def update(self, delta_time: int, actions: Dict[str, bool]) -> None:
        """
        The function is called every frame, and it increases the progress_fac variable by 2 until it
        reaches 1, at which point it creates a new Menu object and calls its enter_state() function
        
        :param delta_time: The time in seconds since the last update
        :param actions: a list of actions that the player has performed
        """
        self.progress_fac += 0.01 # 0.01
        if self.progress_fac > 1:
            self.progress_fac = 1

            self.menu: Menu = Menu(self.base_class)
            self.menu.enter_state()


    def render(self, surface: pygame.Surface) -> None:
        """
        The function draws a rectangle that fills up over time
        
        :param surface: The surface to draw on
        """
        self.base_class.draw_text(surface,
                    'Progress Exploration', (0, 0, 0),
                    self.base_class.GAME_W//2, self.base_class.GAME_H//2)

        # draw a progess bar that fills up over time
        pygame.draw.rect(surface, LOADING_BAR_COLOR, (
                self.base_class.GAME_W//2 - 100, self.base_class.GAME_H//2 + 50,
                200 * self.progress_fac, 20),
                width=0, border_radius=10)

        pygame.draw.rect(surface, (0, 0, 0), (
                self.base_class.GAME_W//2 - 100, self.base_class.GAME_H//2 + 50, 
                200, 20),
                width=2, border_radius=10)
