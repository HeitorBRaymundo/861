import os, sys
import pygame
from pygame.locals import *
import time
from sprite_class import Sprite

# pygame.init()

class PPU():
    speed = [2, 2]
    black = 0, 0, 0

    nth_render = 0

    all_sprites_list = pygame.sprite.Group()
    bg = pygame.sprite.Group()

    clock = pygame.time.Clock()

    def __init__(self, size):
        # size = [width, height]
        self.screen = pygame.display.set_mode(size)
        self.x_limit_position = size[0]
        self.y_limit_position = size[1]

    def build_bg(self, sprite):
        x_axis = 0
        y_axis = 0

        for vertical in range(0, 32):
            for horizontal in range(0, 32):
                bg = Sprite(42, 42, sprite, False)
                bg.rect.x = x_axis
                bg.rect.y = y_axis
                x_axis = x_axis + 8
                self.bg.add(bg)
            x_axis = 0
            y_axis = y_axis + 8


    def build_full_sprite(self, sprites, all_sprites_list, initial_position, array_flags):
        pacman_0 = Sprite(42, 42, sprites[0], array_flags[0])
        pacman_1 = Sprite(42, 42, sprites[1], array_flags[1])
        pacman_2 = Sprite(42, 42, sprites[2], array_flags[2])
        pacman_3 = Sprite(42, 42, sprites[3], array_flags[3])

        # Posicao 1
        pacman_0.rect.x = initial_position[0][0]
        pacman_0.rect.y = initial_position[0][1]

        # Posicao 2 (deslocado 3 * a diferenca entre a posicao 1)
        pacman_1.rect.x = initial_position[0][0] + (initial_position[1][0] - initial_position[0][0]) * 1
        pacman_1.rect.y = initial_position[0][1] + (initial_position[1][1] - initial_position[0][1]) * 1

        # Posicao 3 (deslocado 3 * a diferenca entre a posicao 1)
        pacman_2.rect.x = initial_position[0][0] + (initial_position[2][0] - initial_position[0][0]) * 1
        pacman_2.rect.y = initial_position[0][1] + (initial_position[2][1] - initial_position[0][1]) * 1

        # Posicao 4 (deslocado 3 * a diferenca entre a posicao 1)
        pacman_3.rect.x = initial_position[0][0] + (initial_position[3][0] - initial_position[0][0]) * 1
        pacman_3.rect.y = initial_position[0][1] + (initial_position[3][1] - initial_position[0][1]) * 1
        self.all_sprites_list.add(pacman_0)
        self.all_sprites_list.add(pacman_1)
        self.all_sprites_list.add(pacman_2)
        self.all_sprites_list.add(pacman_3)

        return [pacman_0, pacman_1, pacman_2, pacman_3]

    def build_sprite(self, sprite, initial_position, array_flags):
        return self.build_full_sprite(sprite, self.all_sprites_list, initial_position, array_flags)

    def update_sprite(self, sprite, speed, screen_size):
        [x, y] = speed
        sprite.rect.x = (sprite.rect.x + x) % screen_size[0]
        sprite.rect.y = (sprite.rect.y + y) % screen_size[1]

    def render(self):
        #Game Logic

        #Drawing on Screen
        self.screen.fill((0, 0, 0))

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        self.bg.draw(self.screen)
        self.all_sprites_list.draw(self.screen)

        #Refresh Screen
        pygame.display.update()

        pygame.event.pump()

        #Number of frames per secong e.g. 60
        self.clock.tick(24)

        # self.clock.tick(124)
