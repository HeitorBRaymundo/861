import sys
from py import system
from py.operations import register_instructions
from py.operations import bit
from py.operations import flags
from py.operations import flow_control
from py.operations import interruption
from py.operations import store_load
from py.operations import transfer_sp
# from py.operations import compare
from rom import Rom
from py.operations import *
from memory_helper import *

try:
    file = sys.argv[1]
except:
    pass

nesROM = Rom(file)
systemCPU = system.System(nesROM)

pgr_bytes = nesROM.prg_rom

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
        ASL_zero_page_0x16(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x1e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_absolute_0x1E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x26':
        print("ROL zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_0x26(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x2a':
        print("ROL A")
        ROL_A_0x2A(systemCPU)
    elif opcode == '0x2e':
        print("ROL abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_absolute_0x2E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x36':
        print("ROL zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_index_0x36(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x3e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_abs_X_0x03E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x46':
        print("LSR zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_0x46(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x4a':
        print("LSR A")
        LSR_A_0x4A(systemCPU)
    elif opcode == '0x4e':
        print("LSR abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_absolute_0x4E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x56':
        print("LSR zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_index_0x56(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x5e':
        print("LSR abs,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_abs_X_0x05E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x61':
        print("ADC X,indirect")
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x61(systemCPU, addr)

    elif opcode == '0x65':
        print("ADC zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x65(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x66':
        print("ROR zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_0x66(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x69':
        print("ADC #")
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x69(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x6a':
        print("ROR A")
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROR_A_0x6A(systemCPU)

    elif opcode == '0x6d':
        print("ADC abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x6D(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x6e':
        print("ROR abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_absolute_0x6E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x71':
        print("ADC ind,Y")
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x71(systemCPU, addr)

    elif opcode == '0x75':
        print("ADC zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x75(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x76':
        print("ROR zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_index_0x76(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x79':
        print("ADC abs,Y")
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x79(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x7d':
        print("ADC abs,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        AddWithCarry0x7D(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x7e':
        print("ROR abs,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_abs_X_0x7E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0x88':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0x88(systemCPU)
        print("DEY impl")
    elif opcode == '0xc6':
        print("DEC zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        DEC_zero_page_0xC6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0xc8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xC8(systemCPU)
        print("INY impl")
    elif opcode == '0xca':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0xCA(systemCPU)
        print("DEX impl")
    elif opcode == '0xce':
        print("DEC abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        DEC_absolute_0xCE(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0xd6':
        print("DEC zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 2
        DEC_zero_page_X_0xD6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0xde':
        print("DEC abs,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        DEC_absolute_X_0xDE(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0xe1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xE1(systemCPU, addr)
        print("SBC X,ind")

    elif opcode == '0xe5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE5(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        print("SBC zpg")

    elif opcode == '0xe6':
        print("INC zpg")
        systemCPU.program_counter = systemCPU.program_counter + 2
        INC_zero_page_0xE6(systemCPU, pgr_bytes[systemCPU.program_counter - 1])

    elif opcode == '0xe8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xE8(systemCPU)
        print("INX impl")
    elif opcode == '0xe9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE9(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        print("SBC #")

    elif opcode == '0xed':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xED(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
        print("SBC abs")

    elif opcode == '0xee':
        print("INC abs")
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_absolute_0xEE(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])

    elif opcode == '0xf1':
        print("SBC ind,Y")
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF1(systemCPU, addr)

    elif opcode == '0xf5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xF5(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        print("SBC zpg,X")

    elif opcode == '0xf6':
        print("INC zpg,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_zero_page_X_0xF6(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])

    elif opcode == '0xf9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xF9(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
        print("SBC abs,Y")

    elif opcode == '0xfd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        SubWithCarry0xFD(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
        print("SBC abs,X")

    elif opcode == '0xfe':
        print("INC abs,X")
        systemCPU.program_counter = systemCPU.program_counter + 3
        INC_absolute_X_0xFE(systemCPU, pgr_bytes[systemCPU.program_counter - 1], pgr_bytes[systemCPU.program_counter - 2])
     #print(opcode)
        #print("Instrução invalida!")

    # FUSCA \/
    elif opcode == '0x8': # Flags / stack
        # print("PHP impl")
        PHP0x08(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x18':
        # print("CLC impl")
        CLC0x18(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x28':
        # print("PLP impl")
        PLP0x28(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x38':
        # print("SEC impl")
        SEC0x38(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x48':
        # print("PHA impl")
        PHA0x48(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x68':
        # print("PLA impl")
        PLA0x68(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0xb8':
        # print("CLV impl")
        CLV0xB8(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0xd8':
        # print("CLD impl")
        CLD0xD8(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0xf8':
        # print("SED impl")
        SED0xF8(systemCPU)
        systemCPU.program_counter = systemCPU.program_counter + 1
        # i = i + 1
    elif opcode == '0x24': # Bit test HELP
        # print("BIT zpg")
        address = get_zero_page_addr(pgr_bytes[i + 1])
        BIT_zpg0x24(systemCPU, address)
        i = i + 1
    elif opcode == '0x2c':
        # print("BIT abs")
        address = get_absolute_addr(pgr_bytes[i + 1], pgr_bytes[i + 2])
        BIT_abs0x2C(systemCPU, address)
        i = i + 2
    elif opcode == '0x40': # interrupt

        RTI0x40(systemCPU)
        # i = i + 1
    elif opcode == '0x58':

        CLI0x58(systemCPU)
        # i = i + 1
    elif opcode == '0xea': # NOP
        systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x0': # Flow control HELP
        # BRK0x00(systemCPU)
        # i = i + 1
        systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x10':

        BPL0x10(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x20':

        JSR0x20(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x30':

        BMI0x30(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x4c':

        JMP_abs0x4C(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x50':

        BVC0x50(systemCPU)
        # i = i + 1
    elif opcode == '0x60':

        RTS0x60(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x6C':

        JMP_ind0x6C(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x70':

        BVS0x70(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0x78':

        SEI0x78(systemCPU)
        # i = i + 1
    elif opcode == '0x90':

        BCC0x90(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0xb0':

        BCS0xB0(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0xd0':

        BNE0xD0(systemCPU, pgr_bytes[i + 1])
        i = i + 1
    elif opcode == '0xf0':
        # print("BEQ rel")
        # print(hex(pgr_bytes[i + 1]))
        # print(hex(pgr_bytes[i + 2]))
        BEQ0xF0(systemCPU, pgr_bytes[i + 1])
        i = i + 1


    # HEITOR \/
    elif opcode == '0x1':
      print('ORA X, ind')
      OrWithAcumulator0x01(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x5':
      print('ORA zpg')
      OrWithAcumulator0x05(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x9':
      print('ORA #')
      OrWithAcumulator0x09(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xd':
      print('ORA abs')
      OrWithAcumulator0x0D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x11':
      print('ORA ind, Y')
      OrWithAcumulator0x11(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x15':
      print('ORA zpg, X')
      OrWithAcumulator0x15(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x19':
      print('ORA abs, Y')
      OrWithAcumulator0x19(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x1d':
      print('ORA abs, X')
      OrWithAcumulator0x1D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x21':
      print('AND X, ind')
      AndWithAcumulator0x21(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x25':
      print('AND zpg')
      AndWithAcumulator0x25(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x29':
      print('AND #')
      AndWithAcumulator0x29(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x2d':
      print('AND abs')
      AndWithAcumulator0x2D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x31':
      print('AND ind, Y')
      AndWithAcumulator0x31(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x35':
      print('AND zpg, X')
      AndWithAcumulator0x35(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x39':
      print('AND abs, Y')
      AndWithAcumulator0x39(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x3d':
      print('AND abs, X')
      AndWithAcumulator0x3D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x41':
      print('EOR ind, X')
      ExclusiveOrWithAcumulator0x41(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x45':
      print('EOR zpg')
      ExclusiveOrWithAcumulator0x45(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x49':
      print('EOR #')
      ExclusiveOrWithAcumulator0x49(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x4d':
      print('EOR abs')
      ExclusiveOrWithAcumulator0x4D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x51':
      print('EOR ind, Y')
      ExclusiveOrWithAcumulator0x51(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x55':
      print('EOR zpg, X')
      ExclusiveOrWithAcumulator0x55(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0x59':
      print('EOR abs, Y')
      ExclusiveOrWithAcumulator0x59(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0x5d':
      print('EOR abs, X')
      ExclusiveOrWithAcumulator0x5D(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0xc0':
      print('CPY #')
      CompareWithY0xC0(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xc1':
      print('CMP X, ind')
      CompareWithAcumulator0xC1(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xc4':
      print('CPY zpg')
      CompareWithY0xC4(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xc5':
      print('CMP zpg')
      CompareWithAcumulator0xC5(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xc9':
      print('CMP #')
      CompareWithAcumulator0xC9(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xcc':
      print('CPY abs')
      CompareWithY0xCC(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0xcd':
      print('CMP abs')
      CompareWithAcumulator0xCD(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0xd1':
      print('CMP ind, Y')
      CompareWithAcumulator0xD1(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xd5':
      print('CMP zpg, X')
      CompareWithAcumulator0xD5(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xd9':
      print('CMP abs, Y')
      CompareWithAcumulator0xD9(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0xdd':
      print('CMP abs, X')
      CompareWithAcumulator0xDD(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2
    elif opcode == '0xe0':
      print('CPX #')
      CompareWithX0xE0(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xe4':
      print('CPX zpg')
      CompareWithX0xE4(systemCPU, pgr_bytes[systemCPU.program_counter + 1])
      systemCPU.program_counter = systemCPU.program_counter + 1
    elif opcode == '0xec':
      print('CPX abs')
      CompareWithX0xEC(systemCPU, pgr_bytes[systemCPU.program_counter + 1], pgr_bytes[systemCPU.program_counter + 2])
      systemCPU.program_counter = systemCPU.program_counter + 2



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
        pass

    if addr is None:
       print ("|pc = ", hex(systemCPU.program_counter + 0x8000),"|a = ",systemCPU.getA(), "| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
    else:
       print ("|pc = ", hex(systemCPU.program_counter + 0x8000),"|a = ",systemCPU.getA(),"| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = {}|".format(hex(addr), systemCPU.loadMem(addr)))
