import pygame, random
from settings import tile_size, screen_width, screen_heigth
from tile import Tile
from player import Player
from enemy import Enemy
from bird import Bird


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)

        self.world_shift = -0.5

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "b":
                    tile = Bird((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

        for i in range (25):
            enemy = Enemy((random.randint(300,screen_width), random.randint(0, screen_heigth)))
            self.enemies.add(enemy)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update(self.tiles)
        self.enemies.update()
        self.player.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        for e in self.enemies:
            e.draw_bullets(self.display_surface)

        #detects collisions
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)
        for enemy in collided_with:
            print(enemy.rect.x, enemy.rect.y)
            print(enemy)


        collided_with2 = pygame.sprite.groupcollide(self.player.sprite.bullets, self.enemies, True, True)
        for enemy in collided_with2:
            print(enemy.rect.x, enemy.rect.y)
            print(enemy)
            self.player.sprite.lives += 50
            print("lives: " + str(self.player.sprite.lives))

        for e in self.enemies:
            collided_with3 = pygame.sprite.groupcollide(e.bullets, self.player, True, False)
            for p in collided_with3:
                self.player.sprite.lives -= 50
                print("lives: " + str(self.player.sprite.lives))


