from py import system
from py.operations import register_instructions
from py.operations import bit
from py.operations import flags
from py.operations import flow_control
from py.operations import interruption
# from py.operations import compare

from py.operations import *

systemCPU = system.System()

def printSystemStatus():
    return


# Read file
with open('./emulator/bin/compares', 'rb') as file:

    rom_bytes = file.read()

    # set the header size
    header_size = 16
    # get the binary header
    header_bytes = rom_bytes[0:16]

    # ve se o mirror ta setado
    # '{:08b}'.format(header_bytes[6])[4]

    # get the number of pgr_counters
    pgr_counter =  int.from_bytes(header_bytes[4:5], byteorder='big')
    pgr_bytes = rom_bytes[header_size:header_size+(16* pgr_counter*1024)]

    # import pdb; pdb.set_trace()

    i = 0

    while i < len(pgr_bytes):
        opcode = hex(pgr_bytes[i])

        if opcode != '0x0':
            print(opcode)

        if opcode == '0x0':
            continue
        elif opcode == '0xa0':
            print("LDY abs")
            i = i + 1
        elif opcode == '0xb9':
            print("LDA abs,y")
            i = i + 2
        elif opcode == '0xbe':
            print("LDX abs, y")
            i = i + 2
        elif opcode == '0x6':
            print("ASL zpg")
            ASL_zero_page_0x06(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xa':
            print("ASL A")
            ASL_A_0x0A(systemCPU)
        elif opcode == '0xe':
            print("ASL abs")
            ASL_absolute_0x0E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x16':
            print("ASL zpg,X")
            ASL_zero_page_0x16(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x1e':
            print("ASL abs,X")
            ASL_absolute_0x1E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x26':
            print("ROL zpg")
            ROL_zero_page_0x26(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x2a':
            print("ROL A")
            ROL_A_0x2A(systemCPU)
        elif opcode == '0x2e':
            print("ROL abs")
            ROL_absolute_0x2E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x36':
            print("ROL zpg,X")
            ROL_zero_page_index_0x36(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x3e':
            print("ROL abs,X")
            ROL_abs_X_0x03E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x46':
            print("LSR zpg")
            LSR_zero_page_0x46(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x4a':
            print("LSR A")
            LSR_A_0x4A(systemCPU)
        elif opcode == '0x4e':
            print("LSR abs")
            LSR_absolute_0x4E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x56':
            print("LSR zpg,X")
            LSR_zero_page_index_0x56(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x5e':
            print("LSR abs,X")
            LSR_abs_X_0x05E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x61':
            print("ADC X,indirect")
            AddWithCarry0x61(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x65':
            print("ADC zpg")
            AddWithCarry0x65(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x66':
            print("ROR zpg")
            ROR_zero_page_0x66(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x69':
            print("ADC #")
            AddWithCarry0x69(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x6a':
            print("ROR A")
            ROR_A_0x6A(systemCPU)
        elif opcode == '0x6d':
            print("ADC abs")
            AddWithCarry0x6D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x6e':
            print("ROR abs")
            ROR_absolute_0x6E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x71':
            print("ADC ind,Y")
            # AddWithCarry0x71(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            #### ATENCAO AO INDEX
            i = i + 2
        elif opcode == '0x75':
            print("ADC zpg,X")
            AddWithCarry0x75(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x76':
            print("ROR zpg,X")
            ROR_zero_page_index_0x76(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x79':
            print("ADC abs,Y")
            AddWithCarry0x79(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x7d':
            print("ADC abs,X")
            AddWithCarry0x7D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x7e':
            print("ROR abs,X")
            ROR_abs_X_0x7E(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x88':
            DecreaseReg0x88(systemCPU)
            print("DEY impl")
        elif opcode == '0xc6':
            print("DEC zpg")
            DEC_zero_page_0xC6(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xc8':
            IncreaseReg0xC8(systemCPU)
            print("INY impl")
        elif opcode == '0xca':
            DecreaseReg0xCA(systemCPU)
            print("DEX impl")
        elif opcode == '0xce':
            print("DEC abs")
            DEC_absolute_0xCE(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xd6':
            print("DEC zpg,X")
            DEC_zero_page_X_0xD6(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xde':
            print("DEC abs,X")
            DEC_absolute_X_0xDE(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xe1':
            # SubWithCarry0xE1(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            print("SBC X,ind")
            i = i + 2
        elif opcode == '0xe5':
            SubWithCarry0xE5(systemCPU, pgr_bytes[i + 1])
            print("SBC zpg")
            i = i + 1
        elif opcode == '0xe6':
            print("INC zpg")
            INC_zero_page_0xE6(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xe8':
            IncreaseReg0xE8(systemCPU)
            print("INX impl")
        elif opcode == '0xe9':
            SubWithCarry0xE9(systemCPU, pgr_bytes[i + 1])
            print("SBC #")
            i = i + 1
        elif opcode == '0xed':
            SubWithCarry0xED(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            print("SBC abs")
            i = i + 2
        elif opcode == '0xee':
            print("INC abs")
            INC_absolute_0xEE(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xf1':
            print("SBC ind,Y")
            i = i + 2
        elif opcode == '0xf5':
            SubWithCarry0xF5(systemCPU, pgr_bytes[i + 1])
            print("SBC zpg,X")
            i = i + 1
        elif opcode == '0xf6':
            print("INC zpg,X")
            INC_zero_page_X_0xF6(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 1
        elif opcode == '0xf9':
            SubWithCarry0xF9(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            print("SBC abs,Y")
            i = i + 2
        elif opcode == '0xfd':
            SubWithCarry0xFD(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            print("SBC abs,X")
            i = i + 2
        elif opcode == '0xfe':
            print("INC abs,X")
            INC_absolute_X_0xFE(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
            #print(opcode)
            #print("Instrução invalida!")
        # FUSCA \/

        # HEITOR \/
        elif opcode == '0x1':
            print('ORA X, ind')
            OrWithAcumulator0x01(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x5':
            print('ORA zpg')
            OrWithAcumulator0x05(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x9':
            print('ORA #')
            OrWithAcumulator0x09(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xd':
            print('ORA abs')
            OrWithAcumulator0x0D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x11':
            print('ORA ind, Y')
            OrWithAcumulator0x11(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x15':
            print('ORA zpg, X')
            OrWithAcumulator0x15(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x19':
            print('ORA abs, Y')
            OrWithAcumulator0x19(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x1d':
            print('ORA abs, X')
            OrWithAcumulator0x1D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x21':
            print('AND X, ind')
            AndWithAcumulator0x21(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x25':
            print('AND zpg')
            AndWithAcumulator0x25(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x29':
            print('AND #')
            AndWithAcumulator0x29(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x2d':
            print('AND abs')
            AndWithAcumulator0x2D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x31':
            print('AND ind, Y')
            AndWithAcumulator0x31(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x35':
            print('AND zpg, X')
            AndWithAcumulator0x35(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x39':
            print('AND abs, Y')
            AndWithAcumulator0x39(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x3d':
            print('AND abs, X')
            AndWithAcumulator0x3D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x41':
            print('EOR ind, Y')
            ExclusiveOrWithAcumulator0x41(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x45':
            print('EOR zpg')
            ExclusiveOrWithAcumulator0x45(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x49':
            print('EOR #')
            ExclusiveOrWithAcumulator0x49(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x4d':
            print('EOR abs')
            ExclusiveOrWithAcumulator0x4D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x51':
            print('EOR ind, Y')
            ExclusiveOrWithAcumulator0x51(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x55':
            print('EOR zpg, X')
            ExclusiveOrWithAcumulator0x55(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0x59':
            print('EOR abs, Y')
            ExclusiveOrWithAcumulator0x59(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0x5d':
            print('EOR abs, X')
            ExclusiveOrWithAcumulator0x5D(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xc0':
            print('CPY #')
            CompareWithY0xC0(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xc1':
            print('CMP X, ind')
            CompareWithAcumulator0xC1(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xc4':
            print('CPY zpg')
            CompareWithY0xC4(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xc5':
            print('CMP zpg')
            CompareWithAcumulator0xC5(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xc9':
            print('CMP #')
            CompareWithAcumulator0xC9(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xcc':
            print('CPY abs')
            CompareWithY0xCC(systemCPU, pgr_bytes[i + 1])
            i = i + 2
        elif opcode == '0xcd':
            print('CMP abs')
            CompareWithAcumulator0xCD(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xd1':
            print('CMP ind, Y')
            CompareWithAcumulator0xD1(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xd5':
            print('CMP zpg, X')
            CompareWithAcumulator0xD5(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xd9':
            print('CMP abs, Y')
            CompareWithAcumulator0xD9(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xdd':
            print('CMP abs, X')
            CompareWithAcumulator0xDD(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2
        elif opcode == '0xe0':
            print('CPX #')
            CompareWithX0xE0(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xe4':
            print('CPX zpg')
            CompareWithX0xE4(systemCPU, pgr_bytes[i + 1])
            i = i + 1
        elif opcode == '0xec':
            print('CPX abs')
            CompareWithX0xEC(systemCPU, pgr_bytes[i + 1], pgr_bytes[i + 2])
            i = i + 2



        # CARTS \/
        elif opcode == '0x81':
            print("STA X,ind")
        elif opcode == '0x84':
            print("STY zpg")
        elif opcode == '0x85':
            print("STA zpg")
        elif opcode == '0x86':
            print("STX zpg")
        elif opcode == '0x8a':
            print("TXA impl")
        elif opcode == '0x8c':
            print("STY abs")
        elif opcode == '0x8d':
            print("STA abs")
        elif opcode == '0x8e':
            print("STX abs")
        elif opcode == '0x91':
            print("STA ind,Y")
        elif opcode == '0x94':
            print("STY zpg,X")
        elif opcode == '0x95':
            print("STA zpg,X")
        elif opcode == '0x96':
            print("STX zpg,Y")
        elif opcode == '0x98':
            print("TYA impl")
        elif opcode == '0x99':
            print("STA abs,Y")
        elif opcode == '0x9a':
            print("TXS impl")
        elif opcode == '0x9d':
            print("STA abs,X")
        elif opcode == '0xa0':
            print("LDY #")
        elif opcode == '0xa1':
            print("LDA X,ind")
        elif opcode == '0xa2':
            print("LDX #")
        elif opcode == '0xa4':
            print("LDY zpg")
        elif opcode == '0xa5':
            print("LDA zpg")
        elif opcode == '0xa6':
            print("LDX zpg")
        elif opcode == '0xa8':
            print("TAY impl")
        elif opcode == '0xa9':
            print("LDA #")
        elif opcode == '0xaa':
            print("TAX impl")
        elif opcode == '0xac':
            print("LDY abs")
        elif opcode == '0xad':
            print("LDA abs")
        elif opcode == '0xae':
            print("LDX abs")
        elif opcode == '0xb1':
            print("LDA ind,Y")
        elif opcode == '0xb4':
            print("LDY zpg,X")
        elif opcode == '0xb5':
            print("LDA zpg,X")
        elif opcode == '0xb6':
            print("LDX zpg,Y")
        elif opcode == '0xb9':
            print("LDA abs,Y")
        elif opcode == '0xba':
            print("TSX impl")
        elif opcode == '0xbc':
            print("LDY abs,X")
        elif opcode == '0xbd':
            print("LDA abs,X")
        elif opcode == '0xbe':
            print("LDX abs,Y")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")
        elif opcode == '0x':
            print("BRK impl")

        else:
            pass

        print ("| a = ", systemCPU.getA(), " | x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ",  " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")

        i = i + 1
        # if (True):
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        # else:
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
