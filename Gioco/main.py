import pygame


class TheProgressExploration:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("The Progress Exploration")
        self.running = True
        self.font = pygame.font.SysFont("comicsansms", 30)
       
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.font.render("Progress Exploration", True, (0, 0, 0)), ( self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 50))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.get_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = TheProgressExploration()
    game.run()