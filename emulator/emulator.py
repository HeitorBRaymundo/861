from py import system
from py.operations import register_instructions
from py.operations import bit
from py.operations import flags
from py.operations import flow_control
from py.operations import interruption
from py.operations import compare

systemCPU = system.System()

def printSystemStatus():
    return


# Read file
with open('./emulator/bin/brk-adc', 'rb') as file:

    rom_bytes = file.read()

    # set the header size
    header_size = 16
    # get the binary header
    header_bytes = rom_bytes[0:16]
    # get the number of pgr_counters
    pgr_counter =  int.from_bytes(header_bytes[4:5], byteorder='big')
    pgr_bytes = rom_bytes[header_size:header_size+(16* pgr_counter*1024)]

    i = 0

    while i < len(pgr_bytes):
        opcode = hex(pgr_bytes[i])

        if opcode == '0x0':
            pass
        elif opcode == '0xa0':
            print("LDY abs")
            i = i + 1
        elif opcode == '0xb9':
            print("LDA abs,y")
            i = i + 2
        elif opcode == '0xbe':
            print("LDX abs, y")
            i = i + 2
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
            # AddWithCarry0x69(systemCPU)
            i = i + 1
        elif opcode == '0x6a':
            print("ROR A")
        elif opcode == '0x6d':
            print("ADC abs")
            # AddWithCarry0x6D(systemCPU, )
            print (rom_bytes[i + 1])
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
<<<<<<< HEAD
        # elif opcode == '0x01':
        #     compare.OrWithAcumulator0x01()
        #     print('ORA X, ind')
        # elif opcode == '0x05':
        #     compare.OrWithAcumulator0x05()
        #     print('ORA zpg')
        # elif opcode == '0x09':
        #     compare.OrWithAcumulator0x09()
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
=======
        elif opcode == '0x01':
            compare.OrWithAcumulator0x01(systemCPU, )
            print('ORA X, ind')
        elif opcode == '0x05':
            compare.OrWithAcumulator0x05()
            print('ORA zpg')
        elif opcode == '0x09':
            compare.OrWithAcumulator0x09(systemCPU, 10)
            print('ORA #')
        elif opcode == '0x0d':
            compare.OrWithAcumulator0x0D()
            print('ORA abs')
        elif opcode == '0x11':
            compare.OrWithAcumulator0x11()
            print('ORA ind, Y')
        elif opcode == '0x15':
            compare.OrWithAcumulator0x15()
            print('ORA zpg, X')
        elif opcode == '0x19':
            compare.OrWithAcumulator0x19()
            print('ORA abs, Y')
        elif opcode == '0x1d':
            compare.OrWithAcumulator0x1D()
            print('ORA abs, X')
        elif opcode == '0x21':
            compare.AndWithAcumulator0x21()
            print('AND X, ind')
        elif opcode == '0x25':
            compare.AndWithAcumulator0x25()
            print('AND zpg')
        elif opcode == '0x29':
            compare.AndWithAcumulator0x29()
            print('AND #')
        elif opcode == '0x2d':
            compare.AndWithAcumulator0x2D()
            print('AND abs')
        elif opcode == '0x31':
            compare.AndWithAcumulator0x31()
            print('AND ind, Y')
        elif opcode == '0x35':
            compare.AndWithAcumulator0x35()
            print('AND zpg, X')
        elif opcode == '0x39':
            compare.AndWithAcumulator0x39()
            print('AND abs, Y')
        elif opcode == '0x3d':
            compare.AndWithAcumulator0x3D()
            print('AND abs, X')
        elif opcode == '0x41':
            compare.ExclusiveOrWithAcumulator0x41()
            print('EOR ind, Y')
        elif opcode == '0x45':
            compare.ExclusiveOrWithAcumulator0x45()
            print('EOR zpg')
        elif opcode == '0x49':
            compare.ExclusiveOrWithAcumulator0x49()
            print('EOR #')
        elif opcode == '0x4d':
            compare.ExclusiveOrWithAcumulator0x4D()
            print('EOR abs')
        elif opcode == '0x51':
            compare.ExclusiveOrWithAcumulator0x51()
            print('EOR ind, Y')
        elif opcode == '0x55':
            compare.ExclusiveOrWithAcumulator0x55()
            print('EOR zpg, X')
        elif opcode == '0x59':
            compare.ExclusiveOrWithAcumulator0x59()
            print('EOR abs, Y')
        elif opcode == '0x5d':
            compare.ExclusiveOrWithAcumulator0x5D()
            print('EOR abs, X')
        elif opcode == '0xc0':
            compare.CompareWithY0xC0()
            print('CPY #')
        elif opcode == '0xc1':
            compare.CompareWithAcumulator0xC1()
            print('CMP X, ind')
        elif opcode == '0xc4':
            compare.CompareWithY0xC4()
            print('CPY zpg')
        elif opcode == '0xc5':
            compare.CompareWithAcumulator0xC5()
            print('CMP zpg')
        elif opcode == '0xc9':
            compare.CompareWithAcumulator0xC9()
            print('CMP #')
        elif opcode == '0xcc':
            compare.CompareWithY0xCC()
            print('CPY abs')
        elif opcode == '0xcd':
            compare.CompareWithAcumulator0xCD()
            print('CMP abs')
        elif opcode == '0xd1':
            compare.CompareWithAcumulator0xD1()
            print('CMP ind, Y')
        elif opcode == '0xd5':
            compare.CompareWithAcumulator0xD5()
            print('CMP zpg, X')
        elif opcode == '0xd9':
            compare.CompareWithAcumulator0xD9()
            print('CMP abs, Y')
        elif opcode == '0xdd':
            compare.CompareWithAcumulator0xDD()
            print('CMP abs, X')
        elif opcode == '0xe0':
            compare.CompareWithX0xE0()
            print('CPX #')
        elif opcode == '0xe4':
            compare.CompareWithX0xE4()
            print('CPX zpg')
        elif opcode == '0xec':
            compare.CompareWithX0xEC()
            print('CPX abs')
>>>>>>> 7ccef71a8bbbcb49a0f368bf63de7a1e492b2bfd



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
            print("BRK impl")"

        else:
            pass


        i = i + 1
        # if (True):
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        # else:
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
