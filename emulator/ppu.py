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
    enable_NMI = 0 #V
    PPU_master_slave = 0 #P
    sprite_height = 0 #H
    bg_tile = 0 #B
    tile_select = 0 #S
    increment_mode = 0 #I
    name_table = 0 #NN

    #Flags da PPUMASK ($2001)
    # BGRs bMmG
    emphasis_blue = 0 #B
    emphasis_green = 0 #G
    emphasis_red = 0 #R
    enable_sprite = 0 #s
    enable_bg = 0 #b
    enable_left_column = 0 #M
    enable_left_bg_column = 0 #m
    greyscale = 0 #G

    #Flags da PPUSTATUS ($2002)
    #VSO- ---- 	
    vblank = 0 #V
    sprite_hit = 0
    sprite_overflow = 0


    #OAMADDR ($2003)
    #aaaa aaaa
    oam_read_write_address = 0

    #OAMDATA ($2004)
    #dddd dddd
    oam_data_read_write = 0

    #PPUSCROLL ($2005)
    #xxxx xxxx 	
    scroll_pos_x = 0
    scroll_pos_y = 0

    #PPUADDR ($2006)
    #aaaa aaaa
    ppu_read_write_address = 0

    #PPUDATA ($2007)
    #dddd dddd
    ppu_data_read_write = 0

    #OAMDMA ($4004)
    #aaaa aaaa
    oam_dma_high_address = 0

    palette_bg = []
    palette_sprites = []

    # VARIAVEIS ANTES USADAS NO EMULATOR.PY
    sprites = []
    spriteWithHexColor = []
    array_flag = []
    bin_flag = []
    posSprite = []
    positionConfigSprite = 0xe000
    
    default_width = 256
    default_height = 224

    VRAM = [0] * 0x2000

    def __init__(self, nesROM, scale):
        # size = [width, height]
        # Verificar se precisa aumentar a VRAM
        self.VRAM[:0x2000] = nesROM.chr_rom
        # self.chr_rom = nesROM.chr_rom
        self.chr_size = nesROM.chr_rom_size * 8 * 1024   
        self.scale = scale
        self.screen = pygame.display.set_mode((self.default_width * self.scale, self.default_height * self.scale))

        self.pic = pygame.surface.Surface((self.default_width, self.default_height))
        self.screen.blit(pygame.transform.scale(self.pic, (self.default_width * self.scale, self.default_height * self.scale)), (0, 0))


        self.PC_OFFSET = 0x8000 if (nesROM.prg_rom_size==2) else 0xC000
        self.prg_bytes = nesROM.pgr_rom
        self.nesROM = nesROM
        # entender o que é isso
        self.SPR_RAM = [0] * 0x0100
        # self.SPR_RAM = np.zeros(0x0100, dtype=np.uint8)
        self.sprite_palette = [0,22,45,48,0,22,45,48,0,22,45,48,0,22,45,48,0,22,45,48]
        # self.sprite_palette = self.nesROM.chr_rom[0x3F10-(self.nesROM.chr_rom_size * 1024 * 8) : 0x3F20-(self.nesROM.chr_rom_size * 1024 * 8)]
        self.bg_palette = self.nesROM.chr_rom[0x3F00-(self.nesROM.chr_rom_size * 1024 * 8) : 0x3F10-(self.nesROM.chr_rom_size * 1024 * 8)]
        # print ("Sprite:")
        # for i in self.sprite_palette:
        #     print(i)
        # print ("BG:")
        # for i in self.bg_palette:
        #     print(i)

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

    def corno_func(self):
        self.pic = pygame.surface.Surface((self.default_width, self.default_height))
        self.screen.blit(pygame.transform.scale(self.pic, (self.default_width * self.scale, self.default_height * self.scale)), (0, 0))
        pygame.display.update()
        

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
        sprite = []
        while i < 8:
            try:
                temporary = bin(rom[i])[2:].zfill(8)
            except:
                break
            sprite.append(temporary)
            # print (i + i, " ", temporary)
            i = i + 1

        return sprite 

    def update_mem_SPR_RAM(self, newMem):
        self.SPR_RAM = newMem

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
        sprite_to_build = Sprite(42, 42, sprites, array_flags, "WHITE")

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
        bgList = []
        spriteList = []
        while i < self.chr_size/2:
            lowList = []
            highList = []
            colorList = []

            lowList = self.read_sprite(self.VRAM[i:], 8)
            highList = self.read_sprite(self.VRAM[i + 8:], 8)
            
            for j in range(8):
                for k in range(8):
                    colorList.append(int(lowList[j][k]) + 2 * int(highList[j][k]))
            bgList.append(colorList)
            i = i + 16
        while i < self.chr_size:
            lowList = []
            highList = []
            colorList = []

            lowList = self.read_sprite(self.VRAM[i:], 8)
            highList = self.read_sprite(self.VRAM[i + 8:], 8)
            
            for j in range(8):
                for k in range(8):
                    colorList.append(int(lowList[j][k]) + 2 * int(highList[j][k]))
            spriteList.append(colorList)
            i = i + 16
        
        self.bgSprite = bgList
        self.sprites = spriteList
        self.colorSprites()

    def colorSprites(self):
        # retirar o primeiro sprite que eh o bg <-- ISSO NO CASO DO NOSSO PACMAN!
        i  = 0
        # begin = self.rom.mapper self.positionConfigSprite - self.PC_OFFSET
        begin = (self.positionConfigSprite - self.PC_OFFSET)%0x4000
        spriteList = self.sprites
        # print (spriteList)
        # print ("begin", begin)
        # local_ppu = ppu.PPU([500, 500])

        # pulo de 32 pois eh o upload dos pallets
        # temp = []
        spriteColored = []
        deslocInicial = 0
        array_flag = []
        bin_flag = []
        posSprite = []

        # print ("AAAAAAAAAAAAAAA")
        # print (self.SPR_RAM)
        # import pdb; pdb.set_trace();
        # existe uma limitacao de 64 sprites (cada sprite tem 4 bytes de configuracao, totalizando 256 posicoes de memoria)     
        while i < 256:
            # print (self.nesROM.pgr_rom[begin + i], self.nesROM.pgr_rom[begin + i + 1], self.nesROM.pgr_rom[begin + i + 2], self.nesROM.pgr_rom[begin + i + 3])
            # print (hex(prg_bytes[i]), " ", deslocInicial)
            newList = []
            # print ("i: ",i)
            for j in spriteList[self.SPR_RAM[i + 1]]:
                # print ("j: ",j)
                # print ("SPR_RAM[i + 2]: ", (4 * (self.SPR_RAM[i + 2] % 4)) + j)
                # (self.nesROM.pgr_rom[begin + i + 1] % 4) eh para ver qual dos blocos de cor ira pegar
                # j eh para identificar qual a cor de cada posicao (0 eh a primeira, 1 eh a segunda, etc.)
                # print ((4 * (self.SPR_RAM[i + 2] % 4)) + j)
                # print (len(self.sprite_palette))
                newList.append(bin(self.sprite_palette[(4 * (self.SPR_RAM[i + 2] % 4)) + j])[2:].zfill(8))

            # Verificacao se precisa inverter verticalmente (falta fazer horizontalmente)
            bin_flag.append(self.nesROM.pgr_rom[begin + i + 1])
            if (self.SPR_RAM[i + 2] >= 64 and self.SPR_RAM[i + 2] < 128):
                array_flag.append(True)
            else:
                array_flag.append(False)
            # Posicao que ira criar o sprite em questao
            posSprite.append([self.SPR_RAM[i + 3], self.SPR_RAM[i]])
            spriteColored.append(newList)

            i = i + 4
            deslocInicial = deslocInicial + 4
        i = 0
        # spriteColored = []
        # print ("AAAA", len(temp))
        # print (self.SPR_RAM)
        # while i < 256:
        #     spriteColored.append(temp[(self.SPR_RAM[i + 1] % 64) ])
        #     i = i + 4

        self.array_flag = array_flag
        self.bin_flag = bin_flag
        self.spriteWithHexColor = spriteColored
        self.posSprite = posSprite


    def tick(self):
        self.cicle_number += 1

    def step(self):
        self.tick()
        can_render = True
        if (can_render): # condicao para poder renderizar
            self.evaluate_sprite()
            self.render_sprite()

