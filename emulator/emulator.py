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

systemCPU = system.System()
filename = './emulator/bin/load'
nesROM = Rom(filename)


pgr_bytes = nesROM.prg_rom

# DAQUI PRA CA EU ACHO Q TA ERRADO
i = 0

while i < len(pgr_bytes):
    opcode = hex(pgr_bytes[i])

    if opcode == '0x0':
        continue
    elif opcode == '0x06':
        print("ASL zpg")
        i = i + 1
    elif opcode == '0x0a':
        print("ASL A")
    elif opcode == '0x0e':
        print("ASL abs")
        i = i + 1
    elif opcode == '0x16':
        print("ASL zpg,X")
        i = i + 2
    elif opcode == '0x1e':
        print("ASL abs,X")
        i = i + 2
    elif opcode == '0x26':
        print("ROL zpg")
        i = i + 1
    elif opcode == '0x2a':
        print("ROL A")
    elif opcode == '0x2e':
        print("ROL abs")
        i = i + 1
    elif opcode == '0x36':
        print("ROL zpg,X")
        i = i + 2
    elif opcode == '0x3e':
        print("ROL abs,X")
        i = i + 2
    elif opcode == '0x46':
        print("LSR zpg")
        i = i + 1
    elif opcode == '0x4a':
        print("LSR A")
    elif opcode == '0x4e':
        print("LSR abs")
        i = i + 1
    elif opcode == '0x56':
        print("LSR zpg,X")
        i = i + 2
    elif opcode == '0x5e':
        print("LSR abs,X")
        i = i + 2
    elif opcode == '0x61':
        print("ADC X,ind")
        # AddWithCarry0x61(systemCPU)
        i = i + 2
    elif opcode == '0x65':
        # AddWithCarry0x65(systemCPU)
        print("ADC zpg")
        i = i + 1
    elif opcode == '0x66':
        print("ROR zpg")
        i = i + 1
    elif opcode == '0x69':
        print("ADC #")
        AddWithCarry0x69(systemCPU, pgr_bytes[i + 1])
        print ("| a = ", systemCPU.getA(), " | x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ",  " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        i = i + 1
    elif opcode == '0x6a':
        print("ROR A")
    elif opcode == '0x6d':
        print("ADC abs")
        # AddWithCarry0x6D(systemCPU, )
        i = i + 1
    elif opcode == '0x6e':
        print("ROR abs")
        i = i + 1
    elif opcode == '0x71':
        print("ADC ind,Y")
        # AddWithCarry0x71(systemCPU)
        #### ATENCAO AO INDEX
        i = i + 2
    elif opcode == '0x75':
        print("ADC zpg,X")
        # AddWithCarry0x75(systemCPU)
        i = i + 2
    elif opcode == '0x76':
        print("ROR zpg,X")
        i = i + 2
    elif opcode == '0x79':
        print("ADC abs,Y")
        # AddWithCarry0x79(systemCPU)
        i = i + 2
    elif opcode == '0x7d':
        print("ADC abs,X")
        # AddWithCarry0x7D(systemCPU)
        i = i + 2
    elif opcode == '0x7e':
        print("ROR abs,X")
        i = i + 2
    elif opcode == '0x88':
        print("DEY impl")
    elif opcode == '0xc6':
        print("DEC zpg")
        i = i + 1
    elif opcode == '0xc8':
        IncreaseReg0xC8()
        print("INY impl")
    elif opcode == '0xca':
        print("DEX impl")
    elif opcode == '0xce':
        print("DEC abs")
        i = i + 1
    elif opcode == '0xd6':
        print("DEC zpg,X")
        i = i + 2
    elif opcode == '0xde':
        print("DEC abs,X")
        i = i + 2
    elif opcode == '0xe1':
        print("SBC X,ind")
        i = i + 2
    elif opcode == '0xe5':
        print("SBC zpg")
        i = i + 1
    elif opcode == '0xe6':
        print("INC zpg")
        i = i + 1
    elif opcode == '0xe8':
        print("INX impl")
    elif opcode == '0xe9':
        print("SBC #")
        i = i + 1
    elif opcode == '0xed':
        print("SBC abs")
        i = i + 1
    elif opcode == '0xee':
        print("INC abs")
        i = i + 1
    elif opcode == '0xf1':
        print("SBC ind,Y")
        i = i + 2
    elif opcode == '0xf5':
        print("SBC zpg,X")
        i = i + 2
    elif opcode == '0xf6':
        print("INC zpg,X")
        i = i + 2
    elif opcode == '0xf9':
        print("SBC abs,Y")
        i = i + 2
    elif opcode == '0xfd':
        print("SBC abs,X")
        i = i + 2
    elif opcode == '0xfe':
        print("INC abs,X")
        i = i + 2
        #print(opcode)
        #print("Instrução invalida!")
    # FUSCA \/

    # HEITOR \/
    # elif opcode == '0x01':
    #     compare.OrWithAcumulator0x01(systemCPU, )
    #     print('ORA X, ind')
    # elif opcode == '0x05':
    #     compare.OrWithAcumulator0x05()
    #     print('ORA zpg')
    # elif opcode == '0x09':
    #     compare.OrWithAcumulator0x09(systemCPU, 10)
    #     print('ORA #')
    # elif opcode == '0x0d':
    #     compare.OrWithAcumulator0x0D()
    #     print('ORA abs')
    # elif opcode == '0x11':
    #     compare.OrWithAcumulator0x11()
    #     print('ORA ind, Y')
    # elif opcode == '0x15':
    #     compare.OrWithAcumulator0x15()
    #     print('ORA zpg, X')
    # elif opcode == '0x19':
    #     compare.OrWithAcumulator0x19()
    #     print('ORA abs, Y')
    # elif opcode == '0x1d':
    #     compare.OrWithAcumulator0x1D()
    #     print('ORA abs, X')
    # elif opcode == '0x21':
    #     compare.AndWithAcumulator0x21()
    #     print('AND X, ind')
    # elif opcode == '0x25':
    #     compare.AndWithAcumulator0x25()
    #     print('AND zpg')
    # elif opcode == '0x29':
    #     compare.AndWithAcumulator0x29()
    #     print('AND #')
    # elif opcode == '0x2d':
    #     compare.AndWithAcumulator0x2D()
    #     print('AND abs')
    # elif opcode == '0x31':
    #     compare.AndWithAcumulator0x31()
    #     print('AND ind, Y')
    # elif opcode == '0x35':
    #     compare.AndWithAcumulator0x35()
    #     print('AND zpg, X')
    # elif opcode == '0x39':
    #     compare.AndWithAcumulator0x39()
    #     print('AND abs, Y')
    # elif opcode == '0x3d':
    #     compare.AndWithAcumulator0x3D()
    #     print('AND abs, X')
    # elif opcode == '0x41':
    #     compare.ExclusiveOrWithAcumulator0x41()
    #     print('EOR ind, Y')
    # elif opcode == '0x45':
    #     compare.ExclusiveOrWithAcumulator0x45()
    #     print('EOR zpg')
    # elif opcode == '0x49':
    #     compare.ExclusiveOrWithAcumulator0x49()
    #     print('EOR #')
    # elif opcode == '0x4d':
    #     compare.ExclusiveOrWithAcumulator0x4D()
    #     print('EOR abs')
    # elif opcode == '0x51':
    #     compare.ExclusiveOrWithAcumulator0x51()
    #     print('EOR ind, Y')
    # elif opcode == '0x55':
    #     compare.ExclusiveOrWithAcumulator0x55()
    #     print('EOR zpg, X')
    # elif opcode == '0x59':
    #     compare.ExclusiveOrWithAcumulator0x59()
    #     print('EOR abs, Y')
    # elif opcode == '0x5d':
    #     compare.ExclusiveOrWithAcumulator0x5D()
    #     print('EOR abs, X')
    # elif opcode == '0xc0':
    #     compare.CompareWithY0xC0()
    #     print('CPY #')
    # elif opcode == '0xc1':
    #     compare.CompareWithAcumulator0xC1()
    #     print('CMP X, ind')
    # elif opcode == '0xc4':
    #     compare.CompareWithY0xC4()
    #     print('CPY zpg')
    # elif opcode == '0xc5':
    #     compare.CompareWithAcumulator0xC5()
    #     print('CMP zpg')
    # elif opcode == '0xc9':
    #     compare.CompareWithAcumulator0xC9()
    #     print('CMP #')
    # elif opcode == '0xcc':
    #     compare.CompareWithY0xCC()
    #     print('CPY abs')
    # elif opcode == '0xcd':
    #     compare.CompareWithAcumulator0xCD()
    #     print('CMP abs')
    # elif opcode == '0xd1':
    #     compare.CompareWithAcumulator0xD1()
    #     print('CMP ind, Y')
    # elif opcode == '0xd5':
    #     compare.CompareWithAcumulator0xD5()
    #     print('CMP zpg, X')
    # elif opcode == '0xd9':
    #     compare.CompareWithAcumulator0xD9()
    #     print('CMP abs, Y')
    # elif opcode == '0xdd':
    #     compare.CompareWithAcumulator0xDD()
    #     print('CMP abs, X')
    # elif opcode == '0xe0':
    #     compare.CompareWithX0xE0()
    #     print('CPX #')
    # elif opcode == '0xe4':
    #     compare.CompareWithX0xE4()
    #     print('CPX zpg')
    # elif opcode == '0xec':
    #     compare.CompareWithX0xEC()
    #     print('CPX abs')



    # CARTS \/
    # STORES
    elif opcode == '0x81':
        print("STA (Indirect, X)")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x84':
        print("STY Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x85':
        print("STA Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x86':
        print("STX Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x8c':
        print("STY Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x8d':
        print("STA Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInA0x8D(register='A', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x8e':
        print("STX Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x91':
        print("STA (Indirect), Y")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x94':
        print("STY Zero Page, X")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x95':
        print("STA Zero Page, X")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x96':
        print("STX Zero Page, Y")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x99':
        print("STA Absolute, Y")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x99(register='A', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x9d':
        print("STA Absolute, X")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)
        i = i + 2

    # LOADS
    elif opcode == '0xa0':
        print("LDY #Immediate")
        operand = pgr_bytes[i + 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xa1':
        print("LDA (Indirect, X)")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa2':
        print("LDX #Immediate")
        operand = pgr_bytes[i + 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xa4':
        print("LDY Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa5':
        print("LDA Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa6':
        print("LDX Zero Page")
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa9':
        print("LDA #Immediate")
        operand = pgr_bytes[i + 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xac':
        print("LDY Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xad':
        print("LDA Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadInA0xAD(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xae':
        print("LDX Absolute")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xb1':
        print("LDA (Indirect), Y")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb4':
        print("LDY Zero Page, X")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb5':
        print("LDA Zero Page, X")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb6':
        print("LDX Zero Page, Y")
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb9':
        print("LDA Absolute, Y")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromA0xB9(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbc':
        print("LDY Absolute, X")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbd':
        print("LDA Absolute, X")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadInA0xBD(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbe':
        print("LDX Absolute, Y")
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)
        i = i + 2

    # TRANSFERS BETWEEN REGISTERS
    elif opcode == '0x8a':
        print("TXA impl")
    elif opcode == '0x98':
        print("TYA impl")
    elif opcode == '0xaa':
        print("TAX impl")
    elif opcode == '0xa8':
        print("TAY impl")

    # TRANSFERS TO THE STACK POINTER
    elif opcode == '0x9a':
        print("TXS impl")
        Transfer_X_to_SP_Op_0x9A(system=systemCPU)
    elif opcode == '0xba':
        print("TSX impl")
        Transfer_SP_to_X_Op_0xBA(system=systemCPU)
    elif opcode == '0x':
        print("BRK impl")

    else:
        pass


    i = i + 1

    if (True):
       print ("|a = ",systemCPU.getA(), "| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
    else:
       print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
