import os
import pygame
import sys
import time

from pygame.locals import *
from states.blueprint import Blueprint
from states.title import Title



class TheProgressExploration:
    def __init__(self):
        pygame.init()
        self.GAME_W, self.GAME_H = 480, 270
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1400, 700  # 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Progress Exploration")
        self.running, self.playing = True, True
        self.actions = {'left': False, 'right': False,
                        'up': False, 'down': False,
                        }

        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()
       
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def draw(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(
            self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        self.screen.blit(self.font.render("Progress Exploration", True, (0, 0, 0)), ( self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 50))
        pygame.display.flip()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, False, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.get_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = TheProgressExploration()
    game.run()