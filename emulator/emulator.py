import sys
from py import system
from py.operations import *
from rom import Rom
from memory_helper import *
from threading import Timer,Thread,Event
# from controllers import *
import time
import ppu
import pygame

try:
    file = sys.argv[1]
except:
    pass

nesROM = Rom(file)
systemCPU = system.System(nesROM)

pygame.init()
pygame.display.set_mode((256, 224))

# nesROM.pgr_rom = nesROM.prg_rom
chr_rom = nesROM.chr_rom
chr_size = nesROM.chr_rom_size * 8 * 1024
controler_read_state = 0
all_keys = []


i = 0
spriteList = []
in_forever = False


local_ppu = ppu.PPU(nesROM, 1)
local_ppu.evaluate_sprite()

# Inicializa i e begin com a posicao inicial das informacoes do sprite (onde ele esta, qual a cor, se reflete, etc.)
begin = local_ppu.positionConfigSprite - local_ppu.PC_OFFSET

maxSprite = i + 256


# retirar o primeiro sprite que eh o bg <-- ISSO NO NOSSO PACMAN

bg = local_ppu.sprites[0]

bg_list = []
for j in bg:
    # + 16 para ir para o pallete das cores do sprite
    # (nesROM.pgr_rom[i + 1] % 4) eh para ver qual dos blocos de cor ira pegar
    # j eh para identificar qual a cor de cada posicao (0 eh a primeira, 1 eh a segunda, etc.)
    bg_list.append(bin(nesROM.pgr_rom[begin + j])[2:].zfill(8))

# print(bg_list)
# local_ppu.build_bg(bg_list)

for i in range(int(len(local_ppu.spriteWithHexColor))):
    # print(local_ppu.spriteWithHexColor[4*i:4*(i + 1)])
    local_ppu.build_sprite(local_ppu.spriteWithHexColor[i], local_ppu.posSprite[i], local_ppu.array_flag[i])

local_ppu.render()
# import pdb;pdb.set_trace()

temp = (nesROM.pgr_rom[0x2002]%128) + 128
exec("temp = b"+'"\\'+hex(temp)[1:]+'"')
nesROM.pgr_rom = nesROM.pgr_rom[:0x2002] + temp + nesROM.pgr_rom[0x2003:]
systemCPU.rom.prg_rom = nesROM.pgr_rom
systemCPU.ppu_set = 1


def execute(opcode, systemCPU, pgr_bytes):
    
    """
    adad
    """
    addr = None
    stack = None
    systemCPU.all_keys = latch_controllers()

    # print(hex(systemCPU.program_counter), opcode)

    # if systemCPU.program_counter == (12511):
        # import pdb;pdb.set_trace()

    # print(systemCPU.mem)

    if opcode == '0x0':
        systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        ASL_zero_page_0x06(systemCPU, addr)
        systemCPU.cycle_counter += 5
    elif opcode == '0xa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ASL_A_0x0A(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_absolute_0x0E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x16':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ASL_zero_page_index_0x16(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x1e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_abs_X_0x01E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 7
    elif opcode == '0x26':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_0x26(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 5
    elif opcode == '0x2a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROL_A_0x2A(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x2e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_absolute_0x2E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x36':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_index_0x36(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x3e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_abs_X_0x3E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 7
    elif opcode == '0x46':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_0x46(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 5
    elif opcode == '0x4a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        LSR_A_0x4A(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x4e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_absolute_0x4E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x56':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_index_0x56(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x5e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_abs_X_0x05E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 7
    elif opcode == '0x61':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x61(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0x65':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x65(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0x66':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_0x66(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 5
    elif opcode == '0x69':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x69(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 2
    elif opcode == '0x6a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROR_A_0x6A(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x6d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x6D(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x6e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_absolute_0x6E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x71':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x71(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x75':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x75(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x76':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_index_0x76(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 6
    elif opcode == '0x79':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x79(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x7d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x7D(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x7e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_abs_X_0x7E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 7
    elif opcode == '0x88':

        # if systemCPU.Y == 0 and systemCPU.contadorLixo == 3:
        #     import pdb;pdb.set_trace()
        #     print("YAHSADSADASF")        

        if systemCPU.Y == 0:
            systemCPU.contadorLixo += 1
            print("oi")
            
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0x88(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xc6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        DEC_zero_page_0xC6(systemCPU, addr)
        systemCPU.cycle_counter += 5
    elif opcode == '0xc8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        # if systemCPU.Y == 255:
        #     print("aaaaaaaaa")
        IncreaseReg0xC8(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xca':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0xCA(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xce':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        DEC_absolute_0xCE(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xd6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_zero_page_X_0xD6(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xde':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_absolute_X_0xDE(systemCPU, addr)
        systemCPU.cycle_counter += 7
    elif opcode == '0xe1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xE1(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xe5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xE5(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0xe6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        INC_zero_page_0xE6(systemCPU, addr)
        systemCPU.cycle_counter += 5
    elif opcode == '0xe8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        # if systemCPU.X == 255:
        #     print("yuji coco")
        IncreaseReg0xE8(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xe9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE9(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        systemCPU.cycle_counter += 2
    elif opcode == '0xed':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xED(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0xee':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        INC_absolute_0xEE(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xf1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF1(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xf5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xF5(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0xf6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_zero_page_X_0xF6(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xf9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF9(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xfd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xFD(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xfe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_absolute_X_0xFE(systemCPU, addr)
        systemCPU.cycle_counter += 7
    elif opcode == '0x8': # Flags / stack
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHP0x08(systemCPU)
        systemCPU.cycle_counter += 3
        stack_val = systemCPU.stack_val_return
    elif opcode == '0x18':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLC0x18(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x28':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLP0x28(systemCPU)
        systemCPU.cycle_counter += 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
    elif opcode == '0x38':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEC0x38(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x48':
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHA0x48(systemCPU)
        systemCPU.cycle_counter += 3
        stack_val = systemCPU.stack_val_return
    elif opcode == '0x68':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLA0x68(systemCPU)
        systemCPU.cycle_counter += 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
    elif opcode == '0xb8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLV0xB8(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xd8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLD0xD8(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xf8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        SED0xF8(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x24': # Bit test HELP

        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        BIT_zpg0x24(systemCPU, addr)
        systemCPU.cycle_counter += 3
        # i = i + 1
    elif opcode == '0x2c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        BIT_abs0x2C(systemCPU, addr)


        systemCPU.cycle_counter += 4
        # i = i + 2
    elif opcode == '0x40': # interrupt
        # RTI0x40(systemCPU)
        # import pdb;pdb.set_trace()
        # PLP0x28(systemCPU)
        systemCPU.on_nmi = False
        systemCPU.cycle_counter += 6
    elif opcode == '0x58':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLI0x58(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xea': # NOP
        systemCPU.program_counter = systemCPU.program_counter + 1
        systemCPU.cycle_counter += 2
    elif opcode == '0x10':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        old_pc = systemCPU.program_counter
        BPL0x10(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0x20':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.stack_push(systemCPU.program_counter, 2)
        systemCPU.program_counter = get_absolute_addr(low, high) - 0x8000
        systemCPU.cycle_counter += 6
        # i = i + 1
    elif opcode == '0x30':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BMI0x30(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0x4c': # JMP abs
        # import pdb;pdb.set_trace()
        global in_forever
        if in_forever:
            pgr_bytes = nesROM.prg_rom
            
            in_forever = False
            systemCPU.stack_push(systemCPU.program_counter,2)
            systemCPU.stack_push(0,1)
        else:
            systemCPU.program_counter = systemCPU.program_counter + 3
            low = pgr_bytes[systemCPU.program_counter - 2]
            high = pgr_bytes[systemCPU.program_counter - 1]
            systemCPU.program_counter = get_absolute_addr(low, high) - 0x8000
            systemCPU.cycle_counter += 3
    elif opcode == '0x50':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVC0x50(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0x60':
        lo = systemCPU.stack_pop()
        hi = systemCPU.stack_pop()
        hi = hi << 8
        if systemCPU.stack_neg:
            systemCPU.program_counter = - (((hi | lo) ^ 0xfff) + 1)
        else:
            systemCPU.program_counter = hi | lo
        systemCPU.cycle_counter += 6
    elif opcode == '0x6c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        systemCPU.cycle_counter += 5

    elif opcode == '0x70':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVS0x70(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0x78':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEI0x78(systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x90':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCC0x90(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0xb0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCS0xB0(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0xd0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        # print(hex(old_pc+0x8000))
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BNE0xD0(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2

    elif opcode == '0xf0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BEQ0xF0(systemCPU, setPCToAddress)
        systemCPU.cycle_counter += 2
        if systemCPU.branch_hit:
            systemCPU.cycle_counter += 1
        if page_diff(old_pc, systemCPU.program_counter):
            systemCPU.cycle_counter += 2
    elif opcode == '0x1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        OrWithAcumulator0x01(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0x5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        OrWithAcumulator0x05(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0x9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        OrWithAcumulator0x09(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        OrWithAcumulator0x0D(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x11':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        OrWithAcumulator0x11(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x15':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        OrWithAcumulator0x15(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x19':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x19(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x1d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x1D(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x21':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        AndWithAcumulator0x21(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0x25':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        AndWithAcumulator0x25(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0x29':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        AndWithAcumulator0x29(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0x2d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        AndWithAcumulator0x2D(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x31':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        AndWithAcumulator0x31(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x35':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        AndWithAcumulator0x35(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x39':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x39(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x3d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x3D(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x41':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        ExclusiveOrWithAcumulator0x41(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0x45':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        ExclusiveOrWithAcumulator0x45(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0x49':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        ExclusiveOrWithAcumulator0x49(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0x4d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        ExclusiveOrWithAcumulator0x4D(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x51':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        ExclusiveOrWithAcumulator0x51(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x55':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        ExclusiveOrWithAcumulator0x55(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x59':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x59(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x5d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x5D(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xc0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithY0xC0(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xc1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        CompareWithAcumulator0xC1(systemCPU, addr)
        systemCPU.cycle_counter += 6
    elif opcode == '0xc4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithY0xC4(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0xc5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithAcumulator0xC5(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0xc9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithAcumulator0xC9(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xcc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithY0xCC(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0xcd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithAcumulator0xCD(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0xd1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        CompareWithAcumulator0xD1(systemCPU, addr)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xd5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        CompareWithAcumulator0xD5(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0xd9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xD9(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xdd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xDD(systemCPU, addr)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xe0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithX0xE0(systemCPU, operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xe4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithX0xE4(systemCPU, addr)
        systemCPU.cycle_counter += 3
    elif opcode == '0xec':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithX0xEC(systemCPU, addr)
        systemCPU.cycle_counter += 4
    elif opcode == '0x81':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 6
    elif opcode == '0x84':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0x85':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0x86':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0x8c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0x8d': # STA abs (para controle)
        global controler_read_state
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        
        obj = StoreInA0x8D(register='A', address=addr, system=systemCPU)
        obj.execute()
        del obj
        systemCPU.cycle_counter += 4
    elif opcode == '0x8e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0x91':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 6
    elif opcode == '0x94':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0x95':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0x96':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0x99':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x99(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 5
    elif opcode == '0x9d':
        # if systemCPU.program_counter == 0x106:
        #     import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)
        systemCPU.cycle_counter += 5
    elif opcode == '0xa0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xa1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 6
    elif opcode == '0xa2':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xa4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0xa5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0xa6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 3
    elif opcode == '0xa9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)
        systemCPU.cycle_counter += 2
    elif opcode == '0xac':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0xad': # LDA abs
        # global player1_key_index
        # global player2_key_index
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)            

        # if addr == 16406:
        #     systemCPU.A = get_key(all_keys, player1_key_index, 1)
        #     if player1_key_index != 7:
        #         player1_key_index += 1
        #     else:
        #         player1_key_index = 0
        # elif (addr == 16407):
        #     systemCPU.A = get_key(all_keys, player2_key_index, 2)
        #     if player2_key_index != 7:
        #         player2_key_index += 1
        #     else:
        #         player2_key_index = 0
        LoadInA0xAD(register='A', position=addr, system=systemCPU)
        
        if addr == 0x2002:
            systemCPU.setFLAG('N',1)

        systemCPU.cycle_counter += 4
    elif opcode == '0xae':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0xb1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 5
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xb4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0xb5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0xb6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
    elif opcode == '0xb9':
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
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xbc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xbd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)

        # if addr == 0x8004:
        #     import pdb;pdb.set_trace()

        LoadInA0xBD(register='A', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getX()):
            systemCPU.cycle_counter += 1
    elif opcode == '0xbe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)
        systemCPU.cycle_counter += 4
        if page_diff(addr, addr - systemCPU.getY()):
            systemCPU.cycle_counter += 1
    elif opcode == '0x8a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TXA_0x8A(first_register='X', second_register='A', system=systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x98':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TYA_0x98(first_register='Y', second_register='A', system=systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xaa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAX_0xAA(first_register='A', second_register='X', system=systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0xa8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAY_0xA8(first_register='A', second_register='Y', system=systemCPU)
        systemCPU.cycle_counter += 2
    elif opcode == '0x9a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_X_to_SP_Op_0x9A(system=systemCPU).execute()
        systemCPU.cycle_counter += 2
    elif opcode == '0xba':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_SP_to_X_Op_0xBA(system=systemCPU).execute()
        systemCPU.cycle_counter += 2
    elif opcode == '0x':
        systemCPU.program_counter = systemCPU.program_counter + 1
    else:
        print(opcode)
        print ("Erro")
        pass

run_count = 0

while True:

    opcode = hex(nesROM.pgr_rom[systemCPU.program_counter])
    # print(hex(systemCPU.program_counter+0x8000), opcode)
    operand_low = nesROM.pgr_rom[systemCPU.program_counter + 1]
    operand_high = nesROM.pgr_rom[systemCPU.program_counter + 2]
    addr = get_absolute_addr(operand_low, operand_high)

    # if addr == 0x2007 and systemCPU.address2006 == 0x20ba:
    #     import pdb;pdb.set_trace()

    if (addr == 0x2000):
        if (opcode in ['0x8d', '0x9d', '0x99']):
            value = systemCPU.A
        elif opcode == '0x8e':
            value = systemCPU.X
        elif opcode == '0x8c':
            value = systemCPU.Y
        local_ppu.update_ppu_control(value)
    execute(opcode, systemCPU, nesROM.pgr_rom)
        
    run_count += 1

    if run_count == 30:
        if systemCPU.active_nmi and not (systemCPU.on_nmi):
            
            systemCPU.on_nmi = True
            systemCPU.program_counter = ((systemCPU.rom.prg_rom[systemCPU.rom.interrupt_handlers['NMI_HANDLER'] + 1 - systemCPU.PC_OFFSET] << 8) + \
                                      systemCPU.rom.prg_rom[systemCPU.rom.interrupt_handlers['NMI_HANDLER'] - systemCPU.PC_OFFSET]) - \
                                      systemCPU.PC_OFFSET
            local_ppu.evaluate_sprite()
            local_ppu.all_sprites_list = pygame.sprite.Group()
            local_ppu.corno_func()
            local_ppu.update_corno_dois(systemCPU.batatinha[0x2000:0x23c0])
            local_ppu.update_bg()
            local_ppu.update_mem_SPR_RAM(systemCPU.mem[0x200:0x300])
            
            for i in range (64):
                if (local_ppu.flag_enable_render):
                    pos = local_ppu.posSprite[i]
                    spritesToPrint = local_ppu.spriteWithHexColor[i]
                    array_flags_to_print = local_ppu.array_flag[i]
                    local_ppu.build_sprite(spritesToPrint, pos, array_flags_to_print)
            local_ppu.render()
            
        run_count = 0
        systemCPU.cycle_counter = 0

