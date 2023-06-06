import pygame, sys
from level import Level
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))
clock = pygame.time.Clock()
level = Level(level_map, screen)

pygame.font.init()
font = pygame.font.Font("fonts/Goldman-Bold.ttf", 40)
text = font.render("Plane Game", True, (0,100,0))

pygame.font.init()
font = pygame.font.Font("fonts/Goldman-Regular.ttf", 40)

#code for when players have 0 lives so the game is over
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if level.player.sprite.lives <=    0:
        break

    screen.fill((0,191,255))
    level.run()

    #text for displaying lives on the screen
    screen.blit(text, (0, 0))
    text1 = font.render(str(level.player.sprite.lives), True, (0,100,0))
    screen.blit(text1, (300, 0))
    pygame.display.update()
    clock.tick(fps)


