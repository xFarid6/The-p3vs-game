import pygame
import time
import os
from states.blueprint import Blueprint
from states.load_spritesheet import Spritesheet
from settings import *
from typing import TypeVar, List, Dict

main_class_ref = TypeVar("reference to class in main")


class Menu(Blueprint):
    def __init__(self, base_class: main_class_ref) -> None:
        """
        It loads the background and the fox sprite sheet, and it sets the initial values of the
        variables.
        
        :param base_class: the class that contains the game canvas
        """
        self.base_class: main_class_ref = base_class
        self.prev_state: object = None

        # Load backgrounds
        self.backgrounds_path: str = os.path.join(os.path.dirname(__file__), '../assets/Backgrounds/')
        self.background: Surface = pygame.image.load(os.path.join(self.backgrounds_path, 'merged-full-background.png'))

        # resize the background to the game canvas size
        self.background: Surface = pygame.transform.scale(self.background, (self.base_class.GAME_W, self.base_class.GAME_H))
        self.bg_rect: Rect = self.background.get_rect()
        self.bg_copy: Surface = self.background.copy()
        self.bg_x: int = 0
        # print(id(self.background), id(self.bg_copy))

        self.fox: Spritesheet = Spritesheet(os.path.join(os.path.dirname(__file__), '../player/Fox Sprite Sheet.png'))
        self.fox_actions: Dict[str, List[pygame.Surface]] = self.fox.load_anims(size=32, 
            anim_names={'tail_wiggle', 'look_back', 'run', 'jump', 'scared', 'sleep', 'sit'},
            frames=[5, 14, 8, 11, 5, 6, 7])
        self.tw_i: float = 0.0
        self.anim_names: List[str] = ['tail_wiggle', 'look_back', 'run', 'jump', 'scared', 'sleep', 'sit']
        self.selected_anim: str = 'sleep'
        self.swap: float = 0
        self.fox_x: int = 0
        self.fox_speed: int = 10


    def update(self, delta_time: float, actions: Dict[str, bool]) -> None:
        """
        The background moves to the left, and the fox's animation changes when the spacebar is pressed
        
        :param delta_time: The time in seconds since the last update
        :param actions: a dictionary of all the actions that are currently being pressed
        """
        self.bg_rect.x -= 1
        if self.bg_rect.x <= -self.background.get_width():
            self.bg_rect.x = 0

        self.tw_i += 0.1
        if self.tw_i >= len(self.fox_actions[self.selected_anim]):
            self.tw_i = 0

        if actions['space']:
            self.selected_anim = self.anim_names[self.swap % len(self.anim_names)]
            self.swap += 1
            self.tw_i = 0
            actions['space'] = False
            

    def render(self, surface: pygame.Surface) -> None:
        """
        The function renders the background, the fox, and the text on the screen
        
        :param surface: the surface to draw the fox on
        """
        surface.blit(self.background, (self.bg_rect.x, 0))
        surface.blit(self.bg_copy, self.bg_rect.topright)
        self.base_class.draw_text(surface,
                    'Menu', BLACK,
                    self.base_class.GAME_W//2, self.base_class.GAME_H//2 - 100)

        # draw a text that says "press space to start"
        self.base_class.draw_text(surface,
                    'Space to start', BLACK,
                    self.base_class.GAME_W//2 - 100, self.base_class.GAME_H//2, 
                    font=COMICSANS, size=24)

        # draw a text that says "press escape to quit"
        self.base_class.draw_text(surface,
                    'Escape to quit', BLACK,
                    self.base_class.GAME_W//2 + 100, self.base_class.GAME_H//2,
                    font=COMICSANS, size=24)

        # draw the fox with her animation at the bottom left of the screen
        self.fox.draw(surface, self.fox_actions[self.selected_anim][int(self.tw_i)], (self.fox_x, self.base_class.GAME_H - 32))