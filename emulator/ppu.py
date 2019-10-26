import os, sys
import pygame
from pygame.locals import *
import time
from sprite_class import Sprite

pygame.init()

class PPU():
    speed = [2, 2]
    black = 0, 0, 0

    all_sprites_list = pygame.sprite.Group()

    clock = pygame.time.Clock()

    def __init__(self, size):
        # size = [width, height]
        self.screen = pygame.display.set_mode(size)
        self.x_limit_position = size[0]
        self.y_limit_position = size[1]

    def build_full_sprite(self, sprites, all_sprites_list, initial_position, array_flags):
        pacman_0 = Sprite(42, 42, sprites[0], array_flags[0])
        pacman_1 = Sprite(42, 42, sprites[1], array_flags[1])
        pacman_2 = Sprite(42, 42, sprites[2], array_flags[2])
        pacman_3 = Sprite(42, 42, sprites[3], array_flags[3])

        pacman_0.rect.x = initial_position[0]
        pacman_0.rect.y = initial_position[1]

        pacman_1.rect.x = initial_position[0] + 21
        pacman_1.rect.y = initial_position[1]

        pacman_2.rect.x = initial_position[0]
        pacman_2.rect.y = initial_position[1] + 21

        pacman_3.rect.x = initial_position[0] + 21
        pacman_3.rect.y = initial_position[1] + 21

        self.all_sprites_list.add(pacman_0)
        self.all_sprites_list.add(pacman_1)
        self.all_sprites_list.add(pacman_2)
        self.all_sprites_list.add(pacman_3)

        return [pacman_0, pacman_1, pacman_2, pacman_3]

    # initial_position = [x, y]
    def build_sprite(self, sprite, initial_position, array_flags):
        return self.build_full_sprite(sprite, self.all_sprites_list, initial_position, array_flags)

    def update_sprite(self, sprite, new_position):
        [x, y] = new_position
        sprite.rect.x = x
        sprite.rect.y = y

    def render(self):
        #Game Logic
        self.all_sprites_list.update()

        #Drawing on Screen
        self.screen.fill((0, 0, 0))

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        self.all_sprites_list.draw(self.screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        self.clock.tick(24)

# if not pygame.font: print('Warning, fonts disabled')
# if not pygame.mixer: print('Warning, sound disabled')

# pixels = [
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
#     "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100", "00000100",
# ]

apixels_2 = [
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
    "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100", "00011100",
]

apixels_3 = [
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
    "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100", "00101100",
]

apixels_4 = [
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
    "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101", "00111101",
]

def teste(pixels, pixels_2, pixels_3, pixels_4, array_flags):
    sprites = [pixels, pixels_2, pixels_3, pixels_4]

    ppu = PPU([500, 500])

    first_sprite = ppu.build_sprite(sprites, [200,300], array_flags)
    second_sprite = ppu.build_sprite(sprites, [200,100], array_flags)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn=False

        if (first_sprite[0].rect.x >= 500):
            ppu.update_sprite(first_sprite[0], [0, 300])
            ppu.update_sprite(first_sprite[1], [21, 300])
            ppu.update_sprite(first_sprite[2], [0, 321])
            ppu.update_sprite(first_sprite[3], [21, 321])
            
        else:
            ppu.update_sprite(first_sprite[0], [first_sprite[0].rect.x + 10, 300])
            ppu.update_sprite(first_sprite[1], [first_sprite[1].rect.x + 10, 300])
            ppu.update_sprite(first_sprite[2], [first_sprite[2].rect.x + 10, 321])
            ppu.update_sprite(first_sprite[3], [first_sprite[3].rect.x + 10, 321])

        ppu.render()


# size = width, height = 400, 500
# speed = [2, 2]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# all_sprites_list = pygame.sprite.Group()
# pacman = (build_sprite(sprites, all_sprites_list, [200, 300]), [200, 400])
#
# pacman_2 = (build_sprite(sprites, all_sprites_list, [200, 100]), [200, 400])
#
#
# # ball = pygame.image.load("logo-ic-unicamp.png")
# # ballrect = ball.get_rect()
# # ball2 = pygame.image.load("logo-ic-unicamp.png")
# # ballrect2 = ball.get_rect()
# # ball3 = pygame.image.load("logo-ic-unicamp.png")
# # ballrect3 = ball.get_rect()
#
# # print (ballrect)
# # print (type(ball))
# # ballrect.top = ballrect.top + 100
# # print (ballrect)
#
# # print (dir(ballrect))
# clock = pygame.time.Clock()
# limit_position = 400
# i = 0
# while i < 2000:
#     # ballrect.top = ballrect.top - 1
#     # print (ballrect.top)
#     # ballrect.left = ballrect.left - 1
#     # screen.fill(black)
#     # screen.blit(ball, ballrect)
#     # time.sleep(0.01)
#     # i = i + 1
#     #
#     # ballrect2.left = ballrect.left
#     # ballrect2.top = ballrect.top
#     # ballrect3.left = ballrect.left
#     # ballrect3.top = ballrect.top
#     #
#     # if (ballrect.top * -1 > ballrect.height):
#     #     ballrect.top = 240 - ballrect.height
#     #
#     # if (ballrect.left * -1 > ballrect.width):
#     #     ballrect.left = 320 - ballrect.width
#     #
#     # if (ballrect.top < 0):
#     #     ballrect2.top = ballrect.top + 240
#     #     # ballrect2.left = ballrect.left
#     #     screen.blit(ball2, ballrect2)
#     #     pygame.display.flip()
#     #
#     # if (ballrect.left < 0):
#     #     ballrect2.left = ballrect.left + 320
#     #     screen.blit(ball2, ballrect2)
#     #     pygame.display.flip()
#
#
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             carryOn=False
#
#     if (pacman[1][0] >= limit_position):
#         pacman[1][0] = 0
#         pacman[0][0].rect.x = 0
#         pacman[0][1].rect.x = 21
#         pacman[0][2].rect.x = 0
#         pacman[0][3].rect.x = 21
#     else:
#         pacman[1][0] = pacman[1][0] + 10
#         pacman[0][0].rect.x = pacman[0][0].rect.x + 10
#         pacman[0][1].rect.x = pacman[0][1].rect.x + 10
#         pacman[0][2].rect.x = pacman[0][2].rect.x + 10
#         pacman[0][3].rect.x = pacman[0][3].rect.x + 10
#
#     #Game Logic
#     all_sprites_list.update()
#
#     #Drawing on Screen
#     screen.fill((0, 0, 0))
#
#     #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
#     all_sprites_list.draw(screen)
#
#     #Refresh Screen
#     pygame.display.flip()
#
#     #Number of frames per secong e.g. 60
#     clock.tick(24)
#
#
#     # pygame.display.flip()
#
# print ("OI")
