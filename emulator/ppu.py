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
    flag_enable_render = False

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

        # Nao vai funcionar para o generico

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
        sprite_to_build = Sprite(42, 42, sprites, array_flags)

        # Posicao 1
        sprite_to_build.rect.x = initial_position[0]
        sprite_to_build.rect.y = initial_position[1]

        self.all_sprites_list.add(sprite_to_build)
        

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
        self.clock.tick(48)

        # self.clock.tick(124)
