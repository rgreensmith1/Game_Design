import pygame
from settings import screen_width

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((30, 10))
        self.rect = self.image.get_rect(topleft=pos)
        if direction == 0:
            direction = 1
            self.image.fill("red")
        else:
            direction = -1
            self.image.fill("grey")
        self.speed = 10
        self.direction = pygame.math.Vector2(direction * self.speed, 0)

    def update(self):
        self.rect.x += self.direction.x
        if self.rect.x > screen_width or self.rect.x < 0:
            self.kill()
