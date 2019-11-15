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
    flag_enable_render = True

    all_sprites_list = pygame.sprite.Group()
    bg = pygame.sprite.Group()

    clock = pygame.time.Clock()

    cicle_number = 0

    #Flags da PPUCTRL ($2000)
    # VPHB SINN
    flag_enable_NMI = False #V
    flag_PPU_master_slave = False #P
    flag_sprite_height = False #H
    flag_bg_tile = False #B
    flag_tile_select = False #S
    flag_increment_mode = False #I
    flag_name_table = '00' #NN

    #Flags da PPUMASK ($2001)
    # BGRs bMmG
    flag_emphasis_blue = False #B
    flag_emphasis_green = False #G
    flag_emphasis_red = False #R
    flag_enable_sprite = False #s
    flag_enable_bg = False #b
    flag_enable_left_column = False #M
    flag_enable_left_bg_column = False #m
    flag_greyscale = False #G

    #Flags da PPUSTATUS ($2002)
    #VSO- ---- 	
    flag_vblank = False #V
    flag_sprite_hit = False
    flag_sprite_overflow = False


    #OAMADDR ($2003)
    #aaaa aaaa
    oam_read_write_address = '00000000'

    #OAMDATA ($2004)
    #dddd dddd
    oam_data_read_write = '00000000'

    #PPUSCROLL ($2005)
    #xxxx xxxx 	
    scroll_pos_x = '0000'
    scroll_pos_y = '0000'

    #PPUADDR ($2006)
    #aaaa aaaa
    ppu_read_write_address = '00000000'

    #PPUDATA ($2007)
    #dddd dddd
    ppu_data_read_write = '00000000'

    #OAMDMA ($4004)
    #aaaa aaaa
    oam_dma_high_address = '00000000'

    sprites = []

    def __init__(self, size, nesROM):
        # size = [width, height]
        self.screen = pygame.display.set_mode(size)
        self.x_limit_position = size[0]
        self.y_limit_position = size[1]
        self.chr_rom = nesROM.chr_rom
        self.chr_size = nesROM.chr_rom_size * 8 * 1024   

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

    # newControl eh um inteiro entre 0 e 255, precisamos parsear no formato
    #Flags da PPUCTRL ($2000)
    # VPHB SINN
    # flag_enable_NMI = False #V
    # flag_PPU_master_slave = False #P
    # flag_sprite_height = False #H
    # flag_bg_tile = False #B
    # flag_tile_select = False #S
    # flag_increment_mode = False #I
    # flag_name_table = '00' #NN
    def update_ppu_control(self, newControl):
        self.flag_name_table = bin((newMask >> 0) % 4)[2:]
        self.flag_increment_mode = (newMask >> 2) % 2
        self.flag_tile_select = (newMask >> 3) % 2
        self.flag_bg_tile = (newMask >> 4) % 2
        self.flag_sprite_height = (newMask >> 5) % 2
        self.flag_PPU_master_slave = (newMask >> 6) % 2
        self.flag_enable_NMI = (newMask >> 7) % 2

    
    def read_sprite(self, rom, chr_size):
        i = 0
        flag = False
        sprite = []
        while i < 8:
            try:
                temporary = bin(rom[i])[2:].zfill(8)
            except:
                flag = False
                break
            sprite.append(temporary)
            if (temporary != '11111111'):
                flag = True
            # print (i + i, " ", temporary)
            i = i + 1

        return flag, sprite 

    # newMask eh um inteiro entre 0 e 255, precisamos parsear no formato 
    #Flags da PPUMASK ($2001)
    # BGRs bMmG
    # flag_emphasis_blue = False #B
    # flag_emphasis_green = False #G
    # flag_emphasis_red = False #R
    # flag_enable_sprite = False #s
    # flag_enable_bg = False #b
    # flag_enable_left_column = False #M
    # flag_enable_left_bg_column = False #m
    # flag_greyscale = False #G
    def update_ppu_mask(self, newMask):
        self.flag_greyscale = (newMask >> 0) % 2
        self.flag_enable_left_bg_column = (newMask >> 1) % 2
        self.flag_enable_left_column = (newMask >> 2) % 2
        self.flag_enable_bg = (newMask >> 3) % 2
        self.flag_enable_sprite = (newMask >> 4) % 2
        self.flag_emphasis_red = (newMask >> 5) % 2
        self.flag_emphasis_green = (newMask >> 6) % 2
        self.flag_emphasis_blue = (newMask >> 7) % 2

    #OAMADDR ($2003)
    #aaaa aaaa
    def update_OAM_Address(self, newOamAddress):
        self.oam_read_write_address = bin(newOamAddress)[2:]
    #OAMDATA ($2004)
    #dddd dddd
    def update_OAM_Data(self, newOamData):
        self.oam_data_read_write = bin(newOamAddress)[2:]
    #PPUSCROLL ($2005)
    #xxxx xxxx 	
    # tem umas regras mais cabulosas para preencher essas
    def update_scrool_pos(self, newScrollPos):
        self.scroll_pos_x = '0000'
        self.scroll_pos_y = '0000'

    #PPUADDR ($2006)
    #aaaa aaaa
    def update_PPU_Address(self, newPpuAddress):
        self.ppu_read_write_address = bin(newOamAddress)[2:]

    #PPUDATA ($2007)
    #dddd dddd
    def update_PPU_Address(self, newPpuData):
        self.ppu_data_read_write = bin(newPpuData)[2:]

        
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
    

    # percorre todos os CHR para separa os sprites
    # input: chr_pgr e chr_size
    # output: spriteList (cada entrada da lsita é uma lista com a cor já mapeada (mas ainda não é o valor da cor hexa exata)
    # isso será tratado em seguida (podemos migrar para ca)
    def evaluate_sprite(self):
        
        i = 0
        spriteList = []
        while i < self.chr_size:

            # A principio, supomos que nao eh um sprite, se encontrar um valor diferente de '0xff', eh um sprite
            flag = False
            lowList = []
            highList = []

            flag, lowList = self.read_sprite(self.chr_rom[i:], 8)
            
            # Andamos de 8 em 8 posicoes (tamanho do sprite)
            i = i + 8

            # Se encontrou um potencial sprite, verificar se o proximo byte eh o High
            if (flag):
                j = 0
                flag = False
                while j < 8:
                    try:
                        temporary = bin(self.chr_rom[i + j])[2:].zfill(8)
                    except:
                        flag = False
                        break
                    # print (temporary)
                    highList.append(temporary)
                    if (temporary != '11111111'):
                        flag = True
                    j = j + 1

                # se encontrou o High do sprite, talvez nao precisemos disso, supoe que semrpe tem low e high
                if (flag):
                    i = i + 8
                    colorList = []
                    # une o low e high bit para mapear qual sera a cor em cada posicao do sprite
                    for j in range(8):
                        for k in range(8):
                            colorList.append(int(lowList[j][k]) + 2 * int(highList[j][k]))
                    spriteList.append(colorList)
        self.sprites = spriteList

    def colorSprites(self):


    def tick(self):
        self.cicle_number += 1

    def step(self):
        self.tick()
        can_render = True
        if (can_render): # condicao para poder renderizar
            self.evaluate_sprite()
            self.render_sprite()

