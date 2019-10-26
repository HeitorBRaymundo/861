import os, sys
import pygame
from pygame.locals import *
import time

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("logo-ic-unicamp.png")
ballrect = ball.get_rect()
ball2 = pygame.image.load("logo-ic-unicamp.png")
ballrect2 = ball.get_rect()
ball3 = pygame.image.load("logo-ic-unicamp.png")
ballrect3 = ball.get_rect()


# print (ballrect)
# print (type(ball))
# ballrect.top = ballrect.top + 100
# print (ballrect)

# print (dir(ballrect))
i = 0
while i < 2000:
    ballrect.top = ballrect.top - 1
    # print (ballrect.top)
    ballrect.left = ballrect.left - 1
    screen.fill(black)
    screen.blit(ball, ballrect)
    time.sleep(0.01)
    i = i + 1

    ballrect2.left = ballrect.left
    ballrect2.top = ballrect.top
    ballrect3.left = ballrect.left
    ballrect3.top = ballrect.top

    if (ballrect.top * -1 > ballrect.height):
        ballrect.top = 240 - ballrect.height

    if (ballrect.left * -1 > ballrect.width):
        ballrect.left = 320 - ballrect.width

    if (ballrect.top < 0):
        ballrect2.top = ballrect.top + 240
        # ballrect2.left = ballrect.left
        screen.blit(ball2, ballrect2)
        pygame.display.flip()

    if (ballrect.left < 0):
        ballrect2.left = ballrect.left + 320
        screen.blit(ball2, ballrect2)
        pygame.display.flip()
    

    pygame.display.flip()

print ("OI")