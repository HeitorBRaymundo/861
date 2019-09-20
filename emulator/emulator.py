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
    print("")


# Read file
with open('bin/brk', 'rb') as file:
    rom_bytes = file.read()
    rom_bytes = rom_bytes[5:]
    i = 0
    while i < len(rom_bytes):
        opcode = hex(rom_bytes[i])

        if opcode == '0x0':
            pass
        elif opcode == '0xa0':
            print("LDY abs")
            i = i + 1
        elif opcode == '0xb9':
            print("LDA abs,y")
            i = i + 2
        elif opcode == '0xc8':
            register_instructions.IncreaseReg0xC8()
            print("INY")
        elif opcode == '0xbe':
            print("LDX abs, y")
            i = i + 2
        #else:
            #pass
            #print(opcode)
            #print("Instrução invalida!")


        # FUSCA \/



        # IGOR \/




        # HEITOR \/
        elif opcode == '0x01':
            compare.OrWithAcumulator0x01()
            print('ORA X, ind')
        elif opcode == '0x05':
            compare.OrWithAcumulator0x05()
            print('ORA zpg')
        elif opcode == '0x09':
            compare.OrWithAcumulator0x09()
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



        # CARTS \/





        i = i + 1
        # if (True):
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        # else:
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
