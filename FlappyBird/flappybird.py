# make a flappy bird game
import pygame 
import random
import time


class FlappyBird:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True

        
        # bird stuff
        self.bird = Bird(20, 20, 30, 30)
        self.pipes = [
            Pipe(x = 600, y = 0, gap = 200),
            Pipe(x = 800, y = 0, gap = 200),
            Pipe(x = 1000, y = 0, gap = 200),
            Pipe(x = 1200, y = 0, gap = 200),
        ]
        
        self.points = 0


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    exit()
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

        
    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()

        if self.clock.get_time() % 2 == 0:
            self.points += 1


    def draw(self):
        # fill the screen with a sky blue color
        self.screen.fill((135, 206, 250))
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.bird.draw(self.screen)

        # draw the score
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(f"Score: {self.points}", 1, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        pygame.display.flip()

    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    
    def get_distance_from_pipe(self):
        pass


    def play_step(self, move):
        if move:
            self.bird.jump()


class Bird:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.img = pygame.Rect(x, y, width, height)

        self.done = False
        # define a yellowish color for the bird
        self.color = (240, 230, 50)


    def update(self):
        self.velocity += self.gravity
        self.img.y += self.velocity

        # if the bird hits the ground
        if self.img.y > 600 - self.img.height:
            self.img.y = 600 - self.img.height
            self.velocity = 0
            self.done = True

        if self.img.y < 0:
            self.img.y = 0
            self.velocity = 0
            self.done = True

    
    def jump(self):
        self.velocity = -10


    def game_end(self):
        return self.done


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.img)
        if self.game_end() and not self.done:
            print("Game Over")
            self.done = True
            # use the font to write "Game over" message
            # text = self.font.render("Game Over", True, (255, 0, 0))
            # screen.blit(text, (200, 150))
            # text = self.font.render("Press any key to play again", True, (255, 0, 0))
            # screen.blit(text, (100, 200))


class Pipe:
    def __init__(self, x, y, gap):
        self.n = random.randint(100, 300)
        self.img = pygame.Rect(x, y, 50, self.n)
        self.gap = gap
        self.color = (0, 255, 0)


    def update(self):
        self.img.x -= 2
        # if the pipe goes over the screen reset it
        if self.img.x < -50:
            self.reset_pipe()


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.img)
        # draw the other half of the pipe
        pygame.draw.rect(screen, self.color, (self.img.x, self.n + self.gap, 50, pygame.display.get_surface().get_height() - self.n - self.gap))


    def reset_pipe(self):
        self.img.x = 750
        self.n = random.randint(100, 300)
        self.img.y = 0


if __name__ == "__main__":
    game = FlappyBird()
    game.run()