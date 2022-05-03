import os
import pygame
import sys
import time

from typing import Dict, List, TypeVar
from pygame.locals import *
from states.settings import *
from states.blueprint import Blueprint
from states.title import Title


class TheProgressExploration:

    def __init__(self) -> None:
        """
        It initializes pygame, sets the dimensions of the game, and sets up the game screen.
        """
        pygame.init()
        # Dimensions
        self.GAME_W, self.GAME_H = 480, 270
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1400, 700  # 960, 540

        # Screens
        self.game_canvas: Surface = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen: Surface = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # General Setup
        pygame.display.set_caption("Progress Exploration")
        self.clock: Clock = pygame.time.Clock()
        self.font: Font = pygame.font.SysFont("monospace", 30)
        self.running, self.playing = True, True
        self.actions: Dict[str, bool] = {'left': False, 'right': False,
                                        'up': False, 'down': False,
                                        'space': False, 'enter': False,
                                        }

        self.dt, self.prev_time = 0, 0
        self.state_stack: List[object] = []
        self.load_states()

       
    def get_events(self, actions: Dict[str, bool]) -> None:
        """
        The function get_events() takes in a dictionary called actions and then checks for events in the
        pygame.event.get() function. If the event is a QUIT event, then the running variable is set to
        False. If the event is a KEYDOWN event, then the function checks to see if the key pressed is
        the ESCAPE key. If it is, then the running variable is set to False. If the key pressed is the
        SPACE key, then the space key in the actions dictionary is set to True
        
        :param actions: a dictionary of actions that the player can take
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: self.running = False
                elif event.key == K_SPACE: actions['space'] = True
                elif event.key == K_RETURN: actions['enter'] = True
                elif event.key == K_LEFT: actions['left'] = True
                elif event.key == K_RIGHT: actions['right'] = True
                elif event.key == K_UP: actions['up'] = True
                elif event.key == K_DOWN: actions['down'] = True
            elif event.type == pygame.KEYUP:
                if event.key == K_SPACE: actions['space'] = False
                elif event.key == K_RETURN: actions['enter'] = False
                elif event.key == K_LEFT: actions['left'] = False
                elif event.key == K_RIGHT: actions['right'] = False
                elif event.key == K_UP: actions['up'] = False
                elif event.key == K_DOWN: actions['down'] = False
                


    def get_dt(self) -> None:
        """
        The function gets the current time, subtracts the previous time from it, and then sets the
        previous time to the current time
        """
        now: float = time.time()
        self.dt: float = now - self.prev_time
        self.prev_time: float = now


    def update(self, dt:float, actions: Dict[str, bool]) -> None:
        """
        The function updates the current state by calling the update function of the current state
        
        :param actions: a list of actions that the player has pressed
        """
        self.state_stack[-1].update(self.dt, self.actions)


    def draw(self) -> None:
        """
        It draws the game canvas to the screen, using the render function of the top element on the stack.
        """
        self.screen.fill(BLACK)
        self.game_canvas.fill(GRAY)
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(
            pygame.transform.scale(self.game_canvas, (self.screen.get_width(), self.screen.get_height())), (0, 0))
        pygame.display.flip()


    def draw_text(self, surface: pygame.Surface, text: str, 
                color: Tuple[int, int, int], x: int, y: int, 
                font: str='monospace', size: int=30, aa: bool=False) -> None:    # TODO: add possiblity to pick a font -> DONE
        """
        It draws text on the screen
        
        :param surface: the surface to draw the text on
        :param text: The text you want to draw
        :param color: The color of the text
        :param x: The x coordinate of the top left corner of the text
        :param y: the y coordinate of the text
        :param font: The font to use, defaults to monospace (optional)
        :param size: The size of the font, defaults to 30 (optional)
        :param aa: anti-aliasing, defaults to False (optional)
        """
        if font == 'monospace':
            font: Font = pygame.font.SysFont("monospace", size)
            text_surface: Surface = font.render(text, aa, color)
        else:
            font: Font = pygame.font.SysFont(font, size)
            text_surface: Surface = font.render(text, aa, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect: Rect = text_surface.get_rect()
        text_rect.center: Tuple[int, int] = (x, y)
        surface.blit(text_surface, text_rect)


    def load_states(self) -> None:
        """
        It loads the title screen
        """
        self.title_screen: Title = Title(self)
        self.state_stack.append(self.title_screen)


    def reset_keys(self) -> None:
        """
        It sets all the keys to false
        """
        for action in self.actions:
            self.actions[action] = False


    def run(self) -> None:
        """
        "While the game is running, get the events, update the game, and draw the game."
        
        The first line of the function is a while loop. This is a loop that will run as long as the
        condition is true. In this case, the condition is self.running. This is a boolean variable that
        is set to True when the game starts. If the game is running, the loop will continue to run
        """
        while self.running:
            self.clock.tick(60)
            self.get_events(self.actions)
            self.update(self.actions, self.dt)
            self.draw()


if __name__ == "__main__":
    game: TheProgressExploration = TheProgressExploration()
    game.run()