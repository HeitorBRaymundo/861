import pygame
WHITE = (255, 255, 255)

colors = {
"00000000": (124,124,124),
"00000001": (0,0,252),
"00000010": (0,0,188),
"00000011": (68,40,188),
"00000100": (148,0,132),
"00000101": (168,0,32),
"00000110": (168,16,0),
"00000111": (136,20,0),
"00001000": (80,48,0),
"00001001": (0,120,0),
"00001010": (0,104,0),
"00001011": (0,88,0),
"00001100": (0,64,88),
"00001101": (0,0,0),
"00001110": (0,0,0),
"00001111": (0,0,0),
"00010000": (188,188,188),
"00010001": (0,120,248),
"00010010": (0,88,248),
"00010011": (104,68,252),
"00010100": (216,0,204),
"00010101": (228,0,88),
"00010110": (248,56,0),
"00010111": (228,92,16),
"00011000": (172,124,0),
"00011001": (0,184,0),
"00011010": (0,168,0),
"00011011": (0,168,68),
"00011100": (0,136,136),
"00011101": (0,0,0),
"00011110": (0,0,0),
"00011111": (0,0,0),
"00100000": (248,248,248),
"00100001": (60,188,252),
"00100010": (104,136,252),
"00100011": (152,120,248),
"00100100": (248,120,248),
"00100101": (248,88,152),
"00100110": (248,120,88),
"00100111": (252,160,68),
"00101000": (248,184,0),
"00101001": (184,248,24),
"00101010": (88,216,84),
"00101011": (88,248,152),
"00101100": (0,232,216),
"00101101": (120,120,120),
"00101110": (0,0,0),
"00101111": (0,0,0),
"00110000": (252,252,252),
"00110001": (164,228,252),
"00110010": (184,184,248),
"00110011": (216,184,248),
"00110100": (248,184,248),
"00110101": (248,164,192),
"00110110": (240,208,176),
"00110111": (252,224,168),
"00111000": (248,216,120),
"00111001": (216,248,120),
"00111010": (184,248,184),
"00111011": (184,248,216),
"00111100": (0,252,252),
"00111101": (248,216,248),
"00111110": (0,0,0),
"00111111": (0,0,0),
"11111110": (0,0,0),
"11111111": (0,0,0)
}

class Sprite(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height, drawing, flag):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.flag = flag

        self.build_image(drawing)

        # Draw the car (a rectangle!)
        # pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def build_image(self, pixels):
        default_size = 3
        x_offset = 0 if not self.flag else 21
        y_offset = 0
        cur_pixel = 0
        if (self.flag):
            for y in range(0, 8):
                for x in range(0, 8):
                    pygame.draw.rect(self.image, colors[pixels[cur_pixel]], (x_offset, y_offset, default_size, default_size))
                    x_offset = x_offset - default_size
                    cur_pixel = cur_pixel + 1
                x_offset = 21
                y_offset = y_offset + default_size
        else:
            for y in range(0, 8):
                for x in range(0, 8):
                    pygame.draw.rect(self.image, colors[pixels[cur_pixel]], (x_offset, y_offset, default_size, default_size))
                    x_offset = x_offset + default_size
                    cur_pixel = cur_pixel + 1
                x_offset = 0
                y_offset = y_offset + default_size


def build_sprite(sprites, all_sprites_list, pos):
    pacman_0 = Sprite(48, 48, sprites[0])
    pacman_1 = Sprite(48, 48, sprites[1])
    pacman_2 = Sprite(48, 48, sprites[2])
    pacman_3 = Sprite(48, 48, sprites[3])

    pacman_0.rect.x = pos[0].x
    pacman_0.rect.y = pos[0].y

    pacman_1.rect.x = pos[1].x
    pacman_1.rect.y = pos[1].y

    pacman_2.rect.x = pos[2].x
    pacman_2.rect.y = pos[2].y

    pacman_3.rect.x = pos[3].x
    pacman_3.rect.y = pos[3].y

    all_sprites_list.add(pacman_0)
    all_sprites_list.add(pacman_1)
    all_sprites_list.add(pacman_2)
    all_sprites_list.add(pacman_3)

    return [pacman_0, pacman_1, pacman_2, pacman_3]

# SCREENWIDTH=400
# SCREENHEIGHT=500
#
# size = (SCREENWIDTH, SCREENHEIGHT)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Pacman da Vitoria")

# all_sprites_list = pygame.sprite.Group()
#
# pacman = (build_sprite(sprites, all_sprites_list), [200, 400])

#Allowing the user to close the window...
# carryOn = True
# clock = pygame.time.Clock()
#
# limit_position = 400
#
# while carryOn:
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
#     clock.tick(60)
#
# pygame.quit()
