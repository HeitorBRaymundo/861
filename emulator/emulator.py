import sys
from py import system
from py.operations import *
from rom import Rom
from memory_helper import *
from threading import Timer,Thread,Event
import time
import ppu
from controllers import *
import pygame
# from teste_carts import igu

cycle_counter = 0
stop_threads = False

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

        self.cycle_counter = 0
        self.last_timestamp = time.time()
        # print("Cycles: ", self.cycle_counter)
        # print("Time Elapsed: ", time.time() - self.last_timestamp)

    def run(self):
        while not self.stopped.wait(0.00000000000000001):
            if self.cycle_counter >= 60:
                # print("Cycles: ", self.cycle_counter)
                # print("Time Elapsed: ", time.time() - self.last_timestamp)
                self.cycle_counter = 0
                self.last_timestamp = time.time()
            else:
                pass

try:
    file = sys.argv[1]
except:
    pass

nesROM = Rom(file)
systemCPU = system.System(nesROM)

pygame.init()
pygame.display.set_mode((100, 100))

pgr_bytes = nesROM.prg_rom
chr_rom = nesROM.chr_rom
chr_size = nesROM.chr_rom_size * 8 * 1024
controler_read_state = 0
all_keys = []
player1_key_index = 0
player2_key_index = 0


stopFlag = Event()
thread = MyThread(stopFlag)
# thread.start()


i = 0

spriteList = []
posSprite = []
in_forever = True

# percorre todos os CHR para separa os sprites
# input: chr_pgr e chr_size
# output: spriteList (cada entrada da lsita é uma lista com a cor já mapeada (mas ainda não é o valor da cor hexa exata)
# isso será tratado em seguida (podemos migrar para ca)
while i < chr_size:

    # A principio, supomos que nao eh um sprite, se encontrar um valor diferente de '0xff', eh um sprite
    flag = False
    lowList = []
    highList = []

    j = 0
    while j < 8:
        try:
            temporary = bin(chr_rom[i + j])[2:].zfill(8)
        except:
            flag = False
            break
        lowList.append(temporary)
        if (temporary != '11111111'):
            flag = True
        # print (i + j, " ", temporary)
        j = j + 1

    # Andamos de 8 em 8 posicoes (tamanho do sprite)
    i = i + 8

    # Se encontrou um potencial sprite, verificar se o proximo byte eh o High
    if (flag):
        j = 0
        flag = False
        while j < 8:
            try:
                temporary = bin(chr_rom[i + j])[2:].zfill(8)
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

positionConfigSprite = 0xe000


# ESSA PARTE IRA QUANDO O CLOCK BATER 60. COMO O PROPRIO JOGO IRA ALTERAR O VALOR DO X E Y DO PACMAN, IRA FUNCIONAR AS EXPECTED

# Inicializa i e begin com a posicao inicial das informacoes do sprite (onde ele esta, qual a cor, se reflete, etc.)
i = positionConfigSprite - systemCPU.PC_OFFSET
begin = positionConfigSprite - systemCPU.PC_OFFSET
# existe uma limitacao de 64 sprites (cada sprite tem 4 bytes de configuracao, totalizando 256 posicoes de memoria)
maxSprite = i + 256


# retirar o primeiro sprite que eh o bg
# bg = [spriteList[0], spriteList[0], spriteList[0], spriteList[0]]
bg = spriteList[0]
spriteList = spriteList[1:]

# local_ppu = ppu.PPU([500, 500])

# pulo de 32 pois eh o upload dos pallets
spriteWithHexColor = []
offsetzinho = 0
deslocInicial = 0
array_flag = []
bin_flag = []
while i < maxSprite:
    # print (hex(pgr_bytes[i]), " ", deslocInicial)
    if (hex(pgr_bytes[i]) != '0xff'):
        if (deslocInicial > 31 and deslocInicial % 4 == 1):
            newList = []
            for j in spriteList[pgr_bytes[i]]:
                # + 16 para ir para o pallete das cores do sprite
                # (pgr_bytes[i + 1] % 4) eh para ver qual dos blocos de cor ira pegar
                # j eh para identificar qual a cor de cada posicao (0 eh a primeira, 1 eh a segunda, etc.)
                newList.append(bin(pgr_bytes[begin + 16 + 4 * (pgr_bytes[i + 1] % 4) + j])[2:].zfill(8))

            # import pdb; pdb.set_trace()
            # Verificacao se precisa inverter verticalmente (falta fazer horizontalmente)
            bin_flag.append(pgr_bytes[i + 1])
            if (pgr_bytes[i + 1] >= 64 and pgr_bytes[i + 1] < 128):
                array_flag.append(True)
            else:
                array_flag.append(False)
            # Posicao que ira criar o sprite em questao
            posSprite.append([pgr_bytes[i + 2], pgr_bytes[i - 1]])
            spriteWithHexColor.append(newList)
            i = i + 3
            deslocInicial = deslocInicial + 3

    i = i + 1
    deslocInicial = deslocInicial + 1

# array_flag = [array_flag[1], array_flag[0], array_flag[3], array_flag[2]]
local_ppu = ppu.PPU([256, 240])

bg_list = []
for j in bg:
    # + 16 para ir para o pallete das cores do sprite
    # (pgr_bytes[i + 1] % 4) eh para ver qual dos blocos de cor ira pegar
    # j eh para identificar qual a cor de cada posicao (0 eh a primeira, 1 eh a segunda, etc.)
    bg_list.append(bin(pgr_bytes[begin + j])[2:].zfill(8))

print(bg_list)
local_ppu.build_bg(bg_list)

for i in range(int(len(spriteWithHexColor)/ 4)):
    # print(spriteWithHexColor[4*i:4*(i + 1)])
    local_ppu.build_sprite(spriteWithHexColor[4*i:4*(i + 1)], posSprite[4*i:4*(i + 1)], array_flag[4*i:4*(i + 1)])

# time.sleep(10)
# ppu.teste(spriteWithHexColor[0], spriteWithHexColor[1], spriteWithHexColor[2], spriteWithHexColor[3], array_flag, posSprite)
local_ppu.render()

temp = pgr_bytes[0x2002] + 128
exec("temp = b"+'"\\'+hex(temp)[1:]+'"')
pgr_bytes = pgr_bytes[:0x2002] + temp + pgr_bytes[0x2003:]
systemCPU.rom.prg_rom = pgr_bytes
systemCPU.ppu_set = 1

while True:
    opcode = hex(pgr_bytes[systemCPU.program_counter])

    addr = None
    stack = None
    # print (opcode + " " +  hex(pgr_bytes[systemCPU.program_counter + 1]))

    # import pdb; pdb.set_trace()

    if opcode == '0x0':
        systemCPU.program_counter = systemCPU.program_counter + 1
        stop_threads = True
        # this will stop the timer
        # stopFlag.set()
        break

    elif opcode == '0x6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        ASL_zero_page_0x06(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ASL_A_0x0A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_absolute_0x0E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x16':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ASL_zero_page_index_0x16(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x1e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_abs_X_0x01E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x26':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_0x26(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x2a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROL_A_0x2A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x2e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_absolute_0x2E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x36':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_index_0x36(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x3e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_abs_X_0x3E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x46':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_0x46(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x4a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        LSR_A_0x4A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_absolute_0x4E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x56':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_index_0x56(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x5e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_abs_X_0x05E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x61':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x61(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x65':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x65(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x66':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_0x66(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x69':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x69(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x6a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROR_A_0x6A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x6d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x6D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x6e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_absolute_0x6E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x71':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x71(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x75':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x75(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x76':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_index_0x76(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x79':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x79(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x7d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x7D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x7e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_abs_X_0x7E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x88':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0x88(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xc6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        DEC_zero_page_0xC6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xc8':
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xC8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xca':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0xCA(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xce':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        DEC_absolute_0xCE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xd6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_zero_page_X_0xD6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xde':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_absolute_X_0xDE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0xe1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xE1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xe5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xE5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xe6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        INC_zero_page_0xE6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xe8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xE8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE9(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xed':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xED(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xee':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        if addr == 0x200:
            print("OI IGU")
        INC_absolute_0xEE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xf1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xf5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xF5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xf6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_zero_page_X_0xF6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xf9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF9(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xfd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xFD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xfe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_absolute_X_0xFE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 7

    # PAREI AQUI
    # FUSCA \/
    elif opcode == '0x8': # Flags / stack
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHP0x08(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3
        stack_val = systemCPU.stack_val_return
        # i = i + 0
    elif opcode == '0x18':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLC0x18(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x28':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLP0x28(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
        # i = i + 0
    elif opcode == '0x38':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEC0x38(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x48':
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHA0x48(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3
        stack_val = systemCPU.stack_val_return
        # i = i + 0
    elif opcode == '0x68':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLA0x68(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
        # i = i + 0
    elif opcode == '0xb8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLV0xB8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xd8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLD0xD8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xf8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        SED0xF8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x24': # Bit test HELP

        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        BIT_zpg0x24(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
        # i = i + 1
    elif opcode == '0x2c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        BIT_abs0x2C(systemCPU, addr)


        thread.cycle_counter = thread.cycle_counter + 4
        # i = i + 2
    elif opcode == '0x40': # interrupt
        systemCPU.program_counter = systemCPU.program_counter + 1

        # print("PIROCA")
        # Renders screen
        in_forever = True

        print("MEMORIA DO PACMAN: ")
        print(systemCPU.loadMem(0x200), systemCPU.loadMem(0x203))

        local_ppu.all_sprites_list = pygame.sprite.Group()
        for i in range (0x200,0x250, 16):
            if (systemCPU.loadMem(i) != -1):
                pos = []
                spritesToPrint = []
                array_flags_to_print = []
                pos.append([systemCPU.loadMem(i + 3), systemCPU.loadMem(i)])
                pos.append([systemCPU.loadMem(i + 7), systemCPU.loadMem(i + 4)])
                pos.append([systemCPU.loadMem(i + 11), systemCPU.loadMem(i + 8)])
                pos.append([systemCPU.loadMem(i + 15), systemCPU.loadMem(i + 12)])
                spritesToPrint.append(spriteWithHexColor[systemCPU.loadMem(i + 1)  + 4 * (systemCPU.loadMem(i + 2) % 4)])
                spritesToPrint.append(spriteWithHexColor[systemCPU.loadMem(i + 5) + 4 * (systemCPU.loadMem(i + 6) % 4)])
                spritesToPrint.append(spriteWithHexColor[systemCPU.loadMem(i + 9) + 4 * (systemCPU.loadMem(i + 10) % 4)])
                spritesToPrint.append(spriteWithHexColor[systemCPU.loadMem(i + 13) + 4 * (systemCPU.loadMem(i + 14) % 4)])
                array_flags_to_print.append(array_flag[systemCPU.loadMem(i + 1)])
                array_flags_to_print.append(array_flag[systemCPU.loadMem(i + 5)])
                array_flags_to_print.append(array_flag[systemCPU.loadMem(i + 9)])
                array_flags_to_print.append(array_flag[systemCPU.loadMem(i + 13)])
                # print ("--------------------")
                # print (systemCPU.loadMem(i + 1))
                # print (systemCPU.loadMem(i + 5))
                # print (systemCPU.loadMem(i + 9))
                # print (systemCPU.loadMem(i + 13))
                # print ("spritesToPrint", spritesToPrint)
                # print (spriteWithHexColor[systemCPU.loadMem(i + 1)])
                # print (spriteWithHexColor[systemCPU.loadMem(i + 5)])
                # print (spriteWithHexColor[systemCPU.loadMem(i + 9)])
                # print (spriteWithHexColor[systemCPU.loadMem(i + 13)])
                # print ("pos", pos)
                # print ("array_flags_to_print", array_flags_to_print)
                # print (array_flag)
                # print ("--------------------")
                local_ppu.build_sprite(spritesToPrint, pos, array_flags_to_print)

        local_ppu.render()
        # import pdb; pdb.set_trace()
        RTI0x40(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6
        # i = i + 0
    elif opcode == '0x58':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLI0x58(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xea': # NOP
        systemCPU.program_counter = systemCPU.program_counter + 1
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x10':
        systemCPU.program_counter = systemCPU.program_counter + 2

        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        old_pc = systemCPU.program_counter

        BPL0x10(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0x20':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.stack_push(systemCPU.program_counter, 2)
        systemCPU.program_counter = get_absolute_addr(low, high) - 0x8000
        thread.cycle_counter = thread.cycle_counter + 6
        # i = i + 1
    elif opcode == '0x30':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BMI0x30(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4c': # JMP abs
        if (in_forever):
            systemCPU.program_counter = ((systemCPU.rom.prg_rom[systemCPU.rom.interrupt_handlers['NMI_HANDLER'] + 1 - systemCPU.PC_OFFSET] << 8) + systemCPU.rom.prg_rom[systemCPU.rom.interrupt_handlers['NMI_HANDLER'] - systemCPU.PC_OFFSET]) - 0x8000
            in_forever = False
            systemCPU.stack_push(systemCPU.program_counter,2)
            systemCPU.stack_push(0,1)
        else:
            systemCPU.program_counter = systemCPU.program_counter + 3
            low = pgr_bytes[systemCPU.program_counter - 2]
            high = pgr_bytes[systemCPU.program_counter - 1]
            systemCPU.program_counter = get_absolute_addr(low, high) - 0x8000
            thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x50':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVC0x50(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x60':
        lo = systemCPU.stack_pop()
        hi = systemCPU.stack_pop()
        hi = hi << 8

        if systemCPU.stack_neg:
            systemCPU.program_counter = - (((hi | lo) ^ 0xfff) + 1)
        else:
            systemCPU.program_counter = hi | lo
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x6c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        thread.cycle_counter = thread.cycle_counter + 5

    elif opcode == '0x70':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVS0x70(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x78':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEI0x78(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x90':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCC0x90(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xb0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCS0xB0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xd0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BNE0xD0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xf0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BEQ0xF0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    # HEITOR \/
    elif opcode == '0x1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        OrWithAcumulator0x01(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        OrWithAcumulator0x05(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        OrWithAcumulator0x09(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        OrWithAcumulator0x0D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x11':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        OrWithAcumulator0x11(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x15':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        OrWithAcumulator0x15(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x19':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x19(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x1d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x1D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x21':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        AndWithAcumulator0x21(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x25':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        AndWithAcumulator0x25(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x29':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        AndWithAcumulator0x29(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x2d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        AndWithAcumulator0x2D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x31':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        AndWithAcumulator0x31(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x35':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        AndWithAcumulator0x35(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x39':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x39(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x3d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x3D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x41':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        ExclusiveOrWithAcumulator0x41(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x45':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        ExclusiveOrWithAcumulator0x45(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x49':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        ExclusiveOrWithAcumulator0x49(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        ExclusiveOrWithAcumulator0x4D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x51':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        ExclusiveOrWithAcumulator0x51(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x55':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        ExclusiveOrWithAcumulator0x55(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x59':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x59(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x5d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x5D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xc0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithY0xC0(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xc1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        CompareWithAcumulator0xC1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xc4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithY0xC4(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xc5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithAcumulator0xC5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xc9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithAcumulator0xC9(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xcc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithY0xCC(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xcd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithAcumulator0xCD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xd1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        CompareWithAcumulator0xD1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xd5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        CompareWithAcumulator0xD5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xd9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xD9(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xdd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xDD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xe0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithX0xE0(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithX0xE4(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xec':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithX0xEC(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4

    # CARTS \/
    # STORES
    elif opcode == '0x81':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0x84':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x85':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x86':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x8c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x8d': # STA abs (para controle)
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)

        if (addr == 16406 or addr == 16407):
            if (controler_read_state == 0 and systemCPU.A == 1):
                controler_read_state = 1
            elif (controler_read_state == 1 and systemCPU.A == 0):
                controler_read_state = 0
                all_keys = latch_controllers()
            elif (controler_read_state == 1 and systemCPU.A != 0):
                controler_read_state = 0
        elif addr == 0x4014:
            pass
            # import pdb; pdb.set_trace()
        StoreInA0x8D(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x8e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x91':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0x94':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x95':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x96':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x99':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        # if addr == 0x220 and in_forever:
        #     import pdb;pdb.set_trace()
        # if addr >= 0x0200:
        #     pass
        #     # import pdb; pdb.set_trace()
        StoreInA0x99(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5


    elif opcode == '0x9d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5


    # LOADS
    elif opcode == '0xa0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xa1':
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0xa2':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xa4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xac':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xad': # LDA abs
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        if (addr == 16406):
            print(systemCPU.A)
            systemCPU.A = get_key(all_keys, player1_key_index, 1)
            if player1_key_index != 7:
                player1_key_index += 1
            else:
                player1_key_index = 0
            if systemCPU.A != 0:
                print(systemCPU.A, player1_key_index)

        elif (addr == 16407):
            systemCPU.A = get_key(all_keys, player2_key_index, 2)
            if player2_key_index != 7:
                player2_key_index += 1
            else:
                player2_key_index = 0

        else:
            LoadInA0xAD(register='A', position=addr, system=systemCPU)

        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xae':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb1':
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xb4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb9':
        # TA AQUI A PORRA DO BUG TOMA NU CU CARALHO PORRA SI FUDE
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)

        if addr >= 0xe000:
            value_to_load = pgr_bytes[addr - systemCPU.PC_OFFSET]
            systemCPU.A = value_to_load
        else:
            LoadFromA0xB9(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadInA0xBD(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1


    # TRANSFERS BETWEEN REGISTERS
    elif opcode == '0x8a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TXA_0x8A(first_register='X', second_register='A', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x98':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TYA_0x98(first_register='Y', second_register='A', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xaa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAX_0xAA(first_register='A', second_register='X', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xa8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAY_0xA8(first_register='A', second_register='Y', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2

    # TRANSFERS TO THE STACK POINTER
    elif opcode == '0x9a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_X_to_SP_Op_0x9A(system=systemCPU).execute()
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xba':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_SP_to_X_Op_0xBA(system=systemCPU).execute()
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x':
        systemCPU.program_counter = systemCPU.program_counter + 1
    else:
        print ("Erro")
        pass



    # if addr is None and stack is None:
    #    # print("PC: ", systemCPU.program_counter)
    #    print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
    #           "| a = 0x%0.2x" % systemCPU.getA(), "| x = 0x%0.2x" %  systemCPU.getX(), \
    #           "| y = 0x%0.2x" %  systemCPU.getY(), "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
    #           "| p[NV-BDIZC] =", systemCPU.printFLAG(),"|")
    # elif addr is not None and stack is None:
    #    print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
    #           "| a = 0x%0.2x" % systemCPU.getA(), \
    #           "| x = 0x%0.2x" %  systemCPU.getX(), \
    #           "| y = 0x%0.2x" %  systemCPU.getY(), \
    #           "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
    #           "| p[NV-BDIZC] =", systemCPU.printFLAG(),\
    #           "| MEM[0x%0.4x]" % addr, "= 0x%0.2x" % systemCPU.loadMem(addr),"|")
    # elif addr is None and stack is not None:
    #    print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
    #           "| a = 0x%0.2x" % systemCPU.getA(), \
    #           "| x = 0x%0.2x" %  systemCPU.getX(), \
    #           "| y = 0x%0.2x" %  systemCPU.getY(), \
    #           "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
    #           "| p[NV-BDIZC] =", systemCPU.printFLAG(),\
    #           "| MEM[0x%0.4x]" % stack, "= 0x%0.2x" % stack_val,"|")
