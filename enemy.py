import pygame, random
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("graphics/player/idle/BiplanesAndFighterPlanes.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.fire_counter = 0
        self.fire = random.randint(1, 130)

        self.bullets = pygame.sprite.Group()
        self.firing = False

    def fire_bullets(self):
        bullet = Bullet((self.rect.centerx, self.rect.centery), -1)
        self.bullets.add(bullet)


    def update(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)

        #code for the random firing of the enemies
        self.fire_counter += 1
        if self.fire_counter == self.fire:
            self.fire_counter = 0
            self.fire = random.randint(1, 130)
            self.fire_bullets()
        self.bullets.update()

    def draw_bullets(self, surface):
        self.bullets.draw(surface)
