import pygame
import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pass
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.hit_box = pygame.rect.inflate(0, -10)

        self.direction = pygame.math.Vector2()
        self.speed = 5 # pygame.math.Vector2(0, 0)

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * speed
        self.collision(direction = 'horizontal')
        self.hit_box.y += self.direction.y * speed
        self.collision(direction = 'vertical')

        self.rect.center = self.hit_box.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if self.direction.x > 0:
                    self.hit_box.right = sprite.hit_box.left
                if self.direction.x < 0:
                    self.hit_box.left = sprite.hit_box.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if self.direction.y > 0:
                    self.hit_box.bottom = sprite.hit_box.top
                if self.direction.y < 0:
                    self.hit_box.top = sprite.hit_box.bottom

    def update(self, delta_time):
        self.controls()
        self.move(self.speed)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.camera = None

    def draw(self, surface):
        for sprite in self.sprites():
            if sprite.rect.y < self.camera.rect.y:
                surface.blit(sprite.image, sprite.rect)

    def update(self, delta_time):
        self.sprites().sort(key = lambda sprite: sprite.rect.centery)
        super().update(delta_time)
