import pygame

from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        # self.image = pygame.Surface((32, 64))
        # self.image.fill("red")
        self.image = pygame.image.load("graphics/player/idle/Bomber.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.lives = 1000
        self.bullets = pygame.sprite.Group()
        self.firing = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.x = 0
            self.direction.y = 0

        if keys[pygame.K_SPACE] and not self.firing:
            self.fire()
            self.firing = True
        elif not keys[pygame.K_SPACE] and self.firing:
            self.firing = False

    def fire(self):
        bullet = Bullet((self.rect.centerx, self.rect.centery), self.direction.x)
        self.bullets.add(bullet)

    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                if self.direction.x >= 0 :
                    self.rect.right = tile.rect.left

    def vertical_movement_collision(self, tiles):
        self.rect.y += self.direction.y * self.speed
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                if self.direction.y < 0 :
                    self.rect.top = tile.rect.bottom


    def update(self, tiles):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
        self.bullets.update()

    def draw_bullets(self, surface):
        self.bullets.draw(surface)


