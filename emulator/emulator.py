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

systemCPU = system.System()
filename = './emulator/bin/transfer_registers'
nesROM = Rom(file)

pgr_bytes = nesROM.prg_rom

# DAQUI PRA CA EU ACHO Q TA ERRADO
i = 0

while i < len(pgr_bytes):
    opcode = hex(pgr_bytes[i])
    addr = None

    if opcode == '0x0':
        i = i + 1
        continue
    elif opcode == '0x06':
        i = i + 1
    elif opcode == '0x0a':
        pass
    elif opcode == '0x0e':
        pass
        i = i + 2
    elif opcode == '0x16':
        pass
        i = i + 2
    elif opcode == '0x1e':
        pass
        i = i + 2
    elif opcode == '0x26':
        pass
        i = i + 1
    elif opcode == '0x2a':
        pass
    elif opcode == '0x2e':
        pass
        i = i + 2
    elif opcode == '0x36':
        pass
        i = i + 1
    elif opcode == '0x3e':
        pass
        i = i + 2
    elif opcode == '0x46':
        pass
        i = i + 1
    elif opcode == '0x4a':
        pass
    elif opcode == '0x4e':
        pass
        i = i + 1
    elif opcode == '0x56':
        pass
        i = i + 2
    elif opcode == '0x5e':
        pass
        i = i + 2
    elif opcode == '0x61':
        pass
        # AddWithCarry0x61(systemCPU)
        i = i + 2
    elif opcode == '0x65':
        # AddWithCarry0x65(systemCPU)
        pass
        i = i + 1
    elif opcode == '0x66':
        pass
        i = i + 1
    elif opcode == '0x69':
        AddWithCarry0x69(systemCPU, pgr_bytes[i + 1])
        print ("| a = ", systemCPU.getA(), " | x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ",  " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        i = i + 1
    elif opcode == '0x6a':
        pass
    elif opcode == '0x6d':
        pass
        # AddWithCarry0x6D(systemCPU, )
        i = i + 1
    elif opcode == '0x6e':
        pass
        i = i + 1
    elif opcode == '0x71':
        pass
        # AddWithCarry0x71(systemCPU)
        #### ATENCAO AO INDEX
        i = i + 2
    elif opcode == '0x75':
        pass
        # AddWithCarry0x75(systemCPU)
        i = i + 2
    elif opcode == '0x76':
        pass
        i = i + 2
    elif opcode == '0x79':
        pass
        # AddWithCarry0x79(systemCPU)
        i = i + 2
    elif opcode == '0x7d':
        pass
        # AddWithCarry0x7D(systemCPU)
        i = i + 2
    elif opcode == '0x7e':
        pass
        i = i + 2
    elif opcode == '0x88':
        pass
    elif opcode == '0xc6':
        pass
        i = i + 1
    elif opcode == '0xc8':
        pass

    elif opcode == '0xca':
        pass
    elif opcode == '0xce':
        pass
        i = i + 1
    elif opcode == '0xd6':
        pass
        i = i + 2
    elif opcode == '0xde':
        pass
        i = i + 2
    elif opcode == '0xe1':
        pass
        i = i + 2
    elif opcode == '0xe5':
        pass
        i = i + 1
    elif opcode == '0xe6':
        pass
        i = i + 1
    elif opcode == '0xe8':
        pass
    elif opcode == '0xe9':
        pass
        i = i + 1
    elif opcode == '0xed':
        pass
        i = i + 1
    elif opcode == '0xee':
        pass
        i = i + 1
    elif opcode == '0xf1':
        pass
        i = i + 2
    elif opcode == '0xf5':
        pass
        i = i + 2
    elif opcode == '0xf6':
        pass
        i = i + 2
    elif opcode == '0xf9':
        pass
        i = i + 2
    elif opcode == '0xfd':
        pass
        i = i + 2
    elif opcode == '0xfe':
        pass
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
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x84':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x85':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x86':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x8c':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x8d':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInA0x8D(register='A', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x8e':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x91':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x94':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x95':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x96':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0x99':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x99(register='A', address=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0x9d':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)
        i = i + 2

    # LOADS
    elif opcode == '0xa0':
        operand = pgr_bytes[i + 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xa1':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa2':
        operand = pgr_bytes[i + 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xa4':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa5':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa6':
        operand = pgr_bytes[i + 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xa9':
        operand = pgr_bytes[i + 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)
        i = i + 1
    elif opcode == '0xac':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xad':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadInA0xAD(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xae':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xb1':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb4':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb5':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb6':
        operand = pgr_bytes[i + 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)
        i = i + 1
    elif opcode == '0xb9':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromA0xB9(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbc':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbd':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadInA0xBD(register='A', position=addr, system=systemCPU)
        i = i + 2
    elif opcode == '0xbe':
        operand_low = pgr_bytes[i + 1]
        operand_high = pgr_bytes[i + 2]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)
        i = i + 2

    # TRANSFERS BETWEEN REGISTERS
    elif opcode == '0x8a':
        Transfer_TXA_0x8A(first_register='X', second_register='A', system=systemCPU)
    elif opcode == '0x98':
        Transfer_TYA_0x98(first_register='Y', second_register='A', system=systemCPU)
    elif opcode == '0xaa':
        Transfer_TAX_0xAA(first_register='A', second_register='X', system=systemCPU)
    elif opcode == '0xa8':
        Transfer_TAY_0xA8(first_register='A', second_register='Y', system=systemCPU)

    # TRANSFERS TO THE STACK POINTER
    elif opcode == '0x9a':
        Transfer_X_to_SP_Op_0x9A(system=systemCPU).execute()
    elif opcode == '0xba':
        Transfer_SP_to_X_Op_0xBA(system=systemCPU).execute()
    elif opcode == '0x':
        pass


    else:
        pass


    i = i + 1

    if addr is None:
       print ("|a = ",systemCPU.getA(), "| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
    else:
       print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = {}|".format(hex(addr), systemCPU.loadMem(addr)))
