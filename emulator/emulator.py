import sys
from py import system
from py.operations import *
from rom import Rom
from memory_helper import *

try:
    file = sys.argv[1]
except:
    pass

nesROM = Rom(file)
systemCPU = system.System(nesROM)

pgr_bytes = nesROM.prg_rom

# import pdb; pdb.set_trace()

while systemCPU.program_counter < len(pgr_bytes) - 6:
    opcode = hex(pgr_bytes[systemCPU.program_counter])
    addr = None

    if opcode == '0x0':
        systemCPU.program_counter = systemCPU.program_counter + 1
        continue
    elif opcode == '0x6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ASL_zero_page_0x06(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ASL_A_0x0A(systemCPU)
    elif opcode == '0xe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_absolute_0x0E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x16':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ASL_zero_page_index_0x16(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x1e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_abs_X_0x01E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x26':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_0x26(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x2a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROL_A_0x2A(systemCPU)
    elif opcode == '0x2e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_absolute_0x2E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x36':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_index_0x36(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x3e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_abs_X_0x3E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x46':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_0x46(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x4a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        LSR_A_0x4A(systemCPU)
    elif opcode == '0x4e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_absolute_0x4E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x56':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_index_0x56(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x5e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_abs_X_0x05E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x61':
        systemCPU.program_counter = systemCPU.program_counter + 2
        address = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x61(systemCPU, address)
    elif opcode == '0x65':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x65(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x66':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_0x66(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x69':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x69(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x6a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROR_A_0x6A(systemCPU)
    elif opcode == '0x6d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x6D(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x6e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_absolute_0x6E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x71':
        systemCPU.program_counter = systemCPU.program_counter + 2
        address = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x71(systemCPU, address)
    elif opcode == '0x75':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x75(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x76':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_index_0x76(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x79':
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x79(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x7d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x7D(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x7e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_abs_X_0x7E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0x88':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0x88(systemCPU)
    elif opcode == '0xc6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        DEC_zero_page_0xC6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xc8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xC8(systemCPU)
    elif opcode == '0xca':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0xCA(systemCPU)
    elif opcode == '0xce':
        systemCPU.program_counter = systemCPU.program_counter + 3
        DEC_absolute_0xCE(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xd6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        DEC_zero_page_X_0xD6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xde':
        systemCPU.program_counter = systemCPU.program_counter + 3
        DEC_absolute_X_0xDE(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xe1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        address = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xE1(systemCPU, address)
    elif opcode == '0xe5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE5(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xe6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        INC_zero_page_0xE6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xe8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xE8(systemCPU)
    elif opcode == '0xe9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE9(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xed':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xED(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    elif opcode == '0xee':
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_absolute_0xEE(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    elif opcode == '0xf1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        address = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF1(systemCPU, address)
    elif opcode == '0xf5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xF5(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
    elif opcode == '0xf6':
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_zero_page_X_0xF6(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    elif opcode == '0xf9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xF9(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    elif opcode == '0xfd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xFD(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    elif opcode == '0xfe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_absolute_X_0xFE(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
    # FUSCA \/
    elif opcode == '0x8': # Flags / stack
        systemCPU.program_counter = systemCPU.program_counter + 1
        PHP0x08(systemCPU)
        # i = i + 0
    elif opcode == '0x18':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLC0x18(systemCPU)
        # i = i + 0
    elif opcode == '0x28':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLP0x28(systemCPU)
        # i = i + 0
    elif opcode == '0x38':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEC0x38(systemCPU)
        # i = i + 0
    elif opcode == '0x48':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PHA0x48(systemCPU)
        # i = i + 0
    elif opcode == '0x68':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLA0x68(systemCPU)
        # i = i + 0
    elif opcode == '0xb8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLV0xB8(systemCPU)
        # i = i + 0
    elif opcode == '0xd8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLD0xD8(systemCPU)
        # i = i + 0
    elif opcode == '0xf8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        SED0xF8(systemCPU)
        # i = i + 0
    elif opcode == '0x24': # Bit test HELP

        systemCPU.program_counter = systemCPU.program_counter + 2
        address = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        BIT_zpg0x24(systemCPU, address)
        # i = i + 1
    elif opcode == '0x2c':

        systemCPU.program_counter = systemCPU.program_counter + 3
        address = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        BIT_abs0x2C(systemCPU, address)
        # i = i + 2
    elif opcode == '0x40': # interrupt
        systemCPU.program_counter = systemCPU.program_counter + 1
        RTI0x40(systemCPU)
        # i = i + 0
    elif opcode == '0x58':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLI0x58(systemCPU)
        # i = i + 0
    elif opcode == '0xea': # NOP
        systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x0': # Flow control HELP
        # BRK0x00(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x10':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BPL0x10(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0x20':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.stack_push(systemCPU.program_counter)
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        # i = i + 1
    elif opcode == '0x30':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BMI0x30(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0x4c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
    elif opcode == '0x50':
        systemCPU.program_counter = systemCPU.program_counter + 1
        BVC0x50(systemCPU)
        # i = i + 0
    elif opcode == '0x60':
        systemCPU.program_counter = systemCPU.stack_pop()
    elif opcode == '0x6c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000

    elif opcode == '0x70':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVS0x70(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0x78':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEI0x78(systemCPU)
        # i = i + 0
    elif opcode == '0x90':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCC0x90(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0xb0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCS0xB0(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0xd0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BNE0xD0(systemCPU, setPCToAddress)
        # i = i + 1
    elif opcode == '0xf0':



        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BEQ0xF0(systemCPU, setPCToAddress)
        # i = i + 1

    # HEITOR \/
    elif opcode == '0x1':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_indirect_addr_x(systemCPU, operand, offset)
      OrWithAcumulator0x01(systemCPU, address)
    elif opcode == '0x5':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      OrWithAcumulator0x05(systemCPU, address)
    elif opcode == '0x9':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      OrWithAcumulator0x09(systemCPU, operand)
    elif opcode == '0xd':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      OrWithAcumulator0x0D(systemCPU, address)
    elif opcode == '0x11':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
      OrWithAcumulator0x11(systemCPU, address)
    elif opcode == '0x15':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_zero_page_addr(operand, offset)
      OrWithAcumulator0x15(systemCPU, address)
    elif opcode == '0x19':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.Y
      address = get_absolute_addr(operand_low, operand_high, offset)
      OrWithAcumulator0x19(systemCPU, address)
    elif opcode == '0x1d':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_absolute_addr(operand_low, operand_high, offset)
      OrWithAcumulator0x1D(systemCPU, address)
    elif opcode == '0x21':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
      AndWithAcumulator0x21(systemCPU, address)
    elif opcode == '0x25':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      AndWithAcumulator0x25(systemCPU, address)
    elif opcode == '0x29':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      AndWithAcumulator0x29(systemCPU, operand)
    elif opcode == '0x2d':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      AndWithAcumulator0x2D(systemCPU, address)
    elif opcode == '0x31':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
      AndWithAcumulator0x31(systemCPU, address)
    elif opcode == '0x35':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_zero_page_addr(operand, offset)
      AndWithAcumulator0x35(systemCPU, address)
    elif opcode == '0x39':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.Y
      address = get_absolute_addr(operand_low, operand_high, offset)
      AndWithAcumulator0x39(systemCPU, address)
    elif opcode == '0x3d':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_absolute_addr(operand_low, operand_high, offset)
      AndWithAcumulator0x3D(systemCPU, address)
    elif opcode == '0x41':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
      ExclusiveOrWithAcumulator0x41(systemCPU, address)
    elif opcode == '0x45':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      ExclusiveOrWithAcumulator0x45(systemCPU, address)
    elif opcode == '0x49':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      ExclusiveOrWithAcumulator0x49(systemCPU, operand)
    elif opcode == '0x4d':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      ExclusiveOrWithAcumulator0x4D(systemCPU, address)
    elif opcode == '0x51':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
      ExclusiveOrWithAcumulator0x51(systemCPU, address)
    elif opcode == '0x55':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_zero_page_addr(operand, offset)
      ExclusiveOrWithAcumulator0x55(systemCPU, address)
    elif opcode == '0x59':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.Y
      address = get_absolute_addr(operand_low, operand_high, offset)
      ExclusiveOrWithAcumulator0x59(systemCPU, address)
    elif opcode == '0x5d':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_absolute_addr(operand_low, operand_high, offset)
      ExclusiveOrWithAcumulator0x5D(systemCPU, address)
    elif opcode == '0xc0':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      CompareWithY0xC0(systemCPU, operand)
    elif opcode == '0xc1':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
      CompareWithAcumulator0xC1(systemCPU, address)
    elif opcode == '0xc4':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      CompareWithY0xC4(systemCPU, address)
    elif opcode == '0xc5':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      CompareWithAcumulator0xC5(systemCPU, address)
    elif opcode == '0xc9':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      CompareWithAcumulator0xC9(systemCPU, operand)
    elif opcode == '0xcc':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      CompareWithY0xCC(systemCPU, address)
    elif opcode == '0xcd':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      CompareWithAcumulator0xCD(systemCPU, address)
    elif opcode == '0xd1':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
      CompareWithAcumulator0xD1(systemCPU, address)
    elif opcode == '0xd5':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_zero_page_addr(operand, offset)
      CompareWithAcumulator0xD5(systemCPU, address)
    elif opcode == '0xd9':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.Y
      address = get_absolute_addr(operand_low, operand_high, offset)
      CompareWithAcumulator0xD9(systemCPU, address)
    elif opcode == '0xdd':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      offset = systemCPU.X
      address = get_absolute_addr(operand_low, operand_high, offset)
      CompareWithAcumulator0xDD(systemCPU, address)
    elif opcode == '0xe0':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      CompareWithX0xE0(systemCPU, operand)
    elif opcode == '0xe4':
      systemCPU.program_counter = systemCPU.program_counter + 2
      operand = pgr_bytes[systemCPU.program_counter - 1]
      address = get_zero_page_addr(operand)
      CompareWithX0xE4(systemCPU, address)
    elif opcode == '0xec':
      systemCPU.program_counter = systemCPU.program_counter + 3
      operand_low = pgr_bytes[systemCPU.program_counter - 2]
      operand_high = pgr_bytes[systemCPU.program_counter - 1]
      address = get_absolute_addr(operand_low, operand_high)
      CompareWithX0xEC(systemCPU, address)

    # CARTS \/
    # STORES
    elif opcode == '0x81':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)

    elif opcode == '0x84':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)

    elif opcode == '0x85':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)

    elif opcode == '0x86':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)

    elif opcode == '0x8c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)

    elif opcode == '0x8d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInA0x8D(register='A', address=addr, system=systemCPU)

    elif opcode == '0x8e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)

    elif opcode == '0x91':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)

    elif opcode == '0x94':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)

    elif opcode == '0x95':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)

    elif opcode == '0x96':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)

    elif opcode == '0x99':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x99(register='A', address=addr, system=systemCPU)

    elif opcode == '0x9d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)


    # LOADS
    elif opcode == '0xa0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)

    elif opcode == '0xa1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)

    elif opcode == '0xa2':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)

    elif opcode == '0xa4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)

    elif opcode == '0xa5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)

    elif opcode == '0xa6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)

    elif opcode == '0xa9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)

    elif opcode == '0xac':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)

    elif opcode == '0xad':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadInA0xAD(register='A', position=addr, system=systemCPU)

    elif opcode == '0xae':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)

    elif opcode == '0xb1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)

    elif opcode == '0xb4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)

    elif opcode == '0xb5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)

    elif opcode == '0xb6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)

    elif opcode == '0xb9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromA0xB9(register='A', position=addr, system=systemCPU)

    elif opcode == '0xbc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)

    elif opcode == '0xbd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadInA0xBD(register='A', position=addr, system=systemCPU)

    elif opcode == '0xbe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)


    # TRANSFERS BETWEEN REGISTERS
    elif opcode == '0x8a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TXA_0x8A(first_register='X', second_register='A', system=systemCPU)
    elif opcode == '0x98':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TYA_0x98(first_register='Y', second_register='A', system=systemCPU)
    elif opcode == '0xaa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAX_0xAA(first_register='A', second_register='X', system=systemCPU)
    elif opcode == '0xa8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAY_0xA8(first_register='A', second_register='Y', system=systemCPU)

    # TRANSFERS TO THE STACK POINTER
    elif opcode == '0x9a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_X_to_SP_Op_0x9A(system=systemCPU).execute()
    elif opcode == '0xba':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_SP_to_X_Op_0xBA(system=systemCPU).execute()
    elif opcode == '0x':
        systemCPU.program_counter = systemCPU.program_counter + 1
    else:
        print ("Erro")
        pass

    if addr is None:
       print ("| pc = 0x%0.4X" % int(hex(systemCPU.program_counter + 0xC000), 16),\
              " | a = 0x%0.2X" % systemCPU.getA(), "| x = 0x%0.2X" %  systemCPU.getX(), \
              "| y = 0x%0.2X" %  systemCPU.getY(), "| sp = 0x%0.4X" %  int(systemCPU.getSP(), 16), \
              "| p[NV-BDIZC] = ", systemCPU.getFLAG(),"|")
    else:
       print ("| pc = 0x%0.4X" % int(hex(systemCPU.program_counter + 0xC000), 16),\
              " | a = 0x%0.2X" % systemCPU.getA(), \
              "| x = 0x%0.2X" %  systemCPU.getX(), \
              "| y = 0x%0.2X" %  systemCPU.getY(), \
              "| sp = 0x%0.4X" %  int(systemCPU.getSP(), 16), \
              "| p[NV-BDIZC] = ", systemCPU.getFLAG(),\
              "| MEM[0x%0.4X]" % addr, " = 0x%0.2X" % systemCPU.loadMem(addr),"|")
